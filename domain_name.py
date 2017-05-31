# written by Parth V
# you probably will need to install tld package to extract the top level domain name
from tld import get_tld


def get_domain_name(url):
    '''
    Function returns the top level domain name when given the url of the website
    :param url: Url of the website
    :return: top level url using get_tld from tld
    '''
    return get_tld(url)


