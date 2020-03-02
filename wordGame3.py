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
I'll be sure to call every HOLIDAY.

Regards,

NAME

"""

proseString2 = proseString

ocInput = raw_input(" Please Enter An Occupation   : ")
proseString2 = proseString2.replace("OCCUPATION", ocInput)

countryInput = raw_input(" Please Enter A Country   : ")
proseString2 = proseString2.replace("COUNTRY", countryInput)

pluralNounInput = raw_input(" Please Enter A Plural Noun   : ")
proseString2 = proseString2.replace("PLURAL_NOUN", pluralNounInput)

verbInput = raw_input(" Please Enter An Action   : ")
proseString2 = proseString2.replace("VERB", verbInput)

adjectiveInput = raw_input(" Please Enter An Adjective   : ")
proseString2 = proseString2.replace("ADJECTIVE", adjectiveInput)

personalItem = raw_input(" Please Enter A Personal Item    : ")
proseString2 = proseString2.replace("PERSONAL_ITEM", personalItem)

holiday = raw_input(" Please Enter Visting Holiday     : ")
proseString2 = proseString2.replace("HOLIDAY", holiday)

userName = raw_input(" Please Enter Your Name          : ")
proseString2 = proseString2.replace("NAME", userName)

print(proseString2)