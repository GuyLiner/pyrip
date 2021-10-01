import tkinter as tk
import os
import configparser
import youtube_dl
import json
import argparse
import gui
import img_pull

def confchk():
    if not(os.path.exists(r'config/config.ini')):
        config = configparser.ConfigParser()
        default = config['DEFAULT']
        default['username'] = ''
        default['client_id'] = ''
        default['client_secret'] = ''
        default['user_agent']=""
        default['username']=""
        default['password']=""

        if not(os.path.exists('config')):
            os.mkdir('config')
        with open(r'config/config.ini','w') as configfile:
            config.write(configfile)

def main():
    confchk()
    parser = argparse.ArgumentParser(description='Program that will pull images from specified subreddit.')
    subparsers = parser.add_subparsers(metavar='[cli,gui]',dest='ui_opt',required=True)

    cli_cmds = subparsers.add_parser('cli', help='Command Line arguments')
    cli_cmds.add_argument('-n',
                        '--pullnum',
                        type=int,
                        required=True,
                        help='Specify how many posts you want to pull')

    cli_cmds.add_argument('-s',
                        '--subreddit',
                        required=True,
                        help='Specify the subreddit')

    start_gui = subparsers.add_parser('gui', help='Starts the application in Graphical Mode')
    args = parser.parse_args()

    if(args.ui_opt == 'cli'):
        ImgPull = img_pull.img_pull(args.subreddit)
        ImgPull.pull(args.pullnum)

    elif(args.ui_opt == 'gui'):
        root=tk.Tk()
        app = gui.Window(master=root)
        app.mainloop()

if __name__ == '__main__':
    main()
