from configs import connection_url
import sys
import psycopg

try:
    ## récupération du numéro de téléphone
    phone_number = str(sys.argv[1])
    if not phone_number:
        print("False")
    
    ## recupération des 5 premiers caractères representant le code du gateway
    gateway_code = str(phone_number[0:5]).upper()
    ## recupération du numéro sans le gateway
    number_whithout_code = str(phone_number[5:])
    
    # recupération du realm du gateways
    with psycopg.connect(connection_url) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT realm price FROM gateways WHERE code=%s", (gateway_code,))
            record = cur.fetchone()
            
            if(record):
                print("True")
            else:
                print("False")
except Exception as e:
    print("False")