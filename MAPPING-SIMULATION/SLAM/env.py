#script para o ambiente virtual
import math
import pygame

class ConstroiAmbiente:                                 #classe para construir ambiente virtual
    def __init__(self, MapDim):                         #construtor da classe
        pygame.init()                                   #inicializa pygame
        self.pointCloud=[]                              #declarar list to store points
        self.MapaExterno = pygame.image.load('map1.png') #carrega o mapa
        self.mapa, self.mapw = MapDim
        self.MapWindomName = 'ROBOT MAPPING SIMULATOR'  #coloca um nome na janela
        pygame.display.set_caption(self.MapWindomName)  #abre a janela
        self.map = pygame.display.set_mode((self.mapa, self.mapw))  #retorna o mapa principal (vazio)
        self.map.blit(self.MapaExterno, (0, 0))                     #desenha mapa externo por cima
        #declaração valores RGB
        self.black = (0, 0, 0)
        self.Blue = (0, 0, 255)
        self.Green = (0, 255, 0)
        self.Red = (255, 0, 0)
        self.white = (255, 255, 255)

    def AD2pos(self, distance, angle, robotPosition):
        x = distance*math.cos(angle) + robotPosition[0]
        y = -distance*math.sin(angle) + robotPosition[1]
        return (int(x), int(y))

    def dataStorage(self, data):
        print(len(self.pointCloud))
        for element in data:
            point = self.AD2pos(element[0], element[1], element[2])
            if point not in self.pointCloud:
                self.pointCloud.append(point)

    def show_sensorData(self):
        self.infomap = self.map.copy()
        for point in self.pointCloud:
            self.infomap.set_at((int(point[0]), int(point[1])), (255, 0, 0))

