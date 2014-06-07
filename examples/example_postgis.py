import psycopg2

conn = psycopg2.connect("dbname=test user=postgres")
cur = conn.cursor()

sql = "SELECT states.name, county.name"
sql += " FROM states, county"
sql += " WHERE states.name = 'Texas' AND ST_Contains(states.geom, county.geom)"
cur.execute(sql)

for item in cur.fetchall():
    print item

#shp2pgsql -s 4326 states > states.sql
#psql -d test -h localhost -U postgres -f states.sql