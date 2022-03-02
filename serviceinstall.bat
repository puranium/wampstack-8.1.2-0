@echo off
rem -- Check if argument is INSTALL or REMOVE

if not ""%1"" == ""INSTALL"" goto remove

if exist "D:\Bitnami\wampstack-8.1.2-0\mysql\scripts\serviceinstall.bat" (start "" /MIN "D:\Bitnami\wampstack-8.1.2-0\mysql\scripts\serviceinstall.bat" INSTALL)
if exist "D:\Bitnami\wampstack-8.1.2-0\postgresql\scripts\serviceinstall.bat" (start "" /MIN "D:\Bitnami\wampstack-8.1.2-0\postgresql\scripts\serviceinstall.bat" INSTALL)
if exist "D:\Bitnami\wampstack-8.1.2-0\elasticsearch\scripts\serviceinstall.bat" (start "" /MIN "D:\Bitnami\wampstack-8.1.2-0\elasticsearch\scripts\serviceinstall.bat" INSTALL)
if exist "D:\Bitnami\wampstack-8.1.2-0\logstash\scripts\serviceinstall.bat" (start "" /MIN "D:\Bitnami\wampstack-8.1.2-0\logstash\scripts\serviceinstall.bat" INSTALL)
if exist "D:\Bitnami\wampstack-8.1.2-0\kibana\scripts\serviceinstall.bat" (start "" /MIN "D:\Bitnami\wampstack-8.1.2-0\kibana\scripts\serviceinstall.bat" INSTALL)
if exist "D:\Bitnami\wampstack-8.1.2-0\apache2\scripts\serviceinstall.bat" (start "" /MIN "D:\Bitnami\wampstack-8.1.2-0\apache2\scripts\serviceinstall.bat" INSTALL)
if exist "D:\Bitnami\wampstack-8.1.2-0\apache-tomcat\scripts\serviceinstall.bat" (start "" /MIN "D:\Bitnami\wampstack-8.1.2-0\apache-tomcat\scripts\serviceinstall.bat" INSTALL)
if exist "D:\Bitnami\wampstack-8.1.2-0\resin\scripts\serviceinstall.bat" (start "" /MIN "D:\Bitnami\wampstack-8.1.2-0\resin\scripts\serviceinstall.bat" INSTALL)
if exist "D:\Bitnami\wampstack-8.1.2-0\activemq\scripts\serviceinstall.bat" (start "" /MIN "D:\Bitnami\wampstack-8.1.2-0\activemq\scripts\serviceinstall.bat" INSTALL)
if exist "D:\Bitnami\wampstack-8.1.2-0\openoffice\scripts\serviceinstall.bat" (start "" /MIN "D:\Bitnami\wampstack-8.1.2-0\openoffice\scripts\serviceinstall.bat" INSTALL)
if exist "D:\Bitnami\wampstack-8.1.2-0\subversion\scripts\serviceinstall.bat" (start "" /MIN "D:\Bitnami\wampstack-8.1.2-0\subversion\scripts\serviceinstall.bat" INSTALL)
rem RUBY_APPLICATION_INSTALL
if exist "D:\Bitnami\wampstack-8.1.2-0\mongodb\scripts\serviceinstall.bat" (start "" /MIN "D:\Bitnami\wampstack-8.1.2-0\mongodb\scripts\serviceinstall.bat" INSTALL)
if exist "D:\Bitnami\wampstack-8.1.2-0\lucene\scripts\serviceinstall.bat" (start "" /MIN "D:\Bitnami\wampstack-8.1.2-0\lucene\scripts\serviceinstall.bat" INSTALL)
if exist "D:\Bitnami\wampstack-8.1.2-0\third_application\scripts\serviceinstall.bat" (start "" /MIN "D:\Bitnami\wampstack-8.1.2-0\third_application\scripts\serviceinstall.bat" INSTALL)
if exist "D:\Bitnami\wampstack-8.1.2-0\nginx\scripts\serviceinstall.bat" (start "" /MIN "D:\Bitnami\wampstack-8.1.2-0\nginx\scripts\serviceinstall.bat" INSTALL)
if exist "D:\Bitnami\wampstack-8.1.2-0\php\scripts\serviceinstall.bat" (start "" /MIN "D:\Bitnami\wampstack-8.1.2-0\php\scripts\serviceinstall.bat" INSTALL)
goto end

:remove

if exist "D:\Bitnami\wampstack-8.1.2-0\third_application\scripts\serviceinstall.bat" (start "" /MIN "D:\Bitnami\wampstack-8.1.2-0\third_application\scripts\serviceinstall.bat")
if exist "D:\Bitnami\wampstack-8.1.2-0\lucene\scripts\serviceinstall.bat" (start "" /MIN "D:\Bitnami\wampstack-8.1.2-0\lucene\scripts\serviceinstall.bat")
if exist "D:\Bitnami\wampstack-8.1.2-0\mongodb\scripts\serviceinstall.bat" (start "" /MIN "D:\Bitnami\wampstack-8.1.2-0\mongodb\scripts\serviceinstall.bat")
rem RUBY_APPLICATION_REMOVE
if exist "D:\Bitnami\wampstack-8.1.2-0\subversion\scripts\serviceinstall.bat" (start "" /MIN "D:\Bitnami\wampstack-8.1.2-0\subversion\scripts\serviceinstall.bat")
if exist "D:\Bitnami\wampstack-8.1.2-0\openoffice\scripts\serviceinstall.bat" (start "" /MIN "D:\Bitnami\wampstack-8.1.2-0\openoffice\scripts\serviceinstall.bat")
if exist "D:\Bitnami\wampstack-8.1.2-0\resin\scripts\serviceinstall.bat" (start "" /MIN "D:\Bitnami\wampstack-8.1.2-0\resin\scripts\serviceinstall.bat")
if exist "D:\Bitnami\wampstack-8.1.2-0\activemq\scripts\serviceinstall.bat" (start "" /MIN "D:\Bitnami\wampstack-8.1.2-0\activemq\scripts\serviceinstall.bat")
if exist "D:\Bitnami\wampstack-8.1.2-0\apache-tomcat\scripts\serviceinstall.bat" (start "" /MIN "D:\Bitnami\wampstack-8.1.2-0\apache-tomcat\scripts\serviceinstall.bat")
if exist "D:\Bitnami\wampstack-8.1.2-0\apache2\scripts\serviceinstall.bat" (start "" /MIN "D:\Bitnami\wampstack-8.1.2-0\apache2\scripts\serviceinstall.bat")
if exist "D:\Bitnami\wampstack-8.1.2-0\kibana\scripts\serviceinstall.bat" (start "" /MIN "D:\Bitnami\wampstack-8.1.2-0\kibana\scripts\serviceinstall.bat")
if exist "D:\Bitnami\wampstack-8.1.2-0\logstash\scripts\serviceinstall.bat" (start "" /MIN "D:\Bitnami\wampstack-8.1.2-0\logstash\scripts\serviceinstall.bat")
if exist "D:\Bitnami\wampstack-8.1.2-0\elasticsearch\scripts\serviceinstall.bat" (start "" /MIN "D:\Bitnami\wampstack-8.1.2-0\elasticsearch\scripts\serviceinstall.bat")
if exist "D:\Bitnami\wampstack-8.1.2-0\postgresql\scripts\serviceinstall.bat" (start "" /MIN "D:\Bitnami\wampstack-8.1.2-0\postgresql\scripts\serviceinstall.bat")
if exist "D:\Bitnami\wampstack-8.1.2-0\mysql\scripts\serviceinstall.bat" (start "" /MIN "D:\Bitnami\wampstack-8.1.2-0\mysql\scripts\serviceinstall.bat")
if exist "D:\Bitnami\wampstack-8.1.2-0\php\scripts\serviceinstall.bat" (start "" /MIN "D:\Bitnami\wampstack-8.1.2-0\php\scripts\serviceinstall.bat")
if exist "D:\Bitnami\wampstack-8.1.2-0\nginx\scripts\serviceinstall.bat" (start "" /MIN "D:\Bitnami\wampstack-8.1.2-0\nginx\scripts\serviceinstall.bat")
:end
