# written by Parth V

# nmap scan of the server

import os

def get_nmap(ip,options='-F'):
    '''
    Function to get NMAP scan of the server
    :param options: optional parameters
    :param ip: ip address
    :return: nmap result
    '''
    command = 'nmap ' + options + ' ' + ip
    process = os.popen(command)

    result = str(process.read())

    return result
