# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 16:03:31 2022

@author: Mariana Laneiro, LM 65874, Pavlo Severylov, LM 64424, Filipe Esteves, LM 65622
"""

from labi import labirinto 
exist_lib = False #Boliano que indica a existencia de labirinto
global lab #Variavel do objeto lab
lab = None 
game_state= "SETUP"
HELP = "upload: leitura do labirinto do jogo\nprint: mostrar labirinto do jogo\nrebel: adicionar soldado rebelde\nstart: iniciar o jogo\nmove: mover as personagens\nrebels: listar soldados rebeldes\nstormtroopers: listar stormtroopers\npath: listar caminho percorrido por soldado rebelde\nprisoners: listar rebeldes capturados por stormtrooper\nreset: reiniciar o jogo\nhelp: mostrar os comandos do jogo\nexit: sair do jogo"
      
def upload():
    """
        Realiza a leitura do labirinto atraves das suas dimensões.

        Parameters
        ----------
        None.

        Returns
        -------
        None.
        """
    global exist_lib
    global lab
    l,c = input().split()
    l=int(l)
    c=int(c)
    lista=[]
    for i in range(l):
        lista.append(input())
    if exist_lib:
        print("Maze already defined.")
    else:
        lab= labirinto(l, c, lista)
        exist_lib= True
        print("Maze accepted.")

def display():
    """
        Função que mostra o mapa.

        Parameters
        ----------
        None.

        Returns
        -------
        None.
        """
    global exist_lib
    global lab
    if not exist_lib:
        print("Maze is undefined.")
    else:
        lab.display()
        if game_state != "SETUP":
            print('Points:', lab.get_pontos(), 'Timer:', lab.tempo(), 'Rebels:', lab.rebel_number(), 'Game:', game_state+".")

def rebel():
    """
        Função que após acionar o commando rebel comunica ao labi a imformação para criar um rebelde.

        Parameters
        ----------
        None.

        Returns
        -------
        None.
        """
    global game_state 
    global exist_lib
    global lab
    nome= input()
    l,c = input().split()
    l=int(l)
    c=int(c)
    if not exist_lib:
        print("Maze is undefined.")
    elif game_state != "SETUP":
        print("Game setup has already finished.")
    elif nome in lab.get_nome_lista():
        print('Rebel name already exists.')
    elif not lab.isvalid(l, c):
        print('Invalid maze position.')
    else:
        lab.add_rebels(nome, l, c)
        print("Rebel added.")
           
def ajuda():
    """
        Função que indica as instruções do jogo ao utilizador.

        Parameters
        ----------
        None.

        Returns
        -------
        None.
        """
    print(HELP)
      
def start():
    """
        Função que da inicio ao jogo. 

        Parameters
        ----------
        None.

        Returns
        -------
        None.
        """
    global game_state 
    global exist_lib
    global lab
    if not exist_lib:
        print('Maze is undefined.')
    elif game_state != "SETUP":
        print("Game setup has already finished.")
    elif lab.rebel_number() == 0:
        print('Game needs a rebel.')
    else:
        game_state = 'ON'
        print('Points:', lab.get_pontos(), 'Timer:', lab.tempo(), 'Rebels:', lab.rebel_number(), 'Game:', game_state+".")

def move():
    """
        Função que comunica ao labi o nomivento dos rebeldes, dos stormtroopers atualiza o timer e verifica se o jogo acabou.

        Parameters
        ----------
        None.

        Returns
        -------
        None.
        """
    global exist_lib
    global lab
    move=str(input())
    global game_state
    if game_state != "ON":
        print("Game is not on.")
    else:
        lab.move(move)
        if lab.acabar():
            game_state = "OVER"
        print('Points:', lab.get_pontos(), 'Timer:', lab.tempo(), 'Rebels:', lab.rebel_number(), 'Game:', game_state+".")

def rebels():
    """
        Função que da print das informações dos rebeldes adicionados.

        Parameters
        ----------
        None.

        Returns
        -------
        None.
        """
    global game_state 
    global exist_lib
    global lab
    if not exist_lib:
        print('Maze is undefined.')
    elif len(lab.get_rebeldes()) == 0:
        print("Nothing to list.")
    else:
        print("Rebels:")
        for rebel in lab.get_rebeldes().values():
            print(rebel.get_nome(), rebel.get_coor()[0],rebel.get_coor()[1], rebel.estado(), rebel.get_pontos())

def stormtroopers():
    """
        Função que da print das informações dos stormtroopers.

        Parameters
        ----------
        None.

        Returns
        -------
        None.
        """
    global game_state 
    global exist_lib
    global lab
    if not exist_lib:
        print('Maze is undefined.')
    elif len(lab.get_stormtroopers()) == 0:
        print("Nothing to list.")
    else:
        print("Stormtroopers:")
        for stormtrooper in lab.get_stormtroopers().values():
           print(stormtrooper.get_nome() , stormtrooper.get_posicaoS()[0],stormtrooper.get_posicaoS()[1], stormtrooper.get_estado())

def path():
    """
        Função que apos o comando path ser acionado da imformação do rebel especificado e mostra o seu caminho. 

        Parameters
        ----------
        None.

        Returns
        -------
        None.
        """
    global game_state 
    global exist_lib
    global lab
    name=input()
    if game_state != "ON" and game_state != "OVER":
        print("Game has not started.")
    elif name not in lab.get_rebeldes():
        print("Rebel does not exist.")
    else:
        rebelde = lab.get_rebeldes()[name]
        print("Rebel",name,"has taken", len(rebelde.get_trajecto())-1, "steps and is", rebelde.estado()+":")
        for posicao in rebelde.get_trajecto():
            print(posicao[0],posicao[1])

def prisoners():
    """
        Função que mostra o nome e a posição dos rebeles que foram capturados pelo dado stormtrooper.

        Parameters
        ----------
        None.

        Returns
        -------
        None.
        """
    identificador= input()
    if game_state != "ON" and game_state != "OVER":
        print("Game has not started.")
    elif identificador not in lab.get_stormtroopers():
        print("Stormtrooper does not exist.")
    else:
        stormtrooper = lab.get_stormtroopers()[identificador]
        print("Stormtrooper",identificador, "has captured", len(stormtrooper.get_rc()), "rebels and is", stormtrooper.get_estado()+":")
        for rebelde in stormtrooper.get_rc():
            print(rebelde.get_nome(), rebelde.get_coor()[0],rebelde.get_coor()[1])

def reset():
    """
        Função que renicia o jogo.

        Parameters
        ----------
        None.

        Returns
        -------
        None.
        """
    global game_state 
    global exist_lib
    global lab
    game_state = "SETUP"
    lab = None
    exist_lib = False
    print("Game was reset.")
    
    
def main():
    global game_state
    global exist_lib
    global lab
    command= input()  
    while command != "exit" : 
        
        if command == "help":
            ajuda()
        elif command == "upload":
            upload()
        
        elif command == "print":
            display()
        elif command == "rebel":
            rebel()
        elif command == "start":
            start()
        elif command == "rebels":
            rebels()
        elif command == "stormtroopers":
            stormtroopers()
        elif command == "move":
            move()
        elif command == "path":
            path()
        elif command == "reset":
            reset()
        elif command == "prisoners":
            prisoners()
        command= input()
    print("Exiting.")
main()
 
        
        
    
    
