# Importing required libraries
import pandas as pd # Need to install on new system
import xml.etree.ElementTree as ET

excelPath = "test.xlsx"

# Update any value in excel
def read_update_excel():
    try:
        # Reading Excel
        df = pd.read_excel(excelPath, dtype='object')

        for i in range(0,len(df)):

            # Get column value
            colA = df.get("Name")[i]
            colB = df.get("Marks")[i]

            print(colA)

            # Update column value
            df.at[i, "Marks"] = 100

        # Update final result in excel
        df.to_excel(excelPath, index=False)

    except Exception as e:
        print("Exception", str(e))


# Find any value in excel
def find_in_excel(colName=None, value=None):
    try:

        # Reading Excel
        ldf = pd.read_excel(excelPath, dtype='object')

        # Find value in excel and column name should not contain spaces or special symbol
        result = ldf.loc[(ldf[colName] == value)]

        if not result.empty:
            rowNo = result.index._data # Row Number

            # Get another column value
            Marks = result.Marks._values[0]
            print(Marks)

    except Exception as e:
        print(str(e))


read_update_excel()
find_in_excel('Name','s1')