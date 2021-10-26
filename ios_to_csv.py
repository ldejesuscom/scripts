# Connect to switch list of IPs in hosts.txt file and runs the command entered by user.
# A csv file is generated for each device in the text document with the data structured in columns.
import csv
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetmikoAuthenticationException
import getpass

# Prompts user to input the command they wish to run against the list of IPs.
command = input("Enter the command you want to run: ").lower()

def ios_to_csv(ios_output):
    # Automatically create column header out of the Rows "keys" or command output from textfsm.
    header = list(ios_output[0].keys())

    # Write to CSV File.  Header and Rows.
    with open((f'{host}_{command}.csv'), 'a', encoding = 'UTF8', newline='') as file:
        writer = csv.DictWriter(file, header)
        writer.writeheader()
        writer.writerows(ios_output)



# Read from a list of hostnames to connect to
hosts = open('hosts.txt','r')
hosts = hosts.read()
hosts = hosts.strip().splitlines()
userName = input('\nUsername: ')

# Loop to process hosts in hosts.txt file
for host in hosts:
    # SSH Authentication Error handling.  Gives three more attempts to enter password.
    print(f"\nAttempting {host} ...\n")
    for attempt in range(3):
        try:
            # Get password from input
            passWord = getpass.getpass()
            # Define device type and connection attributes
            device = {
                'device_type': 'cisco_ios',
                'ip': host,
                'username': userName,
                'password': passWord,
            }
        
            # Netmiko SSH Connection Handler
            net_connect = ConnectHandler(**device)
            # If connection is successful, continue with script.
            break

        except NetmikoAuthenticationException:
            print(f"Authentication Error.  Please try again.")

	# Execute commands
    output = net_connect.send_command(command, use_textfsm = True)
    print('-------------- Output from ' + host + '------------------')
    print(output)
    ios_to_csv(output)
    # Disconnect from each instance
    net_connect.disconnect()
print('\n!!!!!!!!!!!!!!! DONE !!!!!!!!!!!!!!!!\n')
