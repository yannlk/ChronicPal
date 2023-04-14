import tkinter as tk
from Tk.tk_commands import clear_window
from datetime import date, timedelta
from Collectors.Collector import Collector


def process_collector(collector_index, root, collectors, input_date):
    """Recursive function that:
    Iterates through collectors, displaying the necessary things to the ui and doing necessary data changes with input
    """
    clear_window(root)  # Removes all widgets from previous iteration

    print('beginning "process_collector" function, collector index:', collector_index)

    if collector_index >= len(collectors):  # If cycle is finished
        print(f'    All collectors cycled through')
        tk.Label(root, text="Nothing else is due today :)").pack()
        return

    collector = collectors[collector_index]
    print(f'    Collector name {collector.question}')

    if collector.due(input_date):
        print(f'    Current collector is due')

        collector.entry(root, collectors, collector_index, input_date)

        if collector_index > 0:
            redo_button = tk.Button(root, text="Redo Previous Entry", command=lambda: redo_entry(collector_index - 1,
                                                                                                 root, collectors,
                                                                                                 input_date))
            redo_button.pack()

    else:         # Skip to the next collector if the current one is not due
        print(f'    Current collector is not due')

        collector_index += 1
        process_collector(collector_index, root, collectors, input_date)


def handle_submit(collector, answer, root, collectors, collector_index, repeat, zeros, input_date):
    """Handle Submit from the process collector side"""
    Collector(collector.question, collector.repeat, collector.category, collector.zeros, collector.last_done)\
        .col_handle_submit(answer, input_date, repeat, zeros)
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
