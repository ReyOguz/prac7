#!/usr/bin/python3

import sys
import psycopg2 as pg


def main(argv):
    if len(argv) != 3:
        print("Usage: ./avgrat taster|beer|brewer Name")
        return
    
    category = str(argv[1])
    name = str(argv[2])

    if (category != 'taster') and (category != 'beer') and (category != 'brewer'):
        print("Usage: ./avgrat taster|beer|brewer Name")
        return

    con = pg.connect("dbname=beers")
    cur = con.cursor()

    if category == 'taster':
        cur.execute('select * from avgTaster(%s)',[name])
        print(cur.fetchone()[0])    
    elif category == 'beer':
        cur.execute("select * from avgBeer(%s)", [name])
        print(cur.fetchone()[0])        
    else:
        cur.execute("select * from avgBrewer(%s)", [name])
        print(cur.fetchone()[0])
    con.close()
    return


main(sys.argv)

















