#!/bin/bash

echo 'HTML PARSER:'
echo '***MUST BE PAGE SOURCE***'
echo 'FILE TO BE PARSED: '

read HTML

echo 'Now parsing HTML: '
#move to proper directory where python file and new HTML file must be located
cd ~/Documents/schoolprojects
wget --output-document=index.html ${HTML}
python3 RosadoXavier_096_p2.py
cat index_resources.txt | less




