import os
import json
import re

def get_results():

    # Ruta donde se guarda el archivo JSON
    output_path = 'scraper/results/output.json'

    if os.path.isfile(output_path):
        # Leer los datos del archivo JSON generado por Scrapy
        with open(output_path, 'r') as f:
            news_entries = [json.loads(line) for line in f]
    else:
        news_entries = []

    return news_entries

def is_word(word):
    return bool(re.search('[a-zA-Z0-9]', word))

def get_number_of_words(sentence):

    splited_sentence = sentence.split()
    words = [word for word in splited_sentence if is_word(word)]

    return len(words)

def filter_more_than_five_words(entries):

    entries_filtered = [entrie for entrie in entries if get_number_of_words(entrie['title']) > 5]
    entries_filtered.sort(key=lambda x: int(x['number_of_comments']), reverse=True)

    return entries_filtered

def filter_less_than_five_words(entries):

    entries_filtered = [entrie for entrie in entries if get_number_of_words(entrie['title']) <= 5]
    entries_filtered.sort(key=lambda x: int(x['points']), reverse=True)

    return entries_filtered



