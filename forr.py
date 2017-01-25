#Þröstur Haraldsson
#25.1.2017

#Dæmi1
#Notandi velur tölu sem verður notuð í þessu dæmi
tala1=int(input("Sláðu inn tölu"))
#Notandi velur aðra tölu sem verður líka notuð í þessu dæmi
tala2=int(input("Sláðu inn aðra tölu"))
#Hér er verið að leggja saman tölurnar sem notandinn valdi
samlagning=tala1 + tala2
#Hér er verið að margfalda tölurnar sem notandinn valdi
margfoldun=tala1 * tala2
#Hér er prentaður texti á skjáinn
print("Ef þú leggur tölurnar saman þá færðu")
#Hér er prentuð útkoman á samlagninguni
print(samlagning)
#Hér er prentaður texti á skjáinn
print("Ef þú margfaldar tölurnar saman þá færðu")
#Hér er prentuð útkoman á margföldunini
print(margfoldun)
#Þessi prentun gerir bil á milli dæma og gerir þetta aðeins snirtilegra fyrir notanda
print("")

#Dæmi2
#Hér skrifar notandi fornafn
fornafn=input("Fornafn?")
#Hér skrifar notandi eftirnafn
eftnafn=input("Eftirnafn?")
#Hér er heilsað notanda með fornafninu og eftirnafninu sem hann valdi
print("Halló",fornafn,eftnafn)
#Þessi prentun gerir bil á milli dæma og gerir þetta aðeins snirtilegra fyrir notanda
print("")

#Dæmi3
#Hér fær notandi að skrifa texta
text=input("Texti:")
#Þetta er til að telja stóru stafina
telstor=0
#Þetta er til að telja litlu stafina
tellitill=0
#Þetta er til að telja hve oft það kemur lítill stafur á eftir stórum
storlitill=0
#Þetta er til að telja hvern einasta staf í textanum, ég þarf þetta til þess að telja litlu stafina sem koma á eftir stórum
telAlla = 0
#Hér er farið í gegnum textann staf fyrir staf
for c in text:
    #fyrir hvern staf í textanum bætist 1 við teljarann
    telAlla += 1
    #ef einhver stafur í textanum er lítill þá fer hann hér inn
    if c.islower():
        #fyrir hvern staf sem kemur hér inn bætist 1 við teljarann
        tellitill=tellitill+1
    #Ef einhver stafur í textanum er lítill þá fer hann hér inn
    if c.isupper():
        #fyrir hvern staf sem kemur hér inn bætist 1 við teljarann
        telstor=telstor+1
        #ef það er lítill stafur á eftir þessum stóra sem kom hér í gegn þá fer sá litli hér í gegn
        if (text[telAlla+1].islower()):
            #fyrir hvern staf sem kemur hér inn bætist 1 við teljarann
            storlitill=storlitill+1
#Hér er prentað út hve margir stórir stafir voru í textanum
print("Það eru",telstor,"stórir stafir")
#Hér er prentað út hve margir litlir stafir voru í textanum
print("það eru",tellitill,"litlir stafir")
#Hér er prentað út hve margir litlir stafir komu beint á eftir stórum staf
print("Það eru",storlitill,"litlir stafir beint á eftir stórum")