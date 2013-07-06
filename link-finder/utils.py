'''
Created on Jul 6, 2013

@author: fahad
'''
import urllib2
import re


def get_pattern():
    """
    This pattern is insufficient to capture *ALL* the possible cases we may have in the html
    This pattern returns all relative urls on the page
    what about absolute urls? 
    """
    pattern = 'href="/(.*)/"'
    return pattern


def send_and_receive(url):
    req = urllib2.Request(url)
    resp = None
    
    # We can add retries if response code wasn't 2xx, 4xx or 5xx (That is, we had a network problem)
    try:
        resp = urllib2.urlopen(req)
        page_data = resp.read()
        
    finally:
        if resp:
            resp.close()
        
    return page_data

    
def find_links(url):
    """
    url = 'http://something.com/'
    url = 'http://something.com/download'
    url = 'http://something.com/documentation'
    """
#    if base_url:
#        full_url = base_url + url
#    else:
#        full_url = url
    
    page_data = send_and_receive(url)
    urls_on_this_page = re.findall(get_pattern(), page_data)
    return urls_on_this_page


if __name__ == '__main__':
    url = 'http://still-beyond-8192.herokuapp.com/'
    links = find_links(url)
    print links
    
    
    
    