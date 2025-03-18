from configs import connection_url
import sys
import psycopg

from custom_exception import MissingDataError, InvalidDataError

from helpers import make_log


def check_moyolink_code(customer_id, password) -> dict:
    """
    Vérifie si le couple (customer_id, password) est valide.
    
    :param customer_id: L'id du customer.
    :param password: Le mot de passe de l'application.
    """
    try:
        if not customer_id or not password:
            raise MissingDataError("CustomerId ou password absent")

        with psycopg.connect(connection_url, row_factory=psycopg.rows.dict_row) as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "SELECT * FROM call_verifications WHERE 'customerId'=%s and password=%s",
                    (customer_id, password),
                )
                record = cur.fetchone()

                if record:
                    return {"success": True, "data": {"code": record}}
                else:
                    raise InvalidDataError("Le code de l'application est invalide")
    except Exception as e:
        raise e


def main():
    try:
        customer_id = str(sys.argv[1])
        password = str(sys.argv[2])

        check_moyolink_code(customer_id, password)
    except MissingDataError as e:
        make_log(str(e), 4)
        return {"success": False, "message": str(e)}
    except InvalidDataError as e:
        make_log(str(e), 4)
        return {"success": False, "message": str(e)}
    except Exception as e:
        make_log(str(e), 4)
        return {"success": False, "message": str(e)}


print(main())
