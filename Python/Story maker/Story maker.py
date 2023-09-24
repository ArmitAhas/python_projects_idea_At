from random import choice

print("This is a beautiful story for you: ")
starter = ["In far faraway land","Once upon a time","Long time ago"]
char = ["a powerful king lived","a prince named harry lived","a kind and poor farmer lived"]
time = ["one day ","on a moonlit night ","in a warm noon "]
plot = ["was passing by","was passing through the middle of"]
place = ["the green forest","the stone bridge","the beautiful town"]
char2 = ["and saw a pretty princess","and saw a strong knight", "and saw a strange witch"]
age = ["who was younger than him","who was older than him","who was so young"]
doing = ["and was getting closer to him","and was riding a white horse","and was looking at him"]
end = ["and he was scared and ran away.","and he was very proud to see that person.","and without paying any attention, he passed by him and continued his way."]


print(choice(starter),"\n"
      +choice(char),"\n"
      +choice(time)
      +choice(plot),"\n"
      +choice(place),"\n"
      +choice(char2),"\n"
      +choice(age),"\n"
      +choice(doing),"\n"
      +choice(end),"\n"
      +"'THE END'")