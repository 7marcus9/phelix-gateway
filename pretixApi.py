from config import Config
import urllib.request
import json

def getAll():
	contents = urllib.request.urlopen("{}/download/?key={}".format(Config.serverUrl, Config.key))
	jsonObj = json.loads(contents.read().decode('UTF-8'))
	return jsonObj

def getInfo(voucher):
	return ""

def search(searchstr):
	return ""

def redeem(secret, datetime):
	return ""
