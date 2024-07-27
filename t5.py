import pandas as pd
import matplotlib.pyplot as plt
data = {
    'Name': ['John', 'Vihan', 'Numbo', 'Krishna', 'Arithi'],
    'Social': [15, 50, 75, 96, 37],
    'English': [95, 95, 66, 65, 60],
    'Hindi': [60, 85, 64, 56, 67],
    'Math': [50, 13, 77, 6, 90],
    'Science': [59, 44, 56, 88, 66]}
df = pd.DataFrame(data)
print("\n Original DataFrame:")
print(df)
pivot_table = df.melt(id_vars=['Name'], var_name='Subject', value_name='Score')
pivot_table = pivot_table.pivot_table(index='Name', columns='Subject', values='Score', aggfunc='mean')
print("\nPivot Table:")
print(pivot_table)
df['Total'] = df[['Social', 'English', 'Hindi', 'Math', 'Science']].sum(axis=1)
print("\nDataFrame with Total Scores:")
print(df)
sorted_df = df[df['English'] > 80].sort_values(by='English', ascending=False)
print("\nSorted DataFrame (English > 80):")
print(sorted_df)
df.plot(kind='bar', x='Name', y=['Social', 'English', 'Hindi', 'Math', 'Science'], stacked=True)
plt.xlabel('Name')
plt.ylabel('Scores')
plt.title('Student Scores in the Subject')
plt.show()