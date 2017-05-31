# written by Parth V

###############################################
#                                             #
#	  Website Reconnaissance Using Python     #
#                                             #
###############################################

from general import *
from domain_name import *
from ip_address import *
from nmap import *
from robots_txt import *
from whois import *

# to store results of each website
ROOT_DIR = 'projects'

create_dir(ROOT_DIR)


def create_report(name, url, ip_add, nmap, whois, robots):
    '''
    Writes final report to file 
    :param name: name of the website
    :param url: its url
    :param ip_add: its ipv4 add
    :param nmap: nmap data
    :param whois: whois result
    :param robots: robots. txt file
    :return: void
    '''

    FILE_NAME = name + '.txt'
    FILE_FOLDER_PATH = ROOT_DIR + '/' + name
    FILE_PATH = FILE_FOLDER_PATH + '/' + FILE_NAME

    create_dir(FILE_FOLDER_PATH)

    data = '** Name ** ' + '\n' + name + '\n' + 'URL: ' + url + '\n'
    data += data + '** Ip Address ** ' + '\n' + ip_add + '\n'
    data += data + '** Nmap Scan **: ' + '\n' + nmap + '\n'
    data += data + '** Whois **: ' + '\n' + whois + '\n'
    data += data + '** Robots file ** : ' + '\n' + robots + '\n'

    write_file(FILE_PATH, data)


def gather_info(name, url):
    '''
    Function to gather information
    :param name: website name
    :param url: url of the website
    :return:  void
    '''

    # works on url
    robots = get_robots_txt(url)

    # works on url
    domain_name = get_domain_name(url)

    # works on url
    ip_add = get_ip_address(url)

    # works with server ip
    nmap = get_nmap(ip_add)

    # works with domain name
    whois = get_whois(domain_name)

    create_report(name, url, ip_add, nmap, whois, robots)
