d1={'Telangana':'TS','Andhra pradesh':"AP",'Delhi':'DL','Ta,il Nadu':'TN'}
d1['Karnataka']='KA'
print(d1)
d1.setdefault('Gujarat','does not exist')
print(d1['Gujarat'])
