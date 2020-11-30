from app import app
import urllib.request,json
from .models import Sources,Headlines,News

News = news.News



# Getting api key
api_key = None
# Getting the movie base url
base_url = None

def configure_request(app):
    global api_key,base_url,head_news_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['BASE_URL']
    headline_news_url = app.config['HEADLINE_API_URL']


def get_sources():
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = base_url.format(api_key)
    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_results(sources_results_list)


    return sources_results

def process_results(sources_list):
    '''
    Function  that processes the news result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain news details

    Returns :
        news_results: A list of news objects
    '''
    sources_results = []
    for source_item in sources_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
      
        if id:
            sources_object = Sources(id,name,description,url)
            sources_results.append(sources_object)

    return sources_results

def get_headlines():
    '''
    function that gets the response to the category json
    '''
    get_headlines_url = 'https://newsapi.org/v2/top-headlines?country=us&apiKey={}'.format(api_key)
    print(get_headlines_url)
    with urllib.request.urlopen(get_headlines_url) as url:
        get_headlines_data = url.read()
        get_headlines_response = json.loads(get_headlines_data)

        get_headlines_results = None

        if get_headlines_response['articles']:
            get_headlines_list = get_headlines_response['articles']
            get_headlines_results = process_articles_results(get_headlines_list)

    return get_headlines_results

def news_source(id):
    news_source_url = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'.format(id,api_key)
    print(news_source_url)
    with urllib.request.urlopen(news_source_url) as url:
        news_source_data = url.read()
        news_source_response = json.loads(news_source_data)

        news_source_results = None

        if news_source_response['news']:
            news_source_list = news_source_response['news']
            news_source_results = process_news_results(news_source_list)


    return article_source_results

def process_news_results(news):
    '''
    function that processes the json files of articles from the api key
    '''
    news_source_results = []
    for news in news:
        author = news.get('author')
        description = news.get('description')
        time = news.get('publishedAt')
        url = news.get('urlToImage')
        image = news.get('url')
        title = news.get ('title')

        if url:
            news_objects = News(author,description,time,image,url,title)
            news_source_results.append(news_objects)

    return article_source_results

def get_category(category):
    '''
    function that gets the response to the category json
    '''
    get_category_url = head_news_url.format(category,api_key)
    print(get_category_url)
    with urllib.request.urlopen(get_category_url) as url:
        get_category_data = url.read()
        get_cartegory_response = json.loads(get_category_data)

        get_cartegory_results = None

        if get_cartegory_response['articles']:
            get_cartegory_list = get_cartegory_response['articles']
            get_cartegory_results = process_articles_results(get_cartegory_list)

    return get_cartegory_results