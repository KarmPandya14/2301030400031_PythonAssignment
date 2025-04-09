import pandas as pd

# Create a simple DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Marks': [85, 92, 78]
}

df = pd.DataFrame(data)

# Show average marks
average = df['Marks'].mean()
print(df)
print(f"\nClass Average: {average}")
