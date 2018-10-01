from django.shortcuts import render
from .util import access_tweets, get_songs, tone_analyser


def  index(request):
	song=get_songs                    # object to access songs
	actual_name = access_tweets		  # object to access tweets
	analyser=tone_analyser			  # object to get emotions
	tweets=" "

	if request.method == "POST":
		try:
			screen_name=request.POST.get("name", request)
			all_tweet, minutes = actual_name.get_tweets(actual_name.api, screen_name)
			for i in all_tweet:
				tweets = tweets +str(i) + ". "
			user = actual_name.api.get_user(screen_name = screen_name)
			name = user.name
			emotion=analyser.analyser(tweets)
			songs=song.song(emotion)
		except :
			return render(request, 'Problem3/404.html',{ 'wrong': screen_name })

		zippedlist=zip(minutes,all_tweet)

		context = {
			'username': name ,
			'result':all_tweet,
			'minutes': minutes,
			'zipped': zippedlist,
			'emotion': emotion,
			'songs': songs

		}
		return render(request, 'Problem3/index2.html', context)


	return render(request, 'Problem3/index.html')
