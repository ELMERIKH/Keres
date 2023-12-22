
![Alt text](<2023-12-14 10_44_16-.png>)

Greetings

Keres a is Powershell rev-shell backdoor with persistence 

it generates a PE exe that spawns a powershell process that starts a powershell rev-shell with persistence (if process stops an other one is spawned , if process is running don t spawn new process)

also it makes a batch and vbs file for persistent startup using reg.exe

you can add -Ps (optional) to generate only a .ps1 file

(compilation with nuitka)

Update ! : 

added obfuscation for the PE using Pyarmor

to do : 

add more options (DLL PE, no startup ...)

SETUP :

git clone https://github.com/ELMERIKH/Keres

cd keres

pip install -r requirements.txt

sudo apt install patchelf (Linux)

python3 keres.py

(PS : if on linux after running use wine to compile pewpew.py or just compile it on windows env) 

DISCLAIMER :

ME The author takes NO responsibility and/or liability for how you choose to use any of the tools/source code/any files provided. ME The author and anyone affiliated with will not be liable for any losses and/or damages in connection with use of Keres. By using Keres or any files included, you understand that you are AGREEING TO USE AT YOUR OWN RISK. Once again Keres is for EDUCATION and/or RESEARCH purposes ONLY.


