import tkinter as tk


class NumberCol:
    """An object that represents a Collection of a number for Data.csv"""

    def __init__(self, question, repeat, zeros, last_done):  # Initiate the object
        self.question = question
        self.repeat = float(repeat)
        self.zeros = float(zeros)
        self.category = 'Number'
        self.last_done = last_done

    def due(self, input_date):
        """Checks if the Collector is due -> Returns True or False"""
        if self.repeat + take_zeros(self.zeros) < 1:
            if self.last_done != str(input_date):
                return True
            return False

        from Collectors.Collector import Collector
        Collector(self.question, self.repeat - 0.1, self.category, self.zeros, self.last_done) \
            .change_collector(self.repeat - 0.1, self.zeros, input_date)

        return False

    def new_rpt_zrs(self, input_value):
        """Takes the old repeat and zeros and the input value and gives the new repeat and zeros"""
        inpt = int(input_value)
        if inpt == 0:
            return [self.repeat + 0.4, self.zeros + 1]
        elif inpt == 1:
            return [self.repeat, self_pos(self.zeros - 2)]
        elif inpt == 2:
            return [self_pos(self.repeat - 0.2), self.zeros/3]
        elif inpt == 3:
            return [self_pos(self.repeat - 0.4), self.zeros/5]
        elif inpt == 4:
            return [self_pos(self.repeat - 0.6), 0]
        elif inpt == 5:
            return [0, 0]

    def entry(self, root, collectors, collector_index, input_date):
        # Create the UI elements for the current collector
        tk.Label(root, text=self.question).pack()

        entry_data = tk.StringVar()
        ui_entry = tk.Entry(root, textvariable=entry_data)
        ui_entry.pack()

        def handle_entry(event):
            input_value = entry_data.get()
            try:
                if input_value == '' or -1 <= int(input_value) <= 5:
                    if -1 == int(input_value):
                        input_value = 'NaN'
                    if input_value == '':  # If user enters empty they mean 0
                        input_value = 1

                    new_rpt_zrs = self.new_rpt_zrs(input_value)

                    from Collectors.ColTk import handle_submit

                    handle_submit(self, input_value, root, collectors, collector_index, new_rpt_zrs[0], new_rpt_zrs[1],
                                  input_date)
                else:
                    raise ValueError
            except ValueError:
                error_label = tk.Label(root, text="Please enter an integer between 0 and 5.")
                error_label.pack()
                ui_entry.delete(0, tk.END)
                ui_entry.focus_set()

        ui_entry.bind("<Return>", handle_entry)

        ui_entry.focus_set()  # Puts focus on the entry


def self_pos(number):
    """Based on a number return the smallest positive integer"""
    return min(0, number)


def take_zeros(number):
    return min(0.02*number + 0.003*number**2, 0.999)
