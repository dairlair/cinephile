import scrapy
import datetime
import time


class PornhubVideosMainSpider(scrapy.Spider):
    content_type: str = 'video'
    name: str = 'pornhub-videos-main'
    start_urls = [
        'https://www.pornhub.com/',
    ]

    def parse(self, response):
        for video_link in response.css('#videoCategory a.videoPreviewBg'):
            yield {
                'spider': self.name,
                'type': self.content_type,
                'url': video_link.css('::attr(href)').extract_first(),
                'title': video_link.css('::attr(title)').extract_first(),
                'foundAtTimestamp': time.time(),
                'foundAt': datetime.datetime.now().astimezone().isoformat(),
                'videoId': video_link.css('img::attr(data-video-id)').extract_first(),
                'duration': video_link.css('var.duration::text').extract_first()
            }

        next_page = response.css('link[rel=next]::attr(href)').extract_first()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

    # private String spider +;
    # private String type; +
    # private String url; +
    # private String title; +
    # private String previewUrl;
    # private DateTime foundAt; ~