from flask import render_template,redirect,url_for
from . import main
from ..request import get_sources, get_headlines,get_category,article_source
#Views 
@main.route('/')
def index():
    '''
    Root function returning index/home page with data
    '''
    source = get_sources()
    headlines = get_headlines()
    return render_template('index.html',sources=source, headlines = headlines)
@main.route('/articles/<id>')
def article(id):
    '''
    View article page function that returns the various article details page and its data
    '''
    # title= 'Articles'
    articles = article_source(id)
    title = f'{id}'
    return render_template('articles.html',articles= articles,title=title )
@main.route('/categories/<category>')
def category(category):
    '''
    function to return the categories.html page and its content
    '''
    category = get_category(category)
    title = f'{category}'
    category = category
    return render_template('categories.html',title = title,category = category )