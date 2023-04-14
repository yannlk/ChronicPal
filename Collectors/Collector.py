from Collectors.Number.number import NumberCol
from Collectors.Checklist.checklist import ChecklistCol
import pandas as pd


class Collector:
    """An object that represents a row Data.csv"""

    def __init__(self, question, repeat, category, zeros, last_done):  # Initiate the object
        self.question = question
        self.repeat = repeat
        self.category = category
        self.zeros = zeros
        self.last_done = last_done

    def submit_data(self, entry_data, input_date):
        """Adds the input (entry_data) to Data.csv under the row of the Collector at the Column of the Date Specified"""
        df_data = pd.read_csv('Data/Data.csv', index_col='Name')

        if str(input_date) in df_data.columns:  # check if there is a column with today's date
            df_data.at[self.question, str(input_date)] = entry_data
            print(f'    {df_data[str(input_date)]}')

        else:
            df_data[str(input_date)] = ['NaN'] * len(df_data.index)  # Create new column for today's date
            df_data.at[self.question, str(input_date)] = entry_data

        df_data.to_csv('Data/Data.csv')  # Write the changes

    def col_handle_submit(self, answer, input_date, repeat, zeros):
        """Handles the submit action of new data by making necessary changes"""
        self.submit_data(answer, input_date)
        self.change_collector(repeat, zeros, input_date)

    def change_collector(self, repeat, zeros, current_date):
        """Changes the due date of the collector to the next due date, once the data has been submitted"""
        df_collectors = pd.read_csv('Data/Collectors.csv', index_col='Name')
        df_collectors.at[self.question, 'LastDone'] = current_date
        df_collectors.at[self.question, 'Repeat'] = repeat
        df_collectors.at[self.question, 'Days'] = zeros
        df_collectors.to_csv('Data/Collectors.csv')

    def create_collector_type(self):
        """Takes a collector object and 'translates' it into a specific collector type object"""
        if self.category == 'Number':
            return NumberCol(self.question, self.repeat, self.zeros, self.last_done)

        elif self.category == 'Checklist':
            return ChecklistCol(self.question, self.last_done)


def init_collectors():
    """Takes every row in collector.csv and creates a collector item from it, outputs a list of all these items."""

    df_collectors = pd.read_csv('Data/Collectors.csv', index_col='Name')

    collectors = []

    for nm in df_collectors.index:  # For every collector row
        try:  # try to see if there is a last done date
            last_done = df_collectors.loc[nm, 'LastDone']
        except KeyError:  # if there isn't: item never done before, put date as past date
            last_done = '01-01-2000'

        collectors.append(Collector(nm, df_collectors.loc[nm, 'Repeat'], df_collectors.loc[nm, 'Type'],
                          df_collectors.loc[nm, 'Days'], last_done).create_collector_type())

    print('From function "init_collectors": The length of collectors is:', len(collectors))
    return collectors

