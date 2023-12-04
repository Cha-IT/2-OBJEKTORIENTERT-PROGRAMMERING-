# Et system for å håndtere scener, dialog og liknende. 

class Scene:
    def __init__(self,tittel,beskrivelse="",valgTekst="",slutt=False) -> None:
        self.tittel = tittel
        self.neste_scener = []
        self.beskrivelse = beskrivelse
        self.scene_valg = valgTekst
        self.avslutterSpill = slutt
    def leggTilNesteScene(self,scene):
        self.neste_scener.append(scene)
    def setBeskrivelse(self,beskrivelse):
        self.beskrivelse=beskrivelse
    def setValgTekst(self,valgtekst):
        self.scene_valg = valgtekst
    def valg(self):
        print(self.beskrivelse)
        for i in range(len(self.neste_scener)):
            print(f"{i+1}: {self.neste_scener[i].scene_valg}")
        svar = int(input(" Hva gjør du? ")) - 1 
        return self.neste_scener[svar]
        
class Spill:
    def __init__(self,startScene:Scene) -> None:
        self.scene = startScene
        self.over=False

    def spill(self):
        while not self.over:
            self.meny()
        print(self.scene.beskrivelse)
        print("Spillet er slutt, jaja ")
    def meny(self):
        self.scene = self.scene.valg()
        self.over = self.scene.avslutterSpill
    
pratTittel ="Praten med Borgermesteren"
sceneStart = Scene("Åpning")
sceneStart.setBeskrivelse("Du starter spillet, hva vil du gjøre")
sceneStart.setValgTekst("Tilbake til start")

ScenePrat1 = Scene(pratTittel)
ScenePrat1.setBeskrivelse("Du går en tur til borgermesteren i byen \n \n De forteller at det har vært mange angrep i det siste på beboere i slum-områdene av byen \n \n Hva vil du gjøre")
ScenePrat1.setValgTekst("Gå til borgermesteren")
sceneStart.leggTilNesteScene(ScenePrat1)
ScenePrat2 = Scene(pratTittel)
ScenePrat2.setValgTekst("Hva kan jeg gjøre?")
ScenePrat2.setBeskrivelse("Du vil hjelpe? Herlig! \n Gå til slummen og undersøk hva som skjer der!")
ScenePrat2.leggTilNesteScene(sceneStart)

ScenePrat3 = Scene(pratTittel, slutt=True)
ScenePrat3.setValgTekst("Har ikke byen vakter for å gjøre slikt?")
ScenePrat3.setBeskrivelse("Nei, der har vi ikke :| ")
ScenePrat3.leggTilNesteScene(sceneStart)

ScenePrat1.leggTilNesteScene(ScenePrat2)
ScenePrat1.leggTilNesteScene(ScenePrat3)

slumTittel = "Den store Slummen"
slum1 = Scene(slumTittel)
slum1.setBeskrivelse("Du går inn i slummen \n Der ser du et spor som går inn til kloakken.")
slum1.setValgTekst("Gå til slummen")
ScenePrat2.leggTilNesteScene(slum1)

slumKamp=Scene(slumTittel,slutt=True)
slumKamp.setValgTekst("Følg sporet inn i kloakken")
slumKamp.setBeskrivelse("Du går inn i kloakken, det er mørkt, fuktig og ganske så uhyggenisk, du liker det svært dårlig... \n\n Du hører en lyd bak deg, og når du snur deg ser du en stor krokkodille. Denne skremmer livet fra deg. Da vi ikke har kamp implementert enda \n \n Game over")
slum1.leggTilNesteScene(slumKamp)

slumHjem=Scene(slumTittel,slutt=True)
slumHjem.setValgTekst("Nei, dette blir for skummelt. Vi kan la byvakten håndtere dette")
slumHjem.setBeskrivelse("Du går hjem, og blir aldri en eventyrer. Slummen spises sakte opp av en kjempekrokodille og byen henfaller i ruiner og fra flyttning")
slum1.leggTilNesteScene(slumHjem)

spill = Spill(sceneStart)
spill.spill()
