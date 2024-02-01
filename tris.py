board = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
mossa=""

def printBoard(board):
    cont=0
    for values in board.values():
        print('|'+values+'|',end="")
        cont+=1
        if(cont==3):
            print()
            print("--------")
            cont=0
    return ""        

def controllaPosizione(board,mossa):
  if(mossa in board.keys()):
      return True
  else:
      return False
      

def controllaVittoria(board):
    pareggio=True
    if(board['top-L']==board['mid-M']==board['low-R']=='X' and board['top-L']!=''):
        print("Tris diagonale")
        pareggio=True
        return "Vittoria"
    if(board['top-R']==board['mid-M']==board['low-L']=='X' and board['top-R']!=''):
        print("Tris diagonale")
        pareggio=True
        return "Vittoria"
    if(board['top-L']==board['mid-L']==board['low-L']=='X' and board['top-L']!=''):
        print("Tris verticale a sinistra")
        pareggio=True
        return "Vittoria"
    if(board['top-M']==board['mid-M']==board['low-M']=='X' and board['top-M']!=''):
        print("Tris verticale al centro")
        pareggio=True
        return "Vittoria"
    if(board['top-R']==board['mid-R']==board['low-R']=='X' and board['top-R']!=''):
        print("Tris verticale a destra")
        pareggio=True
        return "Vittoria"
    if(board['top-L']==board['top-M']==board['top-R']=='X' and board['top-L']!=''):
        print("Tris orizzontale prima riga")
        pareggio=True
        return "Vittoria"
    if(board['mid-L']==board['mid-M']==board['mid-R']=='X' and board['mid-L']!=''):
        print("Tris orizzontale seconda riga")
        pareggio=True
        return "Vittoria"
    if(board['low-L']==board['low-M']==board['low-R']=='X' and board['low-L']!=''):
        print("Tris orizzontale terza riga")
        pareggio=True
        return "Vittoria"
    else:
        pareggio=False
        return "Pareggio"
def aggiungiSegno(board,turn):
    if(mossa in board.keys()):
        board[mossa]=turn
        return board

def cambiaTurno(turn):
    if(turn=='X'):
        return 'O'
    else:
        return 'X'


posizione=controllaPosizione(board,mossa)
turn = 'X'
for i in range (9):
    print("scelte disponibili:",board.keys())
    print(printBoard(board))
    mossa=input("Inserisci una posizione:")
    while (controllaPosizione(board,mossa)==False):
        print("Posizione occupata o inesistente")
        mossa=input("Inserisci una posizione:")
        if(controllaPosizione(board,mossa)==True):
            break
    print(aggiungiSegno(board,turn))
    print(printBoard(board))
    print(controllaVittoria(board))
    turn=cambiaTurno(turn)
    
    