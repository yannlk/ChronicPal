from tk_commands import *
from random import shuffle
from ColTk import *

collectors = init_collectors()  # Initiate collector objects which represent each Row of the Dataset
shuffle(collectors)  # Give random order to those collectors

root = root_init()  # Initiate Tkinter window

collector_index = 0  # Index of the current collector being processed

initiator(collector_index, root, collectors)

root.mainloop()  # Tkinter Command to make sure the loop runs
