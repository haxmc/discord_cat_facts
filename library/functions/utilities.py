import library.functions.fetch as fetch

import random

def help_command(timestamp, message):
    eventlog = open('library/bin/logfiles/bot_logfile.log', 'a') # open status log file for writing
    # long, complicated help message, modify if you add more commands

    if message.channel.is_private == True:
        message_server = 'any server I\'m in'
    else:
        message_server = message.server.name

    msg = 'Hello! Here\'s all the commands you can use with me on ' + message_server + '.\n\n'
    msg = msg + '1] `c!help`: Gives you this menu!\n'
    msg = msg + '2] `c!breedplz`: Fetches information about a random cat breed!\n'
    msg = msg + '\t\t `all` - option will list out all of the breeds currently recognized that you could get information on.\n'
    msg = msg + '\t\t `{breed name}` - option will list information on the specific breed you listed, unless no match is found.\n'
    msg = msg + '3] `c!factplz <code>`: Fetches a cat fact along with some form of digital media:\n'
    msg = msg + '\t\t `jpg`: gives a .jpg image of a kitty. {This is the default with no selection code}\n'
    msg = msg + '\t\t `gif`: gives a .gif of a kitty\n'
    msg = msg + '4] `c!devhelp <your comment>`: Gets the attention of the dev who moderates me! I\'ll send them your username and comment, and they\'ll DM you when they can! *Don\'t worry, I never store user information without permission!*\n'

    logentry = str(timestamp) + ' :: User asked for help, received all commands for cat bot.\n'

    eventlog.write(logentry)

    print(logentry)

    eventlog.close()

    return msg

def r_breed_info_fetch(timestamp, message):
    eventlog = open('library/bin/logfiles/bot_logfile.log', 'a') # open status log file for writing
    breed_info, breed_status = fetch.r_cat_breed_grabber() # receive dictionary, integer

    breed_num = random.randint(0, len(breed_info))

    breed_msg = 'Here information about the **' + breed_info[breed_num]["breed"] + '**:\n'
    breed_msg = breed_msg + '\t\tCountry of Origin: **' + breed_info[breed_num]["country"] + '**\n'
    breed_msg = breed_msg + '\t\tOrigin Type: **' + breed_info[breed_num]["origin"] + '**\n'
    breed_msg = breed_msg + '\t\tCoat: **' + breed_info[breed_num]["coat"] + '**\n'
    breed_msg = breed_msg + '\t\tPattern: **' + breed_info[breed_num]["pattern"] + '**\n'

    end_msg = 'Isn\'t that fascinating? *meow*'

    logentry = str(timestamp) + ' :: Call: Breed info fetch. Breed API call status: ' + str(breed_status) + "\n"

    eventlog.write(logentry)
    print(logentry)

    eventlog.close()

    return breed_msg, end_msg

def a_breed_info_fetch(timestamp, message):
    eventlog = open('library/bin/logfiles/bot_logfile.log', 'a') # open status log file for writing

    breed_list, breed_status = fetch.a_cat_breed_grabber()

    breed_msg = "Full list of breeds:\n"
    for breed in breed_list:
        breed_msg = breed_msg + '\t\t' + breed + '\n'
    
    end_msg = 'Isn\'t that fascinating? *meow*'

    logentry = str(timestamp) + ' :: Call: Breed info fetch (all). Breed API call status: ' + str(breed_status) + "\n"

    eventlog.write(logentry)
    print(logentry)

    eventlog.close()

    return breed_msg, end_msg

def s_breed_info_fetch(timestamp, message, name_param):
    eventlog = open('library/bin/logfiles/bot_logfile.log', 'a') # open status log file for writing

    breed_list, breed_info, breed_status = fetch.s_cat_breed_grabber()

    for breed_num, breed in enumerate(breed_list):
        if name_param == breed:
            breed_msg = 'Here information about the **' + breed_info[breed_num]["breed"] + '**:\n'
            breed_msg = breed_msg + '\t\tCountry of Origin: **' + breed_info[breed_num]["country"] + '**\n'
            breed_msg = breed_msg + '\t\tOrigin Type: **' + breed_info[breed_num]["origin"] + '**\n'
            breed_msg = breed_msg + '\t\tCoat: **' + breed_info[breed_num]["coat"] + '**\n'
            breed_msg = breed_msg + '\t\tPattern: **' + breed_info[breed_num]["pattern"] + '**\n'

            end_msg = 'Isn\'t that fascinating? *meow*'

            break
        elif name_param != breed:
            breed_msg = 'Oops! I couldn\'t find that breed for you.'
            end_msg = 'Check the list of all breeds with the command `c!breedplz all`'

    logentry = str(timestamp) + ' :: Call: Breed info fetch (all). Breed API call status: ' + str(breed_status) + "\n"

    eventlog.write(logentry)
    print(logentry)

    eventlog.close()

    return breed_msg, end_msg


def fact_jpg_fetch(timestamp, message):
    eventlog = open('library/bin/logfiles/bot_logfile.log', 'a') # open status log file for writing
    msg, fact_status = fetch.cat_fact_grabber()
    msg = 'Fact: ' + msg.format(message)
    cat_jpg, jpg_status = fetch.cat_jpg_grabber()
    end_msg = 'Stay tuned for the next fact! *meow*'

    logentry = str(timestamp) + ' :: Call: Fact and JPEG fetch. Fact API call status: ' + str(fact_status) + '; Image API call status: ' + str(jpg_status) + '\n'

    eventlog.write(logentry)
    print(logentry)

    eventlog.close()

    return msg, cat_jpg, end_msg

def fact_gif_fetch(timestamp, message):
    eventlog = open('library/bin/logfiles/bot_logfile.log', 'a') # open status log file for writing
    msg, fact_status = fetch.cat_fact_grabber()
    msg = 'Fact: ' + msg.format(message)
    cat_gif, gif_status = fetch.cat_gif_grabber()
    end_msg = 'Stay tuned for the next fact! *meow*'

    logentry = str(timestamp) + ' :: Call: Fact and GIF fetch. Fact API call status: ' + str(fact_status) + '; GIF API call status: ' + str(gif_status) + '\n'

    eventlog.write(logentry)
    print(logentry)

    eventlog.close()

    return msg, cat_gif, end_msg

def contact_dev(timestamp, message):
    eventlog = open('library/bin/logfiles/bot_logfile.log', 'a') # open status log file for writing
    commentlog = open('library/bin/logfiles/bot_comments.log', 'a') # open comment log file for writing

    if message.channel.is_private == True:
        message_channel = 'Direct Message'
        message_server = 'Direct Message'
    else:
        message_channel = message.channel.name 
        message_server = message.server.name
    
    message_author_name = str(message.author)
    message_author_comment = message.content.lstrip('c!devhelp')

    help_msg = 'Hi! ' + message_author_name + ' has a comment on my performance, seen below:\n\n'
    help_msg = help_msg + '\t\t`' + message_author_comment + '`\n\n'
    help_msg = help_msg + 'Thank you! Please message them asap.'

    logentry = str(timestamp) + ' :: Comment logged from user on '+ message_server + ':' + message_channel + ', please check bot_comment logs' + '\n'

    eventlog.write(logentry) # make entry in log

    comment_logentry = str(timestamp) + ' :: Comment logged from user on '+ message_server + ':' + message_channel + ' :: Comment: ' + message_author_comment + '\n'

    commentlog.write(comment_logentry) # make entry in log
    print(comment_logentry)

    commentlog.close()
    eventlog.close()

    return help_msg