# Roster to Twitter
This is an application for taking in a roster and returning a list of Twitter handles for each player. It works by
reading in names and searching for them using Twitters API. It then enhances the search results by highlighting those 
who are followed by a player on the roster and moving them to the top of the list. 

## Why only Twitter?
Theoretically, the same thing can be done with other social medias and the goal of the project was to include Twitter, Instagram, 
and Snapchat. Sadly these are the state of the APIs:

* **Snapchat**: Nonexistent, at one point their was an unofficial API but it has since been taken down. 
    * Apparently Davyeon knows someone high up there so it may be possible but would require special partnership
* **Instagram**: Since the Facebook acquisition the API has slowly been develving, at this point you have to fill out an application
that includes a video and an essay, which I didn't have time for, and it seems like this app would still be rejected. 
* **Twitter**: The api is great 

This is why it only works for Twitter, it would be easy to extend it to these other playforms if it weren't for their APIs. 

## How to use

1. Upload the roster in .xlsx format with a column that has a players name

or
1. Use an espn link to a roster page

2. Find the players accounts use
3. Click the download button

## Tech Stack

This project is coded in Python but there are three big libraries used in this application:

#### Django 

This is the web framework used to create the site. The documentation is great on
[their website](https://docs.djangoproject.com/en/2.0/) but also [this tutorial](https://tutorial.djangogirls.org/en/) 
is really good. 

#### Openpyxl

Python library for dealing with Excel files, documentation [here](https://openpyxl.readthedocs.io/en/stable/).

#### Tweepy

Python library for Twitter, Cursor feature is awesome and saves API calls, documentation 
[here](http://tweepy.readthedocs.io/en/v3.5.0/)