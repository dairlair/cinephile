import scrapy
import datetime
import time


class XhamsterVideosMainSpider(scrapy.Spider):
    content_type: str = 'video'
    name: str = 'xhamster-videos-main'
    base_url: str = 'https://xhamster.com'
    start_urls = [
        base_url,
    ]

    def parse(self, response):
        for video in response.css('div.video-thumb'):
            link = video.css('a.video-thumb__image-container')
            img = video.css('img.thumb-image-container__image')
            yield {
                'spider': self.name,
                'type': self.content_type,
                'url': link.css('::attr(href)').extract_first(),
                'title': img.css('::attr(alt)').extract_first(),
                'foundAtTimestamp': time.time(),
                'foundAt': datetime.datetime.now().astimezone().isoformat(),
                'videoId': video.css('::attr(data-video-id)').extract_first(),
                'duration': video.css('div.thumb-image-container__duration::text').extract_first()
            }

        next_page = response.css('a[data-page=next]::attr(href)').extract_first()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
