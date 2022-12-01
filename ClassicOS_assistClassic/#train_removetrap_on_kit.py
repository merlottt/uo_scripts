#use first Kit from second method https://www.uoguide.com/Remove_Trap#Method_2
paths = [
            [ 2,2,3,3 ],
            [ 3,2,2,3 ],
            [ 3,2,3,2 ],
            [ 3,3,2,2 ],
            [ 2,3,3,2 ],
            [ 2,3,2,3 ],
            [ 2,3,4,3,2,2 ]
        ]
        
traptrainkit = 0x4063e834           
gumpid = 0x26f70a6a


def kitstep(btn):
    print("reply to gump:"+str(btn))
    WaitForGump(gumpid, 2000)
    Pause(1000)
    ReplyGump(gumpid, btn)

for route in paths:
    print("Tried next solition"+str(route))
    CreateTimer("removetrap")
    SetTimer("removetrap",0)
    UseSkill("Remove Trap")
    WaitForTarget(5000)
    Target(traptrainkit)
    ClearJournal()
    i = 0
    for step in route:
        if not InJournal("fail") or InJournal("successfully") or InJournal("wait"):
            kitstep(route[i])
            i=i+1
    while Timer("removetrap") < 10000:
        Pause(1000)
        