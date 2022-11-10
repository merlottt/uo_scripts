#UO script: Helper for tamer
#Run on ClassicAssist (ClassicUO client)

UnsetAlias("Target4taming")
if not FindAlias("Target4taming"):
    PromptAlias("Target4taming")

currentfolowers = Followers()
while Followers() == currentfolowers:
    Pathfind("Target4taming")
    UseSkill("Animal Taming")
    Target("Target4taming")
    Pause(1000)
    if InJournal('You have no chance of taming this creature'):
        IgnoreObject(Target4taming)
        Stop()
        
while Followers() != currentfolowers:
    Rename("Target4taming", "oo")  
    # Release pet
    WaitForContext(Target4taming, 10, 15000)
    WaitForGump(0x909cc741, 5000)
    ReplyGump(0x909cc741, 2)
    Pause(1000)