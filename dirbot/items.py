from scrapy import Item, Field


class Website(Item):

    name = Field()
    description = Field()
    url = Field()
