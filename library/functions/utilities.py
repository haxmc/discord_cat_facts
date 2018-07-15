import library.functions.fetch as fetch

def help_command(timestamp):
    eventlog = open('library/bin/logfiles/bot_logfile.log', 'a') # open status log file for writing
    # long, complicated help message, modify if you add more commands
    msg = 'Hello! Here\'s all the commands you can use with me.\n\n'
    msg = msg + '1] `c!help` or `c!helpplz`: Gives you this menu!\n\n'
    msg = msg + '2] `c!factplz <code>`: Fetches a cat fact along with some form of digital media:\n'
    msg = msg + '\t\t `jpg`: gives a .jpg image of a kitty. {This is the default with no selection code}\n'
    msg = msg + '\t\t `gif`: gives a .gif of a kitty\n\n'
    msg = msg + '3] `c!devhelp <your comment>`: gets the attention of the dev who moderates me! I\'ll send them your username and comment, and they\'ll DM you when they can! *Don\'t worry, I never store user information without permission!*\n'

    logentry = str(timestamp) + ' :: User asked for help, received all commands for cat bot.\n'

    eventlog.write(logentry)

    print(logentry)

    eventlog.close()

    return msg

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

    logentry = str(timestamp) + ' :: Call: Fact and GIF fetch. Fact API call status: ' + str(fact_status) + '; GIF API call status: ' + str(gif_status)+ '\n'

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