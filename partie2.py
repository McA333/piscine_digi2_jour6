import pandas as pd

def create_multi_index_df(df) :
    data = pd.read_csv(df)
    data.set_index("FL_DATE", inplace=True)
    print(data.head(5))

create_multi_index_df("./flights.csv")