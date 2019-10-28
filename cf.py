import requests
from bs4 import BeautifulSoup
import sys

URL = "https://codeforces.com/submissions/Yoo_booy/page/"
k=1
acc=0
rej=0
total=0
prev=0
print('Getting data',end='')
sys.stdout.flush()
while True:
	print('.',end='')
	sys.stdout.flush()
	try:
		r = requests.get(URL + str(k))
	except:
		break
	#print("Getting data from "+ URL + str(k))
	soup = BeautifulSoup(r.content, 'html5lib')
	p=len(str(soup))
	if p == prev:
		break
	table = soup.find('table', attrs = {'class': 'status-frame-datatable'})
	for row in table.findAll('span', attrs = {'class':'submissionVerdictWrapper'}):
		total+=1
		e=row.findAll('span', attrs = {'class': "verdict-accepted"})
		if len(e) != 0:
			acc+=1
		e = row.findAll('span', attrs = {'class': "verdict-rejected"})
		if len(e) != 0:
			rej+=1  
	k+=1
	prev=p
print('\rNumber of accepted submissions = ' + str(acc))
print('Number of rejected submissions = ' + str(rej))
print('Number of non compilable submissions = ' + str(total-rej-acc))
print('Total number of submissions = ' + str(total))