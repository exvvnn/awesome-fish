import os
import shutil

def fish_install(*args, **kwargs):
    if os.name == "posix":
        # macOS or Linux
        if os.system("which brew > /dev/null 2>&1") != 0:
            print("Homebrew is not installed. Please install it first.")
            print("You can install it by running: /bin/bash -c \"$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)\"")
            print("After installing Homebrew, please run this script again.")
            exit()
        os.system("brew install fish")
        print("Installing Friendly Interactive Shell...")
    elif os.name == "nt":
        # Windows
        if os.system("where choco > nul 2>&1") != 0:
            print("Chocolatey is not installed. Please install it first.")
            print("You can install it by running: powershell -Command \"Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))\"")
            print("After installing Chocolatey, please run this script again.")
            exit()
        os.system("choco install fish")
        print("Installing Friendly Interactive Shell...")


