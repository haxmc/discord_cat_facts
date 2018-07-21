# Changelog for Cat Facts Bot for Discord (newest on top)

## Version 0.6.6 - Minor Feature Update - 7/21/2018

### 0.6.6 Tweaks

- Added functionality to `c!breedplz` command
    - User has ability to view all cat breeds using the `all` parameter
    - User has the ability to view a specific cat breed by specifying the breed name as a parameter to the command.

## Version 0.6.5 - New Feature Release - 7/20/2018

### New Features

- Use the `c!breedplz` command to get information about a random cat breed.

### 0.6.5 Tweaks

- Recognized an issue with the bot timing out after 12 hours of inactivity. Fixed with code to keep WebSocket connection alive by sending a heartbeat every so often.
- merged the functionality of the `c!faq` feature (Issue #3) into the `c!help` command with resolution of Issue #8.
- removed `c!helpplz` command, due to redundancy

## Version 0.6.0 - First major update to Alpha version - 7/15/2018

### 0.6.0 Tweaks

- Improved user comment logging, expands on original logging interface by storing user comments in a log file for the bot dev to look over, as well as sending a DM to the dev with each comment.
- Improved bot status logging, creates more entries for more events, included calls to the bot (what the call, and the status code), comments logged, etc.
- Updated bot file structure to accomodate more complex bot operations

## Version 0.5.0 - Initial Alpha Release of Cat Facts bot for Discord - 7/11/2018

### Original Features

- Able to use `c!help` or `c!helpplz` commands to access available functions of the Discord bot
- Able to use `c!factplz` command with parameters `jpg` or `gif` to access a random cat fact from the `http://catfact.ninja` API using the /fact endpoint, as well as fetch a image (`jpg`) or GIF (`gif`) from `http://thecatapi.com/api` API using the /image endpoint with several search parameters.
- Able to use `c!devhelp` to reach out to the developer/maintainer of the bot directly, logging the comment in a DM, reminding the developer to respond and take action on the comment.
