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
        print(cur.execute('select * from avgTaster(%s)',[name]))
        print(cur.fetchone())
        return 
    # elif category == 'beer':
    #     return 
    # else:
    #     # category = brewer
    #     return
    
    con.close()

main(sys.argv)

