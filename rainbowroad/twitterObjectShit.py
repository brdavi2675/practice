## HIIIIIIIIIIIIIIIII

from twitter_scraper import get_tweets
from twitter_scraper import get_trends
from twitter_scraper import Profile







tUserList = []
tUserList.append( "macmiller" )

tUserObjs = []

for x in range( len( tUserList ) ):
    newUser = Profile( tUserList[x] )
    newUserData = newUser.to_dict()
    newUserObj = ( newUser, newUserData )




print( newUserObj )
print( newUserObj )















