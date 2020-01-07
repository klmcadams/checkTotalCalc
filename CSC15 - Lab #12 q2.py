import tkinter

class RestaurantReceiptGUI:
    def __init__(self):
        # Create the main window
        self.main_window = tkinter.Tk()

        # Create frames to group widgets.
        self.top_frame1 = tkinter.Frame()
        self.top_frame2 = tkinter.Frame()
        self.top_frame3 = tkinter.Frame()
        self.mid_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()

        # Create the widgets for the top frames.
        self.total_label = tkinter.Label(self.top_frame1,
                                    text = 'Enter the total check amount:')
        self.total_entry = tkinter.Entry(self.top_frame1, width = 10)

        self.tax_label = tkinter.Label(self.top_frame2,
                                    text = 'Enter a tax amount (%):')
        self.tax_entry = tkinter.Entry(self.top_frame2, width = 10)

        self.tip_label = tkinter.Label(self.top_frame3,
                                    text = 'Enter a tip amount (%):')
        self.tip_entry = tkinter.Entry(self.top_frame3, width = 10)

        # Pack the top frame’s widgets
        self.total_label.pack(side='left')
        self.total_entry.pack(side='left')
        self.tax_label.pack(side='left')
        self.tax_entry.pack(side='left')
        self.tip_label.pack(side='left')
        self.tip_entry.pack(side='left')

        # Create the widgets for the middle frame.
        self.descr_label = tkinter.Label(self.mid_frame,
                                text= 'Total Check Amount Calculated:')

        # We need a StringVar object to associate with
        # an output label. Use the object’s set method
        # to store a string of blank characters.
        self.value = tkinter.StringVar()

        # Create a label and associate it with the
        # StringVar object. Any value stored in the
        # StringVar object will automatically be displayed
        # in the label.
        self.totalbill_label = tkinter.Label(self.mid_frame,
                                textvariable=self.value)

        # Pack the middle frame’s widgets.
        self.descr_label.pack(side='left')
        self.totalbill_label.pack(side='left')

        # Create the button widgets for the bottom frame.
        self.calc_button = tkinter.Button(self.bottom_frame,
            text='Convert',command=self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame,
                                text='Quit',
                                command=self.main_window.destroy)

        # Pack the buttons.
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Pack the frames.
        self.top_frame1.pack()
        self.top_frame2.pack()
        self.top_frame3.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()

        # Enter the tkinter main loop.
        tkinter.mainloop()

        # The convert method is a callback function for
        # the Calculate button.

    def convert(self):
        total = float(self.total_entry.get())
        tip = float(self.tip_entry.get())
        tax = float(self.tax_entry.get())

        totalamt = total + (total*tip)/100 + (total*tax)/100

        self.value.set(totalamt)

totalcalc = RestaurantReceiptGUI()
