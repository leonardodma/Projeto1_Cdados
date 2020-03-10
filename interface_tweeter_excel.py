import pygame
import pygame.freetype
import time
import pandas as pd

pygame.init()
pygame.freetype.init()

SIZE = WIDTH, HEIGHT = (1024-100, 720-100)
FPS = 30
screen = pygame.display.set_mode(SIZE, pygame.RESIZABLE)
clock = pygame.time.Clock()

def exibir(surface, text, pos, font, color=pygame.Color('black')):
    words = [word.split(' ') for word in text.splitlines()] 
    space = font.size
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface, word_rect = font.render(word, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]
                y += word_height  
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  
        y += word_height  

df = pd.read_excel("Coke.xlsx")
tweets = df['Treinamento'].tolist()

font = pygame.freetype.Font("OpenSansEmoji.ttf", 30)

contador = 0
lista_classificacao = []
done = False

while not done:

    for event in pygame.event.get():

        screen.fill(pygame.Color('white'))

        try:
            exibir(screen, tweets[contador], (20, 20), font)
            pygame.display.flip()
        except:
            done = True
    
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_RIGHT:
                lista_classificacao.append(1)
                try:
                    exibir(screen, tweets[contador], (20, 20), font)
                    pygame.display.flip()
                    print(lista_classificacao)
                    contador = contador + 1
                except: 
                    pass

            elif event.key == pygame.K_LEFT:
                lista_classificacao.append(2)
                try:
                    exibir(screen, tweets[contador], (20, 20), font)
                    pygame.display.flip()
                    print(lista_classificacao)
                    contador = contador + 1
                except:
                    pass

            elif event.key == pygame.K_DOWN:
                lista_classificacao.append(3)
                try:
                    exibir(screen, tweets[contador], (20, 20), font)
                    pygame.display.flip()
                    print(lista_classificacao)
                    contador = contador + 1
                except: 
                    pass

            elif event.key == pygame.K_SPACE:
                screen.fill(pygame.Color('white'))
                contador = contador - 1
                exibir(screen, tweets[contador], (20, 20), font)
                pygame.display.flip()
                try:
                    lista_classificacao.pop()
                    print(lista_classificacao)
                except:
                    screen.fill(pygame.Color('white'))
                    exibir(screen, "Fim", (20, 20), font)
                    pygame.display.flip()
                    contador = contador + 1
                    time.sleep(0.5)

df["Etiquetas"] = lista_classificacao

df.to_excel("tabela_etiquetada.xlsx", index=False)
                
exibir(screen, "Fim da etiquetagem!", (20, 20), font)
pygame.display.flip()
time.sleep(2)