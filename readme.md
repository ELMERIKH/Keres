
![!\[Alt text\](<>)](<2023-12-31 09_49_35-Kali-Linux-2021.3-vmware-amd64 - VMware Workstation 17 Player (Non-commercial us.png>)

Greetings
-------------------------------------

Keres a is Powershell rev-shell backdoor with persistence for windows and linux (pwsh)

it generates a PE exe that spawns a powershell process that starts a powershell rev-shell with persistence (if process stops an other one is spawned , if process is running don t spawn new process)

also it creates a Hidden batch and vbs file for persistent startup using reg.exe (value 'keres')

you can add -Ps (optional) to generate only a .ps1 file that do same thing

run the.ps1 file like the following for persistent startup (you can also change name of file btw ,reg value 'Meow'):

./keres.ps1 -p


(compilation with nuitka)

Update ! : 
-------------------------------------------

added obfuscation for the PE using Pyarmor

to do : 

add more options (DLL PE, startup for linux...)

SETUP :
---------------------

git clone https://github.com/ELMERIKH/Keres

cd keres

pip install -r requirements.txt

sudo apt install patchelf (Linux)

python3 keres.py

(PS : if on linux and want to compile a win binary use wine to compile ./dist/pewpew.py or pewpew.py or just compile it on a windows env) 

tutorial: [wine-tuto](wine-tuto/wine.md)
-------------------

DISCLAIMER :
----------------------------------

ME The author takes NO responsibility and/or liability for how you choose to use any of the tools/source code/any files provided. ME The author and anyone affiliated with will not be liable for any losses and/or damages in connection with use of Keres. By using Keres or any files included, you understand that you are AGREEING TO USE AT YOUR OWN RISK. Once again Keres is for EDUCATION and/or RESEARCH purposes ONLY.


