import pandas as pd
import re
import json
import datetime

category_mapping = {
   'BILLS' : 9,
   'INVESTMENT' : 8,
   'FOOD & DRINKS' : 12,
   'TRAVEL' : 13,
   'SHOPPING' : 11,
   'GROCERIES' : 16,
   'ENTERTAINMENT' : 10,
   'HEALTH' :  14,
   'EDUCATION' : 17,
   'FUEL' : 15,
   'BUSINESS EXPENSES' : 18,
   'GROOMING' : 19
}

others_category = 20

def format_row(name, amount, trans_date, tran_category, id):
    # date = re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1', trans_date)
    date = datetime.datetime.strptime(trans_date, "%d-%m-%Y").strftime("%Y-%m-%d")
    category = category_mapping.get(tran_category, others_category)

    dic = {
        "name": name,
        "currency": float(amount),
        "time": date + "T09:21:53.423562",
        "type": "expense",
        "accountId": 0,
        "categoryId": category,
        "superId": id,
        "description": None,
        "fromAccountId": None,
        "toAccountId": None,
        "transferAmount": 0.0
    }

    return dic



# Reading the data
data = pd.read_csv('axio_expense_report_01-09-2002_to_30-11-2023.csv')

# Apply a select condition based on following conditions
# 1 - All debit transactions
# 2 - Where the expense category is selected as yes
expense_data = data[ (data['DR/CR'] == 'DR') & (data['EXPENSE'] == 'Yes') ]


json_result = {
    "expenses": [],
    "accounts": [
        {
            "name": "Vipul",
            "bankName": "Bank",
            "number": "",
            "cardType": "bank",
            "superId": 0,
            "amount": 0.0,
            "color": 4293467747
        }
    ],
    "categories": [
        {
            "name": "Investment",
            "description": "",
            "icon": 984940,
            "superId": 8,
            "budget": 0.0,
            "color": 4284513675,
            "isBudget": False,
            "isDefault": False
        },
        {
            "name": "Bills",
            "description": "",
            "icon": 984801,
            "superId": 9,
            "budget": 0.0,
            "color": 4283215696,
            "isBudget": False,
            "isDefault": False
        },
        {
            "name": "Entertainment",
            "description": "",
            "icon": 987204,
            "superId": 10,
            "budget": 0.0,
            "color": 4288423856,
            "isBudget": False,
            "isDefault": False
        },
        {
            "name": "Shopping",
            "description": "",
            "icon": 984218,
            "superId": 11,
            "budget": 0.0,
            "color": 4286141768,
            "isBudget": False,
            "isDefault": False
        },
        {
            "name": "Food",
            "description": "",
            "icon": 987204,
            "superId": 12,
            "budget": 0.0,
            "color": 4294198070,
            "isBudget": False,
            "isDefault": False
        },
        {
            "name": "Travel",
            "description": "",
            "icon": 984805,
            "superId": 13,
            "budget": 0.0,
            "color": 4291681337,
            "isBudget": False,
            "isDefault": False
        },
        {
            "name": "Health",
            "description": "",
            "icon": 990028,
            "superId": 14,
            "budget": 0.0,
            "color": 4294940672,
            "isBudget": False,
            "isDefault": False
        },
        {
            "name": "Fuel",
            "description": "",
            "icon": 983307,
            "superId": 15,
            "budget": 0.0,
            "color": 4294924066,
            "isBudget": False,
            "isDefault": False
        },
        {
            "name": "Groceries",
            "description": "",
            "icon": 984284,
            "superId": 16,
            "budget": 0.0,
            "color": 4287349578,
            "isBudget": False,
            "isDefault": False
        },
        {
            "name": "Education",
            "description": "",
            "icon": 983768,
            "superId": 17,
            "budget": 0.0,
            "color": 4282339765,
            "isBudget": False,
            "isDefault": False
        },
        {
            "name": "Business Expense",
            "description": "",
            "icon": 984774,
            "superId": 18,
            "budget": 0.0,
            "color": 4278238420,
            "isBudget": False,
            "isDefault": False
        },
        {
            "name": "Grooming",
            "description": "",
            "icon": 988553,
            "superId": 19,
            "budget": 0.0,
            "color": 4291681337,
            "isBudget": False,
            "isDefault": False
        },
        {
            "name": "Other",
            "description": "",
            "icon": 984213,
            "superId": 20,
            "budget": 0.0,
            "color": 4294961979,
            "isBudget": False,
            "isDefault": False
        }
    ]
}

# Forming the JSON to be written
counter = 0
for index, row in expense_data.iterrows():
    entry = format_row(name=row['PLACE'], amount=float(row['AMOUNT']), trans_date=row['DATE'], tran_category=row['CATEGORY'], id=counter)
    json_result["expenses"].append(entry)
    counter += 1

datetime.datetime.strptime("21/12/2008", "%d/%m/%Y").strftime("%Y-%m-%d")

# Writing the final file
with open('export.json', 'w') as convert_file: 
     convert_file.write(json.dumps(json_result))
