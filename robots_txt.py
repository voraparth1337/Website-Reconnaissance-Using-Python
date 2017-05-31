# written by Parth V

import urllib.request
import io


def get_robots_txt(url):
    '''
    Function gets the robots.txt file
    :param url: url of the website
    :return: robots.txt content
    '''

    # making sure url has forward slash
    if url.endswith('/'):
        path = url
    else:
        path = url + '/'

    robots_location = path + 'robots.txt'

    req = urllib.request.urlopen(robots_location, data=None)

    data = io.TextIOWrapper(req, encoding='utf-8')

    return data.read()
