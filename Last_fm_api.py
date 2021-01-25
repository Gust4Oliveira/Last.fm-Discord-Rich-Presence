import pylast
import time
import DiscordRPC as RPC

API_KEY = "4a47d43987a47ead6689e15009d099b4"
API_SECRET = "4f79bc1115694a8b123f56c88aef6be4"

network = pylast.LastFMNetwork(api_key=API_KEY, api_secret=API_SECRET)


class LastFmUser:
    def __init__(self, username, cooldown):
        self.username = username
        self.user = network.get_user(username)
        self.cooldown = cooldown

    def now_playing(self):
        current_track = None
        try:
            current_track = self.user.get_now_playing()
            pass
        except pylast.WSError:
            print("Connection problem at web serice, retrying connection in " +
                  str(self.cooldown)+" seconds")
            pass
        except pylast.NetworkError:
            print("The app couldn't comunicate with last.fm servers, check your internet connection!")
            pass
        except pylast.MalformedResponseError:
            print("Last.fm internal server error!, retrying connection")
            pass

        if current_track is not None:
            track = current_track
            try:
                album = track.get_album()
                time_remaining = track.get_duration()
            except pylast.WSError:
                print("Connection problem at web serice, retrying connection in " +
                      str(self.cooldown)+" seconds")
                pass
            except pylast.NetworkError:
                print(
                    "The app couldn't comunicate with last.fm servers, check your internet connection!")
                pass
            RPC.enable_RPC()
            RPC.update_Status(str(track), str(album), time_remaining)
            time.sleep(self.cooldown+8)
        else:
            print("No song detected, checking again in " +
                  str(self.cooldown)+" seconds")
            RPC.disable_RPC()
        time.sleep(self.cooldown)
