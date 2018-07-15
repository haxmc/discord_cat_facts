###########################################################
#  _____       _    ______         _     _           _    #
# /  __ \     | |   |  ___|       | |   | |         | |   #
# | /  \/ __ _| |_  | |_ __ _  ___| |_  | |__   ___ | |_  #
# | |    / _` | __| |  _/ _` |/ __| __| | ___ \/ _ \| __| #
# | \__/\ (_| | |_  | || (_| | (__| |_  | |_/ / (_) | |_  #
#  \____/\__,_|\__| \_| \__,_|\___|\__| \____/ \___/ \__| #
###########################################################

      ################################################
      #          Made by de-taylor (Github)          #
      #        2018 - GNU Open Public License        #
      #      Built on Discord.py for delivering      #
      #        on demand cat facts in Discord        #
      # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
      #   ~*~*~ v0.6.0 - Released 07/15/2018 ~*~*~   #
      ################################################

# importing Python modules
import discord # discord.py
import requests # to pull information with APIs
import os # Python standard library, for working with the OS file system
import datetime # Python standard library, for extended logging of bot status
import time # Python standard library, for extended logging of bot status
import library.functions.fetch as fetch # importing custom module that has the API call functionality

# global variables and constants
client = discord.Client() # object instance of class Client
# discord Bot User Token (https://discordapp.com/developers, under 'My Apps')
TOKEN = '' # Bot User Token for Cat Facts Beta Tester, remove before uploading to github
#whoever you want as your POC for bot related inquiries - must use the string of numbers that are the user ID, usernames will not work here
DEV_ID = ''
dev_user = discord.utils.get(client.get_all_members(),id=DEV_ID)

# functions on client events
@client.event # decorator, triggered on any message the bot sees - listens for particular user commands
async def on_message(message): 
    eventlog = open('library/bin/logfiles/bot_logfile.log', 'a') # open status log file for writing
    commentlog = open('library/bin/logfiles/bot_comments.log', 'a') # open comment log file for writing

    ts = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S') # timestamp

    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    
    # user command 1
    if message.content.startswith('c!help') or message.content.startswith('c!helpplz'): 
        # long, complicated help message, modify if you add more commands
        msg = 'Hello! Here\'s all the commands you can use with me.\n\n'
        msg = msg + '1] `c!help` or `c!helpplz`: Gives you this menu!\n\n'
        msg = msg + '2] `c!factplz <code>`: Fetches a cat fact along with some form of digital media:\n'
        msg = msg + '\t\t `jpg`: gives a .jpg image of a kitty. {This is the default with no selection code}\n'
        msg = msg + '\t\t `gif`: gives a .gif of a kitty\n\n'
        msg = msg + '3] `c!devhelp <your comment>`: gets the attention of the dev who moderates me! I\'ll send them your username and comment, and they\'ll DM you when they can! *Don\'t worry, I never store user information without permission!*'

        logentry = str(ts) + '  User asked for help, received all commands for cat bot.\n'

        eventlog.write(logentry)

        print(logentry)

        # sends to channel where original message was posted
        await client.send_message(message.channel, msg)

        eventlog.close()

    # user command 2a - fact with JPEG
    if message.content.startswith('c!factplz jpg'):
        msg, fact_status = fetch.cat_fact_grabber()
        msg = 'Fact: ' + msg.format(message)
        cat_jpg, jpg_status = fetch.cat_jpg_grabber()
        end_msg = 'Enjoy your day! *meow*'

        # sends to channel where original message was posted
        await client.send_file(message.channel, cat_jpg, filename=cat_jpg, content=msg, tts=False)

        # sends to channel where original message was posted
        await client.send_message(message.channel, end_msg)

        logentry = str(ts) + '  Call: Fact and JPEG fetch. Fact API call status: ' + str(fact_status) + '; Image API call status: ' + str(jpg_status) + '\n'

        eventlog.write(logentry)
        print(logentry)

        os.remove(cat_jpg) # removes file once it's posted, for keeping server hard drive clear

        eventlog.close()

    # user command 2b - fact with GIF
    if message.content.startswith('c!factplz gif'):
        msg, fact_status = fetch.cat_fact_grabber()
        msg = 'Fact: ' + msg.format(message)
        cat_gif, gif_status = fetch.cat_gif_grabber()
        end_msg = 'Enjoy your day! *meow*'

        # sends to channel where original message was posted
        await client.send_file(message.channel, cat_gif, filename=cat_gif, content=msg, tts=False)

        # sends to channel where original message was posted
        await client.send_message(message.channel, end_msg)

        logentry = str(ts) + '  Call: Fact and GIF fetch. Fact API call status: ' + str(fact_status) + '; GIF API call status: ' + str(gif_status)+ '\n'

        eventlog.write(logentry)
        print(logentry)

        os.remove(cat_gif) # removes file once it's posted, for keeping server hard drive clear

        eventlog.close()

    # user command 3 - let dev know something is wrong
    if message.content.startswith('c!devhelp'):
        message_author_name = str(message.author)
        message_author_comment = message.content.lstrip('c!devhelp')

        commentlog = open('library/bin/logfiles/bot_comments.log', 'a') # open comment log file for writing

        help_msg = 'Hi! ' + message_author_name + ' has a comment on my performance, seen below:\n\n'
        help_msg = help_msg + '\t\t`' + message_author_comment + '`\n\n'
        help_msg = help_msg + 'Thank you! Please message them asap.'

        await client.send_message(dev_user, help_msg)

        commentlog.write(str(ts) + ' Comment: ' + message_author_comment + '\n') # make entry in log

        logentry = str(ts) + '  Comment logged from user, please check bot_comment logs' + '\n'

        eventlog.write(logentry) # make entry in log
        print(logentry)

        await client.send_message(message.channel, "Your comment has been logged, thank you!")

        commentlog.close()
        eventlog.close()

@client.event # decorator, triggered on ready
async def on_ready(): # need to log different things on on_ready() error
    # open existing logfile for updates, need to check if file exists, and if not, create it later
    logfile = open('library/bin/logfiles/bot_logfile.log', 'a') # need to log different things on file open error
    ts = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S') # need to log different things on time error
    status_note = 'Logged in to Discord as ' + client.user.name + ' with client ' + client.user.id
    error_msg = 'None'

    logentry = str(ts) + '  ' + status_note + '  ' + error_msg + '\n'

    # log status to two different places
    print(logentry)
    logfile.write(logentry)

    logfile.close()

client.run(TOKEN)