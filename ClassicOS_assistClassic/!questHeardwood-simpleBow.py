#vars
items = {
    "fetchtooltype": {"name":"fletcher tools","type":0x1022,"category":8,"button":142},
    "tinkertools":   {"name":"tinker tools","type":0x1eb8,"category":8,"button":23},
    "bow":           {"name":"a bow","type":0x13b2,"category":15,"button":2}
}
ignots          = 0x1bf2
boards          = 0x1bd7
npc             = 0x676
def selectBowlikeQuestItem():
    ClearIgnoreList()  
    ContextMenu("self", 6)  
    Pause(1000)
    for i in range(10):
        FindType(items['bow']['type'],0,"backpack",0)
        Target('found')
        Pause(800)
        IgnoreObject("found")
    CancelTarget()

def startNewQuest():
    while True:  
        UseObject(npc)
        WaitForGump(0x4c4c6db0, 5000)
        if InGump(0x4c4c6db0, "Simple"):
            ReplyGump(0x4c4c6db0, 4)
            break

def endCompletedQuest():
    UseObject(npc)
    WaitForGump(0x4c4c6db0, 5000)
    ReplyGump(0x4c4c6db0, 8)
    Pause(1000)
    WaitForGump(0x4c4c6db0, 5000)
    ReplyGump(0x4c4c6db0, 5)

def craft(tool, craftitem):
    print("Crafting: "+craftitem['name']+":"+str(craftitem['category'])+":"+str(craftitem['button']))
    UseType(tool)
    Pause(1000)
    ReplyGump(0x38920abd, craftitem['category'])
    Pause(1000)
    ReplyGump(0x38920abd, craftitem['button'])
    Pause(1000)
    return
def craft10bows():
    while CountType(items['bow']['type'], "backpack") <= 10:
        print("Count of {}:{}".format(items['bow']['name'],CountType(items['bow']['type'], "backpack")))
        if CountType(items['tinkertools']['type'], "backpack") < 2:
            craft(items['tinkertools']['type'],items['tinkertools'])
            if CountType(ignots,"backpack") < 10:
                print('Need more ignots')
                StopAll()
        if CountType(items['fetchtooltype']['type'], "backpack") < 2:
            craft(items['tinkertools']['type'],items['fetchtooltype'])
            if CountType(ignots,"backpack") < 10:
                print('Need more ignots')
                StopAll()
        craft(items['fetchtooltype']['type'],items['bow'])
        if CountType(boards,"backpack") < 10:
            print('Need more boards')
            StopAll() 
    return
    

startNewQuest()
if CountType(items['bow']['type'], "backpack") < 10:
    craft10bows()
selectBowlikeQuestItem()
endCompletedQuest()

