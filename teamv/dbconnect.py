import os, psycopg2, urlparse

def connect_to_db():
    urlparse.uses_netloc.append("postgres")
    url = urlparse.urlparse(os.environ["DATABASE_URL"])
    
    try:
        conn = psycopg2.connect(
            database=url.path[1:],
            user=url.username,
            password=url.password,
            host=url.hostname,
            port=url.port
        )
    except:
        print "ERROR: Cannot connect to database"

    conn.autocommit = True
    return conn
