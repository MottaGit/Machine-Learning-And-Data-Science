import pygame
import math
import numpy as np

#função para adicionar ruido ao sensor
#adiciona o ruido selecionando um valor aleatório das proximidades do valor real
#pega o valor da distancia medida como média, e seleciona o valor aleatório a partir da distribuição gaussiana, considerando sigma a variância
def add_ruido(distancia, angulo, sigma):
    media = np.array([distancia, angulo])
    covariancia = np.diag(sigma**2)
    distancia, angulo = np.random.multivariate_normal(media, covariancia)
    distancia = max(distancia, 0)
    angulo = max(angulo, 0)
    return [distancia, angulo]

class LaserSensor:                              #simula o laser do sensor de distancia
    def __init__(self, Range, map, ruido):   #3 argumentos para compor o sensor
        self.Range=Range
        self.speed = 4      #velocidade para definir ciclos do sensor
        self.sigma = np.array([ruido[0], ruido[1]])
        self.position = (0, 0)
        self.map = map
        self.W, self.H = pygame.display.get_surface().get_size()
        self.senseObstaculos=[]

    def distancia(self, ObstaculoPosition):
        px = (ObstaculoPosition[0]-self.position[0])**2
        py = (ObstaculoPosition[1]-self.position[1])**2
        return math.sqrt(px + py)

    def sense_obstaculos(self):
        data=[]
        x1, y1 = self.position[0], self.position[1]
        for angle in np.linspace(0, 2*math.pi, 60, False):
            x2, y2 = (x1 + self.Range*math.cos(angle), y1 - self.Range*math.sin(angle))
            for i in range(0, 100):
                u = i/100
                x = int(x2*u + x1*(1-u))
                y = int(y2*u + y1*(1-u))
                if 0 < x < self.W and 0 < y < self.H:
                    color = self.map.get_at((x, y))
                    if(color[0], color[1], color[2]) == (0, 0 ,0):  #se identificou obstaculo
                        distancia = self.distancia((x, y))
                        output = add_ruido(distancia, angle, self.sigma)
                        output.append(self.position)
                        #armazenar as medições
                        data.append(output)
                        break
        if len(data) > 0:
            return data
        else:
            return False

