import os
j=1
while j==1:
  i=input('Для просмотра видео введите номер ссылки, для скачивания - номер ссылки со знаком минус, 0 для выхода: ')
  if i=='':
    print('')
    continue
  if i=='0':
    j=0
    break
  else:
    if int(i)>0:
      command='cat links.txt | head -n'+i+' | tail -n1 > link.txt'
      os.system(command)
      os.system('proxychains mpv --playlist=link.txt')
    else:
       if int(i)<0:
         i=i.replace('-','')
         command='cat links.txt | head -n'+i+' | tail -n1 > link.txt'
         os.system(command)
         f=open('link.txt')
         l=f.read()
         f.close()
         nv=input('Введите для скаченного файла или просто нажмите Enter, в таком случае имя у файла будет как у скаченного видео: ')
         if nv=='':
            os.system('proxychains youtube-dl '+l)
         else:
            nv=' -o '+nv+'.mp4'
            l=l+nv
            l=l.replace('\n','')
            os.system('proxychains youtube-dl '+l)
         print('-----------------------------')
         print('Список скаченных видео:')
         os.system('ls | grep .mp4 > files.txt')
         os.system('nl files.txt')
         print('-----------------------------')
         print("Для просмотра видео введите его порядковый номер, либо нажмите Enter для продолжения работы.")
         n=input()
         if n=='':
           print('-----------------------------')
         else:
           command='cat files.txt | head -n'+n+' | tail -n1 > file.txt'
           os.system(command)
           f=open('file.txt','r')
           fn=f.read()
           f.close()
           fn='"'+fn
           fn=fn+'"'
           fn=fn.replace('\n','')
           os.system('mpv '+fn)
           print(fn)
           print('-----------------------------')
