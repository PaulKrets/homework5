import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

conn = sqlite3.connect('world_happiness.db')
cursor = conn.cursor()

df = pd.read_csv('world_happiness_report.csv')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS happiness (
        Country TEXT,
        Year INTEGER,
        Happiness_Score REAL,
        GDP_per_Capita REAL,
        Social_Support REAL,
        Healthy_Life_Expectancy REAL,
        Freedom_to_Make_Choices REAL,
        Generosity REAL,
        Perception_of_Corruption REAL
    )
''')

df.to_sql('happiness', conn, if_exists='append', index=False)
query = '''
    SELECT Country, Happiness_Score
    FROM happiness
    WHERE Year = 2024 AND Happiness_Score > 7.5
    ORDER BY Happiness_Score DESC
'''
result = pd.read_sql(query, conn)
print(result)
query = '''
    SELECT AVG(Happiness_Score) as Average_Happiness_Score
    FROM happiness
    WHERE Year = 2024
'''
result = pd.read_sql(query, conn)
print(result)



query = '''
    SELECT Country, Happiness_Score
    FROM happiness
    WHERE Year = 2024
'''
data_2024 = pd.read_sql(query, conn)


plt.figure(figsize=(10, 6))
sns.histplot(data_2024['Happiness_Score'], bins=20, kde=True)
plt.title('Распределение индекса счастья в 2024 году')
plt.xlabel('Индекс счастья')
plt.ylabel('Количество стран')
plt.show()

conn.close()


