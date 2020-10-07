import scrapy

class PornhubMainSpider(scrapy.Spider):
    name = 'pornhub-main'
    start_urls = [
        'https://www.pornhub.com/',
    ]

    def parse(self, response):
        for video_link in response.css('#videoCategory a.videoPreviewBg'):
            yield {
                'title': video_link.css('::attr(title)').extract_first(),
                'url': video_link.css('::attr(href)').extract_first(),
                'videoId': video_link.css('img::attr(data-video-id)').extract_first(),
                'duration': video_link.css('var.duration::text').extract_first()
            }

        next_page = response.css('link[rel=next]::attr(href)').extract_first()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)