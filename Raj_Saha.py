# -*- coding: utf-8 -*-
"""yubraj.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1XS5YW-IninbUrB5dtAI0_El5IBOHjfCt
"""

tips

import pandas as pd
tips=pd.read_csv("/content/tips.csv")
tips

import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv("/content/tips.csv")

# Display records from row 6 to row 243 (zero-indexed, so rows 5 to 242)
subset_df = df.iloc[5:243]

print(subset_df)

"""employee csv"""

import pandas as pd

# Sample data
data = {
    'Emp_id': [1, 2, 3, 4, 5, 6],
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank'],
    'dept': ['HR', 'IT', 'Finance', 'IT', 'HR', 'Finance'],
    'basic_sal': [50000, 60000, 70000, 80000, None, 90000],
    'joining_date': ['2010-05-01', '2012-07-15', '2008-09-23', '2015-11-30', '2020-01-10', '2018-06-25'],
    'exp': [12, 9, 15, 7, 4, 11],
    'highest_qual': ['MBA', 'MCA', 'CA', 'BTech', 'MBA', 'CA'],
    'address': ['Address1', 'Address2', 'Address3', 'Address4', 'Address5', 'Address6'],
    'email_id': ['alice@example.com', 'bob@example.com', 'charlie@example.com', 'david@example.com', 'eve@example.com', 'frank@example.com'],
    'mob_no': ['1234567890', '2345678901', '3456789012', '4567890123', '5678901234', '6789012345']
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("/content/employee.csv", index=False)

df = pd.read_csv("/content/employee.csv")
df

exp_more_than_10_years = df[df['exp'] > 10]
count_exp_more_than_10 = exp_more_than_10_years.shape[0]
print("Number of employees with experience more than 10 years:", count_exp_more_than_10)

print("\nDataFrame after replacing NaNs with 0 in 'basic_sal':")
print(df)

total_salary = df['basic_sal'].sum()
print("\nTotal salary of all employees:", total_salary)

average_salary = df['basic_sal'].mean()
print("\nAverage salary of all employees:", average_salary)

rows_10_to_20 = df.iloc[9:20]
print("\nDetails from rows 10 to 20:")
print(rows_10_to_20)

"""iris dataset"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("/content/Iris.csv")
# Countplot
sns.countplot(x='Species', data=df, hue='Species')
plt.title('Countplot of Iris Species')
plt.show()

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("/content/Iris.csv")
# Barplot
sns.barplot(x='Species', y='SepalLengthCm', data=df, hue='Species')
plt.title('Barplot of Sepal Length by Species')
plt.show()

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("/content/Iris.csv")
# Pairplot
sns.pairplot(df, hue='Species')
plt.suptitle('Pairplot of Iris Dataset', y=1.02)
plt.show()

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("/content/Iris.csv")
# Jointplot
sns.jointplot(data=df, x='SepalLengthCm', y='SepalWidthCm', kind='scatter')
plt.title('Jointplot of Sepal Length vs Sepal Width')
plt.show()

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
yubraj=[3,5,7,9,12]
plt.plot(yubraj)
plt.show()

df=pd.read_csv("/content/titanic.csv")
df.isnull() #returns true or failse and it shows where value is null

df.isnull().sum()

age=df["age"]
plt.plot(age,color='green',label='age')
plt.legend()
plt.show()

sns.boxplot(df['age'])

df.isnull().mean()

df["deck"]

import numpy as np
df['deck_yubraj']=np.where(df['deck'].isnull(),1,0)
df['deck_yubraj'].head()

"""ipl dataset"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
df=pd.read_csv("/content/ipl.csv")
print(df)

df.head()

df.info()

df.describe()

df.isnull().sum()

#find missing values
df.fillna(0,inplace=True)
print(df)

#COUNTPLOT
sns.countplot(x='toss_winner',data=df)
plt.show()

#barplot
sns.barplot(x='toss_winner',y='toss_decision',data=df)
plt.show()

#pairplot
sns.pairplot(df)
plt.show()

#jointplot
sns.jointplot(x='toss_winner',y='toss_decision',data=df)
plt.show()

#histogram
sns.histplot(df['toss_winner'])
plt.show()

#distribution plot
sns.displot(df['toss_winner'])
plt.show()

#boxplot
sns.boxplot(x='toss_winner',y='toss_decision',data=df)
plt.show()

#scatter plot
sns.scatterplot(x='toss_winner',y='toss_decision',data=df)
plt.show()