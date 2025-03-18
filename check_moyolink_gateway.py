from configs import connection_url
import sys
import psycopg

from custom_exception import MissingDataError, InvalidDataError

from helpers import make_log
    
def check_moyolink_gateway(callee_phone_number: str = "") -> dict:
    """
    Verifie si le gateways est valide
    
    :param callee_phone_number: Le numéro à appelé contenant le code du gateway.
    """
    try:
        if not callee_phone_number:
            raise MissingDataError("Le numéro à joindre est absent")

        ## recupération des 5 premiers caractères representant le code du gateway
        gateway_code = str(callee_phone_number[0:5]).upper()
        ## recupération du numéro sans le gateway
        number_whithout_code = str(callee_phone_number[5:])

        # recupération du realm du gateways
        with psycopg.connect(connection_url, row_factory=psycopg.rows.dict_row) as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "SELECT realm, password FROM gateways WHERE code=%s",
                    (gateway_code,),
                )
                record = cur.fetchone()

                if record:
                    return {
                        "success": True,
                        "data": {"gateway": record, "callee": number_whithout_code},
                    }
                else:
                    raise InvalidDataError("Le code du gateway est invalide")
    except Exception as e:
        raise e


def main():
    try:
        ## récupération du numéro de téléphone
        phone_number = str(sys.argv[1])

        check_moyolink_gateway(phone_number)
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
