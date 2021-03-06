class Request:
    def __init__(self, url, callback=None):
        self.url = url
        self.callback = callback


class Response:
    def __init__(self, byte_content, request):
        self.content = byte_content
        self.request = request
        self.url = request.url
        self.text = str(byte_content, encoding='utf-8')


class MySpider:
    start_urls = ['http://www.czasg.xyz', 'http://www.czasg.xyz',
                  'http://www.czasg.xyz', 'http://www.czasg.xyz']

    def start_requests(self):
        yield from (Request(url, self.parse) for url in self.start_urls)

    def parse(self, response):
        print(response.url)


if __name__ == '__main__':
    spider = MySpider()

    import aiohttp
    import asyncio


    async def _download(request):  # scrapy是基于Twisted实现的异步下载，此处aiohttp也是凑凑
        async with aiohttp.ClientSession() as session:
            async with session.get(request.url) as response:
                byte_content = await response.content.read()  # 用aiohttp模拟异步下载, 获取DOM
                response = Response(byte_content, request)    # 构建Response对象
                request.callback(response)  # 执行回调


    loop = asyncio.get_event_loop()
    tasks = [_download(request) for request in spider.start_requests()]
    loop.run_until_complete(asyncio.wait(tasks))
