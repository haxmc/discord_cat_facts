# Welcome to the Cat Fact bot for Discord

## Made by Dallas Taylor (de-taylor)

### Built on Discord.py for delivering on demand cat facts in Discord

## Note: This bot was developed for learning purposes, and has been discontinued.

As of August 1, 2018, this bot and its features will be merged with a new bot (https://github.com/de-taylor/fact-of-the-day). All of its functionality will remain the same, but with an updated command structure and new additions for other categories of facts. Please be advised, if you have this bot on your server in its current capacity, that it will not be live again until August 1, 2018. Please keep in touch with the fact-of-the-day repository for further information.

## What it does

- This bot is focused on one thing: kitties. We on the dev team are obsessed. So, this bot does all of the following: 
  - It fetches cat facts from the `catfact.ninja/fact` API endpoint
    - It also supplies cat pictures and gifs along with your fact!
  - It also fetches breed information from the `catfact.nina/breeds` API endpoint.

## Who the bot is for

- Anyone who feels like their Discord server is woefully feline free.

## How to use it

- To add this bot to your discord server, go to `https://discordapp.com/api/oauth2/authorize?client_id=463692732540518422&scope=bot` and add it to whichever server you want!

### Commands

- `c!help` - call for help! I will send you a private message with all of my functionality.
- `c!breedplz <option>` - get information on a random cat breed!
  - `all` - option will list out all of the breeds currently recognized that you could get information on.
  - `{breed name}` - option will list information on the specific breed you listed, if a match is found.
- `c!factplz <option>` - get a random fact! {options below}
  - `jpg` - deliver an image along with your fact!
  - `gif` - deliver a GIF along with your fact!
- `c!devhelp` - DM's the dev (you set the user ID in cat_bot_core.py in the constant `DEV_ID`). Also stores the time, server/channel origin of request, and user comment in a LOG file. User IDs and names are never stored, as per Discord's privacy policy.
