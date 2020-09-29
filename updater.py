import scrapy
from scrapy.crawler import CrawlerProcess
import cfscrape
import logging

# unable the messages
logging.getLogger('scrapy').propagate = False

# main url
base_url = "https://animeflv.net/"

# scraping user
user = 'fcomovaz'

# file to be rewriten
f = open("README.md","w+")

# first strings of the README.md
str1 = "\
# Hi, I'm Francisco! :eyeglasses::pencil2:\n \
\n \
A Mechatronics Engineer monkeying around with code.<img align='left' src='https://media.giphy.com/media/ZVik7pBtu9dNS/giphy.gif' width='230px'>\n \
\n \
My  alma mater: [University of Guanajuato](https://www.ugto.mx/conoce-la-ug/resena-historica-de-la-universidad-de-guanajuato)\n \
\n \
:two::zero: years old\n \
\n \
[![Twitter @fcomovaz](https://img.shields.io/twitter/follow/fcomovaz?style=social)](https://www.twitter.com/fcomovaz/)\n \
[![Github @fcomovaz](https://img.shields.io/github/followers/fcomovaz?label=follow&style=social)](https://github.com/fcomovaz)\n \
\n \
\n \
<img align='right' src='https://media.giphy.com/media/mf4qECoTz8ZVK/giphy.gif' width='25%'>\n \
\n \
```javascript\n \
const fcomovaz = {\n \
    pronouns:   'He' | 'Him',\n \
    askMeAbout: ['maths','anime','historical-fun-facts'],\n \
    languages:  ['HTML5', 'CSS3', 'Javascript', 'C', 'C++', 'Markdown'],\n \
    hobbies:    ['reading', 'science-videos', 'code-for-fun', 'plants'],\n \
    funFact:    'The horse of Alexander the Great was named Bucephalus',\n \
    motto:      'If I can not code it, I do not understand it'\n \
};\n \
```\n \
"

str2 = "\n \
\n \
## My Knowledge\n \
![HTML5](https://img.shields.io/badge/html5%20-%23E34F26.svg?&style=for-the-badge&logo=html5&logoColor=white) ![CSS3](https://img.shields.io/badge/css3%20-%231572B6.svg?&style=for-the-badge&logo=css3&logoColor=white) ![JS](https://img.shields.io/badge/javascript%20-%23323330.svg?&style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)\n \
![C](https://img.shields.io/badge/c%20-%2300599C.svg?&style=for-the-badge&logo=c&logoColor=white) ![Cpp](https://img.shields.io/badge/c++%20-%2300599C.svg?&style=for-the-badge&logo=c%2B%2B&ogoColor=white) ![Shell](https://img.shields.io/badge/shell_script%20-%23121011.svg?&style=for-the-badge&logo=gnu-bash&logoColor=white) ![Git](https://img.shields.io/badge/git%20-%23F05033.svg?&style=for-the-badge&logo=git&logoColor=white) ![Github](https://img.shields.io/badge/github%20-%23121011.svg?&style=for-the-badge&logo=github&logoColor=white) ![Markdown](https://img.shields.io/badge/markdown-%23000000.svg?&style=for-the-badge&logo=markdown&logoColor=white)\n \
\n"

str3 = "\n\
\n \
## My Languages\n \
\n \
[![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=fcomovaz&layout=compact)](https://github.com/anuraghazra/github-readme-stats)\n \
\n \
## My Stats\n \
\n \
![fcomovaz's github stats](https://github-readme-stats.vercel.app/api?username=fcomovaz&theme=vision-friendly-dark&show_icons=true)\n \
\n"


# classes to scrap

class Watching(scrapy.Spider):
    name = "Watching"

    def start_requests(self):
        url = base_url+"perfil/"+user+"/siguiendo"
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
        f.write("\n### Watching\n")
        for a in response.xpath('.//article[@class="Anime alt"]'):
            anime_url = a.xpath(".//h3[@class='Title']//a/@href").extract_first()\
            .replace('/anime/','').replace('-',' ')
            f.write('* ' +anime_url+'\n')

class Favorites(scrapy.Spider):
    name = "Favorites"
    base_url = "https://animeflv.net/"

    def start_requests(self):
        url = base_url+"perfil/"+user+"/favoritos" # url inicial (lista anime)
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
        f.write("\n### Favorites\n")
        for a in response.xpath('.//article[@class="Anime alt"]'):
            anime_url = a.xpath(".//h3[@class='Title']//a/@href").extract_first()\
            .replace('/anime/','').replace('-',' ')
            f.write('* ' +anime_url+'\n')

class Waiting_List(scrapy.Spider):
    name = "Waiting_List"
    base_url = "https://animeflv.net/"

    def start_requests(self):
        url = base_url+"perfil/"+user+"/lista_espera" # url inicial (lista anime)
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
        f.write("\n### My Waiting List\n")
        for a in response.xpath('.//article[@class="Anime alt"]'):
            anime_url = a.xpath(".//h3[@class='Title']//a/@href").extract_first()\
            .replace('/anime/','').replace('-',' ')
            f.write('* ' +anime_url+'\n')

# join 1st string
f.write(str1)

# join 2nd string
f.write(str2)

# join 3rd string
f.write(str3)

# title of the section
f.write("\n## My Anime Preferences\n")

# join anime info
proc = CrawlerProcess()
proc.crawl(Watching)
proc.crawl(Favorites)
proc.crawl(Waiting_List)
proc.start()

# stop code
quit()