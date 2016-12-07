# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 12:43:48 2016

@author: cristinamenghini
"""

""" --------------------------------------------------------------------------
    This script contains helper functions for the parser.
----------------------------------------------------------------------------"""

# Import useful libraries
import re
import json


def find_match(list_prova, string):
    """ This function returns the text of the article and the matches, in the 
    article, with the provided string.
    It takes as inputs:
    
    @list_prova: list of the elements present in the tag "text"
    @string: string to match in the text"""
    
    # Join the elements of @list_prova in a unique string
    text = ' '.join(list_prova)
        
    # Replece '\n' with whitespace
    mod_text = text.replace('\n', ' ')
        
    # Look up for matches with 'Matteo Renzi' performing a case-insensitive
    # matching.
    match = re.search(string, mod_text, flags=re.I)
    
    return mod_text, match
    
    
def load_json(title, text_to_load, language):
    """ This function create (whether it doesn't exist) and append to a .json 
    file the title and the content of each article that contains 'Matteo Renzi'. 
    It takes as inputs:
    
    @title: name of the article
    @text_to_load: text of the article
    @language: language of the article"""
    
    with open('Corpus/wiki_' + language + '_matteo_renzi.json', "a+") as json_file:
        # Each element of the json is stored in line 
        json_file.write("{}\n".format(json.dumps({'title': title, 'text': text_to_load})))
