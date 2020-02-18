<!-- to start project -->

inside of scrapy intro dir -> pipenv shell - to start virtual env

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
