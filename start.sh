#!/bin/bash
echo>results.txt
echo>links.txt
python3 youtubesearch.py
rm ytpage.html
python3 numbering.py
xterm -e python3 player.py &
less results.txt
