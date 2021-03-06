# Barebones implementation of a website update notifier. Credits go to:
# Hunter Thornsberry
# http://www.adventuresintechland.com
# Will be customizing to make more automated.
# Alerts you when a webpage has changed it's content by comparing checksums of the html.

import hashlib
import urllib.request
import random
import time
import pygame
import sys

# TODO: Add selenium to automaticaly open the watched site upon change

# url to be scraped
# url = "https://jagr.github.io"

# time between checks in seconds
sleeptime = 60
if len(sys.argv) != 2:
    url = "https://jagr.github.io"
else:
    url = sys.argv[1]
 
print(f'Monitoring {url}')

def getHash():
    # random integer to select user agent
    randomint = random.randint(0,7)

    # User_Agents
    # This helps skirt a bit around servers that detect repeaded requests from the same machine.
    # This will not prevent your IP from getting banned but will help a bit by pretending to be different browsers
    # and operating systems.
    user_agents = [
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
        'Opera/9.25 (Windows NT 5.1; U; en)',
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
        'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
        'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.142 Safari/535.19',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:11.0) Gecko/20100101 Firefox/11.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:8.0.1) Gecko/20100101 Firefox/8.0.1',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.151 Safari/535.19'
    ]

    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', user_agents[randomint])]
    response = opener.open(url)
    the_page = response.read()

    return hashlib.sha224(the_page).hexdigest()

# url to be scraped
# url = "https://jagr.github.io"

# time between checks in seconds
sleeptime = 60

pygame.mixer.init()
pygame.mixer.music.load("yee.mp3")


current_hash = getHash() # Get the current hash, which is what the website is now

while 1: # Run forever
    if getHash() == current_hash: # If nothing has changed
        print("Not Changed")

    else: # If something has changed
        print("Changed")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue
        current_hash = getHash()
    time.sleep(sleeptime)
