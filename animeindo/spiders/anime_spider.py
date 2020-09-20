import scrapy
import os


class AnimendoSpider(scrapy.Spider):
    name = "animeindo"

    start_urls = [
            'http://animeindo.asia/'
        ]

    def start_reqeusts(self):
        for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        homeUrls = response.css("div#episodes div.episode div.episode-details h3 a::attr('href')").getall()
        # Samehadakuurls = response.css("div.post-show div.dtla h2.entry-title a::attr('href')").getall()
        # titles = response.css("div.post-show div.dtla a.title::text").getall()
        # OPLOVERZ titles = response.css("div.lts div.dtl h2 a.title::text").getall()
        
        if len(homeUrls) > 0 :
            for url in homeUrls:
                detailVideo = response.urljoin(url)
                yield scrapy.Request(detailVideo, callback=self.parse)

        
        detailUrl = response.css("div.player-area div#embed_holder div.videoembedactiveembed div#Container iframe::attr('data-src')").get()
        
        if detailUrl is not None:
            title = response.css("div.bannerep div.bannertit div.titleps h1::text").get()
            os.system("curl -L %s --output %s.mp4" % (detailUrl, title))

