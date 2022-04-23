import argparse
import time
from re import sub
import pyfiglet
from textify import commands
from textify import database

BANNER = pyfiglet.figlet_format("TEXTIFY" , font = "starwars")
VERSION = '0.0.1'
def parseArguments():
    parser = argparse.ArgumentParser(description='Sync your text across devices' , epilog = 'Thanks for using textify!' , prog = 'textify')
    subparser = parser.add_subparsers(dest = 'command')
    login = subparser.add_parser('login' , help = 'Login to the server')
    list = subparser.add_parser('list' , help = 'List all the texts currently in the database')
    pull = subparser.add_parser('pull' , help = 'Pulls all the data from the server')
    push =  subparser.add_parser('push' , help = 'Pushes any given data to the server')
    show = subparser.add_parser('show' , help = "Shows ID of the user")

    push.add_argument('--type', type = str, required=True)
    push.add_argument('--content', type = str, required = True)

    login.add_argument('--ID', type = str, required=False)
    args = parser.parse_args()
    parseHandler(args)

def parseHandler(args):
    if args.command == 'login':
        print("Performing login from textify servers!")
        if args.ID:
            commands.Login(args.ID)
        else:
            commands.Login("")
    elif args.command == 'push':
        print("Pushing data to server")
        content_type = args.type
        content_data = args.content
        content_timestamp = time.time()

        payload = dict(content_type = content_type , content_data = content_data , content_timestamp = content_timestamp)
        commands.Push(payload)

    elif args.command == 'pull':
        commands.Pull()
    elif args.command == 'list':
        texts = database.GetDatabase()
        # texts = [
        #     {
        #         "content_type": "code",
        #         "content_data": "import os",
        #         "content_timestamp":"234234.23",
        #     },
        #     {
        #         "content_type": "code",
        #         "content_data": "import os",
        #         "content_timestamp":"234234.23",
        #     },
        # ]
        for i , text in enumerate(texts , 1):
            print("{}) Content: {}".format(i , text['content_data']))
    elif args.command == 'show':
        id = database.Get_ID()
        print("ID: {}".format(id))
        print("Do not share this with anyone!!!")
    else:
         print(BANNER)
         print('Version {}'.format(VERSION))
         print('Welcome to Textify!')
         print("Run `textify -h` for help")
