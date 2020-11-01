# import needed libraries
import scrapy
from scrapy.crawler import CrawlerProcess
import cfscrape
import logging

# unable the messages
logging.getLogger('scrapy').propagate = False

# main url
base_url = "https://animeflv.net"

# scraping user
user = 'fcomovaz'

# maximum anime list
max_anime = 5

# classes to scrap
class Watching(scrapy.Spider):
    name = "Watching"
    
    def start_requests(self):
        # initial url (following anime)
        url = f"{base_url}/perfil/{user}/siguiendo"
        #Bypass para cloudflare
        token,agent = cfscrape.get_tokens(url=url)
        self.token = token
        self.agent = agent
        self.max = 2
        self.pages = 0
        yield scrapy.Request(url=url,callback=self.parse,
                            cookies=token,
                            headers={'User-Agent': agent})
    def parse(self,response):
        anime_file.write("\n<details><summary>:tv: Watching</summary><br/>\n\n")
        # set anime counter
        counter_anime = 0
        # begin the formated list
        for a in response.xpath('.//article[@class="Anime alt"]'):
            # extract full anime link
            anime_url = a.xpath(".//h3[@class='Title']//a/@href").extract_first()
            # set format to the name
            anime_name = anime_url.replace('/anime/','').replace('-',' ')
            # set the link format to markdown
            anime_link = f"[{anime_name}]({base_url}{anime_url})"
            anime_file.write('* ' +anime_link+'\n')
            # counting the animes
            counter_anime += 1
            if counter_anime == max_anime: break

        anime_file.write("\n</details>\n")
       

class Favorites(scrapy.Spider):
    name = "Favorites"

    def start_requests(self):
        # initial url (favorite anime)
        url = f"{base_url}/perfil/{user}/favoritos"
        #Bypass para cloudflare
        token,agent = cfscrape.get_tokens(url=url)
        self.token = token
        self.agent = agent
        self.max = 2
        self.pages = 0
        yield scrapy.Request(url=url,callback=self.parse,
                            cookies=token,
                            headers={'User-Agent': agent})
    def parse(self,response):
        anime_file.write("\n<details><summary>:heart: Favorites</summary><br/>\n\n")
        # set anime counter
        counter_anime = 0
        # begin the formated list
        for a in response.xpath('.//article[@class="Anime alt"]'):
            # extract full anime link
            anime_url = a.xpath(".//h3[@class='Title']//a/@href").extract_first()
            # set format to the name
            anime_name = anime_url.replace('/anime/','').replace('-',' ')
            # set the link format to markdown
            anime_link = f"[{anime_name}]({base_url}{anime_url})"
            anime_file.write('* ' +anime_link+'\n')
            # counting the animes
            counter_anime += 1
            if counter_anime == max_anime: break

        anime_file.write("\n</details>\n")

class Waiting_List(scrapy.Spider):
    name = "Waiting_List"

    def start_requests(self):
        # initial url (waiting list anime)
        url = f"{base_url}/perfil/{user}/lista_espera"
        #Bypass para cloudflare
        token,agent = cfscrape.get_tokens(url=url)
        self.token = token
        self.agent = agent
        self.max = 2
        self.pages = 0
        yield scrapy.Request(url=url,callback=self.parse,
                             cookies=token,
                             headers={'User-Agent': agent})
    def parse(self,response):
        anime_file.write("\n<details><summary>:alarm_clock: My Waiting List</summary><br/>\n\n")
        # set anime counter
        counter_anime = 0
        # begin the formated list
        for a in response.xpath('.//article[@class="Anime alt"]'):
            # extract full anime link
            anime_url = a.xpath(".//h3[@class='Title']//a/@href").extract_first()
            # set format to the name
            anime_name = anime_url.replace('/anime/','').replace('-',' ')
            # set the link format to markdown
            anime_link = f"[{anime_name}]({base_url}{anime_url})"
            anime_file.write('* ' +anime_link+'\n')
            # counting the animes
            counter_anime += 1
            if counter_anime == max_anime: break

        anime_file.write("\n</details>\n")


# file to be rewriten
anime_file = open("temp_animes.md","w+")

# set title section
anime_file.write("\n## My Anime Preferences\n")

# join anime info
proc = CrawlerProcess()
proc.crawl(Watching)
proc.crawl(Favorites)
proc.crawl(Waiting_List)
proc.start()

# close file
anime_file.close()

# stop code
quit()