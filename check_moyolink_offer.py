from configs import connection_url, psycopg
import sys

try:
    ## recupération de l'id de l'offre
    offer_id = str(sys.argv[1])
    if not offer_id:
        print("False")
    
    ## recupération de l'id et du price de l'offer
    with psycopg.connect(connection_url) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT id, price FROM offers WHERE id=%s", (offer_id,))
            record = cur.fetchone()
            
            if(record):
                print("True")
            else:
                print("False")
except Exception as e:
    print("False")