# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 11:52:04 2016

@author: cristinamenghini
"""

""" --------------------------------------------------------------------------
    This script contains the class used to parse wikimedia xml
----------------------------------------------------------------------------"""

# Import useful library
import xml.sax
from helpers_parser import *

# Define global variables
list_prova = []
language = 'italian'

# Define the class to parse wikimedia xlm

class WikiHandler(xml.sax.ContentHandler):
    
    def __init__(self):
        """An instance created by that class is characterized by the following 
        attributes:
        
        @CurrentData: tag that is being parsed,
        @title: name of the article
        @text : content of the article."""
        
        # All the attributes are initialized as empty strings
        self.CurrentData = ""
        self.title = ""
        self.text = ""
    
    
    def startElement(self, tag, attributes):
        """This method provides the current analyzed tag of the xml. It is 
        recalled when a new element of the xml is called.
        
        @tag: name of the element
        @attributes: optional attribute of the tag."""
    
        # Adjourn the name of the tag of the element
        self.CurrentData = tag

    
    def endElement(self, tag):
        """This method processes the content of the articles and keeps only 
        those that contain 'Matteo Renzi'. It is recalled when all the element
        has been inspected.
        
        @tag: name of the element"""
        
        # Define the global variables used to store the data
        global list_prova
        global language
        
        # Define the text of the article and the presence of matches
        mod_text, match = find_match(list_prova, 'Matteo Renzi')
        
        # Whether there is a match the article is stored
        if match != None:
            #print ('MATCH RENZI')
            load_json(self.title, mod_text, language)
        
        # Re-initialize the list that contains the article's elements 
        list_prova = []
        # Re-initialize two entity attributes
        self.CurrentData = ""
        self.text = ""
    
    
    def characters(self, content):
        """ This method assigns the content of the inspected element to the
        instance attribute 'title' and store in the global variable the 
        elements that compose the text of the article."""
        
        # Whether the inspected tag is 'title'
        if self.CurrentData == "title":
            # Assign its content to the instance attribute 'title'
            self.title = content
        
        # Whether the inspected tag is 'text'
        elif self.CurrentData == "text":  
            
            # Recall the global variable
            global list_prova
            
            # Append content to it
            list_prova += [content]
                          