from configs import connection_url, psycopg
import sys

try:
    customer_id = str(sys.argv[1])
    password = str(sys.argv[2])
    if not customer_id or not password:
        print("False")
    
    
    with psycopg.connect(connection_url) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM subscriber WHERE customerId=%s and password=%s", (customer_id, password))
            record = cur.fetchone()
            
            if(record):
                print("True")
            else:
                print("False")
except Exception as e:
    print("False")