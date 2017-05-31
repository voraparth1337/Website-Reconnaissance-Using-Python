# written by Parth V
import os, re


def get_ip_address(url):
    '''
    Function returns the ip address of the url provided 
    :param url: URL of the website
    :return: IPV4 address of the website
    '''
    command = 'host ' + str(url)

    # to run any process through python, it returns an object
    process = os.popen(command)

    result = str(process.read())

    # regex to get ip from first line
    ipv4 = re.compile(r'[0-9]+(?:\.[0-9]+){3}')

    re.search(ipv4, result).group()
