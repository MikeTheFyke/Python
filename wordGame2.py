proseString = """
Hi mom,

Just writing to tell you that I've quit my job as
a OCCUPATION and I'm moving to COUNTRY.
The truth is, I've always been passionate
about PLURAL_NOUN, and COUNTRY is the
best place in the world to build a career
around them. I'll need to start a small-- At first,
all I'll be allowed to do is to VERB near them,
but when people see how ADJECTIVE I can be,
I'm sure to rise to the top.

Dont't worry about me, and tell dad to take
good care of my PERSONAL_ITEM. 
I'll be sure to call every Holiday.

Regards,

NAME

"""

ocInput = raw_input(" Please Enter An Occupation   : ")
countryInput = raw_input(" Please Enter A Country   : ")
pluralNounInput = raw_input(" Please Enter A Plural Noun   : ")
verbInput = raw_input(" Please Enter An Action   : ")
adjectiveInput = raw_input(" Please Enter An Adjective   : ")
personalItem = raw_input(" Please Enter A Personal Item    : ")


proseString2 = proseString.replace("OCCUPATION",ocInput)
proseString2 = proseString.replace("COUNTRY",countryInput)
proseString2 = proseString.replace("PLURAL_NOUN",pluralNounInput)
proseString2 = proseString.replace("VERB",verbInput)
proseString2 = proseString.replace("ADJECTIVE",adjectiveInput)
proseString2 = proseString.replace("PERSONAL_ITEM",personalItem)

print(proseString2)