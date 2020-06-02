## HIIIIIIIIIIIIIIIII

from twitter_scraper import get_tweets
from twitter_scraper import get_trends
from twitter_scraper import Profile


username = "macmiller"

profile = Profile( username )
profileData = profile.to_dict()
profilePosts = profileData["tweets_count"]


postList = []

for postData in get_tweets( username, pages = 1 ):
    postText = postData["text"]
    
    post = {
        "text": postText,
        "textList": postText.split(),
        "isRetweet": postData["isRetweet"],
        "likeCount": postData["likes"],
        "replyCount": postData["replies"],
        "retweetCount": postData["retweets"],
    }
  
    postList.append( post )
    
    
    
print( postList )
##print( len( postList ) )

#print( postList )
#print( profilePosts )

