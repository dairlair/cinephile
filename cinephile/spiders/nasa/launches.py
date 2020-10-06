import scrapy

class NasaLaunchesSpider(scrapy.Spider):
    name = "nasa"
    start_urls = [
        'https://www.nasa.gov/launchschedule/',
    ]

    def parse(self, response):
        for data in response.css('div.launch-event'):
            yield {
                'launchTitle': data.css('div.title a::text').extract_first(),
                'launchDate': data.xpath('.//div[@class="date"]/text()').extract_first(),
                'launchDescription': data.xpath('.//span[@class="description"]/text()').extract_first()
            }

        next_page = response.css('a[rel="next"]::attr(href)').extract_first()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)