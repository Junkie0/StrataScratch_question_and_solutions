# ID 10363
# Import your libraries
import pandas as pd

# Create two dates for the 1st quarter
start_date = '2023-01-01'
end_date = '2023-03-31'

# Using loc function we are filter the dates by week column
# date must be more than or equal to starting date
# date must be smaller than or equal to ending date
quarter_1 = orders_analysis.loc[(orders_analysis['week'] >= start_date) & (orders_analysis['week'] <= end_date)]