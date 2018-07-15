import discord # discord.py
import requests # to pull information with APIs

# Utility functions for bot
def cat_fact_grabber():
    # API for grabbing a fantastic fact about our favorite felines
    cat_fact_resp = requests.get('https://catfact.ninja/fact')

    resp_data = cat_fact_resp.json() # represents the server response as a JSON object

    return resp_data["fact"], cat_fact_resp.status_code # pulls the string key from the value "fact"

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

    return filename, cat_jpg_resp.status_code

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

    return filename, cat_gif_resp.status_code