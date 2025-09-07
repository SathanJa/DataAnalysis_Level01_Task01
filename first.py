import pandas as pd

#Load the data set
df = pd.read_csv("Titanic Dataset.csv")
print("Initial shape:", df.shape)
print(df.head())

#Identify missing values
print("\nMissing values in each column:")
print(df.isnull().sum())

#Handling Missing Values

if 'Age' in df.columns:
    df['Age'] = df['Age'].fillna(df['Age'].median())
if 'Embarked' in df.columns:
    df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

# Drop rows if critical columns (like 'Survived') are missing
df = df.dropna(subset=['Survived']) if 'Survived' in df.columns else df

#Remove duplicate rows
df = df.drop_duplicates()
print("\nShape after removing duplicates:", df.shape)

#Standardize inconsistent data formats

if 'Sex' in df.columns:
    df['Sex'] = df['Sex'].str.strip().str.lower()

if 'Embarked' in df.columns:
    df['Embarked'] = df['Embarked'].str.strip().str.upper()

# If there are date columns, convert them
for col in df.columns:
    if "date" in col.lower():   # detect columns like "Date of Travel"
        df[col] = pd.to_datetime(df[col], errors='coerce')

#Final cleaned dataset
print("\nCleaned dataset preview:")
print(df.head())

#Save cleaned dataset
df.to_csv("Cleaned_Titanic.csv", index=False)
print("\n Cleaned dataset saved as 'Cleaned_Titanic.csv'")
