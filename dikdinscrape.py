import scrapy

class PostsSpider(scrapy.Spider):
    name = "coba"
    allowed_urls = ['https://dikdin.bkn.go.id']
    start_urls = [
        'https://dikdin.bkn.go.id/informasi'

    ]

    def parse(self, response):
        for row in response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "table-responsive", " " ))]//tbody//tr'):
            yield {
                'Status': row.xpath('td//text()')[2].extract(),
                'Periode Daftar': row.xpath('td//text()')[5].extract(),
                'Instansi': row.xpath('td//text()')[6].extract(),
                'Link Pengumuman': row.xpath('td//@href').extract(),
                'Call Center': row.xpath('td//text()')[8].extract(),
                'Helpdesk': row.xpath('td//text()')[9].extract(),
                'Media Sosial': row.xpath('td//text()')[10].extract()

            }