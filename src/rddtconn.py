import praw
import configparser
from pathlib import Path
class rddtconn():
    def __init__(self):
        self.conf_obj = configparser.ConfigParser()
        self.conf_obj.read(str(Path.home())+r'/.config/pyrip/config.ini')
        self.default_sec = self.conf_obj['DEFAULT']
        self.reddit = praw.Reddit(
            client_id = self.default_sec['client_id'],
            client_secret = self.default_sec['client_secret'],
            user_agent=self.default_sec['user_agent'],
            username=self.default_sec['username'],
            password=r'{0}'.format(self.default_sec['password'])
        )
