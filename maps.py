headers = ["Status", "Duration", "Credit history", "Purpose", "Credit amount", "Savings", "Employment", "Installment rate in % income", "Personal", "Other debtors / guarantors", "Present residence since", "Property", "Age", "Other plans", "Housing", "Number of existing credits at this bank", "Job", "Number of people being liable to provide maintenance for", "Telephone", "Foreign worker", "Risk"]

status_map = {
    'A11': '< 0 DM',
    'A12': '0 <= ... < 200 DM',
    'A13': '>= 200 DM',
    'A14': 'no checking account'
}

history_map = {
    'A30': 'no credits taken',
    'A31': 'all credits paid back duly',
    'A32': 'existing credits paid back duly',
    'A33': 'delay in paying off',
    'A34': 'critical account'
}

purpose_map = {
    'A40': 'car (new)',
    'A41': 'car (used)',
    'A42': 'furniture/equipment',
    'A43': 'radio/television',
    'A44': 'domestic appliances',
    'A45': 'repairs',
    'A46': 'education',
    'A47': 'vacation',
    'A48': 'retraining',
    'A49': 'business',
    'A410': 'others'
}

savings_map = {
    'A61' :'... <  100 DM',
    'A62' :'100 <= ... <  500 DM',
    'A63' :'500 <= ... < 1000 DM',
    'A64' :'.. >= 1000 DM',
    'A65' :'unknown/ no savings account'
}

employment_map = {
    'A71' : 'unemployed',
    'A72' : '... < 1 year',
    'A73' : '1  <= ... < 4 years',
    'A74' : '4  <= ... < 7 years',
    'A75' : '.. >= 7 years'
}

personal_map = {
    'A91' : 'male divorced/separated',
    'A92' : 'female divorced/separated/married',
    'A93' : 'male single',
    'A94' : 'male  married/widowed',
    'A95' : 'female single',
}

otherDebtors_map = {
    'A101' : 'none',
    'A102' : 'co-applicant',
    'A103' : 'guarantor'
}

property_map = {
    'A121' : 'real estate',
    'A122' : 'if not A121 : building society savings agreement/life insurance',
    'A123' : 'if not A121/A122 : car or other, not in attribute 6',
    'A124' : 'unknown / no property'
}

otherPlans_map = {
    'A141' : 'bank',
    'A142' : 'stores',
    'A143' : 'none'
}

housing_map = {
    'A151' : 'rent',
    'A152' : 'own',
    'A153' : 'for free'
}

job_map = {
    'A171' : 'unemployed/ unskilled  - non-resident',
    'A172' : 'unskilled - resident',
    'A173' : 'skilled employee / official',
    'A174' : 'management/ self-employed highly qualified employee/ officer'
}

telephone_map = {
    'A191' : 'none',
    'A192' : 'yes, registered under the customers name'
}

foreign_workers_map = {
    'A201' : 'yes',
    'A202' : 'no'
}

def map_codes(df):
    df["Status"] = df["Status"].map(status_map)
    df["Purpose"] = df["Purpose"].map(purpose_map)
    df["Credit history"] = df["Credit history"].map(history_map)
    df['Savings'] = df['Savings'].map(savings_map)
    df['Employment'] = df['Employment'].map(employment_map)
    df['Personal'] = df['Personal'].map(personal_map)
    df['Other debtors / guarantors'] = df['Other debtors / guarantors'].map(otherDebtors_map)
    df['Property'] = df['Property'].map(property_map)
    df['Other plans'] = df['Other plans'].map(otherPlans_map)
    df['Housing'] = df['Housing'].map(housing_map)
    df['Job'] = df['Job'].map(job_map)
    df['Telephone'] = df['Telephone'].map(telephone_map)
    df['Foreign worker'] = df['Foreign worker'].map(foreign_workers_map)





