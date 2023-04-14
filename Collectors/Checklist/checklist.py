from tkinter import *
import pandas as pd


class ChecklistObject:
    """An object that represents every possible check in the checklist"""
    def __init__(self, name):
        self.status = IntVar()
        self.name = name


class ChecklistCol:
    """An object that represents a Collection of a checklist for Data.csv"""
    def __init__(self, question, last_done):
        self.question = question
        self.item_root = 'Data/' + question + '.csv'
        self.repeat = 0
        self.zeros = 0
        self.category = 'Checklist'
        self.last_done = last_done

    def init_cl_objects(self):
        """Initiate a list of Checklist objects to collect"""
        df_objects = pd.read_csv(self.item_root)
        cl_objects = []
        for nm in df_objects['Checklist']:  # For every collector row
            cl_objects.append(ChecklistObject(nm))

        return cl_objects

    def due(self, input_date):
        """Check if it is due"""
        print(f'        the date last inputted is: {self.last_done}, we are inputting for {input_date}')
        if self.last_done != str(input_date):
            return True
        return False

    def entry(self, root, collectors, collector_index, input_date):
        """Collect the Checklist items"""
        print(f'    beginning checklist entry process for {self.question}')
        cl_objects = self.init_cl_objects()

        def input_cl_obj():
            line = ''
            for obj in cl_objects:
                if obj.status.get() == 1:
                    line += obj.name + '_'

            from Collectors.ColTk import handle_submit

            handle_submit(self, line, root, collectors, collector_index, 0, 0, input_date)

        Label(root, text="Medicines").grid(row=0, sticky=W)
        row = 1
        for cl_obj in cl_objects:
            Checkbutton(root, text=cl_obj.name, variable=cl_obj.status).grid(row=row, sticky=W)
            row += 1

        Button(root, text='Show', command=input_cl_obj).grid(row=row + 1, sticky=W, pady=4)
        mainloop()
