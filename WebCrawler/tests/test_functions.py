import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../web_app')))

from web_app.functions import *
from web_app.models import NewsEntry

@pytest.mark.parametrize("w, expected", [
    ('', False),
    ('hacker', True),
    ('HACKER', True),
    ('HacKeR', True),
    ('*', False),
    ('self-explained', True),
    ('-*-', False),
    ('a', True),
    ('123', True),
    ('2a', True)
])
def test_is_word(w, expected):
    assert is_word(w) == expected

@pytest.mark.parametrize("s, expected", [
    ('', 0),
    ('              ', 0),
    ('This is a self explained example', 6),
    ('This is - a self-explained example', 5),
    ('THIS IS a SELF-explained EXAMPLE', 5),
    ('This, ****- is a self-explained example.', 5),
    ('This is 2 self-explained example', 5)
])
def test_get_number_of_words(s, expected):
    assert get_number_of_words(s) == expected


array_of_news = [
    NewsEntry(1, 'Fitting an Elephant with Four Non-Zero Parameters', 43, 5),
    NewsEntry(2, 'AB 1637 requires all cities and counties to transition to a .gov domain', 20, 9),
    NewsEntry(3, 'Show HN: I built a Jeopardy game maker with buzzer support', 96, 21),
    NewsEntry(4, 'Musical Notation for Modular Synthesizers', 29, 5),
    NewsEntry(5, 'On Building Systems That Will Fail (1991)', 14, 2),
    NewsEntry(6, "Building and scaling Notion's data lake", 93, 22),
    NewsEntry(7, "Writing a BIOS bootloader for 64-bit mode from scratch", 99, 36),
    NewsEntry(8, "Building the Bell System", 26, 0),
    NewsEntry(9, "Templating in JavaScript, from Zero Dependencies on Up (2021)", 10, 4),
    NewsEntry(10, "PermitFlow Is Hiring", 0, 0),
    NewsEntry(11, "Git-PR: patch requests over SSH", 98, 61),
]


def test_filter_more_than_five_words():

    array_of_news_more_than_five_words = [
        NewsEntry(7, "Writing a BIOS bootloader for 64-bit mode from scratch", 99, 36),
        NewsEntry(6, "Building and scaling Notion's data lake", 93, 22),
        NewsEntry(3, 'Show HN: I built a Jeopardy game maker with buzzer support', 96, 21),
        NewsEntry(2, 'AB 1637 requires all cities and counties to transition to a .gov domain', 20, 9),
        NewsEntry(1, 'Fitting an Elephant with Four Non-Zero Parameters', 43, 5),
        NewsEntry(9, "Templating in JavaScript, from Zero Dependencies on Up (2021)", 10, 4),
        NewsEntry(5, 'On Building Systems That Will Fail (1991)', 14, 2)
    ]

    assert filter_more_than_five_words(array_of_news) == array_of_news_more_than_five_words



def test_filter_less_than_five_words():

    array_of_news_less_than_five_words = [
        NewsEntry(11, "Git-PR: patch requests over SSH", 98, 61),
        NewsEntry(4, 'Musical Notation for Modular Synthesizers', 29, 5),
        NewsEntry(8, "Building the Bell System", 26, 0),
        NewsEntry(10, "PermitFlow Is Hiring", 0, 0),
    ]

    assert filter_less_than_five_words(array_of_news) == array_of_news_less_than_five_words