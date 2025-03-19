from configs import connection_url
import sys
import psycopg

from helpers import format_for_kamailio

try:
    customer_id = str(sys.argv[1])
    password = str(sys.argv[2])

    if not customer_id or not password:
        print("success='False';message='CustomerId ou password absent'")

    with psycopg.connect(connection_url, row_factory=psycopg.rows.dict_row) as conn:
        with conn.cursor() as cur:
            cur.execute(
                'SELECT * FROM subscriber WHERE "customerId"=%s and password=%s',  # Ajustez la syntaxe de la requête
                (customer_id, password),
            )
            record = cur.fetchone()

            if record:
                record_str = format_for_kamailio(record)
                print(f"success='True';{record_str}")
            else:
                print("success='False';message='Customer Id is invalid'")
except Exception as e:
    print(f"success='False';message='{str(e)}'")
