import praw
import filetype
import os
from bs4 import BeautifulSoup
import requests
from rddtconn import rddtconn

class img_pull():
    def __init__(self,subreddit):
        self.subreddit_choice=subreddit
        self.reddit=rddtconn().reddit
        self.subreddit=self.reddit.subreddit(self.subreddit_choice)
        self.photos_dir = rddtconn().photodir

    def mkfold(self,foldname,base):
        if os.path.isdir(base+foldname):
            return True

        else:
            os.makedirs(str(base+foldname))

    def pull(self, number):
        for submission in self.subreddit.hot(limit=number):
            title=submission.id
            reddit_image = requests.get(submission.url)

            try:
                type_guess = filetype.guess(reddit_image.content).extension
                self.mkfold(r'/'+type_guess,self.photos_dir)

                with open(str(self.photos_dir+r'/'+type_guess)+'/'+title,'wb') as image:
                    image.write(reddit_image.content)

            except Exception as err:
                self.mkfold(r'/misc',self.photos_dir)
                print(submission.url)

                if('imgur' in submission.url and not('.gif' in submission.url)):
                    with open(self.photos_dir+r'/misc'+'/'+title,'wb') as image:
                        imgur_weblink=requests.get(submission.url)
                        soup=BeautifulSoup(imgur_weblink.content,'html.parser')
                        for link in (soup.find_all('meta')):
                            if(link.get('name') == "twitter:image"):
                                imgur_img=requests.get((link.get('content')))

                                image.write(imgur_img.content)

                elif('imgur' in submission.url and '.gif' in submission.url):
                    with open(self.photos_dir+r'/misc'+'/'+title,'wb') as image:
                        imgur_weblink=requests.get(submission.url)
                        soup=BeautifulSoup(imgur_weblink.content,'html.parser')
                        for link in (soup.find_all('meta')):
                            if(link.get('property') == "og:video:secure_url"):
                                imgur_img=requests.get((link.get('content')))

                                image.write(imgur_img.content)

                elif('redgifs' in submission.url):
                    ydl_opts = {}
                    #with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                    #ydl.download([str(submission.url)])

                else:
                    print('Couldn\'t find what the fuck this was')
