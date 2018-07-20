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
      #      Built on Discord.py for delivering      #
      #        on demand cat facts in Discord        #
      # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
      #   ~*~*~ v0.6.5 - Released 7/20/2018 ~*~*~    #
      ################################################

# importing Python modules
import discord # discord.py, to communicate with Discord
import requests # requests.py to pull information with APIs

import os # Python standard library, for working with the OS file system
import datetime # Python standard library, for extended logging of bot status
import time # Python standard library, for extended logging of bot status

import library.functions.fetch as fetch # importing custom module that has the API call functionality
import library.functions.utilities as utilities # importing custom module that has utility functions

# global variables and constants
client = discord.Client() # object instance of class Client
# discord Bot User Token (https://discordapp.com/developers, under 'My Apps')
TOKEN = BOT_USER_TOKEN # Bot User Token for Cat Facts Beta Tester, remove before uploading to github

#whoever you want as your POC for bot related inquiries - must use the string of numbers that are the user ID, usernames will not work here
DEV_ID = DISCORD_USER_ID # as string, 16 characters long, typically

# functions on client events
@client.event # decorator, triggered on any message the bot sees - listens for particular user commands
async def on_message(message):
    ts = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S') # timestamp

    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    
    # user command 1
    if message.content.startswith('c!help'):
        msg = utilities.help_command(ts, message)

        # sends to channel where original message was posted
        await client.send_message(message.author, msg)

    # user command 2 - breed information
    if message.content.startswith('c!breedplz'):
        breed_msg, end_msg = utilities.breed_info_fetch(ts, message) # expects a formatted string with the breed information

        # sends to channel where original message was posted
        await client.send_message(message.channel, breed_msg)

        await client.send_message(message.channel, end_msg)


    # user command 3a - fact with JPEG
    if message.content.startswith('c!factplz jpg'):
        msg, cat_jpg, end_msg = utilities.fact_jpg_fetch(ts, message)

        # sends to channel where original message was posted
        await client.send_file(message.channel, cat_jpg, filename=cat_jpg, content=msg, tts=False)

        # sends to channel where original message was posted
        await client.send_message(message.channel, end_msg)

        os.remove(cat_jpg) # removes file once it's posted, for keeping server hard drive clear

    # user command 3b - fact with GIF
    if message.content.startswith('c!factplz gif'):
        msg, cat_gif, end_msg = utilities.fact_gif_fetch(ts, message)

        # sends to channel where original message was posted
        await client.send_file(message.channel, cat_gif, filename=cat_gif, content=msg, tts=False)

        # sends to channel where original message was posted
        await client.send_message(message.channel, end_msg)

        os.remove(cat_gif) # removes file once it's posted, for keeping server hard drive clear

    # user command 4 - let dev know something is wrong
    if message.content.startswith('c!devhelp'):
        dev_user = discord.utils.get(client.get_all_members(),id=DEV_ID)
        
        help_msg = utilities.contact_dev(ts, message)

        await client.send_message(dev_user, help_msg)

        await client.send_message(message.channel, "Your comment has been logged, thank you!")

@client.event # decorator, triggered on ready
async def on_ready(): # need to log different things on on_ready() error
    # open existing logfile for updates, need to check if file exists, and if not, create it later
    logfile = open('library/bin/logfiles/bot_logfile.log', 'a') # need to log different things on file open error
    ts = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S') # need to log different things on time error
    status_note = 'Logged in to Discord as ' + client.user.name + ' with client ' + client.user.id
    error_msg = 'None'

    logentry = str(ts) + ' :: ' + status_note + ' :: ' + error_msg + '\n'

    # log status to two different places
    print(logentry)
    logfile.write(logentry)

    logfile.close()

client.run(TOKEN)