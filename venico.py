import pandas as pd
import polars as pl

# Create a pandas DataFrame
data = {'col1': [1, 2, 3, 4, 5], 'col2': ['a', 'b', 'c', 'd', 'e']}
df_pandas = pd.DataFrame(data)

# Convert pandas DataFrame to polars DataFrame
df_polars = pl.from_pandas(df_pandas)

# Now you can perform operations on the polars DataFrame, which should be faster than the equivalent operations on the pandas DataFrame
