import pytest
from cinephile.spiders.factory import SpidersFactory
from cinephile.spiders.pornhub.main import PornhubVideosMainSpider
from cinephile.spiders.xhamster.main import XhamsterVideosMainSpider


def get_spiders_map():
    return [
        ('pornhub-videos-main', PornhubVideosMainSpider),
        ('xhamster-videos-main', XhamsterVideosMainSpider),
    ]



@pytest.mark.parametrize("name,spider_type", get_spiders_map())
def test_spiders_creation(name: str, spider_type: type) -> None:
    # Given
    factory = SpidersFactory()

    # When
    spider = factory.create_spider(name)

    # Then
    assert spider is spider_type

def test_wrong_spiders_creation() -> None:
    factory = SpidersFactory()
    with pytest.raises(EnvironmentError):
        spider = factory.create_spider('unknown-spider')