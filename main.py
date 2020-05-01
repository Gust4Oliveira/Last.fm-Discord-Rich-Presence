import sys
from Last_fm_api import LastFmUser

f = open('username.txt','r')

username = f.read()
User = LastFmUser(username, 2)
while True:
    User.now_playing()
