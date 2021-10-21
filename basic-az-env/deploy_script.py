import os, subprocess, random, string

tenant_id = os.environ['AZ_TENANT']
sub_id = os.environ['AZ_SUB']
user_id = os.environ['AZ_USER']
user_pass = os.environ['AZ_PASS']

rg_name = input('Enter the Resource Group name:\n')
rg_location = input('Enter the Azure Region:\n')
vm_count = int(input('How many VMs do you want to create?\n'))
vm_base_name = input('Name the VM base name:\n')
adm_username = input('Enter the VM Admin Username:\n')

# login to Azure
subprocess.run(["az", "login", "--service-principal", "-u", user_id, "-p", user_pass, "--tenant", tenant_id]) 

# create resource group
subprocess.run(["az", "group", "create", "-l", rg_location, "-n", rg_name])

# create the virtual machine/s
for vm in range(vm_count):
    random_string = ''.join(random.choices(string.ascii_lowercase, k=4))
    vm_name = f"{vm_base_name}-{random_string}"
    subprocess.run(["az", "vm", "create", "-g", rg_name, "-n", vm_name, "--image", "UbuntuLTS", "--admin-username", adm_username, "--generate-ssh-keys", "--public-ip-sku", "Standard"])
    print(f"{vm_name} created.")
