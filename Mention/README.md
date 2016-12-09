# Analize how much and how a *word* or a *regular expression* is mentioned in Wikipedia pages across languages

The proposed scripts allow you to study the mentions of a certain *word* across languages using *Wikipedia* articles. 

## Get data to analyse

### Built the corpus

The data in usage are available on [Wikimedia Downloads](https://dumps.wikimedia.org/backup-index.html) page. Once you are on the Web Site you can choose the language and the date (data referring to *Wikipedia* data until that date)you are interested in to carry out the analysis (i.e. suppose you want to have all the Italian articles you follow the link [`itwiki`](https://dumps.wikimedia.org/ltwiki/20161201/) - referring to a certain date-  and then you proceed downloading the dump `ltwiki-DATE-pages-articles-multistream.xml.bz2 `, where `DATE` will be the date that corresponds to your interest. The dump contains articles, templates, media/file descriptions, and primary meta-pages). This data will be the *corpus* for your analysis.

### Additional data

For analysis that want to take into account other factors, like the pageviews of the articles, through this [link](https://dumps.wikimedia.org/other/pagecounts-ez/merged/) it is possible to get the pageviews for the whole *Wikipedia* corpus for each month since 2011. The documentation related to this data is provided [here](https://dumps.wikimedia.org/other/pagecounts-raw/).

## Script's descriptions



## IPython Notebook example
The goal of this little work is to:

* Find all articles in Italian and Portuguese that mention Matteo Renzi

![](matteo_renzi.png?raw=true)

The code to accomplish this task is stored in the `.py` files mentioned below:

1. `wiki_parser.py`: contains the class used to parse wikimedia `xml`
2. `helpers_parser.py`: gathers functions applied during the parse. 

* Rank them by how frequently they were viewed in November.


Then to play a bit with data:

* Explore the differences between IT and PT in terms of numbers and plots. Are there distinct differences between the languages in terms of what kinds of articles mention Renzi? What's the distribution of number of Renzi mentions per article in IT vs. PT? 