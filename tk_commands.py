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

        def handle_entry(event):
            input_value = entry_data.get()
            if input_value.isdigit() and 0 <= int(input_value) <= 5:
                handle_submit(collector, input_value, root, collectors, collector_index, input_date)
            else:
                error_label = tk.Label(root, text="Please enter an integer between 0 and 5.")
                error_label.pack()
                ui_entry.delete(0, tk.END)
                ui_entry.focus_set()

        ui_entry.bind("<Return>", handle_entry)

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
