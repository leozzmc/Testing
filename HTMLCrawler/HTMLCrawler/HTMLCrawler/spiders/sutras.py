import scrapy


class SutrasSpider(scrapy.Spider):
    name = 'sutras'
    allowed_domains = ['cbetaonline.dila.edu.tw']
    start_urls = ['https://cbetaonline.dila.edu.tw/zh/T0001_001']

    def parse(self, response):
        sutras_title = response.xpath(
            "//a[@class='noteAnchor']/@href='#n0001001'/p[@style='display: block;']/span[@class='t']/span[starts-with(@l,'000')]").get()
        if sutras_title:
            return sutras_title
        else:
            self.logger.error("沒有抓到sutras")

        for sutras in sutras_title:
            print(sutras)
