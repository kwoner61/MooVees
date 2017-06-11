import urllib2
import json

url = 'https://andruxnet-random-famous-quotes.p.mashape.com/?cat=movies&count=5'
api_key = 'LSQLygHwK3mshOgI9ON4phGrkJk4p13JPhnjsnVNiJq2zKdTIY'
headers = {'X-Mashape-Key': api_key, 'Accept': 'application/json'}

# Get and return 5 random movie quotes (movie title + quote)
def get_random_quotes():
  req = urllib2.Request(url,'', headers)
  res = urllib2.urlopen(req)
  res_content = res.read()
  movie_quotes = json.loads(res_content)
  return movie_quotes
  