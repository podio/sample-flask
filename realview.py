from flask import Flask, render_template
import pypodio
import os
import settings

app = Flask(__name__)

podio = pypodio.Podio(client_id = settings.client_id, client_secret = settings.client_secret)
podio.request_oauth_token(settings.username, settings.password)

app_id = settings.app_id #Change this to the AppID of your "Active Listings" app for a demo

root = os.path.dirname(os.path.realpath(__file__))
photo_path = os.path.join(root, 'static/')

def save_photo(photo):
	mimetype = photo['mimetype'].split('/')[1]
	path = photo_path+str(photo['file_id'])+"."+mimetype
	if not os.path.isfile(path):
		p = podio.files_get_file(photo['file_id'], return_url = False)
		try:	
				tmp = open(path, 'wb')
				tmp.write(p)
				tmp.close()
		except Exception:
			raise Exception
	return str(photo['file_id'])+"."+mimetype

class Agent(object):
	def __init__(self, data):
		self.name = data['name']
		self.id = data['profile_id']
		#self.avatar = save_photo(data['avatar'])
		self.email = data['mail'][0]
	def __str__(self):
		return self.name+":"+self.email

class Home(object):
	def __init__(self, data):
		self.price = data['asking price']
		self.photo = save_photo(data['photo'])
		self.address = data['address']
		self.agent = Agent(data['listing agent'])
	def __str__(self):
		return self.address

def fetch_results():
	items = podio.app_get_items(48294)['items']
	res = []
	for item in items:
		itm = {}
		for value in item['fields']:
			#print value['label'],
			if 'value' in value['values'][0]:
				#print value['values'][0]['value']
				itm[value['label'].lower()] = value['values'][0]['value']
		res.append(Home(itm))
	return res


@app.route('/')
def displayHouses():
	houses = fetch_results()
	#for house in houses:
		#print house.photo
	return render_template('index.ji2', homes=houses)
	

if __name__ == "__main__":
    app.run(debug=True)


