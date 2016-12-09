import json
import urllib2
import networkx as nx
import matplotlib.pyplot as plt
from networkx.readwrite import json_graph

oAuth = "BQAuxE9cRk63sb4e9sOKG1YHFo8aqebEjDTH_XHNy3g1Fb"
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
	     graph.add_node(related_artist.name, popularity = related_artist.popularity, followers = related_artist.followers)
	     graph.add_edge(artist.name, related_artist.name)
	     


	return graph


def nameToId(name):
	name = name.replace(" ", "+")
	getID = "https://api.spotify.com/v1/search?q=" + name + "&type=artist "
	#print(getID)
	obj = urllib2.urlopen(getID)
	artistInfo = json.load(obj)
	artistInfo['artists']['items'][0]['id']
	artistID= artistInfo['artists']['items'][0]['id']
	return artistID





def generateData(artistID):
	#artistID = nameToId(name)
	Z = nx.Graph()
	searchArtist = Artist(artistID)
	Z = createGraph(searchArtist, Z)
	'''
	ArtistArray.append(searchArtist)

	for iD in searchArtist.related_artists:
		test = Artist(iD)
		#print(test.name)
		ArtistArray.append(test)
		Z = createGraph(test, Z)


	
	for artist in ArtistArray:
		for iD in artist.related_artists:
			newArtist = Artist(iD)
			print(newArtist.name)
			ArtistArray.append(newArtist)
			Z = createGraph(newArtist, Z, 'red')
	'''


	data = json_graph.node_link_data(Z)
	return data
	'''
	with open('static/artist.json', 'w') as outfile:
		json.dump(data, outfile, indent=4)
	'''


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


artistID = nameToId("kanye west")
#print(artistID)
generateData(artistID)

ArtistArray.append(kanye)
createGraph(kanye, Z)
'''
for iD in kanye.related_artists:
	test = Artist(iD)
	ArtistArray.append(test)
	createGraph(test, Z)



for artist in ArtistArray:
	for iD in artist.related_artists:
		newArtist = Artist(iD)
		ArtistArray.append(newArtist)
		createGraph(newArtist, Z, 'red')
'''


#nx.draw(Z, with_labels = True)
#nx.draw(Z, with_labels = True)
#plt.show()




#data = json_graph.node_link_data(Z)
#with open('kanye.json', 'w') as outfile:
 #  json.dump(data, outfile, indent=4)





