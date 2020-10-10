from cinephile.spiders.pornhub.main import PornhubVideosMainSpider


class SpidersFactory(object):
    def get_map(self) -> dict:
        return {
            PornhubVideosMainSpider.name: PornhubVideosMainSpider
        }

    def create_spider(self, name: str):
        map = self.get_map()
        if name in map:
            return map[name]

        raise EnvironmentError(f'Unknown spider [{name}]')
