import tkinter as tk
from Collector import *
from tk_commands import *
import datetime


def process_collector(collector_index, root, collectors, input_date):
    """Recursive function that:
    Iterates through collectors, displaying the necessary things to the ui and doing necessary data changes with input
    """
    clear_window(root)  # Removes all widgets from previous iteration

    print('beginning "process_collector" function, collector index:', collector_index)

    if collector_index >= len(collectors):  # If cycle is finished
        print(f'    All collectors cycled through')
        question_label = tk.Label(root, text="Nothing else is due today :)")
        question_label.pack()
        return

    collector = collectors[collector_index]
    print(f'    Collector name {collector.question}')

    if collector.due():
        print(f'    Current collector is due')

        # Create the UI elements for the current collector
        question_label = tk.Label(root, text=collector.question)
        question_label.pack()

        entry_data = tk.StringVar()
        ui_entry = tk.Entry(root, textvariable=entry_data)
        ui_entry.pack()

        def handle_entry(event):
            input_value = entry_data.get()
            try:
                if 0 <= int(input_value) <= 5:
                    handle_submit(collector, input_value, root, collectors, collector_index, input_date)
                else:
                    raise ValueError
            except ValueError:
                error_label = tk.Label(root, text="Please enter an integer between 0 and 5.")
                error_label.pack()
                ui_entry.delete(0, tk.END)
                ui_entry.focus_set()

        ui_entry.bind("<Return>", handle_entry)

        ui_entry.focus_set()  # Puts focus on the entry

        if collector_index > 0:
            redo_button = tk.Button(root, text="Redo Previous Entry", command=lambda: redo_entry(collector_index - 1,
                                                                                                 root, collectors,
                                                                                                 input_date))
            redo_button.pack()

    else:         # Skip to the next collector if the current one is not due
        print(f'    Current collector is not due')

        collector_index += 1
        process_collector(collector_index, root, collectors, input_date)


def handle_submit(collector, answer, root, collectors, collector_index, input_date):
    """Handle Submit from the process collector side"""
    collector.col_handle_submit(answer, input_date)
    collector_index += 1
    process_collector(collector_index, root, collectors, input_date)


def redo_entry(prev_collector_index, root, collectors, input_date):
    """Goes back to previous process collector"""
    prev_collector = collectors[prev_collector_index]
    prev_collector.due_date = date.today() + timedelta(days=-int(prev_collector.repeat))
    process_collector(prev_collector_index, root, collectors, input_date)


def initiator(collector_index, root, collectors):
    """Initiates the date collection and therefore pushes to the process collector"""

    def date_entry(event):
        """Entry function for the Data"""
        if entry_date.get() == '':
            submit_date = date.today()
        else:
            submit_date = date.today() + timedelta(float(entry_date.get()))
        print('From function "Initiator", we are collecting for:', submit_date)
        process_collector(collector_index, root, collectors, submit_date)

    question_label = tk.Label(root, text='Date in days before/after today')
    question_label.pack()

    entry_date = tk.StringVar()
    ui_entry = tk.Entry(root, textvariable=entry_date)
    ui_entry.pack()
    ui_entry.bind("<Return>", date_entry)

    ui_entry.focus_set()  # Puts focus on the entry
