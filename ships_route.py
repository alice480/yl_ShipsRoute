import os
import sys

import pygame
import requests

map_request = "https://static-maps.yandex.ru/1.x/?ll=30,59.939095&z=10&size=500,450&l=map&pl=30.316404,59.942683,30.307870,59.945532,30.289202,59.947642,30.217877,59.965376,30.160701,59.957950,29.908702,59.884697"
response = requests.get(map_request)

if not response:
    print("Ошибка выполнения запроса:")
    print(map_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)

map_file = "map.png"
with open(map_file, "wb") as file:
    file.write(response.content)

pygame.init()
screen = pygame.display.set_mode((500, 450))
screen.blit(pygame.image.load(map_file), (0, 0))
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()
os.remove(map_file)
