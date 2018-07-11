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
      #   ~*~*~ v0.5.0 - Released 07/11/2018 ~*~*~   #
      ################################################

# importing Python modules
import discord # discord.py
import requests # to pull information with API
import os # Python standard library, for working with the OS file system

# global variables and constants
client = discord.Client() # object instance of class Client
# discord Bot User Token (https://discordapp.com/developers, under 'My Apps')
TOKEN = BOT_USER_TOKEN
#whoever you want as your POC for bot related inquiries
DEV_ID = USER_ID_OF_DEVELOPER

# Utility functions for bot
def cat_fact_grabber():
    # API for grabbing a fantastic fact about our favorite felines
    cat_fact_resp = requests.get('https://catfact.ninja/fact')

    resp_data = cat_fact_resp.json() # represents the server response as a JSON object

    return resp_data["fact"] # pulls the string key from the value "fact"

def cat_jpg_grabber():
    # API for featuring a fabulous photo full of frisky fellows
    cat_jpg_resp = requests.get('http://thecatapi.com/api/images/get?type=jpg&size=small&format=src', stream=True) 
    # reads the data as a stream becaise it is a large binary file
    filename = "cat_picture.jpg"

    if cat_jpg_resp.status_code == 200:
        # assuming everything goes well
        with open(filename, 'wb') as f: 
            # creating new file on system, writing binary data to it
            for chunk in cat_jpg_resp.iter_content(1024): # arg, size in bytes
                # streaming binary photo data to the new file
                f.write(chunk)

    return filename

def cat_gif_grabber():
    # API for featuring a fabulous photo full of frisky fellows
    cat_gif_resp = requests.get('http://thecatapi.com/api/images/get?type=gif&size=small&format=src', stream=True)
    filename = "cat_gif.gif"

    if cat_gif_resp.status_code == 200:
        # assuming everything goes well
        with open(filename, 'wb') as f:
            # creating new file on system, writing binary data to it
            for chunk in cat_gif_resp.iter_content(1024):
                # streaming binary photo data to the new file
                f.write(chunk)

    return filename

# functions on client events
@client.event # decorator, triggered on any message the bot sees - listens for particular user commands
async def on_message(message): 
    # asynchronous, other parts of program can execute while the request runs

    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    
    # user command 1
    if message.content.startswith('c!help') or message.content.startswith('c!helpplz'): 
        # long, complicated help message, modify if you add more commands
        msg = 'Hello! Here\'s all the commands you can use with me.\n\n'
        msg = msg + '1] `c!help` or `c!helpplz`: Gives you this menu!\n\n'
        msg = msg + '2] `c!factplz <code>`: Fetches a cat fact along with some form of digital media:\n'
        msg = msg + '\t\t `j`: gives a .jpg image of a kitty.\n'
        msg = msg + '\t\t `g`: gives a .gif of a kitty\n\n'
        msg = msg + '3] `c!devhelp <your comment>` {*only on certain servers*}: gets the attention of the dev who moderates me! I\'ll send them your username and comment, and they\'ll DM you when they can!'

        # sends to channel where original message was posted
        await client.send_message(message.channel, msg)

    # user command 2a - fact with JPEG
    if message.content.startswith('c!factplz j'):
        msg = 'Fact: ' + cat_fact_grabber().format(message)
        cat_jpg = cat_jpg_grabber()
        end_msg = 'Enjoy your day! *meow*'

        # sends to channel where original message was posted
        await client.send_file(message.channel, cat_jpg, filename=cat_jpg, content=msg, tts=False)

        # sends to channel where original message was posted
        await client.send_message(message.channel, end_msg)

        os.remove(cat_jpg) # removes file once it's posted, for keeping server hard drive clear

    # user command 2b - fact with GIF
    if message.content.startswith('c!factplz g'):
        msg = 'Fact: ' + cat_fact_grabber().format(message)
        cat_gif = cat_gif_grabber()
        end_msg = 'Enjoy your day! *meow*'

        # sends to channel where original message was posted
        await client.send_file(message.channel, cat_gif, filename=cat_gif, content=msg, tts=False)

        # sends to channel where original message was posted
        await client.send_message(message.channel, end_msg)

        os.remove(cat_gif) # removes file once it's posted, for keeping server hard drive clear

    # user command 3 - let dev know something is wrong
    if message.content.startswith('c!devhelp'):
        message_author_name = str(message.author)
        message_author_comment = message.content.lstrip('c!devhelp')

        help_msg = 'Hi! ' + message_author_name + ' has issued a comment on my performance, seen below:\n\n'
        help_msg = help_msg + '\t\t`' + message_author_comment + '`\n\n'
        help_msg = help_msg + 'Thank you! Please message them asap.'

        dev_user = discord.utils.get(client.get_all_members(),id=DEV_ID)

        await client.send_message(dev_user, help_msg)

        await client.send_message(message.channel, "Your comment has been logged, thank you!")

@client.event # decorator, triggered on ready, creates logs so that the bot admin can review if anything goes wrong
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

client.run(TOKEN)