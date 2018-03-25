import psycopg2

db = psycopg2.connect("dbname=news")
c = db.cursor()

# first question
query1 = "SELECT articles.slug , put.path, put.num, articles.title from articles,\
         (SELECT path, COUNT(*) as num FROM log\
         GROUP BY path ORDER BY num desc\
         LIMIT 3 OFFSET 1) as put order by num desc"
c.execute(query1)
posts = c.fetchall()
print "What are the most popular three articles of all time?"
print
for post in posts:
    if post[0] == post[1][9:]:
        print post[3],"--", post[2], "views"

# second question

query2 = "SELECT authors.name, sum(tiger.num) as views from authors,\
          (SELECT Substring(path, 10) as paths, COUNT(*) as num FROM log\
          GROUP BY path ORDER BY num desc\
          LIMIT 10 OFFSET 1) as tiger\
          join\
          (SELECT author, slug from articles) as lion \
          on tiger.paths = lion.slug \
          where authors.id = lion.author \
          group by authors.name order by views desc"
c.execute(query2)
oath = c.fetchall()
print
print "Who are the most popular article authors of all time?"
print

for name in oath:
    print name[0], "--", name[1], "views"


# third question

query3 = "SELECT lion.days, (cast(tiger.num2 as INTEGER)/cast(lion.num as FLOAT))*100\
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
print
for item in rush:
    if item[1] > 2:
        print item[0], "--", round(item[1], 2), "%" + " error"



db.close()

