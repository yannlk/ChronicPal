from random import shuffle
from Collectors.ColTk import initiator
from Collectors.Collector import init_collectors
from Tk.tk_commands import root_init

collectors = init_collectors()  # Initiate collector objects which represent each Row of the Dataset
shuffle(collectors)  # Give random order to those collectors

root = root_init()  # Initiate Tkinter window

collector_index = 0  # Index of the current collector being processed

initiator(collector_index, root, collectors)  # Function that initiates the whole collecting process

root.mainloop()  # Tkinter Command to make sure the loop runs
