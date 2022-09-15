########################################################################
# mpg_calculator-tkinter_python.py
# Author: Lily Zimmermann
#  Spring 2022 
########################################################################
# This program calculates gas mileage based off of the number of gallons
# of gas a car holds and the number of miles it can be driven according
# to the user
########################################################################

import tkinter

class GasMileageCalculator:
    def __init__(self):

        # Create the main window
        self.main_window = tkinter.Tk()

        # Display a title
        self.main_window.title("Mileage Converter")

        # Create frames for the widgets
        self.top_frame = tkinter.Frame()
        self.middle_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()

        # Create the widgets for the top frame
        self.gasGallons_label = tkinter.Label(self.top_frame,
                                              text='Number of gallons of gas car can hold:')
        self.gas_entry = tkinter.Entry(self.top_frame,
                                       width=20)

        # Pack the top frame's widgets
        self.gasGallons_label.pack()
        self.gas_entry.pack()

        # Create the widgets for the middle frame
        self.miles_label = tkinter.Label(self.middle_frame,
                                         text='Number of miles car can be driven:')
        self.miles_entry = tkinter.Entry(self.middle_frame,
                                         width=20)

        # Pack the middle frame's widgets
        self.miles_label.pack()
        self.miles_entry.pack()

        # Create the button for the bottom frame
        self.calculateMPG_button = tkinter.Button(self.bottom_frame,
                                                  text='Calculate Miles Per Gallon',
                                                  command=self.mileageCaluclator)
        # StringVar is for output
        # The set method is used to store a string of blank characters.
        self.value = tkinter.StringVar()

        # Create a label for StringVar
        self.MPG_result_label = tkinter.Label(self.bottom_frame,
                                              textvariable=self.value)

        # Pack the bottom frame's widgets
        self.calculateMPG_button.pack()
        self.MPG_result_label.pack()

        # Pack the frames
        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

        # Enter the tkinter main loop
        tkinter.mainloop()

    # The mileage calculator is a callback function for the Calculate Miles Per Gallon button
    def mileageCaluclator(self):
        # Get the number of miles car can be driven from miles_entry widget
        miles = float(self.miles_entry.get())

        # Get the number of gallons of gas the car can hold from the gas_entry widget
        gallons = float(self.gas_entry.get())

        # Calculate MPG (MPG = miles / gallons)
        mpg = miles/gallons

        # Set the result of the calculation to the self.value to return to the main
        # init function's MPG_result_label so that it will now hold and display
        # the result
        self.value.set(mpg)

# Create an instance of the GasMileageCalculator.
if __name__== '__main__':
    mileage_calc = GasMileageCalculator()
