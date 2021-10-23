import os, subprocess

subprocess.run(['sudo', 'apt', 'update'])
subprocess.run(['sudo', 'apt', 'upgrade', '-y'])
subprocess.run(['sudo', 'apt', 'install', 'python3', '-y'])
subprocess.run(['sudo', 'apt', 'install', 'python3-pip', '-y'])
subprocess.run(['hostnamectl', 'set-hostname', 'django-server'])
