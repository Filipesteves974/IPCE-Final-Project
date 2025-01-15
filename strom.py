# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 19:01:21 2022

@author: Mariana Laneiro, LM 65874, Pavlo Severylov, LM 64424, Filipe Esteves, LM 65622
"""
#i_d=identificador unico
#estado= capturado ou activo 
#rc= rebeldes

class stormtrooper:
    """
    Classe que representa um stormtrooper.
    
    Attributes:
        i_d: i_d
            String com o i_d do stormtrooper.
        estado: 
            Bool que verifica se o stormtrooper esta ativo. No inicio tem o valor True.
        rc: 
            Lista que contém rebeldes capturados pelo stormtrooper.
        direcao: 
            String com a direcao atual do stormtrooper.
        posiçao: posiçao
            Tuplo que contem a posiçao do rebelde.
            """
    def __init__(self, i_d, posicao):
        self.i_d= i_d
        self.estado= True
        self.rc=[]
        self.direcao= "U"
        self.posicao= posicao 
        
    def get_posicaoS(self):
        """
        Obtem a posição (l, c) do stormtrooper.

        Returns
        -------
        Tuple
            com a linha e coluna que o stormtrooper se encontra.

        """
        return self.posicao
    
    def is_ativo(self):
        """
        Verifica se o stormtrooper esta ativo.

        Returns
        -------
        Bool
            Com valor True se o stormtrooper estiver ativo

        """
        return self.estado
    
    def get_nome(self):
        """
        Obtem o nome do stormtrooper.

        Returns
        -------
        Str
            Com o i_d do stormtrooper.

        """
        return self.i_d
    
    def get_estado(self):
        """
        Devolve o estado do stormtrooper no momento.

        Returns
        -------
        Str
            Se o stormtrooper estiver ativo a string vai ser ACTIVE, 
            Caso o estado do stormtrooper não seja ativo a string vai ser CAPTURED.

        """
        if self.estado:
            return "ACTIVE"
        return "CAPTURED"
    
    def get_rc(self):
        """
        Retorna a lista de rebeldes capturados por este stormtrooper

        Returns
        -------
        List
            Lista com os Rebeldes capturados por este stormtrooper
        """
        return self.rc
    
    def capt(self,rebel):
        """
        stormtrooper captura o rebel, adicionando-o á lista de rebeldes capturados

        Returns
        -------
        None.
        """
        self.rc.append(rebel)
        
    def captured(self):
        """
        Altera o estado do stormtrooper quando este é capturado, passando de ativo/True para False.

        Returns
        -------
        None

        """
        self.estado = False
    
    def mover_stormtrooper(self):
        """
        Realiza os movimentos do stormtrooper

        Returns
        -------
        None.
        """
        direction = self.direcao
        if direction=="U":
            self.posicao= (self.posicao[0]-1, self.posicao[1])
        if direction=="D":
            self.posicao= (self.posicao[0]+1, self.posicao[1])
        if direction=="R":
            self.posicao= (self.posicao[0], self.posicao[1]+1)
        if direction=="L":
            self.posicao= (self.posicao[0], self.posicao[1]-1)
            
    def storm_pos(self):
        """
        Retorna as coordenadas para as quais o stormtrooper se pretende movimentar

        Returns
        -------
        None.
        """
        direction = self.direcao
        if direction == 'U': 
            return (self.posicao[0]-1, self.posicao[1])
        if direction=="D":
            return (self.posicao[0]+1, self.posicao[1])
        if direction=="R":
            return (self.posicao[0], self.posicao[1]+1)
        if direction=="L":
            return (self.posicao[0], self.posicao[1]-1)
        
    def dirchange(self):
        """
        Muda a direcao na qual o stormtrooper se esta a movimentar

        Returns
        -------
        None.
        """
        if self.direcao == "U":
            self.direcao = "D"
        elif self.direcao == "D":
            self.direcao = "L"
        elif self.direcao == "L":
            self.direcao = "R"
        elif self.direcao == "R":
            self.direcao = "U"
        
                