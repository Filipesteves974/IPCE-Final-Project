# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 14:44:56 2022

@author: Mariana Laneiro, LM 65874, Pavlo Severylov, LM 64424, Filipe Esteves, LM 65622
"""
from rebels import rebeldes
from strom import stormtrooper

class labirinto:  
    """
    Classe que representa o jogo.
    
    Attributes:
        stormtroopers : 
            Dicionario que tem strings ligadas a objetos (stormtroopers).
        lista2 : 
            lista de strings.
        linhas: l
            Um inteiro que representa o numero de linhas do labirinto.
        colunas: c
            Um inteiro que representa o numero de colunas do labirinto.
        mapa: m
            Lista de Lista de Str que representa o mapa do jogo.
        oldmapa: nostorm
            Lista de Lista de Str do jogo sem rebeldes e stormtroopers.
        pontos: 
            Int que representa os pontos. No inicio do jogo é igual a 0 (zero).
        timer: 
            Int que representa o tempo. No inicio do jogo é igual a 0 (zero).
        rebeldes : 
            Dicionario que tem strings ligadas a objetos (rebeldes).
            """
    
    def __init__(self, l, c, m):
        self.stormtroopers={}
        self.lista2=[]
        self.linhas=l
        self.colunas=c
        self.mapa= self.l_s(m)
        self.oldmapa = self.nostorm()
        self.pontos = 0
        self.timer = 0
        self.rebeldes= {}

    def nostorm(self):
        """
        Devolve o mapa sem os stormtroopers.

        Returns
        -------
        list
            Mapa sem os stormtroopers.

        """
        oldmapa = []
        for l in range(self.linhas):
            linha = []
            for c in range(self.colunas):
                if self.mapa[l][c] == "S":
                    linha.append(" ")
                else:
                    linha.append(self.mapa[l][c])
            oldmapa.append(linha)
        return oldmapa
                    
    def l_s(self, m):
        """
        Transforma uma lista de strings em uma lista com listas de caracters. E sempre que encontra um S devolve um stormtrooper.

        Parameters
        ----------
        m: 

        Returns
        -------
        list
            lista que contem listas de caracters.
        """
        lista3=[]
        for l in range(len(m)):
            listan=[]
            for c in range(len(m[l])):
                listan.append(m[l][c])
                if m[l][c] == "S":
                    self.stormtroopers["ST-"+str(len(self.stormtroopers)+1)] = stormtrooper("ST-"+str(len(self.stormtroopers)+1),(l,c))
            lista3.append(listan)
        return lista3
        
    def display(self):
        """
        Da print do mapa do jogo.

        Returns
        -------
        None.

        """
        for i in self.mapa:
            for c in i:
                print(c,end="")
            print()
    
    def add_rebels(self, nome, l, c):
        """
        Adiciona os rebeldes ao mapa do jogo na posição inserida.

        Parameters
        ----------
        l: 
            Linha onde se pretende colocar o rebelde (R).
        c:
            Coluna onde se pretende colocar o rebelde (R).

        Returns
        -------
        None.
        
        """
        posicao=(l,c)
        self.rebeldes[nome] = rebeldes(nome, posicao)
        self.lista2.append(nome)
        self.mapa[l][c]= "R"
    
    def get_rebeldes(self):
        """
        Obtem os rebeldes do dicionario.

        Returns
        -------
        Dicionario
                Devolve um dicionario com os rebeldes.

        """
        return self.rebeldes
    
    def get_stormtroopers(self):
        """
        Obtem os stormtroopers do dicionario.

        Returns
        -------
        Dicionario
                Devolve um dicionario com os stormtroopers.

        """
        return self.stormtroopers
        
    def get_nome_lista(self):
        """
        Devolve a lista dos nomes.

        Returns
        -------
        list
            lista com nomes.
            

        """
        return self.lista2
    
    def isvalid(self, l, c):
        """
        Verifica se a posição esta dentro do mapa e vazia.

        Parameters
        ----------
        l: 
            Linha onde se pretende colocar o rebelde (R).
        c:
            Coluna onde se pretende colocar o rebelde (R).

        Returns
        -------
        bool
            a verificação.
        
        """
        if l >= 0 and l < self.linhas and c >= 0 and c < self.colunas:
            if self.mapa[l][c] ==" ":
                return True
        return False
    
    def rebel_number(self):
        """
        Obtem o numero de rebeldes ativos.

        Returns
        -------
        int
            Inteiro correspondente tamanho da lista dos rebeldes ativos.

        """
        return len(list(filter(lambda x: x.is_ativo(), list(self.rebeldes.values()))))
        
    def get_pontos(self):
        """
        Obtem o numero de pontos no jogo.

        Returns
        -------
        int
            Inteiro correspondente aos pontos.

        """
        return self.pontos
    
    def tempo(self):
        """
        Obtem o tempo do jogo.

        Returns
        -------
        int
            Inteiro correspondente ao tempo.

        """
        return self.timer
    
    def podemexer(self, posicao):
        """
        Verifica se pode mexer

        Parameters
        ----------
        posiçao: 
            Posição inserida.
        
        Returns
        -------
        bool
            a verificação.
        
        """
        (l, c) = posicao
        if l >= 0 and l < self.linhas and c >= 0 and c < self.colunas:
           if self.mapa[l][c] !="#":
               return True
        
        return False
    def move_rebels(self, move):
        """
        Movimenta todos os rebeldes, e resolve os efeitos(pontos,capturas,poção).

        Parameters
        ----------
        move:
            String que contem todos os movimentos de todos os rebeldes.

        Returns
        -------
        None.
        
        """
        rebeldesativos = list(filter(lambda x: x.is_ativo(), list(self.rebeldes.values())))
        move=move.split() #separar string em lista
        for i in range(len(rebeldesativos)):
            rebelde= rebeldesativos[i]
            if self.podemexer(rebelde.rebel_pos(move[i])):
                
                l,c=rebelde.get_coor()
                self.mapa[l][c]= " "
                rebelde.move(move[i])
                l,c=rebelde.get_coor()
                
                if self.mapa[l][c] == "S":
                    storm = self.obterSP((l,c))
                    if rebelde.is_super():
                        storm.captured()
                    else:
                        storm.capt(rebelde)
                        rebelde.capturado()         
                  
                if rebelde.is_ativo():
                    if self.oldmapa[l][c] == ".":
                        self.pontos += 10
                        rebelde.add_pontos()
                        self.oldmapa[l][c] = " "
                    
                    
                    if self.mapa[l][c] == "P":
                        rebelde.supercharge()
                        self.oldmapa[l][c] = " "
                        
                    if rebelde.is_super():
                        self.mapa[l][c]="X"
                    else:
                        self.mapa[l][c]="R"
    
    def mover_stormtrooper(self):
        """
        Obtem o tempo do jogo.

        Returns
        -------
        int
            Inteiro correspondente ao tempo.

        """
        for storm in self.stormtroopers.values():
            l,c = storm.storm_pos()
            if not self.podemexer(storm.storm_pos()) or self.mapa[l][c] == "S":
                d = 0
                while (not self.podemexer(storm.storm_pos()) or self.mapa[l][c] == "S") and d <=6 :
                    storm.dirchange()
                    l,c = storm.storm_pos()
                    d +=1
            if self.podemexer(storm.storm_pos()) and self.mapa[l][c] != "S" and storm.is_ativo():
 
                l,c=storm.get_posicaoS()
                self.mapa[l][c]= self.oldmapa[l][c]
                storm.mover_stormtrooper()
                l,c=storm.get_posicaoS()
                
                
                if self.mapa[l][c] == "R":
                    rebelde = self.obterRP((l,c))
                    storm.capt(rebelde)
                    rebelde.capturado()
                if self.mapa[l][c] == "X":
                    storm.captured()
                
                
                if storm.is_ativo():
                    self.mapa[l][c]="S"
                    
    def move(self,move):
        """
        Movimenta todas as personagens e incrementa o tempo.

        Parameters
        ----------
        move:
            String que contem todos os movimentos de todos os rebeldes.

        Returns
        -------
        None.
        
        """
        self.move_rebels(move)
        self.mover_stormtrooper()
        self.timer +=1

    def acabar(self):
        """
        Verifica se é susposto o jogo acabar.

        Returns
        -------
        bool
            com a indicação se o jogo deve acabar ou não.

        """
        if len(list(filter(lambda x: x.is_ativo(), list(self.rebeldes.values())))) == 0:
            return True
        for l in range(self.linhas):
            for c in range(self.colunas):
                if self.mapa[l][c] == ".":
                    return False
        return True
    
    def obterSP(self, posicao):
        """
        Obtem o stormtrooper na posição inserida. 

        Parameters
        ----------
        posicao:
            Input da posição.

        Returns
        -------
        Stormtrooper se existir na posição inserida.
        None se não existir stormtrooper na posição inserida.
        
        """
        for storm in self.stormtroopers.values():
            if storm.get_posicaoS() == posicao:
                return storm
        return None
    
    def obterRP(self,posicao):
        """
        Obtem o rebelde na posição inserida. 

        Parameters
        ----------
        posicao:
            Input da posição.

        Returns
        -------
        Rebelde se existir na posição inserida.
        None se não existir rebelde na posição inserida.
        
        """
        for rebelde in self.rebeldes.values():
            if rebelde.get_coor() == posicao:
                return rebelde
        
                
            
        