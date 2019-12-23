import pandas as pd

pd.set_option("display.max_rows", 500)
print("after set display.max_rows = {}".format(pd.get_option("display.max_rows")))
pd.reset_option("display.max_rows")
print("reset display.max_rows = {}".format(pd.get_option("display.max_rows")))