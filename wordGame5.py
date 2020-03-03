letterHome = [
    # Title
    "A Letter Home",
    # Text String
    """
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

    """,

    # Replacements
    [
        ["An occupation     : ","OCCUPATION"],
        ["A country         : ","COUNTRY"],
        ["A plural noun     : ","PLURAL_NOUN"],
        ["A verb            : ","VERB     : "],
        ["An adjective      : ","ADJECTIVE"],
        ["A personal item   : ","PERSONAL_ITEM"],
        ["A holiday         : ","HOLIDAY"],
        ["Your name         : ","NAME"]
    ]
]

sale = [

    # Title
    "A Great Sale",

    # Text String 2
    """
    SALE SALE SALE SALE
    Today only : Buy NUMBER PLURAL_NOUN and get a free NOUN!

    Sign up for our exclusive METAL card and receive 50% off your first purchase!
    """,

    # Replacements 2
    [
        ["A number         : ","NUMBER"],
        ["A plural noun    : ","PLURAL_NOUN"],
        ["A noun","NOUN    : "],
        ["A type of metal  : ","METAL"]
    ]

]

showAndTell = [
    
    # Title
    "Show and Tell",

    #
    """
    Have you seen my pet ANIMAL ? It's the best-- No pet can VERB1 as
    ADVERB as it can. It's NUMBER years old, and its name is NAME.
    You can VERB2 it if you want, but be careful, because it might
    VERB3 .
    """,

    # Replacements
    [
        ["An animal       : ","ANIMAL"],
        ["A verb          : ","VERB1"],
        ["An adverb       : ","ADVERB"],
        ["A number        : ","NUMBER"],
        ["A name          : ","NAME"],
        ["A verb again    : ","VERB2"],
        ["Another verb    : ","VERB3"]
    ]
]

stories = [
    letterHome,
    sale,
    showAndTell
]

selection = int(input("\nPlease Choose a story number : "))
story = stories[selection - 1]
proseString = story[1]
replacements = story[2]

for prompt, placeholder in replacements:
    userInput = raw_input(prompt)
    proseString = proseString.replace(placeholder,userInput)


print("\nThe Title of this story is : " + str(story[0]) +  "\n" + proseString)
