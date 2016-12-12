# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 00:18:48 2016

@author: cristinamenghini
"""

"""----------------------------------------------------------------------------
This script contains function used to make analysis on data.
----------------------------------------------------------------------------"""

# Import usefull libraries
import re
import json
import codecs
import requests
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup


def article_mentions(json_, string):
    """ This funtion returns the data frame of articles and the number of times they mention the @string.
    It takes as input:
    
    @json_: is the path of the .json to import
    @string: the string you look up for"""
    
    # Initialise the list to store titles and number of matches
    list_titles = []
    list_matches = []
    
    # Read line by line 
    with codecs.open(json_,'rU','utf-8') as f:
        for line in f:
            
            load_line = json.loads(line)
            
            # Get the text
            text = load_line['text']
            
            # Match the string in the text
            match = len(list(re.findall(string, text, flags=re.I)))
            
            # Append to the list the Title of the page and the number of matches
            list_titles.append(load_line['title'])
            list_matches.append(match)
    
    # Convert lists titles in a df
    df_mentions = pd.DataFrame(np.array([list_titles, list_matches]).T, columns=['Title', 'Number of mentions'])
    # Convert type of the columns
    df_mentions['Number of mentions'] = pd.to_numeric(df_mentions['Number of mentions'])
    
    return df_mentions
    
###############################################################################

def get_matches(df_titles):
    """ This function returns a dictionary (key, value):("title_lang_1", 
    "title_lang_2") that matches the article in one language with those of the
    other.
    It takes as input:
    
    @df_titles: is the df of titles of the language with less articles mentioning
                the string."""
    
    # Initialize the output dictionary
    dictionary = {}
    
    # For each title of language_1
    for i in df_titles['Title']:
        
        # Preprocess the title in order to make the request
        title = i.replace(' ','_')
        
        # Send the request
        req = requests.get('https://pt.wikipedia.org/wiki/' + title)
        html = req.content
        soup = BeautifulSoup(html, 'html.parser')
        
        # Find in the HTML source the title of the equivalent IT article
        title_dirty = soup.findAll("a", { "lang" : "it" })
        
        # Whethethe the find gives back an empty list it means that the equivalent
        # doesn't exist.        
        if len(title_dirty) != 0:
            # Reprocess the title
            lang_2_title = title_dirty[0]['title'].split('—')[0].strip()
            
            # Add the title to the dictionary
            dictionary[i] = lang_2_title
        
    
    return dictionary