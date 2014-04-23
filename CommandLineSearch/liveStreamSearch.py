from twython import Twython
import codecs
from operator import itemgetter
from collections import defaultdict
from creds import *


twitter = Twython(APP_KEY, APP_SECRET,
                  FINAL_OAUTH_TOKEN, FINAL_OAUTH_TOKEN_SECRET)
    
while exit != True:
      query = raw_input("What kind of live stream are you looking for?")
      results = False
      if query.find("livestream") == -1 and query.find("live stream") == -1:
          query = query + " live stream"
      print query
      result = twitter.search(q=query, result_type='recent', count=300)
      tweets = result['statuses']
      # I created two dictionaries, one to sort tweets by how many followers the user has and another to 
      # match that tweet id to the text and the expanded URL
      ordered_results = {}
      link_dict = {}
      
      # This count variable isn't used by anything but it was useful when testing to make sure the program
      # was actually filtering out some tweets
      count = 0
      # For each tweet it checks the number of followers is at least 10, and then checks that there is a 
      # link in the tweet
      # Then i stores information into the dictionaries and the continues to sort the tweets by follower and 
      # finally it prints out the tweet text and the expanded URL
      
      file = open("results.txt", 'w')
    
      for tweet in tweets:
                        
        if tweet['user']['followers_count'] >= 10:
                          
          if len(tweet['entities']['urls'])>0:
            parseThis = tweet['text']
            
            ordered_results.setdefault(tweet['id'], tweet['user']['followers_count'])
            link_dict.setdefault(tweet['id'],{}).setdefault(tweet['text'], tweet['entities']['urls'][0]['expanded_url'])
            
      sorted_list = sorted(ordered_results.items(), key=itemgetter(1), reverse=True)
      for key,value in sorted_list[:15]:
                        
        for k in link_dict[key]:
                          
          text = (k + " ***LINK*** :" + link_dict[key][k])
          text = text.encode("utf-8")
          file.write("These results are relevant to the query", query, ":", "\n" text + "\n")
          
          #print k
          #print "***LINK*** :", link_dict[key][k]
      file.close()

      exit = raw_input("Type exit to go back or press enter to search for streams again.  ")
      if exit == "exit":
        exit = True
        
