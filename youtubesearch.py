import os
print('Введите поисковый запрос или нажмите Enter для просмотра подписок.')
req=input()
if req=='':
  os.system('./youtubepars.sh')
  quit()
else:
  os.system('proxychains wget "https://invidious.namazso.eu/search?q='+req+'" -O ytpage.html')
  f=open('ytpage.html')
  s3=''
  s4=''
  r=''
  for line in f:
    if '<p dir="auto">' in line:
      s3=line
      s3=s3.replace('                <p dir="auto">','')
      s3=s3.replace('</p>','')
      f1=open('results.txt','a')
      f1.write(s3)
      f1.close()
    if '<a title="Watch on YouTube" href=' in line:
      s4=line
      s4=s4.replace('        <a title="Watch on YouTube" href="','')
      s4=s4.replace('">','')
      s4=s4 + '\n'
      f1=open('results.txt','a')
      f1.write(s4)
      f1.close()
  f.close()
  f=open('results.txt','r')
  s=f.read()
  s=s.replace('www.youtube.com','invidious.namazso.eu')
  f.close()
  f=open('results.txt','w')
  f.write(s)
  f.close()
