import scrapy
from frases.items import FrasesItem

class FrasesSpider(scrapy.Spider):
	name = 'frases'
	start_urls = ['http://pensador.uol.com.br/frases/']
	
	def parse(self, response):
		for sel in response.css('.phrases-list > .pensa'):

			item = FrasesItem(is_fav=False)
			item['id'] = sel.css('.frase::attr("id")').extract()
			item['autor'] = sel.css('.autor > a::text').extract()
			item['frase'] = sel.css('.frase::text').extract()

			share_sel = sel.css('ul.iconbar')
			# Facebook nao permite coletar os dados do share?!?
			# item['fb_share'] = share_sel.css('li.fb-share > .fb-share-value::text').extract()
			item['fav_count'] = share_sel.css('li.add > span.counter::text').extract()
			yield item

		next_page = response.css('.atual + a::attr("href")')
		if next_page:
			url = response.urljoin(next_page[0].extract())
			yield scrapy.Request(url, self.parse)