f=open('ytpage.html')
s1=''
s2=''
s3=''
s4=''
r=''
for line in f:
  if '<title>' in line:
    s1=line
    s1=s1.replace('<title>','')
    s1=s1.replace(' - Invidious</title>','')
    s1=s1+'---------------------------------------------------------------------------------------------------------------'
    s1=s1+'\n'
    f1=open('results.txt','a')
    f1.write(s1)
    f1.close()
  if '        <p><span style="white-space:pre-wrap">' in line:
    s2=line
    s2=s2.replace('        <p><span style="white-space:pre-wrap">','')
    s2=s2.replace('<br><br></span></p>','')
    s2=s2.replace('<br></span></p>','')
    s2=s2+'---------------------------------------------------------------------------------------------------------------'
    s2=s2+'\n'
    f1=open('results.txt','a')
    f1.write(s2)
    f1.close()
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
