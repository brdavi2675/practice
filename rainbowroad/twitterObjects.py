## HIIIIIIIIIIIIIIIII
## next version of twitterObjectShit for more classes


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
    
    def getInfo( self ):
        return self.info
    
    def getPosts( self ):
        return self.posts
    
    def getObj( self ):
        return self.obj


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


userIdList = ( "macmiller", "realDonaldTrump", "BarackObama" ) ## list of users to grab data from
userObjList = []

## for every account id in the list, get their info and add to obj list
for x in range( len( userIdList ) ):
    userObjList.append( createUserObj( userIdList[x] ) )
    
    
for userId in range( len(userObjList) ):
    test = userObjList[userId]
    print( test.getId() )
    


