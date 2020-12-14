# Computer-Science-problems
Solve a series of simple computer science problems


This project is the first part of Udacity's [Data Structure & Algorithms Nanodegree program](https://www.udacity.com/course/data-structures-and-algorithms-nanodegree--nd256).
The objective is to solve a set of simple problems.

# Project Overview
In this project, complete five tasks based on a fabricated set of calls and texts exchanged during September 2016. Use Python to analyze and answer questions about the texts and calls contained in the dataset. Perform run time analysis of the solution and determine its efficiency.

# About the data

The text and call data are provided in csv files. Text file contains over 9000 logs. Call file contains over 5000 logs.

The text data (text.csv) has the following columns: sending telephone number (string), receiving telephone number (string), timestamp of text message (string).

The call data (call.csv) has the following columns: calling telephone number (string), receiving telephone number (string), start timestamp of telephone call (string), duration of telephone call in seconds (string)

All telephone numbers are 10 or 11 numerical digits long. Each telephone number starts with a code indicating the location and/or type of the telephone number. There are three different kinds of telephone numbers, each with a different format:

Fixed lines start with an area code enclosed in brackets. The area codes vary in length but always begin with 0. Example: "(022)40840621".
Mobile numbers have no parentheses, but have a space in the middle of the number to help readability. The mobile code of a mobile number is its first four digits and they always start with 7, 8 or 9. Example: "93412 66159".
Telemarketers' numbers have no parentheses or space, but start with the code 140. Example: "1402316533".

# Objectives
- Determine phone number with longest time spent over the phone
- profile the numbers called from Bangalore
- Determine which numbers could be disguised telemarketers
