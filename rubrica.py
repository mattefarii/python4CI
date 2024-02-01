import pprint
pp=pprint.PrettyPrinter(indent=4)

rubrica={"Rossi Mario":["123","Via adige","RossiMario@gmail.com"],
         "Bianchi Matteo":["456","Via Milano","BianchiMatteo@gmail.com"],
         "Viola Giorgia":["789","Via MOonza","ViolaGiorgia@gmail.com"]}


#def leggiDati(rubrica):
    
        
    #return [nome,cognome,tel,indirizzo,email]



def leggiChiave(rubrica):
  nomeTrov=""
  if(nome in rubrica.keys()):
      nomeTrov=nome
  return [nome,cognome]

def popola():
  
  return rubrica

def aggiungi(rubrica):
    cognome=input("Inserisci il cognome:")
    while len(cognome)==0:
        cognome=input("Inserisci il cognome:")
    
    nome=input("Inserisci il nome:")
    while len(nome)==0:
        nome=input("Inserisci il nome:")
      
    tel=input("Inserisci il numero di telefono:")
    while len(tel)!=10:
        tel=input("Inserisci il numero di telefono:")
    
    indirizzo=input("Inserisci l'indirizzo:")
    while len(indirizzo)==0:
        indirizzo=input("Inserisci l'indirizzo:")
    
    email=input("Inserisci l'email:")
    while len(email)==0:
        email=input("Inserisci l'email:")
    rubrica[cognome+nome]=[tel,indirizzo,email]
    
    return(rubrica)

def elimina(rubrica):
    daEliminareC=input("cognome:")
    daEliminareN=input("Nome:")
    #trovati=rubrica.get((daEliminareC,daEliminareN))
    if(daEliminareC==daEliminareN in rubrica.values()):
        del rubrica[daEliminareN]
    else:
        print("Inesistente")
       
    return rubrica

def cerca(rubrica):
  cognome=input("Inserisci il cognome da cercare:")
  nome=input("Inserisci il nome da cercare:")
  for i in rubrica.keys():
    if(i==cognome+' '+nome):
     print(rubrica[cognome+' '+nome])
  return ""

def mostra_tutti(rubrica):
  return rubrica

def modifica(rubrica):
    cognome=input("Inserisci il cognome:")
    nome=input("Inserisci il nome")
    for i in rubrica.keys():
      if(i==cognome+' '+nome):
            return rubrica[daModificare]
          
while True:
  print('0) Esci')
  print('1) Popola')
  print('2) Aggiungi')
  print('3) Elimina')
  print('4) Cerca')
  print('5) Mostra tutti')
  print('6) Modifica')
  scelta=int(input('Scegli :'))
  if scelta==0:
    break
  elif scelta==1:
    print(popola())
  elif scelta==2:
    print("\n")
    print(aggiungi(rubrica))
  elif scelta==3:
    print("\n")
    print(elimina(rubrica))
  elif scelta==4:
    print(cerca(rubrica))
  elif scelta==5:
    print(mostra_tutti(rubrica))
  elif scelta==6:
   print(modifica(rubrica))
    
def inserisci_contatto(rubrica):
    nuovoContatto=input("Inserisci il nome del nuovo contatto:")
    nuovoNumero=int(input("Inserisci il numero di telefono:"))
    rurbrica[nuovocontatto]=nuovoNumero
    
    return rubrica