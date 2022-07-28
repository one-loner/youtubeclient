f=open('results.txt','r')
s=''
l=''
i=0
for line in f:
  if 'https://invidious.namazso.eu/' in line:
     i=i+1    
     s=s+str(i)+'. '+line
     l=l+line
  else:
     s=s+line
f.close()
f=open('links.txt','w')
f.write(l)
f.close()
f=open('results.txt','w')
f.write(s)
f.close()
