# Last.fm Discord Rich Presence
### Description
Script that catch your listening status from Last.fm and shares as your discord game activity (Discord Rich Presence)

**Preview:**

![N|Solid](https://cdn.discordapp.com/attachments/673112689207279637/705858416207200319/unknown.png)

## Dependencies
- Pypresence
- Pylast
- Pystray

## Setup

### Windows

> Virus Warning Disclaimer
>
>Recently a issue was opened to notify me that the app is been detected by Windows Defender and others 4 antivirus softwares as a virus ([#2](https://github.com/Gust4Oliveira/Last.fm-Discord-Rich-Presence/issues/2)). I sended to microsoft a false positive report, but to the app be removed from defender it will take some time. For now i recomend runing the app from the source code using python to reduce anoying notifications of virus detection or in last case allowing the app to run even beeing detected as a virus if you don't like or isn't familiar to running it from python.
>
>Just reminding that this app isnt made to infect, steal data or collect usage informations from your computer. This problem happens because the app isnt signed with a certificate, so because isn't from a trusted source it is flaged as a virus. I find out that this issue and is pretty common from .exe aplications builded from python files using pyinstaller.

- Download the latest [release](https://github.com/Gust4Oliveira/Last.fm-Discord-Rich-Presence/releases/tag/1.1).
- Extract the zip file.
- Open the text file named as "username.txt" and edit to your last.fm username.
- Run the .exe file.

If you want that the app open it self when you log on your device follow the extra steps:

- Press Win + R.
- Type "shell:startup" and press enter.
- Right Click inside the folder, click on new and create a shortcut.
- Search for the .exe file that came inside the zip.

And you are good to go, try exiting your user on windows an logging in again to check if it worked, there is also others options such as Windows Task Scheduler.

### Windows, MacOS or Linux (Using Python)
- Download and install python (During the instalation, check the option to add python to the PATH(Windows).
- Download the [source code](https://github.com/Gust4Oliveira/Last.fm-Discord-Rich-Presence/archive/master.zip).
- Create a text file named as "username.txt" in the same folder of the .py files.
- Open the username.txt file and just insert your last.fm username inside of it, like below:

`username`
- open the terminal or cmd/powershell and install all dependencies, by typing the following command:

`pip install -r requirements.txt`
- Open the folder that the source code is located
- Run the .py file at the same terminal using:

`python main.py`

## Knew issues and (maybe) further upgrades
- At the moment, sometimes the song remaining time is stuck at 00:00, that happens when the Last.fm doesn't have the information of the song duration. I'll fix that on the next release.
- a GUI and a Installer that sets it self at the startup app would be very welcome but i really don't know how to do it properly, maybe in furthers versions if worth the work and the time spent.
- About the music album art at the discord status, well, i cound't find a way to show a picture there without using discord assets, and all aplications have a limitation to 150 assets.
