## more random string shit


tweet = "Hello, World! This is a messageto"
tweetLen = len( tweet )

punc = [".", ",", "?", "!", ";", ":", "/", "\'", "\""]
def isPunc( textChar ):
  return textChar in punc


def stringToWordList( words ):
  wordList = []
  word = None

  for x in range( tweetLen ):
    char = tweet[x]
    
    if not isPunc( char ) and char != " ": 
      word = char if word == None else word + char
      
    if char == " " or x + 1 == tweetLen:
      wordList.append( word.lower() )
      word = None
  
  return wordList


print( stringToWordList( tweet ) )
