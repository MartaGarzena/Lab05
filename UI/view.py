import flet as ft

from model import corso


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self.dd_menu = None
        self._page = page
        self._page.title = "Lab O5 - segreteria studenti"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.txt_name = None
        self.btn_hello = None
        self.txt_result = None
        self.txt_container = None

    def load_interface(self):
        """Function that loads the graphical elements of the view"""
        # title
        self._title = ft.Text("App Gestione Studenti", color="blue", size=24)
        self._page.controls.append(self._title)

        self.dd_menu = ft.Dropdown(label="corso", options=[] )
        self._controller.popolaDrop()
        #ROW with some controls
        # text field for the name
        self.txt_name = ft.TextField(label="nome", width=200, hint_text="Insert your name", read_only=True)
        self.txt_matricola = ft.TextField(label="matricola", width=200, hint_text="Insert  your matricola")
        self.txt_cognome = ft.TextField(label="cognome", width=200, hint_text="Insert your cognome", read_only=True)

        self._btn_Studente = ft.ElevatedButton(text="Cerca studente", width=200,
                                               on_click=self._controller.handle_studente)
        self._btn_COrsi = ft.ElevatedButton(text="Cerca corsi", width=200, on_click=self._controller.handle_matricola)
        self._btn_Iscrivi = ft.ElevatedButton(text="Iscriviti", width=200, on_click=self._controller.handle_iscrivi)

        # button for the "hello" reply
        self.btn_Iscritti = ft.ElevatedButton(text="Cerca iscritti", on_click=self._controller.handle_iscritti)

        row1 = ft.Row([self.dd_menu, self.btn_Iscritti], alignment=ft.MainAxisAlignment.CENTER)
        #row2
        row3 = ft.Row([self.txt_matricola, self.txt_name, self.txt_cognome], alignment=ft.MainAxisAlignment.CENTER)
        row4 = ft.Row([self._btn_Studente, self._btn_COrsi, self._btn_Iscrivi], alignment=ft.MainAxisAlignment.CENTER)
        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.add(row1, row3, row4)
        self._page.controls.append(self.txt_result)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        """Function that opens a popup alert window, displaying a message
        :param message: the message to be displayed"""
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
