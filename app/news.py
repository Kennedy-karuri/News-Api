class Sources:

    '''
    source class to define Objects
    '''

    def __init__(self,id,name,description,url):
        self.id= id
        self.name = name
        self.description = description
        self.url = url

class Headlines:
    '''
    class that define instance of headlines
    '''
    def __init__(self,author,description,time,url,image,title):
        self.author = author
        self.description = description
        self.time = time
        self.url = url
        self.image = image
        self.title = title
class Article:
    '''
    Class that instantiates objects of the news article objects of the news sources
    '''
    def __init__(self,author,description,time,url,image,title,content):
        self.author = author
        self.description = description
        self.time = time
        self.url = url
        self.image = image
        self.title = title
        self.content= content

class Category:
    '''
    Class that instantiates objects of the news categories objects of the news sources
    '''
    def __init__(self,author,description,time,url,image,title):
        self.author = author
        self.description = description
        self.time = time
        self.url = url
        self.image = image
        self.title = title