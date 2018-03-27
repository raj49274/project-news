# Project-news

This project is about extracting data from news database using sql statements

## Content
1) project_news.py
2) result.txt

## Aditional requirement
data base file ( https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip )

## How to run
1) ensure that you have vagrant and virtualbox.
2) put all file in vagrant shared directory
3) open your terminal in your pc and login to vagrant machine (by vagrant ssh).
4) change your current working directory to vagrant folder
5) put your database file into vagrant folder ( https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip )
6) to load data base run ( psql -d news -f newsdata.sql ) in your terminal
6) run the command 'python project_news.py'

## about
Answering three question about database
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?
