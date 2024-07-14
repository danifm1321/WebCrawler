import os
import json
import re
from .models import NewsEntry

def get_results():
    """
    This function reads the JSON file of the scraped results line by line and returns a list of hacker news entries.
    If the file does not exist, it returns an empty list.

    Returns:
        list: A list of hacker news entries loaded from the JSON file.
              Each entry is a hacker news dictionary.
    """
    
    # Path to the scraped results file
    output_path = 'scraper/results/output.json'

    news_entries = []

    # Check if the file exists
    if os.path.isfile(output_path):
        # Open the file in read mode
        with open(output_path, 'r') as f:
            # Read each line from the file and convert from JSON to NewsEntry
            for line in f:
                data = json.loads(line)
                news_entry = NewsEntry.from_dict(data)
                news_entries.append(news_entry)
    else:
        # If the file does not exist, initialize an empty list
        news_entries = []

    return news_entries


def is_word(word):
    """
    This function checks if a given string contains at least one alphanumeric character.
    
    Args:
        word (str): The string to be checked.
        
    Returns:
        bool: True if the string contains at least one alphanumeric character, False otherwise.
    """
    
    # Use a regular expression to search for at least one alphanumeric character (a-z, A-Z, or 0-9) in the input string
    return bool(re.search('[a-zA-Z0-9]', word))

def get_number_of_words(sentence):
    """
    This function counts the number of words in a given sentence.
    A word is defined as any sequence containing at least one alphanumeric character.
    
    Args:
        sentence (str): The sentence to be analyzed.
        
    Returns:
        int: The number of words in the sentence.
    """
    
    # Split the sentence into a list of substrings based on whitespace
    splited_sentence = sentence.split()
    
    # Filter the list to include only valid words (those containing at least one alphanumeric character)
    words = [word for word in splited_sentence if is_word(word)]

    # Return the number of valid words
    return len(words)

def filter_more_than_five_words(entries):
    """
    This function filters a list of hacker news to include only those with titles containing more than five words.
    The filtered entries are then sorted in descending order by the number of comments.

    Args:
        entries (list of NewsEntry): A list of entries of hacker news, where each entry has the keys number, title, 
        points and number_of_comments.
        
    Returns:
        list of NewsEntry: A list of filtered and sorted hacker news.
    """
    
    # Filter the entries to include only those with titles containing more than five words
    entries_filtered = [entry for entry in entries if get_number_of_words(entry.title) > 5]
    
    # Sort the filtered entries by the number of comments in descending order
    entries_filtered.sort(key=lambda x: x.number_of_comments, reverse=True)

    return entries_filtered

def filter_less_than_five_words(entries):
    """
    This function filters a list of hacker news to include only those with titles containing five or less words.
    The filtered entries are then sorted in descending order by the number of points.

    Args:
        entries (list of NewsEntry): A list of entries of hacker news, where each entry has the keys number, title, 
        points and number_of_comments.
        
    Returns:
        list of NewsEntry: A list of filtered and sorted hacker news.
    """
    
    # Filter the entries to include only those with titles containing five or less words
    entries_filtered = [entry for entry in entries if get_number_of_words(entry.title) <= 5]
    
    # Sort the filtered entries by the points in descending order
    entries_filtered.sort(key=lambda x: x.points, reverse=True)

    return entries_filtered
