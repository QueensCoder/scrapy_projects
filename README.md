<!-- to start project -->

inside of scrapy intro dir -> pipenv shell - to start virtual env
for using python extension make sure you open the folder that has the pipfile in order to set up the
environment for python to work with python extension correctly

<!--  -->

scrapy startproject myproject [project_dir] - create scrapy project in dir
scrapy commands:

    bench Run quick benchmark test
    fetch Fetch a URL using the Scrapy downloader

    genspider Generate new spider using pre-defined templates   ****

    genspider -t crawl <spider name> <site url>
        - build a spider using specific template

    runspider Run a self-contained spider (without creating a project)
    settings Get settings values
    shell Interactive scraping console
    startproject Create new project
    version Print Scrapy version
    view Open URL in browser, as seen by Scrapy

    crawl <spider-name>
        - this command allows us to crawl using the spider named
      ex:
        scrapy crawl countries
            - regular crawl

        scrapy crawl countries -o population_dataset.csv
            - crawl then create an output file with all the crawled infomation
            - can use different file extensions to make different types of files

XPATH - usually more robust than using css selectors

    xml path language

    examples
        a[href^='https'] - a tag with href that matches https

        ^= - start with
        ~= - between
        $= - end

        or
         //div[@class='intro' or @class='outro']/p
            - get all divs with class intro or class outro then get the p from each div

        starts-with
        //a[starts-with(@href, 'https')]
            - finds href that starts with the second arg passed

        ends-with
        //a[ends-with(@href, '.com')]
            - finds href that ends with second arg
            - only works with xpath 2.0 might have trouble with this in some browsers

        contains
        //a[contains(text(), 'USA')]
            - finds a tag that contains the text USA

        position

        //ul[@id='items']/li[position() = 1 or position() = last()]
            - find the ul named items and get the li at position 1 and the last elemented in the list

        mathmatical operators
        //ul[@id='items']/li[position() > 1]
            - find the li's where the position is greater than 1

CSS selectors - cleaner syntax then xpath

User Agent -

    can change user agent inside of the settings file
    under # USER_AGENT you can change it for one

    or under you can change it for all requests being sent
    # DEFAULT_REQUEST_HEADERS = {}

Setting up Splash

    docker pull scrapinghub/splash

    docker run -it -p 8050:8050 --rm scrapinghub/splash

    Splash is available at 0.0.0.0 address at port 8050 (http).

    then you can kill terminal just remember to shut down splash once you are finished
    or else docker will continue to run splash in the background

    you configure splash with Lua language

Using Scrapy with Splash

    https://github.com/scrapy-plugins/scrapy-splash

Using Selenium

    pipenv install selenium

    determine which driver is required https://selenium-python.readthedocs.io/installation.html#
    and make sure you install the driver for the correct version


    when using a chrome driver you can either locate it using a hard path or add it to an actual path so you can reference it with shutils.which
    in order to add it to path you have to use mv chromedriver <to location>
    you will have to update the chromedriver in path is you update chrome

Pipelines

    # using imdb.pipelines and the class imdb pipeline

    # the number is the priority , lower the number higher the priority

    ITEM_PIPELINES = {
    'imbd.pipelines.ImbdPipeline': 300,
    }

Avoid Getting blocked

    rate limite quests
    can limit how many times 1 ip address can make requests to server, would response with 429

    user-agent - if the user agent is the default scrapy agent it can be banned automatically

    user-agents can be used to track who is issuing requests

    honey pots - nofollow or display none a tags would be traps that scrapers would follow and would cause the ip to be blocked

    robots.txt - will show you which sites can be scraped or not

Best Practices

    dont hit websites to hard
    scrapes can be looked at as DDOS attacks

    concurent requests at 16
    and keep cpu usuage between 90% and 80%

    add a deplay between each requests
    see download.delay in settings.py

    can use random delay or auto throttle

    - enable http caching, caches requsts and reponses

    change obey robots.txt to false

    change user_agent

    permanent block
        - reboot router
        - proxy service
        - crawlera (paid)
        - recaptach (can't get around)

Deploy spiders

    https://scrapinghub.com/

    pipenv or pip install shub
    shub login
    <then enter api key>
    then shub deploy <deploy key>

    need to configure scraping hub to use python3

    update the scrapinghub.yml file to use newever version of scrapy and python3

scrapyd

    pipenv install scrapyd

    to set up client you need to install scrapyd-client

    pipenv install git+https://github.com/scrapy/scrapyd-client.git#egg=scrapyd-client

    pipenv requires that there be an arg for this type of install

    the egg is the name arg found inside of the setup.py

    see the repo: https://github.com/scrapy/scrapyd-client

    need two terminals, first terminal will run scrapyd

    scrapyd

    the second terminal will run

    update the scrapy.cfg
    uncomment the url and add correct url

    scrapyd-deploy local

    after this you need to check the response status, if the status is ok
    you can now issue a request for the job

    now you can perform a curl request in order to schedule the job to start

    curl http://localhost:6800/schedule.json -d project=glass_shop -d spider=best_seller
