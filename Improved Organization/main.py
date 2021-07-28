from Widgets import *
from Window import root


# Top Label:
def create_fur_label(fur_numb):
    for furnace in range(0, fur_numb):
        label2 = Label(root, text=f"Furnace {furnace + 1}")
        label2.grid(row=0, column=2 * furnace)


# Function that creates all labels:
def create_labels(fur_numb):
    for furnace in range(0, fur_numb):
        for x in range(0, len(LABELS_LIST)):
            Labels(LABELS_LIST[x], x, 0, furnace)


# Function that creates all entries:
def create_entries(fur_numb):
    for furnace in range(0, fur_numb):
        for x in range(0, len(LABELS_LIST)):
            Entries(x, 1, INITIAL_PARAM_TEMP[x], furnace)


def create_buttons(fur_numb):
    for furnace in range(0, fur_numb):
        Buttons(0, 1, furnace)
    ExportButton()


# Function that combines all functions (all the above)
def executioner():
    create_labels(NUMBER_OF_FURNACES)
    create_entries(NUMBER_OF_FURNACES)
    create_fur_label(NUMBER_OF_FURNACES)
    create_buttons(NUMBER_OF_FURNACES)


# Statement that starts the app:
if __name__ == "__main__":
    executioner()

    root.mainloop()
