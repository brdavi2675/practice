## HIIIIIIIIIIIIIIIII
## reads from a csv file now


import pandas as pd

from twitter_scraper import get_tweets
from twitter_scraper import get_trends
from twitter_scraper import Profile


class userClass:
    def __init__( self, id, obj, info, posts ):
        self.id = id ## twitter id string
        self.obj = obj ## class object
        self.info = info ## account info like followers
        self.posts = posts ## list of the account's posts
        
    def getId( self ):
        return self.id
        
    def getObj( self ):
        return self.obj
    
    def getInfo( self ):
        return self.info
    
    def getPosts( self ):
        return self.posts


## add a new user object given their account id
def createUserObj( id ):
    newUser = Profile( id )
    
    ## list of their posts as strings
    newUserPosts = []
    for postData in get_tweets( id, pages = 1 ):
        postText = postData["text"]
        post = {
            "text": postText,
            "textList": postText.split(),
            "isRetweet": postData["isRetweet"],
            "likeCount": postData["likes"],
            "replyCount": postData["replies"],
            "retweetCount": postData["retweets"],
        }
        newUserPosts.append( post )
    
    newUserObj = userClass( id, newUser, newUser.to_dict(), newUserPosts )
    return newUserObj


## get a list of account ids from reading a csv file
userIdList = pd.read_csv("twitter_accounts.csv" )
userObjList = []

## for every account id in the list, get their info and add to obj list
for userId in userIdList:
    print( userId ) ## account id
    userObjList.append( createUserObj( userId ) )
    

print( userObjList )
print( len(userObjList) )
