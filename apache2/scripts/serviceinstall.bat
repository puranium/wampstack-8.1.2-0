@echo off
rem -- Check if argument is INSTALL or REMOVE

if not ""%1"" == ""INSTALL"" goto remove

"D:/Bitnami/wampstack-8.1.2-0/apache2\bin\httpd.exe" -k install -n "wampstackApache" -f "D:/Bitnami/wampstack-8.1.2-0/apache2\conf\httpd.conf"

net start wampstackApache >NUL
goto end

:remove
rem -- STOP SERVICE BEFORE REMOVING

net stop wampstackApache >NUL
"D:/Bitnami/wampstack-8.1.2-0/apache2\bin\httpd.exe" -k uninstall -n "wampstackApache"

:end
exit
