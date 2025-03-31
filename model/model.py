from database import corso_DAO
from database import studente_DAO


class Model:
    def get_corsi(self):
        return corso_DAO.getAllCorsi()

    def get_iscritti_corso(self, codins):
        return corso_DAO.getAllStudents(codins)

    def get_tutti_students(self):
        return studente_DAO.getAllStudents()

    def get_corsi_studente(self, matricola):
        return corso_DAO.getCorsiStudente(matricola)
