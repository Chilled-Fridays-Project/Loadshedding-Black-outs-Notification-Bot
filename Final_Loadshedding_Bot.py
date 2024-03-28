from time import sleep
import tweepy
from twilio.rest import Client 
 
consumer_key="NUQw7aYKYoeoJkg7fIqLSa3d7"
consumer_secret="zRsMqa9qfN4obX2Aopblupfo2vpX57DRYNw2wTcVJoSmeGBfik"
access_token="329232099-O1bRUfHiJ0thUZSlHXVvnW1pYhWv5xA24xgcjMMq"
access_token_secret="zXd8mNN54UnExR7k9BboGTSlz75NyVUXDSuJULQeq4E5H"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

account_sid ='AC112c3f2b29f35f63562dcae702cc2642'
auth_token = 'ec8e5b1ace3729b325e39573ee510ce9' 
client = Client(account_sid, auth_token) 

#keyword_tweets=[]
#keyword_d_tweets=[]
#tweets_dates_times=[]


keyword="loadshedding"
k=0
keyword_PTA='group 6'
keyword_PTA2='and 6'

while True:
    
    try: #City of Tshwane loadshedding schedule
        user=api.user_timeline("CityTshwane",tweet_mode="extended")

        ty=open("C:\\Users\\THULARE KABELO\\Documents\\Business\\Chilled Fridays Listening Sessions\\Music Program Codes\\Tshwane_tweets.txt",'r')
        keyword_tweets=ty.read().split("*!>*")
        if '' in keyword_tweets[-1] or 'x0' in keyword_tweets[-1]:
            
            keyword_tweets.pop(-1)
        keyword_tweets=[i.encode('utf-8').decode('unicode_escape') for i in keyword_tweets]
        #open dates of the tweets into a list'
        td=open("C:\\Users\\THULARE KABELO\\Documents\\Business\\Chilled Fridays Listening Sessions\\Music Program Codes\\Tshwane_tweets_date.txt",'r')
        tweets_dates_times=td.read().split("*!>*")
        tweets_dates_times.pop(-1)
        twittt=[]
        twittt_date=[]
        tweet_send=[]
        for i in user:
            tweet=i.full_text
            tweet_date=str(i.created_at)
            _tweet=tweet.casefold()
            if 'group' in _tweet and " 6" in _tweet or keyword in _tweet:
                
                orig_tweet=tweet
                tweet=tweet.encode('utf-8').decode('unicode_escape')                
                #twts=[twt for twt in keyword_tweets if twt == tweet and tweet_date in str(tweets_dates_times)]
                if tweet_date not in str(tweets_dates_times):

                    tweet_send.append(orig_tweet)
                    keyword_tweets.append(tweet)
                    twittt.append(tweet)

                    tweets_dates_times.append(tweet_date)
                    twittt_date.append(tweet_date)

        twittt.reverse()
        tweet_send.reverse()
        twittt_date.reverse()
        for i in range(len(twittt)):
            
            
            message = client.messages.create(  
                          messaging_service_sid='MGedff2c3f26f74f6ee88fea72f504ef9c', 
                          body="City of Tshwane ere...\n\n"+tweet_send[i], 
                          from_= '+18453851922',
                          to='+27743170985' )
            
            with open("C:\\Users\\THULARE KABELO\\Documents\\Business\\Chilled Fridays Listening Sessions\\Music Program Codes\\Tshwane_tweets.txt","a",encoding='unicode_escape') as tweetts:
                


                tweetts.write(twittt[i]+"*!>*")
                
                
            with open("C:\\Users\\THULARE KABELO\\Documents\\Business\\Chilled Fridays Listening Sessions\\Music Program Codes\\Tshwane_tweets_date.txt",'a') as twt_dates:




                twt_dates.write(twittt_date[i]+"*!>*")            
                    
    except:
        pass
    
    try:
        user=api.user_timeline("Eskom_SA",tweet_mode="extended")

        ty=open("C:\\Users\\THULARE KABELO\\Documents\\Business\\Chilled Fridays Listening Sessions\\Music Program Codes\\tweets.txt",'r')
        keyword_tweets=ty.read().split("*!>*")
        if '' in keyword_tweets[-1] or 'x0' in keyword_tweets[-1]:
            keyword_tweets.pop(-1) 
        keyword_tweets=[i.encode('utf-8').decode('unicode_escape') for i in keyword_tweets]
        #open dates of the tweets into a list
        td=open("C:\\Users\\THULARE KABELO\\Documents\\Business\\Chilled Fridays Listening Sessions\\Music Program Codes\\tweets_date.txt",'r')
        tweets_dates_times=td.read().split("*!>*")
        tweets_dates_times.pop(-1)

        twittt=[]
        twittt_date=[]
        tweet_send=[]        
        
        for i in user:
            tweet=i.full_text
            tweet_date=str(i.created_at)
            if keyword in tweet.casefold():
                
                
                orig_tweet=tweet
                tweet=tweet.encode('utf-8').decode('unicode_escape')                
                #twts=[twt for twt in keyword_tweets if twt == tweet and tweet_date in str(tweets_dates_times)]
                if tweet_date not in str(tweets_dates_times):

                    tweet_send.append(orig_tweet)
                    keyword_tweets.append(tweet)
                    twittt.append(tweet)

                    tweets_dates_times.append(tweet_date)
                    twittt_date.append(tweet_date)

        twittt.reverse()
        tweet_send.reverse()
        twittt_date.reverse()
        for i in range(len(twittt)):
            
            
            message = client.messages.create(  
                          messaging_service_sid='MGedff2c3f26f74f6ee88fea72f504ef9c', 
                          body="Eskom ere...\n\n"+tweet_send[i], 
                          from_= '+18453851922',
                          to='+27743170985' )
            
            with open("C:\\Users\\THULARE KABELO\\Documents\\Business\\Chilled Fridays Listening Sessions\\Music Program Codes\\tweets.txt","a",encoding='unicode_escape') as tweetts:
                


                tweetts.write(twittt[i]+"*!>*")
                
                
            with open("C:\\Users\\THULARE KABELO\\Documents\\Business\\Chilled Fridays Listening Sessions\\Music Program Codes\\tweets_date.txt",'a') as twt_dates:




                twt_dates.write(twittt_date[i]+"*!>*")  

    except:
        pass
    
    sleep(60*4)
