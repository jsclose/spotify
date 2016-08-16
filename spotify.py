import json
import urllib2
import networkx as nx
import matplotlib.pyplot as plt
from networkx.readwrite import json_graph

oAuth = "BQDfGwv0sOj-ZRwCm-k0B_koovPEEmnalSsZguvDjPNhgEgp6pywuRl8R9MJ5U2bKAKsyn_HDqZtD4MDyintcs7hLI6sn_Gu_3WScGDChHqfk5ov0JBDVU6sz6Th_r0d2bmxlHb-k9B3qmY"
url = "https://api.spotify.com/v1/artists/0JDkhL4rjiPNEp92jAgJnS/related-artists"


class Artist:	
	def __init__(self, id):
		self.id = id
		self.name = ''
		self.followers = ''
		self.popularity = ''
		self.seen = bool
		self.related_artists = [ ]
		self.get_artist()
		self.get_related_artist()
	
	def get_artist(self):
			getArtist =  "https://api.spotify.com/v1/artists/" + self.id + "/"
			obj = urllib2.urlopen(getArtist)
			artistInfo = json.load(obj)
			self.name = artistInfo['name']
			self.followers = artistInfo['followers']['total']
			self.popularity = artistInfo['popularity']

	def get_related_artist(self):
		url = "https://api.spotify.com/v1/artists/" + self.id + "/related-artists"
		json_obj = urllib2.urlopen(url)
		data = json.load(json_obj)
		for item in data['artists']:
			self.related_artists.append(str(item['id']))


def createGraph(artist, graph):
	    for relatedID in artist.related_artists:
	#create a new artist
	     related_artist = Artist(relatedID)
	     Z.add_node(related_artist.name, popularity = related_artist.popularity, followers = related_artist.followers)
	     Z.add_edge(artist.name, related_artist.name)


ArtistArray = []


#coldplay
coldplay = Artist('4gzpq5DPGxSnKTe4SA8HAU')


#band of horses
BoH = Artist('0OdUWJ0sBjDrqHygGUXeCF')


#neildDiamond

nD = Artist('7mEIug7XUlQHikrFxjTWes')



#bon Iver
bI = Artist('4LEiUm1SRbFMgfqnQTwUbQ')



#kanyeWest
kanye = Artist('5K4W6rqBFWDnAN6FQUkS6x')

Z = nx.Graph()
#go through all of the iDs of the related artistlist

ArtistArray.append(kanye)
createGraph(kanye, Z)

for iD in kanye.related_artists:
	test = Artist(iD)
	ArtistArray.append(test)
	createGraph(test, Z)

'''

for artist in ArtistArray:
	for iD in artist.related_artists:
		newArtist = Artist(iD)
		ArtistArray.append(newArtist)
		createGraph(newArtist, Z, 'red')
'''


#nx.draw(Z, with_labels = True)
#nx.draw(Z, with_labels = True)
#plt.show()



data = json_graph.node_link_data(Z)
with open('kanye.json', 'w') as outfile:
   json.dump(data, outfile, indent=4)





