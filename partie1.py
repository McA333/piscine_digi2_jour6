import pandas as pd

def read_parquet(filename) :

    file_parquet = pd.read_parquet(filename)
    print(file_parquet.head(10))

read_parquet("./flights.parquet")