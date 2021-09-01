# Overview
This page is meant to serve as the main documentation hub for our 30-minute weekly meetings to discuss and troubleshoot coding projects
Fall 2021: Wednesdays from 11:00-11:30am at this zoom link

# Relevant Links
[link] <- 'Coding and Computational Thinking'

[link] FSL Prep Course, Online courses and educational games, written guides, etc.

[link] <- 'Introduction to Coding'

[link] Why coding is important, which languages to learn, conceptualizing the time course of learning new skills, external links (some overlap with first bullet), etc. 

[link] Basic, useful unix/linux tools

[link] Pros and cons of coding an experiment in different languages, with helpful external links

Tutorials:
MATLAB Onramp https://www.mathworks.com/learn/tutorials/matlab-onramp.html 

Introduction to Unix https://(http://fsl.fmrib.ox.ac.uk/fslcourse/online_materials.html)

# Problems to Solve:
<li>Renaming pdfs</li>

Write a script that reads in pdfs, reads the metadata, renames and writes out new pdfs;
From Scott: Extracting pdf metadata in Python: http://mstamy2.github.io/PyPDF2/


<li>Removing PII from .json files</li>

Almost all private data gets stripped out of .json files; however, when heudiconv writes out files with all fields, it includes the date and time of the scan, which is potentially PII; convention is to change that date by some constant
Problem: write script that shifts all scan dates by a constant


<li>Convert source data to BIDS format</li>

E.g., for Jimmy on ISTART effort data
Read in EPrime source data files and output .csv files in BIDS format


<li>Print min. and max. values from BIDS images</li>

Write a script that reads through all the image files in a directory and writes out the min and max value for each image as a data check
(E.g., if all files are supposed to be all positives and you have an image whose min. is negative, you know you have a problem)


<li>Program a task</li>

General project for applying coding skills in a practical way


<li>Convert image format to .png</li>
E.g., for ISTART Shared Reward task
