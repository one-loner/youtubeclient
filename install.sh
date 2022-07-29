#!/bin/bash
touch channels.txt
echo "Установим необходимые дя работы компоненты. Нажмите Enter для начала."
read
sudo apt-get install python3 tor obfs4proxy proxychains mpv xterm wget youtube-dl links2 wget curl
echo =====================================================================================================================
echo "Если установщик не выдал ошибок, то компоненты были успешно установлены."
echo ""
echo "Далее проверим работу Tor. Нажмите Enter для начала. После загрузки страницы нажмите q для выхода."
read
links2 -socks-proxy 127.0.0.1:9050 https://check.torproject.org
echo "Если страница успешно загрузилась, значит Tor работает."
echo "Теперь проверим работу proxychains. Нажмите Enter для начала."
read
proxychains curl https://check.torproject.org
echo "Если выдаётся длинный текст запроса, значит proxychains работает."
echo "Теперь добавьте ссылки на интересные вам каналы в файл channels.txt, после чего для запуска программы введите: ./start.sh"
chmod +x start.sh
chmod +x youtubepars.sh 
