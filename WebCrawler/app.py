from flask import Flask, render_template, redirect
import sys
import subprocess
from web_app.functions import get_results, filter_more_than_five_words, filter_less_than_five_words


app = Flask(__name__)

news_entries = get_results()

@app.route('/run_scraper')
def run_scraper():
    """
    This route triggers a web scraper using Scrapy to crawl Hacker News.
    After scraping, it updates the global variable news_entries with the results.
    Finally, it redirects to the root URL ('/').

    Returns:
        redirect: Redirects to the root URL ('/').
    """
    
    # Run the Scrapy crawler 'hacker_news' from the 'scraper' directory
    subprocess.run(['scrapy', 'crawl', 'hacker_news'], cwd='scraper')

    # Update the global variable news_entries with the results from get_results()
    global news_entries
    news_entries = get_results()

    # Redirect to the root URL ('/')
    return redirect("/")

@app.route('/get_more_than_five_words')
def get_more_than_five_words():
    """
    This route retrieves the entries previously fetched filtered to include only those with titles containing more than five words
    sorted by number of comments, updates the global variable news_entries with the filtered results, and redirects to the root URL 
    ('/').

    Returns:
        redirect: Redirects to the root URL ('/').
    """
    
    # Update the global variable news_entries with the results from get_results()
    global news_entries
    news_entries = get_results()
    
    # Filter news entries to include only those with titles containing more than five words
    news_entries = filter_more_than_five_words(news_entries)

    # Redirect to the root URL ('/')
    return redirect("/")

@app.route('/get_less_than_five_words')
def get_less_than_five_words():
    """
    This route retrieves the entries previously fetched filtered to include only those with titles containing five or fewer words
    sorted by points, updates the global variable news_entries with the filtered results, and redirects to the root URL ('/').

    Returns:
        redirect: Redirects to the root URL ('/').
    """
    
    # Update the global variable news_entries with the results from get_results()
    global news_entries
    news_entries = get_results()
    
    # Filter news entries to include only those with titles containing five or fewer words
    news_entries = filter_less_than_five_words(news_entries)

    # Redirect to the root URL ('/')
    return redirect("/")

# Main route "/"
@app.route('/')
def index():
    """
    This route prepares news entries as dictionaries, prints them to the console,
    and renders an HTML template ('index.html') with the news entries.

    Returns:
        render_template: Renders the 'index.html' template with the news entries.
    """
    
    # Convert each entry object to a dictionary in order to parse them into JSON
    entries_as_dict = [entry.__dict__ for entry in news_entries]
    
    # Render the 'index.html' template with the news entries
    return render_template('index.html', news_entries=entries_as_dict)

if __name__ == '__main__':
    app.run(debug=True)
