# Welcome to the Cat Fact bot for Discord

## Made by Dallas Taylor (de-taylor)

### Built on Discord.py for delivering on demand cat facts in Discord

### v0.6.0 - Released 7/15/2018

## What it does

- This bot does one thing, but it does it well: It fetches cat facts from the catfact.ninja API, using the /fact endpoint
- It also supplies cat pictures and gifs, user's choice!

## Who the bot is for

- Anyone who wants cat facts.
- And cat photos/gifs.

## How to use it

- To add this bot to your discord server, go to `https://discordapp.com/api/oauth2/authorize?client_id=463692732540518422&scope=bot` and add it to whichever server you want!

### Commands

- `c!help` or `c!helpplz` - call for help!
- `c!factplz <option>` - get a random fact! {options below}
  - `jpg` - deliver an image along with your cat!
  - `gif` - deliver a GIF along with your fact!
- `c!devhelp` - DM's the dev (you set the user ID in cat_bot_core.py in the constant `DEV_ID`). Also stores the time, server/channel origin of request, and user comment in a LOG file. User IDs and names are never stored, as per Discord's privacy policy.
