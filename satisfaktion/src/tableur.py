# coding: utf-8
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('projet.json', scope)

client = gspread.authorize(creds)

sheet = client.open('Evaluation CEFIM (réponses)').sheet1

rows = sheet.get_all_records()
pp = pprint.PrettyPrinter()
row_count = sum(1 for row in rows)
for i in range(2,row_count) : 
    data = sheet.row_values(i)
    pp.pprint(data)




