#vars
tongs       = ["tongs",0xfbb,8,86]
tinkertools = ["tinker tools",0x1eb8,8,23]
ignots      = 0x1bf2

bsmatrix    = [ 
                ["dagger",0xf52,43,30,25,45],
                ["mace",0xf5c,64,9,45,55],
                ["maul",0x143b,64,16,55,65],
                ["cutlas",0x1441,43,23,65,72],
                ["katana",0x13ff,43,37,72,90],
                ["xircluet",0x2b6e,22,93,90,100]
                ]
resbox      = 0x401ef83a
craftgump   = 0x38920abd

def craft(tool,name,category,number):
    print("Crafting: "+name+":"+str(category)+":"+str(number))
    UseType(tool)
    Pause(1000)
    ReplyGump(0x38920abd, category)
    Pause(1000)
    ReplyGump(0x38920abd, number)
    Pause(1000)

def getresources(what,count,frombox,tobox):
    MoveType(what, frombox, tobox, -1, -1, -1, 0, count)
    Pause(1000)
    
def smelt(name,itemtype):
    print("smelt :"+name)
    while CountType(itemtype, "backpack", 0) > 0:
        UseType(tongs[1])
        Pause(3333)
        FindType(itemtype,-1,"backpack")
        ReplyGump(craftgump, 14)
        WaitForTarget(1000)
        Target("found")
        print("target")
        Pause(600)

while Skill('Blacksmith') < 100:
    while CountType(ignots, "backpack") < 50:
        print("i need more ignots")
        getresources(ignots,1000,resbox,"backpack")
    while CountType(tinkertools[1], "backpack") < 3:
        craft(tinkertools[1],tinkertools[0],tinkertools[2],tinkertools[3])
    while CountType(tongs[1], "backpack") < 2:
        craft(tinkertools[1],tongs[0],tongs[2],tongs[3]) 
    for i in bsmatrix:
        if Skill('Blacksmith') >= i[4] and Skill('Blacksmith') < i[5]:
            craft(tongs[1],i[0],i[2],i[3])
            smelt(i[0],i[1])

