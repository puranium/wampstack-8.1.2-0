@echo off
"D:\Bitnami\wampstack-8.1.2-0/mariadb\bin\mysql.exe" --defaults-file="D:\Bitnami\wampstack-8.1.2-0/mariadb\my.ini" -u root -e "DELETE FROM mysql.user WHERE User='';"
"D:\Bitnami\wampstack-8.1.2-0/mariadb\bin\mysql.exe" --defaults-file="D:\Bitnami\wampstack-8.1.2-0/mariadb\my.ini" -u root -e "SET Password=password('%1');"

