# Using a sample dataset URL
url = "https://raw.githubusercontent.com/datasets/iris/master/data/iris.csv"
df = pd.read_csv(url)
print("First 5 rows:")
print(df.head())
