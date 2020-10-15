from cinephile.spiders.xhamster.main import XhamsterVideosMainSpider
from scrapy.http import HtmlResponse


def test_pornhub_main_spider() -> None:
    f = open("./cinephile/tests/responses/xhamster-main.html", "r")
    html = f.read()
    spider = XhamsterVideosMainSpider()
    items = []
    response = HtmlResponse(url='https://xhamster.com',
                            body=html, encoding='utf-8')
    for item in spider.parse(response):
        if type(item) is dict:
            del item['foundAt']
            del item['foundAtTimestamp']
        items.append(item)

    expected = [
        {
            'spider': 'xhamster-videos-main', 
            'type': 'video', 
            'url': 'https://xhamster.com/videos/true-anal-gia-paige-back-for-yet-another-ass-pounding-10825473', 
            'title': 'TRUE ANAL Gia Paige back for yet another ass pounding', 
            'videoId': '10825473', 
            'duration': '12:08'
        },
    ]

    assert items == expected
