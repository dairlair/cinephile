class RedisPipeline(object):
    def process_item(self, item, spider):
        print('Items is processed with Redis')
        print(item)
        return item

    def open_spider(self, spider):
        print('Open the Redis connection')

    def close_spider(self, spider):
        print('Close the Redis connection')