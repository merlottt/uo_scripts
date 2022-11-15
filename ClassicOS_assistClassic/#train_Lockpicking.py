# Name: Train Lockpicking Helper
# Description: Select Key and Box, and then script lock box and trying to lockpick it
# Author: MEr
# Shard: uogames
# Date: 11/15/2022

HeadMsg("select key", "self") 
PromptAlias('key')

HeadMsg("select box", "self")  
PromptAlias('box')

while Skill("Lockpicking") < SkillCap("Lockpicking"):
    if not FindType(0x14fc, 0, 'backpack'):
        HeadMsg("cant find lockpick, script stoped", "self")
        Stop()
    
    UseType(0x14fc,0,'backpack')
    WaitForTarget(5000)
    Target(GetAlias("box"))
    Pause(1000)
    
    if InJournal("This does not appear to be locked", "system"):
        UseObject(GetAlias("key"))
        WaitForTarget(5000)
        Target(GetAlias("box"))
        Pause(1000)