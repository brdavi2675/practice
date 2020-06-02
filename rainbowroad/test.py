## Testing shit



#import tensorflow as tf

#a = tf.Variable( 1, name="a" )
#b = tf.Variable( 2, name="b" )
#f = a + b
#tf.print( f )










name = "Test"

xCoord = [0, 0, 0]
yCoord = [1, 2, 3]
zCoord = [5, 3, -2]
position = [xCoord, yCoord, zCoord]

testString = ("Fuck", "you")
testBool = True

ply = [name, position, testString, testBool]


print( ply )
#print( ply[0] )
print( type( ply[0] ) )

for i in range( len(ply) ):
    #print( ply[i] )
    #print( type(ply[i]) )
    value = ply[i]
    
    print( type(value) )
    print( type(value) == 'str'd )

