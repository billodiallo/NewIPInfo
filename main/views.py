from flask import render_template,request,redirect,url_for
from . import main
from flask import render_template,request,redirect,url_for
from ..request import get_source,article_source,get_category,get_headlines


#our views
@main.route('/')
def index():
    '''
    Root function returning index/home page with data
    '''
    source= get_source()
    headlines = get_headlines()
    return render_template('index.html',sources=source, headlines = headlines)