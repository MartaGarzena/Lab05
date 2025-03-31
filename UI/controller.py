import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._idCorsi = {}
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_hello(self, e):
        """Simple function to handle a button-pressed event,
        and consequently print a message on screen"""
        name = self._view.txt_name.value
        if name is None or name == "":
            self._view.create_alert("Inserire il nome")
            return
        self._view.txt_result.controls.append(ft.Text(f"Hello, {name}!"))
        self._view.update_page()

    def handle_studente(self, e):
        if self._view.txt_matricola.value is None or self._view.txt_matricola.value == "":
            self._view.txt_result.controls.append(
                ft.Text("Attenzione. Il campo 'matricola' non può essere vuoto", color="red"))

        else:
            codinsCorso = self._view.dd_menu.value
            listaStud = self._model.get_iscritti_corso(codinsCorso)
            matricola = self._view.txt_matricola.value
            studente = None
            for e in listaStud:
                if e.getMatricola() == int(matricola):
                    studente = e
                    break
            if studente is None:
                self._view.txt_result.controls.append(
                    ft.Text("Attenzione. La matricola selezionata non corrisponde a nessuno", color="red"))
            else:
                self._view.txt_name.value = studente.getNome()
                self._view.txt_matricola.value = matricola
                self._view.txt_cognome.value = studente.getCognome()
        self._view.update_page()

        pass

    def handle_iscrivi(self, e):
        pass

    def handle_matricola(self, e):
        matricola = self._view.txt_matricola.value
        if matricola is None or matricola == "":
            self._view.txt_result.controls.append(
                ft.Text("Attenzione. La matricola  non va bene", color="red"))
        studente = None
        for e in self._model.get_tutti_students():
            if e.getMatricola() == int(matricola):
                studente = e
                break
        if studente is None:
            self._view.txt_result.controls.append(
                ft.Text("Attenzione. Lo studente non c'è", color="red"))
        else:
            corsi=self._model.get_corsi_studente(matricola)
            self._view.txt_result.controls.append(
                ft.Text(f"Lo studente {studente.getMatricola()} è iscritto a {len(corsi)} corsi:", color="pink"))
            for e in corsi:
                self._view.txt_result.controls.append(
                        ft.Text(f"{e}"))
        self._view._page.update()


    def handle_cercaIscritti(self, e):
        if self._view.dd_menu.value is None:
            self._view.txt_result.controls.append(
                ft.Text("Attenzione. Il campo 'corso' non può essere vuoto", color="red"))
            self._view._page.update()
        else:
            codinsCorso = self._view.dd_menu.value
            listaStud = self._model.get_iscritti_corso(codinsCorso)
            if len(listaStud) == 0:
                self._view.txt_result.controls.append(
                    ft.Text(f"Non ci sono iscritti", color="orange"))
            else:
                self._view.txt_result.controls.append(
                    ft.Text(f"Ci sono ben {len(listaStud)} iscritti:", color="green"))
                for e in listaStud:
                    self._view.txt_result.controls.append(
                        ft.Text(f"{e}"))
            self._view._page.update()

    def popolaDrop(self):
        for corso in self._model.get_corsi():
            self._idCorsi[corso.codins] = corso
            self._view.dd_menu.options.append(ft.dropdown.Option(key=corso.codins, text=corso))
        self._view.update_page()
