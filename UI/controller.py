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
        pass

    def handle_iscrivi(self, e):
        pass

    def handle_matricola(self, e):
        pass

    def handle_iscritti(self, e):
        pass

    def popolaDrop(self):
        for corso in self._model.get_corsi():
            self._idCorsi[corso.codins] = corso
            self._view.dd_menu.options.append(ft.dropdown.Option(key=corso.codins, text=corso))
        self._view.update_page()
