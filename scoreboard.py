import requests
import json


class scoreboard:
	# host is the server it connects to
	global scoreboard_host
	scoreboard_host = "http://localhost/scoreboard/api/"
	
	def getTop3(id):
		r = requests.get(scoreboard_host + 'getTop3?id=' +  id)
		return json.loads(r.text)
	
	def getTop5(id):
		r = requests.get(scoreboard_host + 'getTop5?id=' +  id)
		return json.loads(r.text)
		
	def getTop10(id):
		r = requests.get(scoreboard_host + 'getTop10?id=' +  id)
		return json.loads(r.text)
		
	def submitScore(id, name, score):
		requests.get(scoreboard_host + 'submitScore?id=' + id + "&name=" + name + "&score=" + score)
		return