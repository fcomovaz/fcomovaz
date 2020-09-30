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
f = open("sample.txt","w+")

p1 = "\
\
# Hi, I'm Francisco! :eyeglasses::pencil2:\n \
\n \
A Mechatronics Engineer monkeying around with code.<img align='left' src='https://media.giphy.com/media/ZVik7pBtu9dNS/giphy.gif' width='230px'>\n \
\n \
My  alma mater: [University of Guanajuato](https://www.ugto.mx/conoce-la-ug/resena-historica-de-la-universidad-de-guanajuato)\n \
\n \
:two::zero: years old\n \
\n \
<!-- [![Twitter @fcomovaz](https://img.shields.io/twitter/follow/fcomovaz?style=social)](https://www.twitter.com/fcomovaz/)\n \
[![Github @fcomovaz](https://img.shields.io/github/followers/fcomovaz?label=follow&style=social)](https://github.com/fcomovaz) -->\n \
\n \
\n \
[<img align=\"left\" alt=\"https://fcomovaz.github.io/\" width=\"22px\" src=\"https://raw.githubusercontent.com/iconic/open-iconic/master/svg/globe.svg\" />][website]\n \
[<img align=\"left\" alt=\"fcomovaz | Twitter\" width=\"22px\" src=\"https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/twitter.svg\" />][twitter]\n \
[<img align=\"left\" alt=\"fcomovaz | Instagram\" width=\"22px\" src=\"https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/instagram.svg\" />][instagram]\n \
\n \
<br/>\n \
\n \
---\n \
\n \
<img align='right' src='https://media.giphy.com/media/mf4qECoTz8ZVK/giphy.gif' width='20%'>\n \
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
\n \
\n \
## My Knowledge\n \
\n \
<img align=\"left\" alt=\"Visual Studio Code\" width=\"26px\" src=\"https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/visual-studio-code/visual-studio-code.png\" />\n \
\n \
<img align=\"left\" alt=\"HTML5\" width=\"26px\" src=\"https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/html/html.png\" />\n \
<img align=\"left\" alt=\"CSS3\" width=\"26px\" src=\"https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/css/css.png\" />\n \
<img align=\"left\" alt=\"JS\" width=\"26px\" src=\"https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/javascript/javascript.png\" />\n \
\n \
<img align=\"left\" alt=\"terminal\" width=\"26px\" src=\"https://raw.githubusercontent.com/github/explore/d92924b1d925bb134e308bd29c9de6c302ed3beb/topics/terminal/terminal.png\" />\n \
<img align=\"left\" alt=\"Git\" width=\"26px\" src=\"https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/git/git.png\" />\n \
<img align=\"left\" alt=\"Github\" width=\"26px\" src=\"https://github.githubassets.com/images/icons/emoji/octocat.png\" />\n \
\n \
<img align=\"left\" alt=\"C\" width=\"26px\" src=\"https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/c/c.png\" />\n \
<img align=\"left\" alt=\"C++\" width=\"26px\" src=\"https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/cpp/cpp.png\" />\n \
<img align=\"left\" alt=\"Python\" width=\"26px\" src=\"https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/python/python.png\" />\n \
\n \
<img align=\"left\" alt=\"Scilab\" width=\"26px\" src=\"https://avatars1.githubusercontent.com/u/16873035?s=200&v=4\" />\n \
<img align=\"left\" alt=\"Matlab\" width=\"26px\" src=\"https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/matlab/matlab.png\" />\n \
<img align=\"left\" alt=\"Arduino\" width=\"26px\" src=\"https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/arduino/arduino.png\" />\n \
\n \
\n \
<img align=\"left\" alt=\"LaTeX\" width=\"26px\" src=\"https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/latex/latex.png\" />\n \
<img align=\"left\" alt=\"Markdown\" width=\"26px\" src=\"https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/markdown/markdown.png\" />\n \
\n \
\n \
\n \
<br/>\n \
\n \
---\n \
\n \
## Spotify Playing :headphones:\n \
\n\
<div style=\"width:250px;\">\n \
<details><summary>Look at the Music :musical_note: :musical_note:</summary>\n \
\n \
[![spotify-github-profile](https://spotify-github-profile.vercel.app/api/view?uid=21buo33eiklc76ohjsvfv4i7a&cover_image=true)](https://spotify-github-profile.vercel.app/api/view?uid=21buo33eiklc76ohjsvfv4i7a&redirect=true)\n \
\n \
</details>\n \
</div>\n \
\n\
\n \
---\n \
\n \
\n \
## My Anime Preferences\n \
\n \
\n \
\
"

p2 = "\
\n \
---\n \
\n \
## Stadistic Details\n \
\n \
<details>\n \
  <summary>:zap: My Stats</summary>\n \
\n \
  ![fcomovaz's github stats](https://github-readme-stats.vercel.app/api?username=fcomovaz&theme=vision-friendly-dark&show_icons=true)\n \
\n \
</details>\n \
\n \
\n \
<details>\n \
  <summary>:zap: Top Languages</summary>\n \
\n \
  [![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=fcomovaz&layout=compact)](https://github.com/anuraghazra/github-readme-stats)\n \
\n \
</details>\n \
\n\n\n\
[website]: https://fcomovaz.github.io/\n \
[twitter]: https://twitter.com/fcomovaz\n \
[instagram]: https://instagram.com/fcomovaz\n \
\
"

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
        f.write("\n<details><summary>:tv: Watching</summary>\n\n")

        for a in response.xpath('.//article[@class="Anime alt"]'):
            anime_url = a.xpath(".//h3[@class='Title']//a/@href").extract_first()\
            .replace('/anime/','').replace('-',' ')
            f.write('* ' +anime_url+'\n')

        f.write("\n</details>\n")

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
        f.write("\n<details><summary>:heart: Favorites</summary>\n\n")

        for a in response.xpath('.//article[@class="Anime alt"]'):
            anime_url = a.xpath(".//h3[@class='Title']//a/@href").extract_first()\
            .replace('/anime/','').replace('-',' ')
            f.write('* ' +anime_url+'\n')

        f.write("\n</details>\n")

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
        f.write("\n<details><summary>:alarm_clock: My Waiting List</summary>\n\n")

        for a in response.xpath('.//article[@class="Anime alt"]'):
            anime_url = a.xpath(".//h3[@class='Title']//a/@href").extract_first()\
            .replace('/anime/','').replace('-',' ')
            f.write('* ' +anime_url+'\n')

        f.write("\n</details>\n")

# join part1
f.write(p1)

# join anime info
proc = CrawlerProcess()
proc.crawl(Watching)
proc.crawl(Favorites)
proc.crawl(Waiting_List)
proc.start()

# join part2
f.write(p2)

# stop code
quit()