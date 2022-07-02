import netmiko
outfile = open('Multiple_Device_Config.txt','w') #write

for device in devices:
    outfile.write('*' * 30+'\n')
    print('Connecting to the device', device['ip'])
    outfile.write('Connecting to the device : ' + device['ip']+'\n')
    
    try:
        if device['device_type']=='cisco_nxos'
            connection = netmiko.ConnectHandler(device_type=device['device_type'],
                                                port=device['port'],
                                                ip=device['host'],
                                                username=device['username'],
                                                password=device['password'],
                                                verbose=False,
                                                timeout=160)
        elif device['device_type']=='cisco_ios':
            connection = netmiko.ConnectHandler(device_type=device['device_type'],
                                                port=device['port'],
                                                ip=device['ip'],
                                                username=device['username'],
                                                password=device['password'],
                                                secret=device['secret'],
                                                verbose=False,
                                                timeout=160))
            connection.enable()
        
    except Exception as e:
        print('Failed to connect to the device: ', device['ip'], e)
        outfile.write(device['host']+ ': Failed to connect to the device'+'\n')
        
    else:
        for command in commands[device['model_type']]:
            print(command.center(80,'*'), '\n') #print ('{:-<40}'.format(command))
            outfile.write(command.center(80, '*') + '\n') #outfile.write('{:-<40}'.format(command))
            outfile.write(connection.send_command(command)+'\n')
        connection.disconnect()
outfile.close()
