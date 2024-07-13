from flask import Flask, render_template
import sys
import subprocess
from functions import get_results, filter_more_than_five_words, filter_less_than_five_words


app = Flask(__name__)

news_entries = get_results()

@app.route('/run_scraper')
def run_scraper():
    subprocess.run(['scrapy', 'crawl', 'hacker_news'], cwd='scraper')

    global news_entries

    news_entries = get_results()

    return news_entries

@app.route('/get_more_than_five_words')
def get_more_than_five_words():
    global news_entries

    news_entries = get_results()
    news_entries = filter_more_than_five_words(news_entries)

    return news_entries

@app.route('/get_less_than_five_words')
def get_less_than_five_words():
    global news_entries

    news_entries = get_results()
    news_entries = filter_less_than_five_words(news_entries)

    return news_entries

# Ruta principal "/"
@app.route('/')
def index():

    return render_template('index.html', news_entries=news_entries)

# Ejecutar la aplicación Flask si se inicia directamente desde este archivo
if __name__ == '__main__':
    app.run(debug=True)
