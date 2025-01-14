pwd
ls
vi reg.py
python3 reg.py 
vi reg.py 
ll
exit
pwd
ll
git init
ls
pwd
lla
ll
cd .git/
ls
cd config/
vi config
exit
pwd
ls
mkdir flaskProject
cd flaskProject/
python3 -m venv venv
ls
cd venv/
ls
cd bin/
ls
cd ../..
pwd
source venv/bin/activate
deactivate 
source venv/bin/activate
pip install flask
pip freeze > requirements.txt
python3 app.py
cd flaskProject/
python3 app.py
source venv/bin/activate
python3 app.py 
source flaskProject/venv/bin/activate
cd flaskProject/
python3 app.py 
pwd
ll
cd flaskProject/
ll
cd venv/
ll
cd ../..
pwd
source flaskProject/venv/bin/activate
python3 app.py
cd flaskProject/
python3 app.py
exit
ll
source flaskProject/venv/bin/activate
cd flaskProject/
ll
vi app.py 
vi requirements.txt 
cd templates/
ll
vi register.html 
cd ~
pwd
cd flaskProject/
vi users.json 
pwd
cd ~
pwd
ll
vi .git
cd .git
ll
vi config
vi COMMIT_EDITMSG 
vi HEAD 
cd logs/
ll
vi HEAD 
cd ../
cd refs
ll
cd remotes/
ll
cd origin/
ll
vi main
cd ~
exit
java --version
javac --version
exit
pwd
cd ~
pwd
ls
ll
lla
ls la
ls -a
la
ll
mkdir dir
rmdir dir
touch jk
rm jk
file reg.py 
find .py
find reg.py
find style.css
find flaskProject/
clear
pwe
pwd
echo helloworld
echo helloworld >> jk
rm jk
pwd
find .
clear
ping
ping 0.0.0.0
ipconfig
netstart
route
date
ps
cd ~
ll
vi reg.py 
exit
pwd
ls -l
ls -a
ls -l -a
pwd
mysql -u uys_1705817 -p
mysql -u uys_1705817 -p
mkdir sqlProject
cd sqlProject/
python3 -m venv venv
source venv/bin/activate
pip install mysql-connector-python
python3 main.py 
pip install mysql-connector-python
python3 main.py 
cd ~
pwd
ps
man ps
ps aux | grep z
ps aux | grep uys
clear
pwd
cd flaskProject/
source venv/bin/activate
nohup python3 app.py > mylog.log 2>&1 &
pwd
exit
pwd
cd api
python3 -m venv venv
source venv/bin/activate
pip install flask
pip install mysql-connector-python
exit
pwd
cd api
source venv/bin/activate
./ app.py 
python3 app.py 
cd flaskProject/
source venv/bin/activate
pip install mysql-connector-python flask
mysql -u uys_1705817 -p
python3 app.py 
exit
mysql -u uys_1705817 -p
cd api/
source venv/bin/activate
python3 app.py 
cd ~
lsof -i :15022
kill -9 221041
kill -9 221040
lsof -i :15022
cd api
python3 app.py 
pip install mysql-connector-python flask
nohup python3 app.py > mylog.log 2>&1 &
exit
cd api
./ server.sh 
source server.sh 
ll
chmod 755 server.sh 
./server.sh 
bash server.sh 
./server.sh 
ll
vi server.sh 
./server.sh 
exit
pwd
lsof -i :15022
kill -9 225658
kill -9 225660
lsof i :15022
lsof -i :15022
exit
pwd
./server.sh
server.sh
cd api/
./server.sh 
cd ~
pwd
ll
docker build -t flask-uys_1705817 .
cd flaskProject/
source venv/bin/activate
docker build -t flask-uys_1705817 .
docker run -p 15022:15022 flask-uys_1705817
docker build -t flask-uys_1705817 .
docker run -p 15022:15022 flask-uys_1705817
cd flaskProject/
source venv/bin/activate
docker compose down 
docker ps
docker compose
cd ~
docker version
clear
ping -c 2 8.8.8.8
cd flaskProject/
source venv/bin/activate
cd ~
apt-get update
pwd
ll
pwd
docker version
cd api/
python3 app.py 
cd ~
lsof -i: 15022
lsof -i:15022
lsof -i: 15022
lsof -i
sudo lsof -i:15022
docker info
docker image ls
docker image pull httpd
docker image ls
docker pull nginx:1.12
docker pull bitnami/nginx
docker ps
docker run -d --name umyun3 -p 15022:80 nginx:1.12
exit
mysql -u uys_1705817 -p
exit
lsof -i:15022
cd api/
source venv/bin/activate
python3 app.py 
../
cd ~
cd flaskProject/
docker network ls
docker ps
docker stop c422
docker ps
cd ~
cd api/
python3 app.py 
cd ~
mkdir webProj
cd webProj/
python3 -m venv venv
deactivate
source venv/bin/activate
pip install flask
pip install mysql-connector-python flask
pip freeze > requirements.txt
python3 app.py 
python3 apa
python3 app.py 
(venv) $ nohup python3 app.py > mylog.log 2>&1 &
docker ps
lsof -i:15022
docker images
docker pull mysql
docker run -d --name uys mysql
docker ps 
docker ps -a
docker run -d --name mydb -e MYSQL_ROOT_PASSWORD=123 mysql
docker ps
mkdir dockerProj
cd dockerProj/
vi 1.txt
docker rm -f f01b
docker ps
docker run -d --name uysdb --env-file 1.txt mysql
docker ps
hostname
docker exec uysdb hostname
docker exec uysdb date
docker exec -it uysdb bash
docker run -d --name www -p 8383:80 nginx:1.12
docker exec -it www bash
docker ipconfig
docker ps
docker rm -f 9713
vi index.html
docker rm -f 4e98
docker ps
docker ps -a
docker ps
lsof -i:15022
kill -9 485545
kill -9 485538
docker images
docker run -d --name www nginx
docker ps
docker rm -f www
docker ps
docker run -d -name www -p 15022:80 nginx:1.12
docker run -d --name www -p 15022:80 nginx:1.12
docker ps
mkdir bind_volume
docker run -d --name uysweb -p 15022:80 -v /bind_volume:/usr/share/nginx/html nginx:1.12
docker rm -f www
docker run -d --name uysweb -p 15022:80 -v /bind_volume:/usr/share/nginx/html nginx:1.12
docker ps
docker ps -a
docker rm uysweb
docker rm uys
docker rm uysdb
docker rm umyun3
docker run -d --name uysweb -p 15022:80 -v /bind_volume:/usr/share/nginx/html nginx:1.12
docker exec -it uysweb bash
docker inspect uysweb
docker inspect uysweb | grep -A 10 Mounts
docker rm -f uysweb
docker rm uysweb
docker run -d --name uysweb -p 15022:80 -v /bind_volume:/usr/share/nginx/html nginx:1.12
ls /bind_volume
cd ~
cd webProj/
source venv/bin/activate
python3 app.py 
lsof -i:15022
pwd
clear
nohup python3 app.py > mylog.log 2>&1 &
mysql -u uys_1705817 -p
exit
docker ps
docker rm uysweb
docker rm -f uysweb
docker ps
lsof -i:15022
kill -9 574602
lsof -i:15022
exit
docker pull centos
docker run -it --name voltest --tmpfs /abc123 centos
docker ps
docker ps -a
docker rm voltest 
docker volume ls
docker image rm nginx:1.12
docker image ls
ip addr
apt-get -y install bridge-utils
sudo apt-get -y install bridge-untls
brctl show
docker run -d --name uys -p 15022:80 nginx
docker ps
docker inspect uys
ip addr
docker ps
docker rm -f uys
docker run -d --name uys -e MYSQL_ROOT_PASSWORD=123 mysql
docker ps
brctl show
0.
docker ps
docker rm -f uys
docker network ls
docker network create uys
docker network ls
brctl show
docker network rm uys
docker network create --subnet 10.100.1.0/24 uysnet
docker network ls
docker network inspect uysnet 
docker run -d --name uys --network uysnet -p 15022:80 nginx
docker  run  -d  --name  uysdb  --network  uysnet  -e  MYSQL_ROOT_PASSWORD=123  mysql
brctl show
docker inspect uys | grep IPAddr
docker inspect uysdb | grep IPAddr
docker stop uys
docker run -it --name uys1 --network uysnet centos
docker start uys 
docker exec -it uys1 bash
docker ps
docker rm -f uys1
docker rm -f uysdb
docker rm -f uys
docker network create wordpress_net
docker volume create dbfile
docker run -d     --name mysqldb     --network wordpress_net     --volume dbfile:/var/lib/mysql     --env-file 1.txt     mysql
docker run -d     --name mysqldb     --network wordpress_net     --volume dbfile:/var/lib/mysql     -e MYSQL_ROOT_PASSWORD=rootpass     -e MYSQL_DATABASE=wpdb     -e MYSQL_USER=wordpress     -e MYSQL_PASSWORD=wordpress     mysql
docker run -d     --name web     --network wordpress_net     -p 8080:80     -e WORDPRESS_DB_HOST=mysqldb     -e WORDPRESS_DB_NAME=wpdb     -e WORDPRESS_DB_USER=wordpress     -e WORDPRESS_DB_PASSWORD=wordpress     wordpress
docker rm -f web
docker run -d     --name web     --network wordpress_net     -p 15022:80     -e WORDPRESS_DB_HOST=mysqldb     -e WORDPRESS_DB_NAME=wpdb     -e WORDPRESS_DB_USER=wordpress     -e WORDPRESS_DB_PASSWORD=wordpress     wordpress
docker network rm wordpress_net 
docker network ls
docker stop web mysqldb
docker rm web mysqldb
docker network rm wordpress_net 
docker network rm uysnet 
docker volume rm dbfile 
