### Date created
October 18, 2020

### Project Title
Explore US Bikeshare Data with Python

### Description
In this project, we make use of Python to explore data related to bike share systems for three major cities in the United States—Chicago, New York City, and Washington. We have written code to import the data and answer interesting questions about it by computing descriptive statistics. We have also written a script that takes in raw input to create an interactive experience in the terminal to present these statistics.

The bikeshare.py file is set up as a script that takes in raw input to create an interactive experience in the terminal that answers questions about the dataset. The experience is interactive because depending on a user's input, the answers to the questions on the previous page will change! There are four questions that will change the answers:

1. Would you like to see data for Chicago, New York, or Washington?
2. Would you like to filter the data by month, day, or not at all?
3. (If they chose month) Which month - January, February, March, April, May, or June?
4. (If they chose day) Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?

The answers to the questions above will determine the city and timeframe on which you'll do data analysis. After filtering the dataset, users will see the statistical result of the data, and choose to start again or exit.

The script also will prompt the user whether they would like want to see the raw data. If the user answers 'yes,' then the script should print 5 rows of the data at a time, then ask the user if they would like to see 5 more rows of the data. The script should continue prompting and printing the next 5 rows at a time until the user chooses 'no,' they do not want any more raw data to be displayed.

### Files used
- chicago.csv
- new_york_city.csv
- washington.csv

### Credits
* Udacity Explore US Bikeshare Data project
* Mentor review
