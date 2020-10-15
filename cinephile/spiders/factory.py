from cinephile.spiders.pornhub.main import PornhubVideosMainSpider
from cinephile.spiders.xhamster.main import XhamsterVideosMainSpider


class SpidersFactory(object):
    def get_map(self) -> dict:
        return {
            PornhubVideosMainSpider.name: PornhubVideosMainSpider,
            XhamsterVideosMainSpider.name: XhamsterVideosMainSpider,
        }

    def create_spider(self, name: str) -> type:
        map = self.get_map()
        if name in map:
            return map[name]

        raise EnvironmentError(f'Unknown spider [{name}]')
