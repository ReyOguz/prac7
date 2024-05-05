import sys
import psycopg2 as pg

def main():

    if len(sys.argv) != 3:
        print ('Usage: course-roll subject term')
        print('\n')
        return

    subj = sys.argv[1]
    term = sys.argv[2]

    conn = pg.connect("dbname=uni")
    cur = conn.cursor()

    cur.execute("select exists (select 1 from subjects where code = %s)", [subj])

    if not cur.fetchone()[0]:
        print(f'Invalid subject {subj}')
        print('\n')
        conn.close()
        return
    
    cur.execute("select id from subjects where code = %s", [subj])
    subj_id = cur.fetchone()[0]
    
    cur.execute('select exists (select 1 from terms where code = %s)', [term])
    if not cur.fetchone()[0]:
        print(f'Invalid term {term}')
        print('\n')
        conn.close()
        return
    
    cur.execute('select id from terms where code = %s)', [term])
    term_id = cur.fetchone()[0]

    cur.execute('select exists (select 1 from courses where subject = %s and term = %s)', [subj_id, term_id])

    if not cur.fetchone()[0]:
        print(f'No offering: {subj} {term}')
        print('\n')
        conn.close()
        return
    
    cur.execute('select if from courses where subject = %s and term = %s)', [subj_id, term_id])
    course_id = cur.fetchone()[0]


    cur.execute('select longname from subjects where id = %s'[subj_id])
    print(f'{subj} {term} {cur.fetchone()[0]}')

    cur.execute('''
    select p.id, p.family, p.given from
    people p 
    join students s on (p.id = s.id)
    join course_enrolments ce on ce.student = s.id 
    where ce.course = %s
    order by p.family, p.given''', [course_id])

    for s in cur.fetchall():
        print(f'{s[0]} {s[1]}, {s[2]}')

    print('\n')
    conn.close()
    return
    

main()