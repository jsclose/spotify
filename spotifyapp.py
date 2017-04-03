from flask import *
from spotify import nameToId, generateData


app = Flask(__name__)

@app.route('/')
def home():

	return render_template('spotifyindex.html')
	#return make_respone(open('templates/spotifyindex.html').read())


@app.route('/api/v1/related_artist', methods=['POST', 'GET'])
def generate_related_artist_network():
    #text = request.form['text']
    print("getting")
    #name = "Jack Johnson"
    name = request.args.get('artist_name')
    print(name)
    if not name:
        name = "Jack Johnson"
    artistId = nameToId(name)
    print(artistId)
    #return generateData(artistId)
    return jsonify(generateData(artistId))
    
    

if __name__ == '__main__':
	app.run(host='0.0.0.0', port =3000)
	#url_for('static', filename='artist.json')

