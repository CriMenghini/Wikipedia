# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 00:58:23 2016

@author: cristinamenghini
"""

"""----------------------------------------------------------------------------
This script contains function used to make plots.
----------------------------------------------------------------------------"""

# Import useful libraries
import numpy as np
import plotly.plotly as py
import plotly.graph_objs as go


def boxplot_mentions(df_1, df_2, lang_1, lang_2, attribute): 
    """ This fuction return the boxplot of the distribution of the mentions respect the two 
    languages.
    
    It takes as inputs:
    @df_1: the labels given by rater 1
    @df_2: the labels given by rater 2
    @lang_1: name of lang 1
    @lang_2: name of lang 2
    @attribute: name of the variable to plot"""
    
    # Array to plot
    y0 = np.array(df_1[attribute])
    y1 = np.array(df_2[attribute])

    # Define the box-plot related to rater 1
    trace0 = go.Box(name = lang_1,
                    y=y0)
    
    # Define the box-plot  relates to rater 2
    trace1 = go.Box(y=y1,
                    name = lang_2)
    
    # List of data to plot
    data = [trace0, trace1]
    
    # Set up the layout
    layout = go.Layout(title='Distribution of the mentions in the IT and PT corpora',
               # Give labels to the axis
                       xaxis=dict(title='Language'),
                       yaxis=dict(title='Mentions'))
                       
    # Define the figure and plot it            	   
    fig = go.Figure(data=data, layout=layout)
    py.iplot(fig, filename='mentions-distr')
    

def scatter_plot(df_1, df_2, attr_1, attr_2, lang_1, lang_2):
    """ This function plots the observation according to two variables.
    It takes as inputs:
    
    @df_1: name of dataframe 1
    @df_2: name of dataframe 2
    @attr_1: name of the first variable
    @attr_2: name of the second variable
    @lang_1: language of first courpus of pages
    @lang_2: language of second courpus of pages"""
    
    trace0 = go.Scatter(
        x = df_1[attr_1],
        y = df_1[attr_2],#/sum(df_it_mension_pageview['Pageviews'])*100,
        name = lang_1,
        mode = 'markers',
        text= df_1['Title'],
        marker = dict(
            size = 10,
            color = 'rgba(152, 0, 0, .8)',
            line = dict(
                width = 2,
                color = 'rgb(0, 0, 0)'
            )
        )
    )
    
    trace1 = go.Scatter(
        x = df_2[attr_1],
        y = df_2[attr_2],#/sum(df_pt_mension_pageview['Pageviews'])*100,
        name = lang_2,
        mode = 'markers',
        text= df_2['Title'],
        marker = dict(
            size = 10,
            color = 'rgba(255, 182, 193, .9)',
            line = dict(
                width = 2,
            )
        )
    )
    
    data = [trace0, trace1]
    
    layout = dict(title = 'Articles respect Number of mentions and Pageviews',
                  yaxis = dict(title = attr_2),
                  xaxis = dict(title = attr_1)
                 )
    
    fig = dict(data=data, layout=layout)
    py.iplot(fig, filename='mentions-pv')



def bar_plot(df, x_att, y_att_1, y_att_2, var_1, var_2, title_, x_, y_, file_name):
    """This function plots a barplot for two variables. 
    It takes as inputs:
    
    @df: is the dataframe the data is take from
    @x_att: name of the attribute on x-axis
    @y_att_1: name of the attribute on y-axis for var 1
    @y_att_2: name of the attribute on y-axis for var 2
    @var_1: name of var 1
    @var2: name of var 2
    @title_: name of the plot
    @x_: name of x-axis
    @y_:name of y-axis"""
    
    # Define first trace
    trace0 = go.Bar(x=df[x_att],
                    name=var_1,
                    y=df[y_att_1])
    
    # Define second trace
    trace1 = go.Bar(x=df[x_att],
                    name=var_2,
                    y=df[y_att_2])
    
    # Define data and layout
    data = [trace0, trace1]
        
    layout = go.Layout(title=title_,
                           xaxis=dict(title=x_),
                           yaxis=dict(title=y_))
    
    fig = go.Figure(data=data, layout=layout)
    
    # Save plot
    py.iplot(fig, filename=file_name)