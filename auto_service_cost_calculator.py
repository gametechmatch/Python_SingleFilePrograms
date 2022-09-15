########################################################################
# auto_service_cost_calculator.py
# Author: Lily Zimmermann
# Spring 2022
########################################################################
# This program allows a user to select any or all services available
# through Joe's automotive. When user clicks the Calculate Total Cost
# button, total charges are displayed in a window that pops up.
########################################################################
import tkinter
import tkinter.messagebox

class RepairOptionsTwo:
    def __init__(self):

        # Create widgets
        self.__create_main_window()
        self.__create_main_label()
        self.__create_listbox()
        self.__create_total_cost_button()
        self.__create_quit_button()
        self.__identify_selection()

        # start the main loop
        tkinter.mainloop()

    ########################################################################
    # This method creates a title for the main window
    ########################################################################
    def __create_main_window(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("Joe's Automotive")

    ########################################################################
    # This method creates a label for the top of the box
    ########################################################################
    def __create_main_label(self):
        self.main_label = tkinter.Label(self.main_window,
                                   text='PLEASE CHOOSE ALL REPAIRS NEEDED:')
        self.main_label.pack(padx=100, pady=(5, 10))

    ########################################################################
    # This method creates a listbox of the repairs that can be chosen
    ########################################################################
    def __create_listbox(self):
        # Create the listbox
        self.repair_options_listbox = tkinter.Listbox(
            self.main_window, width=30, height=7,
            selectmode=tkinter.MULTIPLE)
        self.repair_options_listbox.pack(padx=10, pady=10)

        # Populate the listbox with repair options
        self.repair_options_listbox.insert(0, 'Oil change: $30.00')
        self.repair_options_listbox.insert(1, 'Lube job: $20.00')
        self.repair_options_listbox.insert(2, 'Radiator flush: $40.00')
        self.repair_options_listbox.insert(3, 'Transmission flush: $100.00')
        self.repair_options_listbox.insert(4, 'Inspection: $35.00')
        self.repair_options_listbox.insert(5, 'Muffler replacement: $200.00')
        self.repair_options_listbox.insert(6, 'Tire rotation: $20.00')

    ########################################################################
    # This method creates a button to push when all repairs have been chosen
    ########################################################################
    def __create_total_cost_button(self):
        # create button for total cost
        self.total_cost_button = tkinter.Button(self.main_window, text='Calculate Total Cost',
                                                command=self.__get_repair_selections)
        self.total_cost_button.pack()

    ########################################################################
    # This method pulls the selections from the get_repair_listbox and
    # calculates the total from the items chosen
    ########################################################################
    def __get_repair_selections(self):
        # Get the index of the selected items
        indexes = self.repair_options_listbox.curselection()

        # Iterate through the indexes tuple to sum up all selections if
        # any repairs were selected
        if (len(indexes) > 0):
            total = 0
            for value in indexes:
                if value == 0:
                    total += 30.00
                elif value == 1:
                    total += 20.00
                elif value == 2:
                    total += 40.00
                elif value == 3:
                    total += 100.00
                elif value == 4:
                    total += 35.00
                elif value == 5:
                    total += 200.00
                elif value == 6:
                    total += 20.00

            # Create a message box that shows the total cost of all repairs
            tkinter.messagebox.showinfo(message=f'${total}')

        # Create a message box with a message that no items selected
        else:
            tkinter.messagebox.showinfo(message='No item selected.')

    ########################################################################
    # This method creates a tuple with the indexes of the repairs chosen
    ########################################################################
    def __identify_selection(self):
        indexes = self.repair_options_listbox.curselection()
        for i in indexes:
            tkinter.messagebox.showinfo(self.repair_options_listbox.get(i))

    ########################################################################
    # This method creates a quit button
    ########################################################################
    def __create_quit_button(self):
        self.quit_button = tkinter.Button(self.main_window,
                                          text='Quit',
                                          command=self.main_window.destroy)
        self.quit_button.pack(pady=10)

# Create an instance of the RepairOptions class
if __name__ == '__main__':
    repair_options_two = RepairOptionsTwo()
