from pygame import mixer
from os import system
from time import sleep
import time
mixer.init()
mixer.music.load('Exercicio#021.mp3')
mixer.music.set_volume(1)
mixer.music.play()
mixer.fadeout(2)
song = f'0:00'
m = s = 0
while(mixer.music.get_busy()):
	system('cls')
	song = f'{m}:{s:0>2}'
	print(song)
	s += 1
	if s == 60:
		m += 1 
		s = 0
	sleep(1)