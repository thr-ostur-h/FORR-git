#Þröstur Haraldsson
#25.1.2017

#Dæmi1
tala1=int(input("Sláðu inn tölu"))
tala2=int(input("Sláðu inn aðra tölu"))
samlagning=tala1 + tala2
margfoldun=tala1 * tala2
print("Ef þú leggur tölurnar saman þá færðu")
print(samlagning)
print("Ef þú margfaldar tölurnar saman þá færðu")
print(margfoldun)
print("")

#Dæmi2
fornafn=input("Fornafn?")
eftnafn=input("Eftirnafn?")
print("Halló",fornafn,eftnafn)
print("")

#Dæmi3
text=input("Texti:")
telstor=0
tellitill=0
storlitill=0
telAlla = 0
for c in text:
    if c.islower():
        tellitill=tellitill+1
    if c.isupper():
        telstor=telstor+1
        if (text[telAlla+1].islower()):
            storlitill=storlitill+1
    telAlla += 1
print("Það eru",telstor,"stórir stafir")
print("það eru",tellitill,"litlir stafir")
print("Það eru",storlitill,"litlir stafir beint á eftir stórum")