from flask import Flask, render_template, url_for, request
from spotify import nameToId, generateData


app = Flask(__name__)

@app.route('/')
def home():
	return render_template('spotifyindex.html')
	#return make_respone(open('templates/spotifyindex.html').read())


@app.route('/', methods=['POST'])
def my_form_post():

    text = request.form['text']
    artistId = nameToId(text)
    print(artistId)
    return generateData(artistId)
    #return render_template('spotifyindex.html') 
    

if __name__ == '__main__':
	app.run(host='127.0.0.1', port =5000)
	url_for('static', filename='kanye.json')

