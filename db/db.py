import psycopg2 as pg

CONNSTR = 'dbname=netology_diploma user=postgres'

def create_db():
    with pg.connect(CONNSTR) as conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS vkinder_candidates (
                        id serial PRIMARY KEY,
                        first_name varchar(50) NOT NULL,
                        last_name varchar(50) NOT NULL,
                        domain varchar(50) UNIQUE NOT NULL""")


def add_candidate(candidate, cursor):
    cursor.execute("""
       INSERT into vkinder_candidates (id, first_name, last_name, domain) 
       values (%s, %s, %s, %s) 
       returning id  
       """, (candidate['id'], candidate['first_name'],
             candidate['last_name'], candidate['domain']))
    candidate_id = cursor.fetchone()[0]
    return candidate_id




if __name__ == '__main__':
    create_db()
    add_candidate()
