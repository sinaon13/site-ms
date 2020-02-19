
text=input("text =")
color2=input("color =")
size=int(input("size ="))
import pygame 

pygame.init() 


if color2=="red":
    color=(255,0,0)
if color2=="blue":
    color=(0,0,255)
if color2=="green":
    color=(0,255,0)
if color2=="yellow":
    color=(255,255,0)

if color2=="black":
    color=(0,0,0)
white=(255,255,255)

X = 400
Y = 400

display_surface = pygame.display.set_mode((X, Y )) 

pygame.display.set_caption('Show Text') 


font = pygame.font.Font('freesansbold.ttf', size) 

text = font.render(text, True, color) 


textRect = text.get_rect() 


textRect.center = (X // 2, Y // 2) 


while True : 

	
	display_surface.fill(white) 

	display_surface.blit(text, textRect) 

	
	for event in pygame.event.get() : 

		
		if event.type == pygame.QUIT : 

			
			pygame.quit() 

			 
			quit() 

		 
		pygame.display.update() 

