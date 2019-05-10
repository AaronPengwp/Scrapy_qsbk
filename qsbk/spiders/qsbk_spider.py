# -*- coding: utf-8 -*-
import scrapy
from qsbk.items import QsbkItem
from scrapy.http.response.html import HtmlResponse

class QsbkSpiderSpider(scrapy.Spider):
    name = 'qsbk_spider'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/text/page/1/']

    def parse(self, response):
        duanzidivs = response.xpath('//div[@id="content-left"]/div')
        for duanzidiv in duanzidivs:
            author = duanzidiv.xpath(".//h2/text()").get().strip()
            content = duanzidiv.xpath('.//div[@class="content"]//text()').getall()# extract = getall
            content = ''.join(content).strip()
            #方法一：以字典的方式传回，不好
            # duanzi = {'author':author,'content':content}
            # yield duanzi
            #方法二：使用items
            item = QsbkItem(author=author, content=content)
            yield item
