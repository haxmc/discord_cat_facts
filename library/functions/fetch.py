import discord # discord.py
import requests # to pull information with APIs

# Utility functions for bot
def cat_fact_grabber():
    # API for grabbing a fantastic fact about our favorite felines
    cat_fact_resp = requests.get('https://catfact.ninja/fact')

    resp_data = cat_fact_resp.json() # represents the server response as a JSON object

    return resp_data["fact"], cat_fact_resp.status_code # pulls the string key from the value "fact"

def r_cat_breed_grabber():
    # API for grabbing an array of information about a particular cat breed

    cat_breed_resp = requests.get('https://catfact.ninja/breeds')
    
    resp_data = cat_breed_resp.json()

    breed_info = []

    while int(resp_data["current_page"]) <= int(resp_data["last_page"]):
        num = 0
        while num < len(resp_data["data"]):
            breed_info.append(resp_data["data"][num])
            num += 1

        if resp_data["next_page_url"] == None:
            break
        else:
            cat_breed_resp = requests.get(resp_data["next_page_url"])
            resp_data = cat_breed_resp.json()

    return breed_info, cat_breed_resp.status_code # returns a dictionary with the breed information, and the status code

def a_cat_breed_grabber():
    cat_breed_resp = requests.get('https://catfact.ninja/breeds')

    resp_data = cat_breed_resp.json() 

    breed_list = []

    while int(resp_data["current_page"]) <= int(resp_data["last_page"]):
        num = 0
        while num < len(resp_data["data"]):
            breed_list.append(resp_data["data"][num]["breed"])
            num += 1

        if resp_data["next_page_url"] == None:
            break
        else:
            cat_breed_resp = requests.get(resp_data["next_page_url"])
            resp_data = cat_breed_resp.json()

    return breed_list, cat_breed_resp.status_code # returns a list of all breed names, and the status code

def s_cat_breed_grabber():
    cat_breed_resp = requests.get('https://catfact.ninja/breeds')

    resp_data = cat_breed_resp.json() 

    breed_list = []
    breed_info = []

    while int(resp_data["current_page"]) <= int(resp_data["last_page"]):
        num = 0
        while num < len(resp_data["data"]):
            breed_list.append(resp_data["data"][num]["breed"])
            breed_info.append(resp_data["data"][num])
            num += 1

        if resp_data["next_page_url"] == None:
            break
        else:
            cat_breed_resp = requests.get(resp_data["next_page_url"])
            resp_data = cat_breed_resp.json()

    return breed_list, breed_info, cat_breed_resp.status_code # returns a list of all breed names, and the status code

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