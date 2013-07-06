'''
Created on Jul 6, 2013

@author: fahad
'''

import utils

class Crawler(object):
    
    def __init__(self, url):
        self.base_url = url
        self.visited = {}
        self.count = 0
        self.queue = []
        
        self.queue.insert(0, self.base_url)
        
        
    def run(self):
        
        while self.queue:
            
            url = self.queue.pop()

            # proceed only if this url is not visited yet
            if not self.visited.get(url, False):
                
                try:
                    list_of_urls = utils.find_links(url)
                except Exception as e:
                    print e
                    list_of_urls = []
                
                for u in list_of_urls:
                    full_url = self.base_url + u
                    
                    # Add this url for visit if not already visited
                    if not self.visited.get(full_url, False):
                        self.queue.insert(0, full_url)
                    
                self.visited[url] = True
                self.count += 1


if __name__ == '__main__':
    crawler = Crawler(url='http://still-beyond-8192.herokuapp.com/')
    crawler.run()
    print crawler.count
    
    with open('all_links', 'w') as f:
        for k,v in crawler.visited.iteritems():
            f.write(k + '\n')
    