@echo off
chcp 65001 >nul
rem Vektoripaja: rakentaa Windows-version omalla koneella ja ajaa itsetestin.
rem Sama kuin GitHub Actionsin julkaisu, mutta ilman zipiä ja releasea.
rem Aja repositoryn kansiossa:  rakenna_exe.bat

if not exist .venv\Scripts\python.exe (
  echo Virtuaaliympäristöä .venv ei löydy. Luo se VS Codessa: Python: Create Environment.
  exit /b 1
)
set PY=.venv\Scripts\python.exe

echo [1/3] Testit
%PY% -m pytest
if %errorlevel%==5 echo Testejä ei vielä ole.
if %errorlevel% neq 0 if %errorlevel% neq 5 exit /b 1

echo [2/3] Rakennus
%PY% -m PyInstaller --noconfirm --clean vektoripaja.spec || exit /b 1
copy /y LUE_MINUT.txt dist\Vektoripaja\ >nul

echo [3/3] Itsetesti
start "" /wait dist\Vektoripaja\Vektoripaja.exe --itsetesti
if errorlevel 1 (
  type "%TEMP%\vektoripaja-itsetesti.log"
  echo Itsetesti ei mennyt läpi.
  exit /b 1
)
type "%TEMP%\vektoripaja-itsetesti.log"
echo Valmis: dist\Vektoripaja\Vektoripaja.exe
