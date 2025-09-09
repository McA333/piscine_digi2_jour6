import pandas as pd
from fastparquet import ParquetFile
import pyarrow.parquet as pq


def read_parquet(filename) :

    file_parquet = pd.read_parquet(filename)
    print(file_parquet.head(10))

def read_parquet_columns(filename, columns) :
    file_read = pd.read_parquet(filename)
    specific_selection = file_read.iloc[columns]
    print(specific_selection)

def read_parquet_batch(filename, batch_size) :

    file_parquet = pd.read_parquet(filename)
    parquet_file = pq.ParquetFile(filename)

    for i in parquet_file.iter_batches(batch_size) :
        print("RecordBatch")
        file_parquet = i.to_pandas()
        break
        

#read_parquet("./flights.parquet")
#read_parquet_columns("./flights.parquet", 2)
#read_parquet_batch("./flights.parquet", 350)