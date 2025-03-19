from configs import connection_url
import sys
import psycopg

from helpers import format_for_kamailio

try:    
    ## récupération du numéro de téléphone
    callee_phone_number = str(sys.argv[1])
    if not callee_phone_number:
        print("success='False';message='Number to call is absent'")

    ## recupération des 5 premiers caractères representant le code du gateway
    gateway_code = str(callee_phone_number[0:5]).upper()
    ## recupération du numéro sans le gateway
    number_whithout_code = str(callee_phone_number[5:])

    # recupération du realm du gateways
    with psycopg.connect(connection_url, row_factory=psycopg.rows.dict_row) as conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT * FROM gateways WHERE code=%s",
                (gateway_code,),
            )
            record = cur.fetchone()

            if record:
                record_str = format_for_kamailio(record)
                print(f"success='True';{record_str};callee='{number_whithout_code}'")
            else:
                print("success='False';message='Gateway code is invalid'")
except Exception as e:
    print(f"success='False';message='{str(e)}'")