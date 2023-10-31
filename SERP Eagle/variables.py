"""
This module stores variables utilized within the bot, providing the flexibility to adjust settings as needed.
"""

SEARCH_QUERY = "My ip address"



"""Timeout for page loading in seconds"""
TIMEOUT_FOR_PAGE_LOAD = 100



"""default timeout in seconds"""
DEFAULT_TIMEOUT = 1



"""
time to sleep, while scrolling down the window.
The program will sleep for seconds before continuing scrolling
(Seconds)
"""
SLEEP_TIME = 1



"""Scrape with headless browser or not
Headless: True
Non-Headless: False
"""
HEADLESS = False



"""
Give proxiy details, like this:

PROXIES = {
    "server": "http://serveraddress.com:port",
    "username": "user",
    "password": "password"
}


If you want to use proxies set its value as none
"""

PROXIES = None
