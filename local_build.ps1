$env:DEV_MODE = "False"
& poetry run pyinstaller .\updater.spec --noconfirm
& mv .\dist\updater.exe .\ -Force # Para el build final
& cp .\updater.exe .\src -Force # Para pruebas en desarrollo
& poetry run pyinstaller .\budget-maker-desktop.spec --noconfirm