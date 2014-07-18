import os, psycopg2, urlparse, logging

def connect_to_db():
    urlparse.uses_netloc.append("postgres")
    url = urlparse.urlparse("postgres://mgjnqgdtczqvpl:6_B_Em7CBcwQ8Ku5lCspwdBuTu@ec2-54-204-40-140.compute-1.amazonaws.com:5432/dfrbbcv9ojtbom")
    
    try:
        conn = psycopg2.connect(
            database=url.path[1:],
            user=url.username,
            password=url.password,
            host=url.hostname,
            port=url.port
        )
        conn.autocommit = True
    except:
        logging.error("Cannot connect to database")

    return conn
