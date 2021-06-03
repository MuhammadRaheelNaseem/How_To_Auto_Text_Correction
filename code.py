from textblob import TextBlob

a= "comuter progrming is gret" 

print("Origninal Text: ",str(a))

b=TextBlob(a)

print("Corrected Text: ",str(b.correct()))
