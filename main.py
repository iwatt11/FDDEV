#!/usr/local/bin/python2.7
import sys
from bs4 import BeautifulSoup
import urllib2
import nltk
URL = "http://well.blogs.nytimes.com/projects/healthy-recipes/recipes/quinoa-salad-with-avocado-and-kalamata-olives"


def get_movie_data():
    # Download IMDB dat
    """"""
    
def main():
    "Open URL"
    page = urllib2.urlopen(URL)
    soup = BeautifulSoup(page)
    x = soup.find('div', attrs={'class' : 'ingredients left'})
    y = x.find_all('li', attrs={'itemprop': 'ingredients'})
    keys = ['NN','JJ','VBP']
    for item in y:
        ingred = item.text
        tokens = nltk.word_tokenize(ingred)
        tagged = nltk.pos_tag(tokens)
        #print tagged
        for word in tagged:
            if word[1] in keys:
                print word
        

   



if __name__ == '__main__':
    sys.exit(main())

