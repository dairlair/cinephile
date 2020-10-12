from cinephile.spiders.factory import SpidersFactory
from cinephile.spiders.pornhub.main import PornhubVideosMainSpider


def test_spiders_creation() -> None:
    # Given
    factory = SpidersFactory()

    # When
    spider = factory.create_spider('pornhub-videos-main')

    # Then
    assert spider is PornhubVideosMainSpider
