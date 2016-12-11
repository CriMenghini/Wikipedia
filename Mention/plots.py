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
    """ This fuction return the boxplot of the distribution of the labels respect the two 
    raters.
    
    It takes as inputs:
    @label_1: the labels given by rater 1
    @label_2: the labels given by rater 2"""
    
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
    
    
trace0 = go.Scatter(
    x = df_it_mension_pageview['Number of mentions'],
    y = df_it_mension_pageview['Pageviews'],#/sum(df_it_mension_pageview['Pageviews'])*100,
    name = 'Italian',
    mode = 'markers',
    text= df_it_mension_pageview['Title'],
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
    x = df_pt_mension_pageview['Number of mentions'],
    y = df_pt_mension_pageview['Pageviews'],#/sum(df_pt_mension_pageview['Pageviews'])*100,
    name = 'Portuguese',
    mode = 'markers',
    text= df_pt_mension_pageview['Title'],
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
              yaxis = dict(title = 'Pageviews'),
              xaxis = dict(title = 'Number of mentions')
             )

fig = dict(data=data, layout=layout)
py.iplot(fig, filename='mentions-pv')