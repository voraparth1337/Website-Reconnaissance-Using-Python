# written by Parth V
import os


def get_whois(url):
    '''
    Function to get whois of the url
    :param url: url 
    :return: whois result 
    '''
    command = 'whois ' + url

    process = os.popen(command)

    result = str(process.read())

    return result
