This is a program that lets you easily track your symptoms when suffering from any sort of diagnosed or undiagnosed
condition. The goal is to make it as quick to use as possible, and crucially,
to have the data in a simple format.

# Features
- Data Entry
  - Enter Data as specific number
  - Enter Data as checklist with items
  - Easy and Quick
- Adaptability
  - When symptoms haven't been present for a while, will ask about specific symptom at longer intervals to avoid overthinking
- Easy Export
  - Simple .csv file with all your data in a simple format

# Setup
The first thing you want to do is go to `Data/Collectors.csv` and add all the
different data objects you want to collect. 

### Data Types
There are currently two data types:
- Numbers
  - For a specific variable input a number from 0-5 based on the prevalence of the variable ie. I had a bad headache `headache = 4` today
- Checklist
  - For a specific topic input the predefined variables, ie. I have a medicine checklist, with all the medicine I sometimes take, at the end of the day I check the ones I took and it is tracked.

### Adding Numbers
In the `Data/Collectors.csv` under `name` put the question you want to show up when you have to input this data type. Then under `type` put `Number`, you can leave the rest empty.

### Adding Checklists
Like for numbers, in the `Data/Collectors.csv` under `name` put the question you want to show up when you have to input this data type. Then under `type` put `Checklist`, you can leave the rest empty.

However, you also need to add the items the checklist will show. To do this you need to:
1. Create a file `Data/name.csv` where name is the specific `name` you inputted in `Data/collectors.csv`
2. Create a column called `Checklist`
3. Under this column, put all the items you would like in your checklist.

### Finishing Touch
Now that all this is set up you are ready to use the application. You can either go straight to using it and test out how good I am at making things intuitive, or first checkout the "Usage" section in this readme.


# Usage
This program is envisioned to be launched once at the end of the day, where the data of that specific day is inputted.
### Launch
To launch the application launch the `main.py` file. 

### Days
When you launch the program you will be asked: "Date in days before/after today".

If you want to enter data for today, either just press `Enter`, or input the value `0`.

If you missed a day and want to input data for a previous day (say yesterday). Enter the number of days before today the specific day is (preceded by a minus sign). So for yesterday you would put `-1` but for 4 days ago you would put `-4`.

### Number
When inputting a number enter a whole number from `0`-`5` corresponding to the data you want to input. If you don't want to input data for that day put `-1`. Pressing `Enter` is an alternative to pressing the onscreen button.

### Checklist
Check all the elements which are relevant and press submit. 

# Future Development

### Short Term
- [ ] Enter ' ' -> 0 for number
- [ ] Difference between didn't fill checklist and none checked
### Medium Term
- [ ] Search function to input data
### Long Term
- [ ] Data Analysis Support
- [ ] Create Way to set up program without using csv Interface

## Ideas
#### Overthinking Problem
- Y/N Base categories before specific questions
#### Easier Interface
- Obsidian Interface
- Application

# Bugs and Contact
Please report bugs to the issues page of this github, and for anything else feel free to contact me.


