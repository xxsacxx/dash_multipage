import pymongo
import pandas as pd
import dash_html_components as html

# use this to import csv into local mongo db
# mongoimport --db db_dash --collection collection_dash --type csv 
# --headerline --file data/data.csv

def pydf():
	myclient = pymongo.MongoClient("mongodb://localhost:27017/")
	mydb = myclient["db_dash"]
	mycol = mydb["collection_dash"]

	df = pd.DataFrame(list(mycol.find()))
	# table = []
	# for index, row in df.iterrows():
	# 	html_row = []
	# 	for i in range(len(row)):
	# 		html_row.append(html.Td([row[i]]))
	# 	table.append(html.Tr(html_row))
	return df



# def make_dash_table(df):
#     ''' Return a dash definition of an HTML table for a Pandas dataframe '''
#     return html.Div([
#         a=pydf()
        
#     ])