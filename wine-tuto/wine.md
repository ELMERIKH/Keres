this is wine tutorial for compiling PEfor windows in linux

steps(assuming you are in ./Keres):

1- sudo apt install wine
-----------------------------------------------------------------------
(if you already have it : sudo apt-get install --reinstall wine)

2- wget https://www.python.org/ftp/python/3.11.5/python-3.11.5-amd64.exe -O python-installer.exe
--------------------------------------------------------------------------------------

install python in wine by running : wine python-installer.exe
--------------------------------------------------------------------------

3- find ~/.wine -name python.exe
------------------------------------------------------
copy the path ,should look like this : /home/kali/.wine/drive_c/users/kali/AppData/Local/Programs/Python/Python311/python.exe

same thing with pip :

find ~/.wine -name pip.exe
--------------------------------------------------
/home/kali/.wine/drive_c/users/kali/AppData/Local/Programs/Python/Python311/Scripts/pip.exe
-----------------------------------------------------------------
5- run like this : 

wine /home/kali/.wine/drive_c/users/kali/AppData/Local/Programs/Python/Python311/Scripts/pip.exe install -r requirements.txt
------------------------------------------------------------------------

or just install nuitka or pyinstaller : 

wine /home/kali/.wine/drive_c/users/kali/AppData/Local/Programs/Python/Python311/Scripts/pip.exe install nuitka
-------------------------------------------------------------------------------------------
or

wine /home/kali/.wine/drive_c/users/kali/AppData/Local/Programs/Python/Python311/Scripts/pip.exe install pyinstaller
-------------------------------------------------------------------

6-you can now compile an exe file for windows in linux:

wine /home/kali/.wine/drive_c/users/kali/AppData/Local/Programs/Python/Python311/python.exe keres.py
-------------------------------------------------------------------

if you used :

wine /home/kali/.wine/drive_c/users/kali/AppData/Local/Programs/Python/Python311/Scripts/pip.exe
---------------------------------------------------

just run keres.py: 

wine /home/kali/.wine/drive_c/users/kali/AppData/Local/Programs/Python/Python311/python.exe keres.py -a 'adresse' -P 'port'
------------------------------------------------------------------------------

should be working :)





