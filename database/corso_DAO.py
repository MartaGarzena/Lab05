# Add whatever it is needed to interface with the DB Table corso
import mysql

from model.corso import Corso
from database.DB_connect import get_connection, DBConnect
from model.studente import Studente


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


def getAllStudents(codins):
    cnx = get_connection()
    result = []

    query = """SELECT studente.*  
                FROM iscrizione, studente 
                WHERE iscrizione.matricola=studente.matricola AND iscrizione.codins=%s"""
    #estrarre tutti i dettagli degli studenti (studente.*)
    #per cui la matricola in iscrizione è uguale a quella in studente
    # filtra per il codice corso ricevuto in input
    if cnx is not None:
        cursor = cnx.cursor(dictionary=True)
        cursor.execute(query, (codins,))
        # viene creato un cursor che esegue la query sostituendo %s con il valore codins.
        for row in cursor:
            result.append(Studente(row["matricola"], row["cognome"], row["nome"], row["CDS"]))
        cursor.close()
        cnx.close()
        return result
    else:
        print("Could not connect")
        return None

def getCorsiStudente(matricola):
    result = []
    cnx = get_connection()
    if cnx is not None:
        cursor = cnx.cursor(dictionary=True)
        cursor.execute(""" SELECT corso.* 
    FROM corso, iscrizione 
    WHERE iscrizione.codins=corso.codins AND iscrizione.matricola = %s
    """, (matricola,))
        for row in cursor:
            result.append(Corso(row["codins"], row["crediti"], row["nome"], row["pd"]))
        cursor.close()
        cnx.close()
        return result





if __name__ == '__main__':
    for c in getCorsiStudente("190634"):
        print(c)

        print(isinstance(c, Corso))


