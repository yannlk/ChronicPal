from tk_commands import *
from datetime import date

collectors = init_collectors()  # Initiate collector objects which represent each Row of the Dataset

date = date.today()

root = root_init()  # Initiate Tkinter window

collector_index = 0  # Index of the current collector being processed

process_collector(collector_index, root, collectors, date)  # Begin the process of collecting and submitting the data

root.mainloop()  # Tkinter Command to make sure the loop runs
