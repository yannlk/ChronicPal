import tkinter as tk
from Collector import *
from tkinter import messagebox


def root_init():
    """Initiate the Tkinter window and namely the Root Object, Returns Root"""
    root = tk.Tk()
    root.title('Anki Data Collection')
    root.geometry('800x800')
    return root


def process_collector(collector_index, root, collectors, input_date):
    """Recursive function that:
    Iterates through collectors, displaying the necessary things to the ui and doing necessary data changes with input
    """
    try:  # Remove Tkinter Widgets from previous iteration
        for widget in root.winfo_children():
            widget.destroy()
    except AttributeError:
        pass

    print('beginning "process_collector" function, collector index:', collector_index)

    display_label = tk.Label(root, text="")
    display_label.pack()

    if collector_index >= len(collectors):
        print(f'    All collectors cycled through')
        # All collectors have been processed, show the display label
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

        ui_entry.bind("<Return>", lambda event: (
            handle_submit(collector, int(entry_data.get()), root, collectors, collector_index, input_date)
            if entry_data.get().isdigit() else
            (messagebox.showerror("Invalid Input", "Please enter a valid integer value"),
             process_collector(collector_index, root, collectors, input_date))
        ))

        ui_entry.focus_set()

    else:         # Skip to the next collector if the current one is not due
        print(f'    Current collector is not due')

        collector_index += 1
        process_collector(collector_index, root, collectors, input_date)


def handle_submit(collector, answer, root, collectors, collector_index, input_date):
    collector.submit_data(answer, input_date)
    change_due_date(collector, input_date)
    collector_index += 1
    process_collector(collector_index, root, collectors, input_date)
