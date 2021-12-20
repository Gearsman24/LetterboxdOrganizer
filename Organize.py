# Internal Libraries for Organize
import os
import collections
import csv

# External Libraries for Organize
import pandas as pd

def get_col_widths(dataframe):
    # First we find the maximum length of the index column   
    idx_max = max([len(str(s)) for s in dataframe.index.values] + [len(str(dataframe.index.name))])
    # Then, we concatenate this to the max of the lengths of column name and its values for each column, left to right
    return [idx_max] + [max([len(str(s)) for s in dataframe[col].values] + [len(col)]) for col in dataframe.columns]

def organize(lists_dir, folder_dir):
    dict_of_folders = {}
    # Get Name of Lists
    filenames = os.listdir(lists_dir)
    for file in filenames:
        # Open Each List
        file_dir = os.path.join(lists_dir, file)
        with open(file_dir) as csvfile:
            # Separate Lists by Tag
            try:
                tag = list(csv.reader(csvfile, delimiter=','))[2][2]
                if(tag == None or tag == ""):
                    tag = 'misc'
            except:
                tag = 'misc'

            if tag in dict_of_folders.keys():
                dict_of_folders[tag] += [file]
            else:
                dict_of_folders[tag] = [file]
        
    dict_of_folders = collections.OrderedDict(sorted(dict_of_folders.items()))

    # Place Organized Lists in Corresponding Folder
    for key in dict_of_folders:
        dict_of_folders[key].sort()
        with pd.ExcelWriter(os.path.join(folder_dir, key + '.xlsx')) as writer:
            # Make Each List Own Sheet
            for f in dict_of_folders[key]:
                df = pd.read_csv(os.path.join(lists_dir, f))
                sheet = os.path.basename(f) if len(os.path.basename(f)) <= 31 else os.path.basename(f)[0:31]
                df.to_excel(writer, sheet_name=sheet, index=False)

                # Auto Fit to Contents
                for column in df:
                    column_width = max(df[column].astype(str).map(len).max(), len(column))
                    col_idx = df.columns.get_loc(column)
                    writer.sheets[sheet].set_column(col_idx, col_idx, column_width)