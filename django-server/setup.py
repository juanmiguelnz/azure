import os, subprocess

server_name = 'django_server'
ip_address = '10.10.10.10'

# subprocess.run(['sudo', 'apt', 'update'])
# subprocess.run(['sudo', 'apt', 'upgrade', '-y'])
# subprocess.run(['sudo', 'apt', 'install', 'python3', '-y'])
# subprocess.run(['sudo', 'apt', 'install', 'python3-pip', '-y'])
# subprocess.run(['hostnamectl', 'set-hostname', 'django-server'])

with open('/etc/hosts') as host_file:
    content = host_file.readlines()

content.insert(1, 'ip_address    server_name')

with open('/etc/hosts', 'w') as host_file:
    content = ''.join(content)
    host_file.write(content)

# /etc/hosts 