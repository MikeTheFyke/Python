beers = [
    ["Budweiser","Flavoured Water"],
    ["BlueLight","Light"],
    ["Moosehead","Light"],
    ["Moosehead","Non-Alcoholic"],
    ["Moosehead","Regular"]
]

print("\n_______________Welcome To The Beer Emporium_______________\n__________________________________________________________\n")

for listItem in beers:
    listitemBrand = listItem[0]
    listitemDraft = listItem[1]

    print("Available Brands : " + str(listitemBrand) + " Available Drafts : " + str(listitemDraft))


print("\n__________________________________________________________\n")

userBeer = raw_input("What brand of beer would you like : ")
userInput = str(userBeer)

userDraft = raw_input("What draft of beer would you like : ")
userDraftInput = str(userDraft)

cart = []
wrongBeerLookedAt = 0

for beer in beers:
    brandOfBeer = beer[0]
    draft = beer[1] 
    if brandOfBeer is userInput and draft is userDraftInput:
        rightBeerBoolean = True
        cart.append(beer)
        break               # break keyword used for ending the for loop once we can confirm a users selection.
    else:
        wrongBeerLookedAt += 1

if len(cart) is 0:
        cart.append("Empty")
        print("\n Sorry We do not have that beer. I looked through " + str(wrongBeerLookedAt) + " kinds of beer looking for it.\n" )
