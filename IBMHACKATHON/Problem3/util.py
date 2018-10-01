import ibm_db
import tweepy, datetime, time
import math
from watson_developer_cloud import ToneAnalyzerV3
from watson_developer_cloud.tone_analyzer_v3 import ToneInput
import json



class access_data:	    # Connection of database to the application.
	dsn=(
		"DRIVER={{IBM DB2 ODBC DRIVER}};"
		"DATABASE=BLUDB;"
		"HOSTNAME=dashdb-txn-sbox-yp-lon02-01.services.eu-gb.bluemix.net;"  
		"PORT=50000;"
		"PROTOCOL=TCPIP;"
		"UID=xxxx;"
		"PWD=xxxx;")
		
	conn = ibm_db.connect(dsn, "", "")
	


	
all_tweet=[]
minutes=[]
class access_tweets:   # Access of tweets
	CONSUMER_KEY = 'xxxxxxxxxxxxxxxx'
	CONSUMER_SECRET = 'xxxxxxxxxxxxxxxx'
	OAUTH_TOKEN = 'xxxxxxxxxxxxxxxx'
	OAUTH_TOKEN_SECRET = 'xxxxxxxxxxxxxxxx'

	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
	api = tweepy.API(auth)	

	def get_tweets(api, username):    # This code access all the user's tweet which was posted in last 24 hrs.
		del all_tweet[:]
		del minutes[:]
		count = 500
		tweets = api.user_timeline(username, count=count)
		for tweet in tweets:
			if (datetime.datetime.now() - datetime.timedelta(hours=5, minutes=30) - tweet.created_at).days < 1 :
				all_tweet.append(tweet.text)
				t=(datetime.datetime.now() - datetime.timedelta(hours=5, minutes=30) - tweet.created_at).seconds//3600
				
				if t<1:
					minute="(" + str(math.floor(((datetime.datetime.now() - datetime.timedelta(hours=5, minutes=30) - tweet.created_at).seconds)//60)) + " min ago) "
					minutes.append(minute)
				else:
					minute="(" + str(math.floor(t)) + " hr ago) "
					minutes.append(minute)				

		return (all_tweet, minutes)

class tone_analyser:     # Analyses user's mood depending on the tweets.
	def analyser(tweet):
		service = ToneAnalyzerV3(
			url='https://gateway.watsonplat',
    		username='xxxxxxxxxxxxxxxx',
    		password='xxxxxxxxxxxxxxxx',
    		version='2017-09-21')

		data=json.dumps(service.tone({'text': tweet}, 'application/json').get_result(),indent=2)
		_dict = json.loads(data)
		info=""

		try:
			score=_dict["document_tone"]["tones"][0]["score"]
			info=_dict["document_tone"]["tones"][0]["tone_name"]
			return info
		except:
			return "invalid"


class get_songs:				# songs suggestions based on emotions.
	def song(emotion):
		
		if emotion=="Sadness":
			songs=[
				"https://www.youtube.com/embed/ez2vSHtdc9E?rel=0&amp;controls=0&amp;showinfo=0",
				"https://www.youtube.com/embed/W0HfHVKLI50?rel=0&amp;controls=0&amp;showinfo=0",
				"https://www.youtube.com/embed/7nNcKVv7Hzk?rel=0&amp;controls=0&amp;showinfo=0",
				"https://www.youtube.com/embed/C8lMW0MODFs?rel=0&amp;controls=0&amp;showinfo=0",
				"https://www.youtube.com/embed/n1gs_zh8zuM?rel=0&amp;controls=0&amp;showinfo=0"
			]
		elif emotion=="Joy":
			songs=[
				"https://www.youtube.com/embed/2vMH8lITTCE?rel=0&amp;controls=0&amp;showinfo=0",
				"https://www.youtube.com/embed/rga784YnL3M?rel=0&amp;controls=0&amp;showinfo=0;start=50",
				"https://www.youtube.com/embed/PqFMFVcCZgI?rel=0&amp;controls=0&amp;showinfo=0",
				"https://www.youtube.com/embed/oDZK9Vwoehk?rel=0&amp;controls=0&amp;showinfo=0",
				"https://www.youtube.com/embed/ALZHF5UqnU4?rel=0&amp;controls=0&amp;showinfo=0"
				
			]
		elif emotion=="Fear":
			songs=[
				"https://www.youtube.com/embed/WeUUwr5_mG4?rel=0&amp;controls=0&amp;showinfo=0",
				"https://www.youtube.com/embed/W0UGEDbjBDs?rel=0&amp;controls=0&amp;showinfo=0",
				"https://www.youtube.com/embed/IN6bEJDu-cM?rel=0&amp;controls=0&amp;showinfo=0",
				"https://www.youtube.com/embed/XHeLr1kHNB8?rel=0&amp;controls=0&amp;showinfo=0",
				"https://www.youtube.com/embed/acIpsyTW6SI?rel=0&amp;controls=0&amp;showinfo=0"
							]
		elif emotion=="Anger":
			songs=[
				"https://www.youtube.com/embed/wDOQMKGYJQo?rel=0&amp;controls=0&amp;showinfo=0",
				"https://www.youtube.com/embed/3vgDb4TQneA?rel=0&amp;controls=0&amp;showinfo=0",
				"https://www.youtube.com/embed/QAsJvKsd2Xk?rel=0&amp;controls=0&amp;showinfo=0",
				"https://www.youtube.com/embed/T235jK9xR8Q?rel=0&amp;controls=0&amp;showinfo=0"	,
				"https://www.youtube.com/embed/wMEOT0yaasQ?rel=0&amp;controls=0&amp;showinfo=0"
			]
		else:
			songs=[]

		return songs