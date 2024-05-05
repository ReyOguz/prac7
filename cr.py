#!/usr/bin/python3

import sys
import psycopg2 as pg2

def main():
    if len(sys.argv) < 3:
        print('Usage: course-roll subject term')
        print('\n')
        return
    
    subj = str(sys.argv[1])
    term = str(sys.argv[2])

    con = pg2.connect("dbname=uni")

    cur = con.cursor()

    # cur.execute('select exists (select 1 from students where id = %s)', [stuId])
    # exists = cur.fetchone()[0]
   
    cur.execute('''
        select s2.id, p.family, p.given from course_enrolments c1
        join courses c2 on (c1.course = c2.id)
        join subjects s on (c2.subject = s.id)
        join terms t on (c2.term = t.id)
        join students s2 on c1.student = s2.id
        join people p on s2.id = p.id
        where s.code = %s and t.code = %s
        order by p.family, p.given
        ''', [subj, term])
    
    list = cur.fetchall()

    print(f'{subj} {term}')

    if len(list) == 0:
        print('No students')
    else: 
        for t in list:
            print(f'{t[0]} {t[1]}, {t[2]}')
    
    print('\n')
    con.close()
    return
        

main()

