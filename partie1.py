import pandas as pd
from fastparquet import ParquetFile


def read_parquet(filename) :

    file_parquet = pd.read_parquet(filename)
    print(file_parquet.head(10))

def read_parquet_columns(filename, columns) :
    file_read = pd.read_parquet(filename)
    specific_selection = file_read.iloc[columns]
    print(specific_selection)

#read_parquet("./flights.parquet")
#read_parquet_columns("./flights.parquet", 2)