voti={"Giuseppe Gullo":[("Matematica", 9, 0),("Italiano",7,3), ("Inglese",7.5,4),("Storia",7.5,4),("Geografia",5,7)],
      "Antonio Barbera":[("Matematica", 8, 1),("Italiano",6,1), ("Inglese",9.5,0),("Storia",8,2),("Geografia",8,1)],
      "Nicola Spina":[("Matematica", 7.5, 2),("Italiano",6,2), ("Inglese",4,3),("Storia",8.5,2),("Geografia",8,2)]}


voti["Albert Einstein"]=[("Matematica", 10, 0),("Italiano",10,0), ("Inglese",10,0),("Storia",10,0),("Geografia",10,0)]



voti["Giuseppe Gullo"].append(("Fisica",9.5,0))
voti["Antonio Barbera"].append(("Fisica",8,1))
voti["Nicola Spina"].append(("Fisica",8,3))
voti["Albert Einstein"].append(("Fisica",10,0))


for studente in voti.keys():
    if(studente=="Giuseppe Gullo"):
        for tupla in voti["Giuseppe Gullo"]:
            for materia in tupla:
                if(materia=="Matematica"):
                    print("Tupla Matematica di Giuseppe Gullo",tupla)
            
            
for studente in voti.keys():
    if(studente=="Nicola Spina"):
        for tupla in voti["Nicola Spina"]:
            for materia in tupla:
                if(materia=="Inglese"):
                    print("Tupla inglese di Nicola Spina",tupla)
        

for studente in voti.keys():
    if(studente=="Antonio Barbera"):
        for tupla in voti["Antonio Barbera"]:
            for materia in tupla:
                if(materia=="Geografia"):
                    for voto in materia:
                        print(voto)
                        print("Voto geografia Antonio Barbera",voto)