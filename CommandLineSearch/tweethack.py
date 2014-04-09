from twython import Twython
from creds import *


twitter = Twython(APP_KEY, APP_SECRET,
                  FINAL_OAUTH_TOKEN, FINAL_OAUTH_TOKEN_SECRET)
    
while exit != True:
      query = raw_input("What kind of live stream are you looking for? ")
      results = False
      if query.find("livestream") == -1 and query.find("live stream") == -1:
          query = query + " live stream"
      print query
      result = twitter.search(q=query, result_type='recent')
      tweets = result['statuses']
      for tweet in tweets:
        parseThis = tweet['text']
        linkIndex = parseThis.find("http://")
        if linkIndex != (-1):
         link = parseThis[linkIndex:]
         print link[:link.find(' ')]
      exit = raw_input("Type exit to go back or press enter to search for streams again.  ")
      if exit == "exit":
        exit = True