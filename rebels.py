# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 19:06:08 2022

@author: Mariana Laneiro, LM 65874
         Pavlo Severylov, LM 64424
         Filipe Esteves, LM 65622
"""

class rebeldes:
    """
    Classe que representa os rebeldes.
    
    Attributes:
        nome: nome
            String com o nome do rebelde.
        ativo: 
            Bool que verifica se o rebelde esta ativo. No inicio tem o valor True.
        super:
            Bool que verifica se o rebelde esta com poção. No inicio tem o valor False.
        posiçao: posiçao
            Tuplo que contem a posiçao do rebelde.
        pontos: 
            Int que representa os pontos. No inicio do jogo é igual a 0 (zero).
        trajecto: 
            Lista que contem o trajeto dos rebeldes,
            
            """
    def __init__(self, nome, posicao):
        
        self.nome = nome 
        self.ativo = True
        self.super = False
        self.posicao = posicao
        self.pontos = 0
        self.trajecto = [posicao]
    
    def get_trajecto(self):
        """
        Devolve trajeto realizado pelo rebelde.

        Returns
        -------
        list
            lista com as varias posiçoes pelas quais o rebelde passou.

        """
        return self.trajecto
    
    def estado(self):
        """
        Devolve o estado do rebelde no momento.

        Returns
        -------
        Str
            Se o rebelde estiver ativo e com poção a string vai ser SUPERCHARGED, 
            se estiver ativo sem poção a string vai ser ACTIVE. 
            Caso o estado do rebelde não seja ativo a string vai ser CAPTURED  

        """
        if self.ativo:
            if self.super:
                return "SUPERCHARGED"
            return "ACTIVE"
        return "CAPTURED"
    
    def supercharge(self):
        """
        Altera o valor boleano do self.super para True caso o rebelde fique supercharge(com poção).

        Returns
        -------
        None.

        """
        self.super = True
        
    def get_coor(self):
        """
        Obtem a posição (l, c) do rebelde.

        Returns
        -------
        Tuple
            com a linha e coluna que o rebelde se encontra.

        """
        return self.posicao
    
    def is_ativo(self):
        """
        Verifica se o rebelde esta ativo.

        Returns
        -------
        Bool
            Com valor True se o rebelde estiver ativo

        """
        return self.ativo
    
    def is_super(self):
        """
        Verifica se o rebelde esta supercharge(com poção).

        Returns
        -------
        Bool
            Com valor True se o rebelde estiver com poção.

        """
        return self.super
    
    def get_nome(self):
        """
        Obtem o nome do rebelde.

        Returns
        -------
        Str
            Com o nome do rebelde.

        """
        return self.nome
    
    def get_pontos(self):
        """
        Obtem os pontos do rebelde.

        Returns
        -------
        Int
            com o valor dos pontos do rebelde.

        """
        return self.pontos
    
    def add_pontos(self):
        """
        Atualiza os pontos do rebelde, aumentado sempre 10 pontos sempre que ganha pontos.

        Returns
        -------
        None.

        """
        self.pontos += 10
    
    def capturado(self):
        """
        Altera o estado do rebelde quando este é capturado, passando de ativo/True para False.

        Returns
        -------
        None

        """
        self.ativo = False
        
    def move(self,direction):
        """
        Realiza os movimentos do rebelde

        Parameters
        ----------
        direction:
            Str, com a diracao na qual o rebelde se vai movimentar

        Returns
        -------
        None.
        """
        if direction=="U":
            self.posicao= (self.posicao[0]-1, self.posicao[1])
        if direction=="D":
            self.posicao= (self.posicao[0]+1, self.posicao[1])
        if direction=="R":
            self.posicao= (self.posicao[0], self.posicao[1]+1)
        if direction=="L":
            self.posicao= (self.posicao[0], self.posicao[1]-1)
        self.trajecto.append(self.posicao)
   
    def rebel_pos(self, direction):
        """
        Retorna as coordenadas para as quais o rebelde se pretende movimentar
        
        Parameters
        ----------
        direction:
            Str, direcao na qual o rebelde se pretende movimentar

        Returns
        -------
        None.
        """
        if direction == 'U': 
            return (self.posicao[0]-1, self.posicao[1])
        if direction=="D":
            return (self.posicao[0]+1, self.posicao[1])
        if direction=="R":
            return (self.posicao[0], self.posicao[1]+1)
        if direction=="L":
            return (self.posicao[0], self.posicao[1]-1)
        