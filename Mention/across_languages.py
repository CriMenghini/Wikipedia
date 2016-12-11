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
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup


def article_mentions(json_, string):
    """ This funtion returns the data frame of articles and the number of times they mention Matteo Renzi.
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

dict_italian = {}
for i in df_pt_titles['Title']:
    #print (i)
    title = i.replace(' ','_')
    req = requests.get('https://pt.wikipedia.org/wiki/' + title)
    html = req.content
    soup = BeautifulSoup(html, 'html.parser')
    title_dirty = soup.findAll("a", { "lang" : "it" })
    if len(title_dirty) != 0:
        ita_title = title_dirty[0]['title'].split('—')[0].strip()
        dict_italian[i] = ita_title