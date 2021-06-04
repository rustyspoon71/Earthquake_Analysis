# Overview

I decided to get a little more familiar with data analysis and with json data so I decided to do a little project. As I feel it is important to know how to work with JSON data
as it is very common.

I am analyzing the US.Gov earthquake data giving the following options: past hour of earthquakes, past day of earthquakes, and past 30 days(month) of earthquakes. 
Here is the link to the data sets.
month: https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.geojson
hour : https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson
day  : https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson

I decided to analyze this because I wanted to see how common mag 5 earth quakes are. Not only that but how many earthquakes happen every hour. Then also by location for each
type of these data sets.





[EarthQuake Analysis](https://youtu.be/ofQ3R7ZPknc)

# Data Analysis Results
How many Earhquakes have happened in the past 24 hours? It was interesting as I ran through my results as many times it was between 
200-300.

Which Places have the most Earthquakes?  Almost in all the situations it was California. As it was greatly higher.

How common are magnitude 5 earthquakes? They are more common then we think as in a 24 hour amount of time there was 22. While over 
a month its 200+.

# Development Environment

I used Visual Studio code to develop the program.

I used python and the requests library to do this program.

# Useful Websites

{Make a list of websites that you found helpful in this project}
* [Earthquake.us.gov](https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php)
* [Python Dictionary Functions](https://www.w3schools.com/python/python_ref_dictionary.asp)

# Future Work

{Make a list of things that you need to fix, improve, and add in the future.}
* Incorporate boundaries for different time windows a user can enter.
* Find typos and merge them in the dictionary for example "CA" and "California" to make them one value.
* Let the user enter a state or country they would like to see data for.
