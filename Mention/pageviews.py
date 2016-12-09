# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 16:53:45 2016

@author: cristinamenghini
"""

""" --------------------------------------------------------------------------
This script contains fuctions to do pageviews analysis.
----------------------------------------------------------------------------"""

# Import useful libraries
import json
import codecs
import pandas as pd


def article_df_from_json(json_):
    """ This funtion returns the data frame of article titles that mention the 
    string of interest.
    It takes as input:
    
    @json_: is the path of the .json to import"""
    
    # Initialise the list to store titles
    list_titles = []
    
    # Read line by line 
    with codecs.open(json_,'rU','utf-8') as f:
        for line in f:
            list_titles.append(json.loads(line)['title'])
    
    # Convert list titles in a df
    list_titles = pd.DataFrame(list_titles, columns=['Title'])
    
    return list_titles
    

def get_pageviews(lang_dict, title_split, split_line):
    """ This function add elements to the dictionary (key, value): (title, pageviews) 
    and returns the dictionary. 
    It takes as inputs:
    
    @lang_dict: the dictionary to adjourn
    @title_split: list of elements in the second column (splitting by ':')
    @split_line: three column entries of a line of the pageviews file"""
    
    # Check whether the split by ':' produces more than one element
    if len(title_split) == 2:
        # Add the article and the respective pageviews to the dictionary
        lang_dict[title_split[1].replace('_', ' ')] = int(split_line[2])
    
    elif len(title_split) == 1:
        # Add the article and the respective pageviews to the dictionary
        lang_dict[title_split[0].replace('_', ' ')] = int(split_line[2])
        
    return lang_dict
    

def filter_pageviews_file(file_name, language_list):
    """ This function return the dictionary (key,(key,value)):('Initials language',('Title','No. pageviews')). 
    It is obtained filtering by the language of the article.
    It takes as inputs:
    
    @file_name: name of the pageviews file to read (i.e. pagecounts-2011-12-views-ge-5-totals)
    @language_list: initials of the language of interest"""
    
    # Initialize the output dictionary
    language_articles_list = {}
    
    # Sort language list
    language_list = sorted(language_list)
    
    # Initialize dictionary for each language
    for language in language_list:
        language_articles_list[language] = {}
      
    with open(file_name) as file:
        # For each line (namely one article)
        for line in file:
            # Split it by the white space
            split_line = line.split(' ')

            # Get title - split second entry of the line by ':'
            title_split = split_line[1].split(':')
            
            
            # Filter by the language namespace
            for lang in language_list:
                if split_line[0].startswith(lang):
                    # Adjurne the language dictionary
                    language_articles_list[lang] = get_pageviews(language_articles_list[lang], title_split, split_line)
                    break

    return language_articles_list
    

def define_ranked_df(dict_art, lang, mention_title):
    """ This funtion returns a DataFrame with columns ['Title', 'Pageviews'] for the specific language
    sorted by the pageviews.
    It takes as inputs:
    
    @dict_art: dictionary (key,(key,value)):('Initials language',('Title','No. pageviews'))
               [return filter_pageviews_file function]
    @lang: string initials of the language of interest
    @mention_title: DataFrame of the articles that contain the word of interest"""
    
    # Define a Dataframe with columns ['Title', 'Pageviews'] for the specified language
    df_total_article = pd.DataFrame(list(dict_art[lang].items()), columns=['Title', 'Pageviews'])

    # Right join between the just defined df and the @mention_title df
    interested_art = pd.merge(df_total_article, mention_title, how = 'right', on=['Title'])
    
    
    # Get the df with all the visited articles of the month
    visited_article = interested_art[interested_art['Pageviews'].notnull()]
    
    print ('Over the whole number of articles in the corpus ', len(interested_art)-len(visited_article), ' have not been visited during the considered perion.')
    
    # Sort the df by the pageviews
    ranked_articles = visited_article.sort_values('Pageviews', ascending = False)
    
    return ranked_articles
    
