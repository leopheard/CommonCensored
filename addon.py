from xbmcswift2 import Plugin, xbmcgui
from resources.lib import commoncensored

plugin = Plugin()
URL = "http://commoncensored.libsyn.com/rss"

@plugin.route('/')
def main_menu():
    items = [
        {
            'label': plugin.get_string(30001), 
            'path': plugin.url_for('all_episodes'),
            'thumbnail': "https://github.com/leopheard/commoncensored/blob/master/resources/media/icon.jpg?raw=true"},
        {
            'label': plugin.get_string(30000), 
            'path': plugin.url_for('all_episodes1'),
            'thumbnail': "https://github.com/leopheard/commoncensored/blob/master/resources/media/icon.jpg?raw=true"},
    ]
    return items


@plugin.route('/all_episodes/')
def all_episodes():
    soup = commoncensored.get_soup(URL)
    playable_podcast = commoncensored.get_playable_podcast(soup)
    items = commoncensored.compile_playable_podcast(playable_podcast)
    return items

@plugin.route('/all_episodes1/')
def all_episodes1():
    soup = commoncensored.get_soup(URL)
    playable_podcast1 = commoncensored.get_playable_podcast1(soup)
    items = commoncensored.compile_playable_podcast1(playable_podcast1)
    return items
if __name__ == '__main__':
    plugin.run()
