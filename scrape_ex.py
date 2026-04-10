import scrapy
import pandas as pd


class AmazonUsSpider(scrapy.Spider):
    name = "scrape_ex"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/"]

    def parse(self, response):
        xpath_laptops = '//li[contains(@class, "xs")]'
        results = []
        laptops = response.xpath(xpath_laptops)
        
        for laptop in laptops:
            xpath_photo =  './/img/@src' #'.//img[contains(@src,"jpg")]'
            xpath_title = './/img/@alt'
            xpath_price = './/p[@class="price_color"]/text()'
            xpath_rating = './/p[contains(@class,"star-rating")]/@class'
            
            photo = laptop.xpath(xpath_photo).get()
            title = laptop.xpath(xpath_title).get()
            price = laptop.xpath(xpath_price).get()
            price_clean = price.replace("£", "")
            rating = laptop.xpath(xpath_rating).get()
            rating_word = rating.split()[-1] if rating else '0'
            rating_map = {
                'One': 1,
                'Two': 2,
                'Three': 3,
                'Four': 4,
                'Five': 5
            }
            rating_num = rating_map.get(rating_word,0)
            
                        
            yield {
                "photo": photo.strip(),
                "title": title.strip(),
                "price": f"$ {price_clean.strip()}",
                "rating": rating_num
            }
