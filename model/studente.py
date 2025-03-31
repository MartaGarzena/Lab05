from dataclasses import dataclass

@dataclass
class Studente:
    matricola: int
    cognome: str
    nome: str
    CDS: str

    def __str__(self):
        return f" {self.cognome}, {self.nome} {self.matricola}"

    def __eq__(self, other):
        return self.matricola == other.matricola

    def getMatricola(self):
        return self.matricola
    def getNome(self):
        return self.nome
    def getCognome(self):
        return self.cognome
