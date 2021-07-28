from Window import root
from VALUES import *


class Labels:
    def __init__(self, text, row, column, fur_numb):
        self.label = Label(root, text=f"{text}")
        self.label.grid(row=row+1, column=column + fur_numb * 2)


class Entries:
    def __init__(self, row, column, parameter, fur_numb):
        self.entry = Entry(root, width=20)
        self.entry.grid(row=row+1, column=column + fur_numb * 2)
        self.entry.insert(0, parameter)


class Buttons:
    def __init__(self, row, column, fur_numb):
        self.is_on = 1

        self.on_button = Button(root, image=ON, bd=0, command=self.switchTemp, relief=SUNKEN)
        self.on_button.grid(row=row, column=column + fur_numb * 2, pady=2, padx=1)

    def switchTemp(self):
        if self.is_on == 1:
            self.on_button.config(image=OFF)
            self.is_on = 0
        else:
            self.on_button.config(image=ON)
            self.is_on = 1


class ExportButton:

    def __init__(self):
        self.export_button = Button(root, image=EXPORT_NEUTRAL, relief=SUNKEN, bd=0)
        self.export_button.grid(row=50, column=0)
        for number in range(10, 40):
            Label(root, text="").grid(row=number, column=0)

        self.export_button.bind("<Button-1>", self.clicked)
        self.export_button.bind("<Enter>", self.enter)
        self.export_button.bind("<Leave>", self.leave)

    def clicked(self, e):
        self.export_button["image"] = EXPORTED
        self.export_button.image = EXPORTED

    def enter(self, e):
        self.export_button["image"] = MOUSE_HOVER
        self.export_button.image = MOUSE_HOVER

    def leave(self, e):
        self.export_button["image"] = EXPORT_NEUTRAL
        self.export_button.image = EXPORT_NEUTRAL
