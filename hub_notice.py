from flask import Flask, request
import requests
import json
from bs4 import BeautifulSoup as bs
import urllib.parse
# for spreadsheet api
from oauth2client.service_account import ServiceAccountCredentials
import gspread

app=Flask(__name__)
@app.route('/')
def hello():
	headers={"user-agent":"Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
	notice_data = {}
	notice_old_data = {}

	def send_msg(msg):
		# api-endpoint
		URL = "//// replace with slackbot webhook url"

		data = {'text':msg}
		headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

		r = requests.post(url = URL, data=json.dumps(data), headers=headers)

	def fetch():
		hub_url = "https://hub.rgukt.ac.in/hub/default/user/login?_next=/hub/default/index"
		r = requests.get(url = hub_url,headers=headers,timeout=10, verify=False)
		soup=bs(r.content,'html5lib')
		notices = soup.findAll('li', attrs={'class':'list-group-item'})

		index = 1

		for i in range(1,5):
			head = sheet_ins.cell(i,1).value
			tail = sheet_ins.cell(i,2).value

			notice_old_data[head]=tail

		for i in notices:
			heading = i.text.strip()

			link = i.find('a')['href']
			if(not link.startswith('http')):
				link = "https://hub.rgukt.ac.in"+link
			else:
				pass

			notice_data[heading] = link
			sheet_ins.update_cell(index,1,heading)
			sheet_ins.update_cell(index,2,link)

			index+=1

		oldKeys = notice_old_data.keys()
		newKeys = notice_data.keys()

		tempKeys = list(set(newKeys) - set(oldKeys))
		
		print(tempKeys)

		for i in tempKeys:
			msg = i +"\n URL: "+ notice_data[i]
			send_msg(msg)

	def getSpreadSheet():
		# define the scope
		scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

		# add credentials to the account
		creds = ServiceAccountCredentials.from_json_keyfile_name('JsonFILENAME_Repalce.json', scope)

		# authorize the clientsheet 
		client = gspread.authorize(creds)
		# get the instance of the Spreadsheet
		sheet = client.open('hub notices')

		# get the first sheet of the Spreadsheet
		sheet_instance = sheet.get_worksheet(0)

		return sheet_instance


	sheet_ins = getSpreadSheet()
	fetch()
	return "Done"

if __name__ == '__main__':
    app.run(host="0.0.0.0",port="4000",debug=True)
