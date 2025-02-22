$env:DEV_MODE = "False"
& poetry run pyinstaller .\updater.spec
& mv .\dist\updater.exe .\ -Force
& poetry run pyinstaller .\budget-maker-desktop.spec