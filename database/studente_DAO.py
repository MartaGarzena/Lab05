# Add whatever it is needed to interface with the DB Table studente

from database.DB_connect import get_connection

from model.studente import Studente
from database.DB_connect import get_connection, DBConnect


def getAllStudents():
    cnx = get_connection()
    res = []

    cursor = cnx.cursor(dictionary=True)
    query = "select * from studente"
    cursor.execute(query)

    for row in cursor:
        res.append(Studente(row["matricola"], row["nome"], row["cognome"], row["CDS"]))

    cnx.close()
    return res

if __name__ == '__main__':
    for e in getAllStudents():
        print(e, isinstance(e, Studente))
