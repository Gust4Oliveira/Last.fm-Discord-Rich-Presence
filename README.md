# Last.fm Discord Rich Presence
### Description
Script that catch your listening status from Last.fm and shares as your discord game activity (Discord Rich Presence)

**Preview:**

![N|Solid](https://cdn.discordapp.com/attachments/673112689207279637/705858416207200319/unknown.png)

## Dependencies
- Pypresence
- Pylast

## Setup

### Windows 
- Download the latest [release](https://github.com/Gust4Oliveira/Last.fm-Discord-Rich-Presence/releases/tag/1.0).
- Create a text file named as "username.txt" in the same folder of the .exe executable.
- Open the username.txt file and just insert your last.fm username inside of it, like below:

`Gust4Oliveira`
- Run the .exe file.

### Windows, MacOS or Linux (Using Python)
- Download and install python (During the instalation, check the option to add python to the PATH(Windows).
- Download the [source code](https://github.com/Gust4Oliveira/Last.fm-Discord-Rich-Presence/archive/master.zip).
- Create a text file named as "username.txt" in the same folder of the .py files.
- Open the username.txt file and just insert your last.fm username inside of it, like below:

`username`
- open the terminal or cmd/powershell and install all dependencies, by typing the following command:

`pip install -r requirements.txt`
- Run the .py file at the same terminal using:

`python main.py`

## Knew issues and (maybe) further upgrades
- At the moment, sometimes the song remaining time is stuck at 00:00, that happens when the Last.fm doesn't have the information of the song duration. (thinking now, i could remove the remaining time when that happens, but i will do this later pepeLaugh)
- Running at the background and a GUI would be very welcome but i really don't know how to do it properly, maybe in furthers versions if worth the work and the time spent.
- About the music album art at the discord status, well, i cound't find a way to show a picture there without using discord assets, and all aplications have a limitation to 150 assets.
