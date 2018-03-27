#!/usr/bin/env python
import psycopg2
import sys


def connect(database_name):
    """Connect to the database.  Returns a database connection."""
    try:
        db = psycopg2.connect(dbname=database_name)
        return db

    except psycopg2.Error as e:
        # THEN you could print an error
        # and perhaps exit the program
        print ("Unable to connect to database")
        sys.exit(1)

db = connect("news")
c = db.cursor()


def execute_query(query):
    c.execute(query)
    posts = c.fetchall()
    return posts


# first question
def print_top_articles():
    """Prints out the top 3 articles of all time."""
    query = """
        SELECT title, count(*) AS views
        FROM log
        JOIN articles
            ON log.path = concat('/article/', articles.slug)
        GROUP BY title
        ORDER BY views desc
        LIMIT 3;"""
    results = execute_query(query)
    # add code to print results
    print "What are the most popular three articles of all time?"
    for result in results:
        print result[0], "--", result[1], "views"


# second question
def print_top_authors():
    """Prints a list of authors ranked by article views."""
    query = """SELECT authors.name, sum(tiger.num) as views from authors,
              (SELECT Substring(path, 10) as paths, COUNT(*) as num FROM log
              GROUP BY path ORDER BY num desc
              LIMIT 10 OFFSET 1) as tiger
              join
              (SELECT author, slug from articles) as lion
              on tiger.paths = lion.slug
              where authors.id = lion.author
              group by authors.name order by views desc;"""
    results = execute_query(query)
    # add code to print results
    print
    print "Who are the most popular article authors of all time?"
    for result in results:
        print result[0], "--", result[1], "views"


# third question
def print_errors_over_one():
    query = """SELECT lion.days, (cast(tiger.num2 as INTEGER)/cast(lion.num as FLOAT))*100
             as error from
             (SELECT date(time) as days, count(status) as num from log
             group by days) as lion
             join
             (SELECT date(time) as days, count(*) as num2 from log
             where status = '404 NOT FOUND'
             GROUP BY days) as tiger
             on lion.days = tiger.days"""
    results = execute_query(query)
    print
    print "On which days did more than 1% of requests lead to errors?"
    for result in results:
        if result[1] > 2:
            print result[0], "--", round(result[1], 2), "%" + " error"

if __name__ == '__main__':
    print_top_articles()
    print_top_authors()
    print_errors_over_one()
    db.close()
