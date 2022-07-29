#!/bin/bash
echo> ytpage.html
echo =======================================ПОДСКАЗКА======================================= > results.txt
echo 'Для поиска по файлу /запрос и ?запрос, n для перехода к следующему результату поиска.'>>results.txt
echo 'Нажмите q для выхода из файла. Для повторного открытия файла наберите less results.txt'>>results.txt
echo 'Внимание: при повторном запуске клиента данный файл будет удалён.'>>results.txt

echo ======================================================================================= >> results.txt

cat channels.txt | while read line
do
      proxychains wget $line -O ytpage.html
      python3 youtubepars.py
      echo ====================================================================================== >>results.txt
done
echo =======================================ПОДСКАЗКА======================================= >> results.txt
echo 'Для поиска по файлу /запрос и ?запрос, n для перехода к следующему результату поиска.'>>results.txt
echo 'Нажмите q для выхода из файла. Для повторного открытия файла наберите less results.txt'>>results.txt
echo 'Внимание: при повторном запуске клиента данный файл будет удалён.'>>results.txt
rm ytpage.html
python3 numbering.py
xterm -e python3 player.py &
less results.txt
rm link.txt file.txt files.txt
