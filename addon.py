from xbmcswift2 import Plugin, xbmcgui

plugin = Plugin()

@plugin.route('/')
def main_menu():
    items = [
        {'label': plugin.get_string(30000), 'path': "http://stream9.addictradio.net/addictalternative", 'is_playable': True},
        {'label': plugin.get_string(30001), 'path': "http://stream9.addictradio.net/addictlounge", 'is_playable': True},
        {'label': plugin.get_string(30002), 'path': "http://stream9.addictradio.net/addictrock", 'is_playable': True},
        {'label': plugin.get_string(30003), 'path': "http://stream9.addictradio.net/addictstar", 'is_playable': True},
        {'label': plugin.get_string(30004), 'path': "http://stream9.addictradio.net/addictldg", 'is_playable': True},
    ]

    return items

if __name__ == '__main__':
    plugin.run()
