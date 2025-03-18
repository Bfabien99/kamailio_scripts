from configs import connection_url
import sys
import psycopg

from custom_exception import MissingDataError, InvalidDataError

from helpers import make_log


def check_moyolink_subscriber(customer_id, password) -> dict:
    """
    Vérifie si le couple (customer_id, password) est valide.
    
    :param customer_id: L'id du customer.
    :param password: Le mot de passe du customer.
    """
    try:
        if not customer_id or not password:
            raise MissingDataError("CustomerId ou password absent")

        with psycopg.connect(connection_url, row_factory=psycopg.rows.dict_row) as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "SELECT * FROM subscriber WHERE 'customerId'=%s and password=%s",
                    (customer_id, password),
                )
                record = cur.fetchone()

                if record:
                    return {"success": True, "data": {"subscriber": record}}
                else:
                    raise InvalidDataError("Informations incorrecte")
    except Exception as e:
        raise e


def main():
    try:
        customer_id = str(sys.argv[1])
        password = str(sys.argv[2])

        check_moyolink_subscriber(customer_id, password)
    except MissingDataError as e:
        print(str(e))
        make_log(str(e), 4)
    except InvalidDataError as e:
        print(str(e))
        make_log(str(e), 4)
    except Exception as e:
        print(str(e))
        make_log(str(e), 4)


print(main())
