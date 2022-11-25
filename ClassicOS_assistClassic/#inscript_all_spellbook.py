DEBUG = False
SetQuietMode(not(DEBUG))
inscriptionGump = 0x38920abd
gumpTimeout     = 5000

UnsetAlias("targetBook")
if not FindAlias("targetBook"):
    PromptAlias("targetBook")

class ScrollInfo:
    def __init__(self, name, itemid, gumpButton1, gumpButton2):
        self.name = name
        self.itemid = itemid
        self.gumpButton1 = gumpButton1
        self.gumpButton2 = gumpButton2

ScrollInfo = [
    ScrollInfo("circle1spell1",0x1f2d,1,2),
    ScrollInfo("circle1spell2",0x1f2e,1,9),
    ScrollInfo("circle1spell3",0x1f2f,1,16),
    ScrollInfo("circle1spell4",0x1f30,1,23),
    ScrollInfo("circle1spell5",0x1f31,1,30),
    ScrollInfo("circle1spell6",0x1f32,1,37),
    ScrollInfo("circle1spell7",0x1f33,1,44),
    ScrollInfo("circle1spell8",0x1f34,1,51),
    ScrollInfo("circle2spell1",0x1f35,8,2),
    ScrollInfo("circle2spell2",0x1f36,8,9),
    ScrollInfo("circle2spell3",0x1f37,8,16),
    ScrollInfo("circle2spell4",0x1f38,8,23),
    ScrollInfo("circle2spell5",0x1f39,8,30),
    ScrollInfo("circle2spell6",0x1f3a,8,37),
    ScrollInfo("circle2spell7",0x1f3b,8,44),
    ScrollInfo("circle2spell8",0x1f3c,8,51),
    ScrollInfo("circle3spell1",0x1f3d,15,2),
    ScrollInfo("circle3spell2",0x1f3e,15,9),
    ScrollInfo("circle3spell3",0x1f3f,15,16),
    ScrollInfo("circle3spell4",0x1f40,15,23),
    ScrollInfo("circle3spell5",0x1f41,15,30),
    ScrollInfo("circle3spell6",0x1f42,15,37),
    ScrollInfo("circle3spell7",0x1f43,15,44),
    ScrollInfo("circle3spell8",0x1f44,15,51),
    ScrollInfo("ArchCure",0x1f45,22,2),
    ScrollInfo("ArchProtection",0x1f46,22,9),
    ScrollInfo("Curse",0x1f47,22,16),
    ScrollInfo("FireField",0x1f48,22,23),
    ScrollInfo("GreaterHeal",0x1f49,22,30),
    ScrollInfo("Lighting",0x1f4a,22,37),
    ScrollInfo("ManaDrain",0x1f4b,22,44),
    ScrollInfo("Recall",0x1f4c,22,51),
    ScrollInfo("BladeSpirit",0x1f4d,29,2),
    ScrollInfo("DispelField",0x1f4e,29,9),
    ScrollInfo("Incognito",0x1f4f,29,16),
    ScrollInfo("MagicReflection",0x1f50,29,23),
    ScrollInfo("MindBlast",0x1f51,29,30),
    ScrollInfo("Paralyze",0x1f52,29,37),
    ScrollInfo("PoisonField",0x1f53,29,44),
    ScrollInfo("SummonCreature",0x1f54,29,51),
    ScrollInfo("Dispel",0x1f55,36,2),
    ScrollInfo("EnergyBolt",0x1f56,36,9),
    ScrollInfo("Explosion",0x1f57,36,16),
    ScrollInfo("Invisibility",0x1f58,36,23),
    ScrollInfo("Mark",0x1f59,36,30),
    ScrollInfo("MassCurse",0x1f5a,36,37),
    ScrollInfo("ParalyzeField",0x1f5b,36,44),
    ScrollInfo("Reveal",0x1f5c,36,51),
    ScrollInfo("ChainLighting",0x1f5d,43,2),
    ScrollInfo("EnergyField",0x1f5e,43,9),
    ScrollInfo("Flamestrike",0x1f5f,43,16),
    ScrollInfo("GateTravel",0x1f60,43,23),
    ScrollInfo("ManaVampire",0x1f61,43,30),
    ScrollInfo("MassDispel",0x1f62,43,37),
    ScrollInfo("MeteorSwarm",0x1f63,43,44),
    ScrollInfo("Polymorph",0x1f64,43,51),
    ScrollInfo("Earthquake",0x1f65,50,2),
    ScrollInfo("EnergyFortex",0x1f66,50,9),
    ScrollInfo("Resurrection",0x1f67,50,16),
    ScrollInfo("SummonAirElemental",0x1f68,50,23),
    ScrollInfo("SummonDaemon",0x1f69,50,30),
    ScrollInfo("SummonEarthElemental",0x1f6a,50,37),
    ScrollInfo("SummonFireElemental",0x1f6b,50,44),
    ScrollInfo("SummonWaterElemental",0x1f6c,50,51)
]


def craftspell(item):
    while not FindType(item.itemid, -1,"backpack"):
        print("creating..."+scroll.name+"="+str(scroll.itemid)+"--"+str(scroll.gumpButton1)+"--"+str(scroll.gumpButton2))
        UseType(0xfbf)
        Pause(1000)
        ReplyGump(inscriptionGump, item.gumpButton1)
        Pause(1000)
        ReplyGump(inscriptionGump, item.gumpButton2)
        Pause(5000)
    MoveType(item.itemid,"backpack", GetAlias("targetBook"),-1,-1,-1,-1,1)

for scroll in ScrollInfo:
    print(scroll.name+"="+str(scroll.itemid)+":"+str(scroll.gumpButton1)+":"+str(scroll.gumpButton2))
    craftspell(scroll)
    Pause(1000)