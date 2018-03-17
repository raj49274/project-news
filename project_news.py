import psycopg2

db = psycopg2.connect("dbname=news")
c = db.cursor()

# first question
query1 = "SELECT path, COUNT(*) as num FROM log\
         GROUP BY path ORDER BY num desc\
         LIMIT 10 OFFSET 1"
c.execute(query1)
posts = c.fetchall()
print "What are the most popular three articles of all time?"
print
print "Candidate is jerk, alleges rival--- ", posts[0][1], "views"
print "Bears love berries, alleges bear--- ", posts[1][1], "views"
print "Bad things gone, say good people--- ", posts[2][1], "views"

# second question
query2 = "SELECT name FROM authors"
c.execute(query2)
oath = c.fetchall()
print
print "Who are the most popular article authors of all time?"
print
print oath[0][0], "--", posts[1][1] + posts[3][1] + posts[6][1] + posts[7][1],\
      "views"

print oath[1][0], "--", posts[0][1] + posts[4][1], "views"
print oath[2][0], "--", posts[2][1], "views"
print oath[3][0], "--", posts[5][1], "views"

# third question

query3 = "SELECT max((cast(tiger.num2 as INTEGER)/cast(lion.num as FLOAT))*100)\
         as error from \
         (SELECT date(time) as days, count(status) as num from log\
         group by days) as lion\
         join\
         (SELECT date(time) as days, count(*) as num2 from log \
         where status = '404 NOT FOUND'\
         GROUP BY days) as tiger\
         on lion.days = tiger.days"


c.execute(query3)
rush = c.fetchall()
print
print "On which days did more than 1% of requests lead to errors?"
print "july 17 2016 --", round(rush[0][0], 1), "%", "error"


db.close()
