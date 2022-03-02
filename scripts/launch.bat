@echo off
CALL D:\Bitnami\wampstack-8.1.2-0\scripts\setenv.bat
START /MIN "WAMP packaged by Bitnami Environment" CMD /C %*
                    