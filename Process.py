'''
The student(a child) will interact with an animated character(a chef in this case).
We have to design a NLP/NLU engine to understand the sentiment and intent behind a
child's statement and respond accordingly.


'''
counter=1
cond=0
flavor=[]
num=[]
Number={"one":1,"two":2,"three":3,"four":4,"five":5} #more than 5 ice creams is harmful for health
Flavours=["acai berry","alaskan mint","all american favorite (cracker jacks)","amaretto brownie cheesecake","amaretto brownie",
          "amaretto cherry","amaretto chocolate chip cheesecake","apple cinnamon","apple pie ala mode","banana chocolate chip",
          "banana coconut macaroon cheesecake","banana french toast","banana fudge swirl","banana pudding","banana split","banana walnut",
          "banana","bananas foster cheesecake","bananas foster","bats in the attic","birthday cake","black cherry cheesecake","black cherry",
          "black raspberry cheesecake","black raspberry","black walnut cheesecake","black walnut","blackberry bramble",
          "blackberry cheesecake","blue moon","blue raspberry","blue skies and rainbows","blueberry banana","blueberry brown sugar",
          "blueberry cheesecake","blueberry french toast","blueberry pie","blueberry sundae","brown sugar cinnamon","brown sugar",
          "brownie snicker finger","bubblegum cheesecake","bubblegum","bumbleberry cheesecake","bumbleberry","butter brickle","butter pecan",
          "buttered almond","butterfinger cheesecake","butterfinger","butterscotch cheesecake","butterscotch","cake batter","caramallow chip",
          "caramel apple crunch","caramel banana","caramel fudge swirl","carrot cake","cheesecake(plain)","cherokee gold","chiefs chip",
          "chocolate brownie chunks","chocolate caramel almond","chocolate cheesecake","chocolate cherry","chocolate chip cookie",
          "chocolate chocolate fudge","chocolate chocolate mint","chocolate cookies & cream","chocolate covered banana(monkeyshines)","chocolate covered strawberry",
          "chocolate espresso","chocolate fudge brownie","chocolate fudge","chocolate l'orange","chocolate malt 'whoppers'","chocolate passion",
          "chocolate peanut butter cheesecake","chocolate peanut butter","chocolate pistachio almond","chocolate poppers","chocolate raspberry truffle",
          "chocolate speed bumps","chocolate swamp","chocolate turtle","chocolate","christmas spagetti","cinnamon turtle","cinnamon",
          "coconut almond delight", "coconut fudge supreme", "coconut ginger", "coconut", "coffee chip cheesecake",
          "coffee and cognac", "coffee with espresso pillows", "coffee", "confetti", "cookie dough", "cotton candy",
          "dulce de leche bonanza", "easter egg hunt (seasonal) (easter m&m's in vanilla)", "eggnog(seasonal)",
          "elvis in white (white chocolate peanutbutter banana)", "english toffee coffee", "firecracker(seasonal)",
          "french toast", "fright night", "frog pond", "frog tracks", "fudge swirl", "georgia peach cheesecake",
          "georgia peach", "german chocolate cheesecake", "german chocolate", "ginger", "gorilla vanilla",
          "grandma's cookies", "grape escape", "grape nuts", "green tea", "green tree frog", "hazelnut coffee",
          "heath bar cheesecake", "heath bar", "heavenly hash", "honey cinnamon graham",
          "honey cinnamon oatmeal cookie", "honey espresso", "honey vanilla", "huckleberry cheesecake",
          "huckleberry pie", "huckleberry", "hulk's cream", "irish coffee", "irish cream", "jack and jill",
          "jamaica bay", "key lime pie", "lemon blueberry cheesecake", "lemon cheesecake", "lemon coconut cheesecake",
          "lemon coconut", "lemon crème", "lemon pie", "leprechan mint", "licorice", "m&m", "mango", "maple pecan",
          "maple walnut", "mexican coffee", "mint chocolate chip", "mocha almond crunch (chocolate base)",
          "mocha cappuccino cheesecake", "mocha chocolate chip cheesecake", "orange cranberry", "orange dream",
          "orange pineapple flip", "oreo fudge cheesecake", "oreo mint cheesecake", "oreo mint", "pb&j", "paradise",
          "peanut butter chip", "peanut butter crunch", "peanut butter cup cheesecake", "peanut butter cup",
          "peanut butter fudge cheesecake", "peanut butter passion (peanut butter with reeses pieces)",
          "peanut butter/banana" ,"elvis sandwich", "peppermint cheesecake", "peppermint twist", "peppermint",
          "pina colada", "pineapple cheesecake", "pineapple", "pistachio cheesecake", "pistachio", "polar bear freeze",
          "praline cheesecake", "pralines and cream", "princess party", "pumpkin cheesecake", "pumpkin",
          "raspberry chocolate chocolate chip","raspberry chocolate truffle","raspberry morning","red cream soda","red raspberry rhapsody"
          ,"red velvet","reese's pieces","rum raisin","sasparilla cream (rootbeer)","sea hunt","season's greetings","smores","snickers caramel cheesecake","snickers","spumoni","strawberry cheesecake",
          "strawberry mango cheesecake","strawberry mango","strawberry shortcake","strawberry","tamarind","the strawberry cake(strawberry coconut cheesecake)","thin mint girl scout cookie",
          "tiramisu toffee cheesecake","tiramisu toffee","vanilla bean cheesecake","vanilla bean","vanilla chocolate chip","vanilla cookies & cream","vanilla with espresso pillows","vanilla",
          "watermelon man","white chocolate macadamia nut","white chocolate macaroon","white chocolate peanutbutter","white chocolate peppermint","white chocolate raspberry truffle","white chocolate raspberry",
          "white chocolate strawberry cheesecake","white chocolate turtle","wigglers and stuff","wild cherry","witergreen","wormy apple"]



def setup():
    #holds the flavours and prices of items available, manual changes need to be performed.
    Menu={'chocolate':20,'strawberry':25,'mango':18,'banana':15}
    return Menu



def costfactor(statement,Menu):
    if "cost" in statement or "price" in statement:
        #search for the flavour requested and provide its cost from the dictionary
        for flavour in Menu:
            if flavour in statement:
                cost =Menu.get(flavour)

    return "The cost of the flavour is "+str(cost)




def serving(statement,Menu):
    i=len(num)-1
    reply=''
    #calculates quantity also
    i=i-1
    global cond
    while(1):
        if "cup" in statement:
            reply = num[i] + ' '
            for flavour in Menu:
                if flavour in flavor:
                    reply+=flavour+" in a cup,"
                    #remove both the flavour and "cup"
                    flavor.remove(flavour)
                    statement=statement.replace("cup",'')
             #       print(flavor)
              #      print(statement)
                    cond=3
                    break


        if "cone" in statement:
            #print('hello')
            reply +=num[i]+' '
            i-=1
            for flavour in Menu:
                #print(flavour)
                if flavour in flavor:
                    #print('true')
                    reply+=flavour+" in a cone "
                    flavor.remove(flavour)
                    statement=statement.replace("cone",'')
                    cond=3
                    #print(reply+" is the reply")

        if len(flavor)==0:
            break
        else :  #invalid input
            print("I did not understand")
            cond=1
            return
    #print(num)
    reply=reply[:-1]+". Getting it ready."
    return reply


def process(statement,Menu):
    flag=0
    check=0
    numcheck=0
    global cond
    global num
#    performing NLP using regex for now....
    stm=''
    if "menu" in statement:
        for flav,cost in Menu.items():
            stm+=flav+', '
        stm =stm[:-2]+'.'
        return "We serve the following flavours of ice cream:"+stm
    if "not" in statement or "other" in statement or "no" in statement or "dont" in statement:
        reply=Not(statement,Menu)
        #print(num)
        cond=0
        return reply
    if "want"  in statement or "like" in statement or "have" in statement: #i want pinna colada

        #search for item in Menu
        for flavour in Menu.keys():
            if flavour in statement:#flavour exists
                flag=1
                flavor.append(flavour)
                cond=1

            if numcheck==0:
                for n in Number:
                    if n in statement:
                        num.append(n)
                #print(num)
            numcheck = 1


        #flavour not found, check if its a flavour even....
        if flag==0:
            for flavour in Flavours:
                if flavour in statement:
                    cond=-1
                    return "Sorry, we do not serve that"
        if cond==1:
            return "Would you like that in a cup or a cone?"

    if "cost" in statement or "price" in statement:
        cond=2
        return statement




    cond=4
    return "I did not understand"



def Not(statement,Menu):
    remains=[]
    #print("Inside NOT")
    #notices a not in the sentence of one form on=r the other, changes the flavours selected to complement of what is there
    for flavours in Menu:
        if flavours not in statement:
            remains.append(flavours)
    s=str(remains)[1:-1]
    Menu=remains
   # print(Menu)
    return "Would you like one of the  following flavours- "+ s


def main():
    Menu=setup()
# Basic response to begin conversation
    global counter
    global num
    if counter==1:
        print("Welcome to Golu's icecream parlor. What would you like to have?")

    if counter==0:
        print('What would you like to have?')
       #reception of inputs, for each input, perform processing to understand what the input requires.
    Statement=input()
    Statement=Statement.lower()
   # print(Statement)
    reply=Statement
    counter = 0
    global cond
    cond=0
    if "dont" in Statement and "order" in Statement:
        print("Please visit again")
        exit(0)
    if cond==0:
        reply=process(reply,Menu)
        print(reply)
        if cond==0:
            main()

    #processing done

    #print(flavor + num)
    if cond==1:
        reply = input()
        reply=serving(reply,Menu)
        print(reply)
    if cond==2:
        reply=costfactor(reply,Menu)
        print(reply)
        main()

    if cond==3:
        reply=input("Anything else?")
        if 'no' in reply or 'nothing' in reply:
            print("Please visit again")
            exit(0)
        else:
            num=[]
            main()

    if cond==4:
        #RE enter the query
        main()




main()