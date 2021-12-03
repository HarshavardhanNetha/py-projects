import os

os.system("rm /etc/environment")
os.system("cp environment /etc/")
try:
	os.system("rm /etc/apt/sources.list.d/webupd8team-ubuntu-atom-focal.list")
finally:
	pass
os.system("sudo dpkg --add-architecture i386")
os.system("sudo apt update -y")
os.system("sudo apt install wine64 wine32 -y")
os.system("wine --version")
os.system("sudo apt install openssh-server -y")
os.system("sudo systemctl enable ssh")
os.system("sudo apt install wakeonlan -y")
os.system("rm /etc/environment")
os.system("cp en/environment /etc/")
os.system("wine setup.exe")
#os.system("rm -r en")
#os.system("rm environment")
