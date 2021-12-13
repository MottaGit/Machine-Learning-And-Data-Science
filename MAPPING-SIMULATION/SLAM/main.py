# SLAM - Simultanous Localization And Mapping.
# Usado para ambientes em que um robô móvel está se movendo em um ambiente desconhecido e tentando construir um mapa de seus arredores.
# Este algoritmo lê um mapa (planta de uma casa) e usa o cursor do mouse como o robô que está navegando pelo ambiente, e mapeando a área com os sensores simulados.
# Simula o LIDAR sensor (Laser Detection and Ranging) tento como origem o cursor do mouse.
# A próxima etapa desta aplicação seria, seria extrair os dados armazenados pelo sensor LIDAR e determinar a locação deste robô.

from SLAM import env, sensors
import pygame
import math

ambiente = env.ConstroiAmbiente((1200, 600))
ambiente.originalMap = ambiente.map.copy()
laser = sensors.LaserSensor(200, ambiente.originalMap, ruido=(0.5, 0.01))
ambiente.map.fill((0, 0, 0))
ambiente.infomap = ambiente.map.copy()

run = True          #variavel auxiliar execução do jogo

while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:   #verifica evento de finalização do jogo
            run = False
        if pygame.mouse.get_focused():
            sensorON = True
        elif not pygame.mouse.get_focused():
            sensorON = False
    if sensorON:
        position = pygame.mouse.get_pos()
        laser.position = position
        sensor_data = laser.sense_obstaculos()
        ambiente.dataStorage(sensor_data)
        ambiente.show_sensorData()

    ambiente.map.blit(ambiente.infomap, (0, 0))
    pygame.display.update()     #atualiza quaisquer mudanças no mapa
