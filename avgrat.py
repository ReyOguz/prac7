#!/usr/bin/python3

import sys
import psycopg2 as pg


def main(argv):
    print('first')
    if len(argv) != 3:
        print("Usage: ./avgrat taster|beer|brewer Name")
        return
    
    print('second')

    category = str(argv[1])
    name = str(argv[2])

    if (category != 'taster') or (category != 'beer') or (category != 'brewer'):
        print("Usage: ./avgrat taster|beer|brewer Name")
        return
    
    print('third')

    con = pg.connect("dbname=beer")
    cur = con.cursor()

    if category == 'taster':
        cur.execute('select from avgTaster(%s)',[name])
        print(cur.fetchone()[0])
        return 
    # elif category == 'beer':
    #     return 
    # else:
    #     # category = brewer
    #     return
    
    con.close()

main(sys.argv)

