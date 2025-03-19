from configs import connection_url
import sys
import psycopg

try:
    callee = str(sys.argv[1])
    callid = str(sys.argv[2])
    column_offer_or_package = str(sys.argv[3])
    offer_or_package_id = str(sys.argv[4])
    customer_id = str(sys.argv[5])
    price_per_minute = str(sys.argv[6])

    if not column_offer_or_package or not callee or not callid or not offer_or_package_id or not customer_id or not price_per_minute:
        print("success='False';message='Required field are missing'")

    with psycopg.connect(connection_url, row_factory=psycopg.rows.dict_row) as conn:
        with conn.cursor() as cur:
            # Adjusted SQL to use RETURNING to retrieve the inserted row
            stmt = cur.execute(
                f'''
                INSERT INTO calls(callee, "callId", "{column_offer_or_package}", customer_id, price_per_minute)
                VALUES(%s, %s, %s, %s, %s)
                ''',
                (callee, callid, offer_or_package_id, customer_id, price_per_minute),
            )

            if stmt:
                print(f"success='True';message='ok'")
            else:
                print("success='False';message='App code is invalid'")
except Exception as e:
    print(f"success='False';message='{str(e)}'")
