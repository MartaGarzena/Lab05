from database import corso_DAO
from database import studente_DAO

class Model:
    def get_corsi(self):
        return corso_DAO.getAllCorsi()

