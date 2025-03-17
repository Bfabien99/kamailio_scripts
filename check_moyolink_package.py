from configs import connection_url, sys, psycopg

try:
    ## recuperation de l'id du package 
    package_id = str(sys.argv[1])
    if not package_id:
        print("False")
    
    ## recupere les informations requises de la bd
    with psycopg.connect(connection_url) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM packages WHERE id=%s", (package_id,))
            record = cur.fetchone()
            
            if(record):
                print("True")
            else:
                print("False")
except Exception as e:
    print("False")