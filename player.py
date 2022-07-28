import os
j=1
while j==1:
  i=input('Введите номер ссылки или 0 для выхода: ')
  if i=='0':
    j=0
    break
  else:
    command='cat links.txt | head -n'+i+' | tail -n1 > link.txt'
    os.system(command)
    os.system('proxychains mpv --playlist=link.txt')
