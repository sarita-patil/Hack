'''import json
with open('employees.json') as f:
    df1=json.load(f)
print(df1)'''

#count no. of duplicate rows
import collections
import pandas as pd
Employees = pd.read_json("employees.json")
Id = [item['userId'] for item in Employees['Employees']]
print(len([item for item, count in collections.Counter(Id).items() if count > 1]))


#count no.of columns
a=len(Employees['Employees'][0])
print(a)
