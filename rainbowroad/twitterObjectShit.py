## HIIIIIIIIIIIIIIIII
## makes a list of objects that are (twitter profile scraper class, then their twitter data as a list)


from twitter_scraper import get_tweets
from twitter_scraper import get_trends
from twitter_scraper import Profile







tUserList = []
tUserList.append( "macmiller" )
tUserList.append( "realDonaldTrump" )

tUserObjs = []

for x in range( len( tUserList ) ):
    newUserId = tUserList[x]
    newUser = Profile( newUserId )
    
    newUserPosts = []
    for postData in get_tweets( newUserId, pages = 1 ):
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
    
    newUserObj = ( newUser, newUser.to_dict(), newUserPosts )
    tUserObjs.append( newUserObj )





print( tUserObjs[1] )


trump = tUserObjs[1]











