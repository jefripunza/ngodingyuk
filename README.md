###  NGODINGYUK  ###

## RULES ##
directory main system: .ngodingyuk -> ok.py
main run file: ~/ngodingyuk (shell) -> python .ngodingyuk/ok.py (echo off)
directory project node.js: project

## MAIN RUN ##
nohup php -S 0.0.0.0:8080 -t ~/ngodingyuk/public_html   > ~/.ngoding-debug/public_html.log      2>&1 &
nohup php -S 0.0.0.0:8001 -t ~/.icecoder/               > ~/.ngoding-debug/icecoder.log         2>&1 &
nohup php -S 0.0.0.0:8002 -t ~/.phpmyadmin/             > ~/.ngoding-debug/phpmyadmin.log       2>&1 &
nohup php -S 0.0.0.0:8004 -t ~/.ngoding-debug/          > ~/.ngoding-debug/ngoding-debug.log    2>&1 &
nohup mysqld_safe                                       > ~/.ngoding-debug/mysqld_safe.log      2>&1 &

# nanti dulu
nohup php -S 0.0.0.0:1002 -t ~/.filemanager/            > ~/.ngoding-debug/filemanager.log 2>&1 &




## REPLACE BRO
phpMyAdmin-5.0.4-all-languages
https://files.phpmyadmin.net/phpMyAdmin/5.0.4/phpMyAdmin-5.0.4-all-languages.zip





### HOW TO INSTALL
cd && pkg install git -y && git clone https://github.com/jefripunza/ngodingyuk.git ngodingyuk && cd ~/ngodingyuk && chmod 755 * && ./install

### PERINTAH TAMBAHAN
mysql -u $(whoami); clear; echo "ok!";
use mysql; set password for 'root'@'localhost' = password(''); flush privileges; quit;