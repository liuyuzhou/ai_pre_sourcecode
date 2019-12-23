import pandas as pd

print("before set display.max_rows = {}".format(pd.get_option("display.max_rows")))
pd.set_option("display.max_rows", 500)
print("after set display.max_rows = {}".format(pd.get_option("display.max_rows")))

print("before set display.max_columns = {}".format(pd.get_option("display.max_columns")))
pd.set_option("display.max_columns", 50)
print("after set display.max_columns = {}".format(pd.get_option("display.max_columns")))