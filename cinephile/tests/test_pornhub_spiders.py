from cinephile.spiders.pornhub.main import PornhubVideosMainSpider
from scrapy.http import HtmlResponse


def test_pornhub_main_spider() -> None:
    f = open("./cinephile/tests/responses/pornhub-main.html", "r")
    html = f.read()
    spider = PornhubVideosMainSpider()
    items = []
    response = HtmlResponse(url='https://pornhub.com',
                            body=html, encoding='utf-8')
    for item in spider.parse(response):
        if type(item) is dict:
            del item['foundAt']
            del item['foundAtTimestamp']
        items.append(item)

    expected = [
        {'spider': 'pornhub-videos-main', 'type': 'video', 'url': 'https://www.pornhub.comhttps://www.pornhub.com/view_video.php?viewkey=ph5ae432c4cb16e', 'title': 'Sexy blonde exhibitionist April strips naked outdoors and amateur babe', 'videoId': None, 'duration': None},
    ]

    assert items == expected
