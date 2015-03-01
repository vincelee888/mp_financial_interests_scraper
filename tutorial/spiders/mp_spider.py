from scrapy.contrib.spiders import CrawlSpider , Rule
from scrapy.contrib.linkextractors import LinkExtractor
from  tutorial.modules import title_parse

from tutorial.items import MpItem


class MpSpider(CrawlSpider):

    name ="mp"
    allowed_domains = ["publications.parliament.uk"]
    start_urls = ["http://www.publications.parliament.uk/pa/cm/cmregmem/150209/part1contents.htm"]
    rules = (
        Rule(
            LinkExtractor(
                allow_domains = allowed_domains,
                restrict_xpaths = '//h3/following-sibling::p/a'
            ),
            callback = 'parsemp'
        ),
    )

    def parsemp(self, response):
        parsedTitle = title_parse.parse(response.xpath('//h2/text()').extract()[0])

        mp = MpItem()
        mp["name"] = parsedTitle.firstName + " " + parsedTitle.surname
        mp["borough"] = parsedTitle.borough

        print mp["name"]

        yield mp