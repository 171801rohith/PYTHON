import polars as pl
import pandas as pd

data_list_pd = [[1, "Abhishek"], [2, "Kritharth"], [3, "Karthik"]]
print(pl.DataFrame(data_list_pd, schema = ["ID", "Name"]))
print(pd.DataFrame(data_list_pd, columns = ["ID", "Name"]))
