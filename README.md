# Welcome to the Stack Builder's coding exercise.

This exercise consists in a web crawler that, using scraping techniques, extracts the first 30 entries from https://news.ycombinator.com/ and displays them in a web page. It also allows to do two filtering operations: entries with more than five words in the title ordered by the number of comments, and entries with less than or equal five words in the title ordered by pints.

To test it, you will only need to have poetry and python 3.12 installed. You can install poetry by simply using pip.
```
pip poetry
```

Then, situated in the WebCrawler folder, you must install the dependencies.
```
poetry install
```

When the dependencies are installed, you must enter inside poetry's environment using
```
poetry shell
```

We are almost done! Now you can run the web server using
```
python app.py
```

Now, you can enjoy the coding exercise in the following URL: http://127.0.0.1:5000/.
