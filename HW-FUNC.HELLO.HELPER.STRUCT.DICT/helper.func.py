
def split(text):
    words = []
    word = ""
    for c in text:      # same as list, dictionary
        if c != " ":
            word += c
        else: 
            words.append(word)
            word = ""
    words.append(word)
    return words 

# CALLING OUR FUNCTION
print( split( "hello people" ) )
print( split( "I love python3 " ) )