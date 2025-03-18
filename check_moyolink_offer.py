from configs import connection_url
import sys
import psycopg

from custom_exception import MissingDataError, InvalidDataError

from helpers import make_log


def check_offer_id(offer_id: str = "") -> dict:
    """
    Vérifie si l'offre est valide
    
    :param offer_id: L'id de l'offre
    """
    try:
        if not offer_id:
            raise MissingDataError("L'id de l'offre est absent")

        ## recupération de l'id et du price de l'offer
        with psycopg.connect(connection_url, row_factory=psycopg.rows.dict_row) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT id, price FROM offers WHERE id=%s", (offer_id,))
                record = cur.fetchone()

                if record:
                    return {"success": True, "data": {"offer": record}}
                else:
                    raise InvalidDataError("L'id de l'offre est invalide")
    except Exception as e:
        raise e


def main():
    try:
        ## recupération de l'id de l'offre
        offer_id = str(sys.argv[1])

        check_offer_id(offer_id)
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
