# Welcome to the Cat Fact bot for Discord

## Made by Dallas Taylor (de-taylor) || 2018 - MIT License

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

## Licensing Information

Copyright 2018 Dallas Taylor (de-taylor)

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.