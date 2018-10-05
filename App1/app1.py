import json
from difflib import get_close_matches

#loads json data file
data = json.load(open("data.json"))
#function to use key to return data
def translate(w):
    #case sensitivity
    w = w.lower()
    #Checks for nonexisting words
    if w in data:
        return formatOutput(data[w])
    #Capitalize first letter
    elif w.title() in data:
        return formatOutput(data[w.title()])
    elif w.upper() in data:
        return formatOutput(data[w.upper()])
    #Check for closest match
    elif len(get_close_matches(w, data.keys())) > 0:
        answer = input("Did you mean %s instead? Enter Y if yes, or N if no." % get_close_matches(w, data.keys())[0])
        answer = answer.lower()
        if answer == "y":
            return formatOutput(data[get_close_matches(w, data.keys())[0]])
        elif answer == "n":
            print("The word doesn't exist. Please double check it and try again.")
            return wordInput(w)
        else:
            print("We didn't understand your entry. Try again.")
            return wordInput(w)

    else:
        return "The word doesn't exist. Please double check it and try again."

def wordInput(wd):
    #user input word to search
    wd = input("Enter word: ")
    #print data from key
    return(translate(wd))

def formatOutput(out):
    if type(out) == list:
        for item in out:
            
            print("\n" +item)
        answer = input("\nWould you like to enter a new word? Enter Y if yes, or N if no.")
        answer = answer.lower()
        if answer == "y":
            print("")
            wordInput(out)

    else:
        print("\n" +out)
    return""


word = input("Enter word: ")
print(translate(word))
