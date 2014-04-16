from twython import Twython
import codecs
from operator import itemgetter
from collections import defaultdict
from creds import *


twitter = Twython(APP_KEY, APP_SECRET,
                  FINAL_OAUTH_TOKEN, FINAL_OAUTH_TOKEN_SECRET)
    
while exit != True:
      query = raw_input("What kind of live stream are you looking for? ")
      results = False
      if query.find("livestream") == -1 and query.find("live stream") == -1:
          query = query + " live stream"
      print query
      result = twitter.search(q=query, result_type='recent', count=300)
      tweets = result['statuses']
      ordered_results = {}
      link_dict = {}
      print result
      count = 0
      for tweet in tweets:
        print tweet['user']['followers_count']
        if tweet['user']['followers_count'] >= 10:
          if len(tweet['entities']['urls'])>0:
            parseThis = tweet['text']
            ordered_results.setdefault(tweet['id'], tweet['user']['followers_count'])
            link_dict.setdefault(tweet['id'],{}).setdefault(tweet['text'], tweet['entities']['urls'][0]['expanded_url'])
      print link_dict
      sorted_list = sorted(ordered_results.items(), key=itemgetter(1), reverse=True)
      for key,value in sorted_list[:15]:
        for k in link_dict[key]:
          print k
          print "***LINK*** :", link_dict[key][k]

      exit = raw_input("Type exit to go back or press enter to search for streams again.  ")
      if exit == "exit":
        exit = True