from configs import connection_url
import sys
import psycopg

from custom_exception import MissingDataError, InvalidDataError

from helpers import make_log


def check_package_id(package_id: str = "") -> dict:
    """
    Vérifie si le package est valide
    
    :param package_id: L'id du package
    """
    try:
        if not package_id:
            raise MissingDataError("L'id du package est absent")

        ## recupération de l'id et du price de l'package
        with psycopg.connect(connection_url, row_factory=psycopg.rows.dict_row) as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "SELECT id, price, is_available FROM packages WHERE id=%s",
                    (package_id,),
                )
                record = cur.fetchone()

                if record:
                    return {"success": True, "data": {"package": record}}
                else:
                    raise InvalidDataError("L'id du package est invalide")
    except Exception as e:
        raise e


def main():
    try:
        ## recupération de l'id du package
        package_id = str(sys.argv[1])

        print(check_package_id(package_id))
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
