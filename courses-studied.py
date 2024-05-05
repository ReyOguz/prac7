#!/usr/bin/python3

import sys
import psycopg2 as pg2

def main():
    if len(sys.argv) < 3:
        print('Usage: ./courses-studied studentID term')
        return

    stuId = str(sys.argv[1])
    term = str(sys.argv[2])

    con = pg2.connect("dbname=uni")

    cur = con.cursor()

    cur.execute('select exists (select 1 from students where id = %s)', [stuId])
    exists = cur.fetchone()[0]

    if not exists:
        print('No such student')
    else:
        cur.execute('''
            from course_enrolments c1
            join courses c2 on (c1.course = c2.id)
            join subjects s on (c2.subject = s.id)
            join terms t on (c2.term = t.id)
            where c1.student = %s and t.code = %s
            ''', [stuId, term])
        list = cur.fetchall()
        for t in list:
            print(f'{t[0]} {t[1]}')

    con.close()
    return
        

main()

