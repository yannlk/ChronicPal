import pandas as pd
from datetime import date, timedelta


class Collector:
    """An object that represents a row Data.csv"""

    def __init__(self, question, due_date, repeat):  # Initiate the object
        self.question = question
        self.due_date = date(int(due_date.split('-')[0]), int(due_date.split('-')[1]), int(due_date.split('-')[2]))
        self.repeat = repeat

    def due(self):
        """Checks if the Collector is due -> Returns True or False"""
        if self.due_date <= date.today():
            return True
        return False

    def submit_data(self, entry_data, input_date):
        """Adds the input (entry_data) to Data.csv under the row of the Collector at the Column of the Date Specified"""
        df_data = pd.read_csv('Data.csv', index_col='Name')

        if str(input_date) in df_data.columns:  # check if there is a column with today's date
            df_data.at[self.question, str(input_date)] = entry_data

        else:
            df_data[str(input_date)] = ['NaN'] * len(df_data.index)  # Create new column for today's date
            df_data.at[self.question, str(input_date)] = entry_data

        df_data.to_csv('Data.csv')  # Write the changes


def init_collectors():
    """Takes every row in collector.csv and creates a collector item from it, outputs a list of all these items."""

    df_collectors = pd.read_csv('Collectors.csv', index_col='Name')

    collectors = []

    for nm in df_collectors.index:  # For every collector row
        collectors.append(Collector(nm, df_collectors.loc[nm, 'Due Date'], df_collectors.loc[nm, 'Repeat']))

    print('From function "init_collectors": The length of collectors is:', len(collectors))
    return collectors


def change_due_date(collector, date):
    """Changes the due date of the collector to the next due date, once the data has been submitted"""
    df_collectors = pd.read_csv('Collectors.csv', index_col='Name')
    df_collectors.at[collector.question, 'Due Date'] = str(date + timedelta(days=int(collector.repeat)))
    df_collectors.to_csv('Collectors.csv')
