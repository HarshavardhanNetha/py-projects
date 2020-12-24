import requests
from bs4 import BeautifulSoup as bs

headers={"user-agent":"Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
login_data={'username': 'b171325', 'password': 'password'}

with requests.Session() as s:
    url="http://lms.rgukt.ac.in/login/index.php"
    r = s.get(url,headers=headers)
    soup=bs(r.content,'html5lib')
    login_data['logintoken']=soup.find('input', attrs={'name':'logintoken'})['value']
    r = s.post(url,headers=headers,data=login_data)
    
    url="http://lms.rgukt.ac.in/mod/attendance/view.php?id=1226"
    r = s.get(url,headers=headers)
    soup=bs(r.content,'html5lib')
    #attendance_data={}
    #attendance_data[sessid]=soup.find('a', attrs={'name':'logintoken'})['value']
    for x in soup.findAll('td', attrs={'class':'statuscol cell c2 lastcol'}):
        print(x.find('a')['href'])
        url=x.find('a')['href']
    	print(x.find('a').contents[0])
    r = s.get(url,headers=headers)
    print()
    soup=bs(r.content,'html5lib')
    attnd_data={
        '_qf__mod_attendance_student_attendance_form': '1',
        'mform_isexpanded_id_session': '1',
        'submitbutton': 'Save changes'
    }
    print(r.content)
    attnd_data['sessid']=soup.find('input', attrs={'name':'sessid'})['value']
    attnd_data['sesskey']=soup.find('input', attrs={'name':'sesskey'})['value']
    
    values=soup.findAll('input', attrs={'name':'status'})
    
    attnd_data['status']=values[0]['value']

    print(attnd_data)

    
    url = 'http://lms.rgukt.ac.in/mod/attendance/attendance.php'

    r = s.post(url,headers=headers,data=attnd_data)

    print("Attendance submitted successfully!")

'''
sessid: 11073
sesskey: 6e5PlG7ijK
sesskey: 6e5PlG7ijK
_qf__mod_attendance_student_attendance_form: 1
mform_isexpanded_id_session: 1
status: 543
submitbutton: Save changes
'''