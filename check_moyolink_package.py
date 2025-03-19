from configs import connection_url
import sys
import psycopg

from helpers import format_for_kamailio

try:
    # récupération de l'id du package
    package_id = str(sys.argv[1])
    if not package_id:
        print("success='False';message='Package Id missing'")

    ## recupération de l'id et du price du package
    with psycopg.connect(connection_url, row_factory=psycopg.rows.dict_row) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT id, price FROM packages WHERE id=%s", (package_id,))
            record = cur.fetchone()

            if record:
                record_str = format_for_kamailio(record)
                print(f"success='True';{record_str}")
            else:
                print("success='False';message='Invalid package Id'")
except Exception as e:
    print(f"success='False';message='{str(e)}'")