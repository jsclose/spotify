'''
{
    "artist": "The Quintet",
    "title": "Jazz at Massey Hall",
    "itunes": "https://itunes.apple.com/us/album/quintet-jazz-at-massey-hall/id152035858",
    "cover": "http://a5.mzstatic.com/us/r30/Features/e7/f0/51/dj.suakypmw.170x170-75.jpg",
    "color": "#B03239",
    "text": "#191A18",
    "musicians": [
      "Dizzy Gillespie",
      "Charles Mingus",
      "Charlie Parker",
      "Bud Powell",
      "Max Roach"
    ]
  }
 '''

import json
import urllib2
import networkx as nx
import matplotlib.pyplot as plt
from networkx.readwrite import json_graph
import jsonpickle

oAuth = "BQDfGwv0sOj-ZRwCm-k0B_koovPEEmnalSsZguvDjPNhgEgp6pywuRl8R9MJ5U2bKAKsyn_HDqZtD4MDyintcs7hLI6sn_Gu_3WScGDChHqfk5ov0JBDVU6sz6Th_r0d2bmxlHb-k9B3qmY"
url = "https://api.spotify.com/v1/artists/0JDkhL4rjiPNEp92jAgJnS/related-artists"


class Artist:	
	def __init__(self, id):
		self.id = id
		self.artist = ''
		self.title = ''
		self.cover = ''
		self.followers = ''
		self.musicians = [ ]
	
	def get_artist(self, id):
			getArtist =  "https://api.spotify.com/v1/artists/" + id + "/"
			obj = urllib2.urlopen(getArtist)
			artistInfo = json.load(obj)
			self.artist = artistInfo['name']
			self.followers = artistInfo['followers']['total']

	def get_related_artist(self, id):
		url = "https://api.spotify.com/v1/artists/" + id + "/related-artists"
		json_obj = urllib2.urlopen(url)
		data = json.load(json_obj)
		for item in data['artists']:
			self.musicians.append(str(item['name']))

	def get_album(self, id):
		getAlbum = "https://api.spotify.com/v1/artists/"+ id + "/albums"
		#"https://api.spotify.com/v1/albums/" + id + "/"
		obj = urllib2.urlopen(getAlbum)
		artistInfo = json.load(obj)
		self.title = artistInfo['items'][0]['name']
		self.cover = artistInfo['items'][0]['images'][0]['url']
		print artistInfo['items'][0]['images'][0]['url']



kanye = Artist('5K4W6rqBFWDnAN6FQUkS6x')
kanye.get_artist(kanye.id)
kanye.get_related_artist(kanye.id)
kanye.get_album(kanye.id)


frozen = jsonpickle.encode(kanye)
print frozen





