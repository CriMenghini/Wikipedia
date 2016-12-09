# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 11:52:04 2016

@author: cristinamenghini
"""

""" ----------------------------------------------------------------------------
This script contains a class to parse wikimedia xml and a function to execute it.
------------------------------------------------------------------------------"""

# Import useful library
import xml.sax
from helpers_parser import *

# Define the class to parse wikimedia xlm

class WikiHandler(xml.sax.ContentHandler):
    
    """-------------------------------------------------------------------------------------------
    This class defines a parser for the Wikimedia dump for a specific language in xml format (i.e. 
    https://dumps.wikimedia.org/itwiki/20161120/itwiki-20161120-pages-articles-multistream.xml.bz2)
    
    More information about the data is in the README file.
    
    To parse the file SAX parser has been used. The reason behind the choice is that due to the 
    size of the document to parse, rather that load in memory the entire file, it is inspected 
    going through elements one by one.
    --------------------------------------------------------------------------------------------"""
    
    def __init__(self, language, topic):
        """An instance created by that class is characterized by the following 
        attributes:
        
        @CurrentData: tag that is being parsed
        @title: name of the article
        @text: content of the article
        @language: language you are workig with
        @topic: string (i.e. word, regular expression)
        @_charBuffer: buffer for the article content."""
        
        # Attributes initialization as empty strings
        self.CurrentData = ""
        self.title = ""
        self.text = ""
        self.language = language
        self.topic = topic
        self._charBuffer = []
    
    
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
        
        # Define the text of the article and the presence of matches
        mod_text, match = find_match(self._charBuffer, self.topic)
        
        # Whether there is a match the article is stored
        if match != None:
            #print ('MATCH STRING')
            load_json(self.title, mod_text, self.language, self.topic)
        
        # Re-initialize the buffer that contains the article's elements 
        self._charBuffer = []
        # Re-initialize two entity attributes
        self.CurrentData = ""
        self.text = ""
    
    
    def characters(self, content):
        """ This method assigns the content of the inspected element to the
        instance attribute 'title' and store in the global variable the 
        elements that compose the text of the article.
        
        @content: conten of the tag"""
        
        # Whether the inspected tag is 'title'
        if self.CurrentData == "title":
            # Assign its content to the instance attribute 'title'
            self.title = content
        
        # Whether the inspected tag is 'text'
        elif self.CurrentData == "text":  

            self._charBuffer.append(content)             
                          
                          
def parse_articles(language, xml_, topic):
    """ This function executes the parse of the articles.
    It takes as inputs:
    
    @language: language of the articles
    @xml_: file to parse
    @topic: string (i.e. word, regular expression)"""
    
    # create an XMLReader
    parser = xml.sax.make_parser()
    
    # Define the new Handler
    Handler = WikiHandler(language, topic)
    parser.setContentHandler(Handler)
    
    # Parse
    parser.parse(xml_)