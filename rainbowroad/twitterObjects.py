## HIIIIIIIIIIIIIIIII
## next version of twitterObjectShit for more classes


from twitter_scraper import get_tweets
from twitter_scraper import get_trends
from twitter_scraper import Profile


class userClass:
    def __init__( self, id, info, posts ):
        self.id = id # set this to twitter id
        self.info = info
        self.posts = posts


def createUserObj( id ):
    newUser = Profile( id )
    
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
    
    newUserObj = userClass( newUser, newUser.to_dict(), newUserPosts )
    return newUserObj






userObjList = []

userIdList = ( "macmiller", "realDonaldTrump" )
for x in range( len( userIdList ) ):
    userObjList.append( createUserObj( userIdList[x] ) )
    
    
    
    
fuck = userObjList[1]
print( fuck.posts )



