bandage = 0xe21
target  = 0x2e19c

def veterinaringHELP(target):
    if Distance(target) > 3: 
        print("closer....")
        return
    if not TimerExists("vetHELP"):
        CreateTimer("vetHELP")  
        UseType(bandage,-1,"backpack")
        WaitForTarget(500)
        Target(target)
    if Timer("vetHELP")  > 4000:
        RemoveTimer("vetHELP")
    return
    
def main():
    if FindObject(target, 10):
        if DiffHitsPercent(target) > 5:  #if Hits 95% and less
            veterinaringHELP(target)
        return


while not Dead("self"):
    main()
    Pause(500)