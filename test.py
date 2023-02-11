from configparser import ConfigParser

config = ConfigParser()
config.read('settings.ini')
print(config['last.fm']['user'])
