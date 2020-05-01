from pypresence import Presence
import datetime

client_id = '702984897496875072'
RPC = Presence(client_id)
already_enabled = False
already_disabled = True
start_time = None
LastTrack = None


def enable_RPC():
    global already_enabled,already_disabled
    if already_enabled == False:
        RPC.connect()
        print('Connected with Discord')
        already_enabled = True
        already_disabled = False


def update_Status(track, album, time_remaining):
    global start_time, LastTrack
    if LastTrack == track:
        pass
    else:
        print("Now Playing: " + track)
        start_time = datetime.datetime.now().timestamp()
        LastTrack = track
        trackList = track.split('-')
        time_remaining = str(time_remaining)[0:3]
        if album != 'None':
            RPC.update(details=trackList[1], state=album, end=float(time_remaining)+start_time,
                   large_image='icon', large_text='Last.fm Discord Rich Presence')
        else:
            RPC.update(details=trackList[1], state=trackList[0], end=float(time_remaining)+start_time,
                   large_image='icon', large_text='Last.fm Discord Rich Presence')


def disable_RPC():
    global already_enabled
    global already_disabled
    if already_disabled == False:
        RPC.clear()
        RPC.close()
        print('Disconnected from Discord due to inactivity')
        already_disabled = True
        already_enabled = False
