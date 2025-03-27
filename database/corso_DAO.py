# Add whatever it is needed to interface with the DB Table corso
import mysql

from model.corso import Corso
from database.DB_connect import get_connection, DBConnect


def getAllCorsi():
    cnx = get_connection()
    res = []

    cursor = cnx.cursor(dictionary=True)
    query = "select * from corso"
    cursor.execute(query)

    for row in cursor:
        res.append(Corso(row["codins"], row["crediti"], row["nome"], row["pd"]))

    cnx.close()
    return res

if __name__ == '__main__':
    for c in getAllCorsi():
        print(c)

        print(isinstance(c, Corso))


