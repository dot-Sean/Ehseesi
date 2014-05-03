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
      sort = raw_input("How would you like the results to be sorted? (time, followers, favorites, retweets)")
      if sort != "followers" and sort != "favorites" and sort != "retweets" and sort != "time":
        print "I'm sorry. That is not a valid search option. Defaulting to \"time\" sort"
        sort_by = False

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
      # Then it stores information into the dictionaries and then continues to sort the tweets by follower and 
      # finally it prints out the tweet text and the expanded URL
      
      file = open("results.txt", 'w')
    
      for tweet in tweets:
        if sort == "time":
          sort_by = False
        elif sort == "followers":
          sort_by = tweet['user']['followers_count']
        elif sort == "favorites":
          sort_by = tweet['favorite_count']  
        elif sort == "retweets":
          sort_by = tweet['retweet_count']
        if sort_by == False:
          for tweet in tweets:
            if count == 15:
              break
            
            elif tweet['user']['followers_count'] >= 10:
                          
              if len(tweet['entities']['urls'])>0:
                count += 1
                text =  (tweet['text'] + "***LINK*** : " + tweet['entities']['urls'][0]['expanded_url'])
                text = text.encode("utf-8")
                file_output = text + "\n"
                print file_output
                file.write(file_output)
                
        else:
          if tweet['user']['followers_count'] >= 10:
                          
            if len(tweet['entities']['urls'])>0:
              parseThis = tweet['text']
            
              ordered_results.setdefault(tweet['id'], sort_by)
              link_dict.setdefault(tweet['id'],{}).setdefault(tweet['text'], tweet['entities']['urls'][0]['expanded_url'])
            
      sorted_list = sorted(ordered_results.items(), key=itemgetter(1), reverse=True)
      print "These results are relevant to the query " + query + ":\n"
      file.write ("These results are relevant to the query " + query + ":\n")
      if sort_by:
        for key,value in sorted_list[:15]:
                          
          for k in link_dict[key]:
                            
            text = (k + " ***LINK*** : " + link_dict[key][k])
            text = text.encode("utf-8")
            file_output = text + "\n"
            print file_output
            file.write(file_output)
            
            #print k
            #print "***LINK*** :", link_dict[key][k]
        
      file.close()

      exit = raw_input("Type exit to go back or press enter to search for streams again. ")
      if exit == "exit":
        exit = True
        
