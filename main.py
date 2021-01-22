import sys, copy, os, random, time, subprocess
from datetime import datetime

try:
	import pygame
except:
	subprocess.call([sys.executable, "-m", "pip", "install", "pygame"])
	import pygame


sys.setrecursionlimit(100000)

#dimension of app
WIDTH = 800
HEIGHT = 804
CANVAS = (600, 804)
TILESIZE = 12

#colors ==============
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

color1 = (0,0,0)
color2 = (255,255,255)
color3 = (70, 70, 70)
color4 = (91, 96, 95)
color5 = (161,161,148)

color6 = (255,191,45)
color7 = (245,134,30)
color8 = (172, 60, 90)
color9 = (137, 33, 67)
color10 = (71,43,93)

color11 = (2,21,26)
color12 = (4,58,71)
color13 = (8, 120, 145)
color14 = (145, 170, 157)
color15 = (180,30,20)

color16 = (61,57,56)
color17 = (219,95,4)
color18 = (239, 239, 239)
color19 = (113, 173, 35)
color20 = (56,124,43)

color21 = (236,188,180)
color22 = (209, 163, 164)
color23 = (195,149,130)
color24 = (161,102,94)
color25 = (80,51,53)

color26 = (216,152,69)
color27 = (245, 223, 171)
color28 = (88,181,171)
color29 = (133,96,88)
color30 = (212,88,71)

color31 = (255, 0, 0)
color32 = (0, 255, 0)
color33 = (0, 0, 255)
color34 = (255, 255, 0)
color35 = (255, 0, 255)

color36 = (0, 255, 255)
color37 = (184, 225, 242)
color38 = (69, 4, 20)
color39 = (57, 0, 14)
color40 = (98, 21, 254)

#initialize pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
canvas = pygame.Surface(CANVAS)
canvas.fill(WHITE)
pygame.display.set_caption("PIXEL PAINT")
clock = pygame.time.Clock()


current_path = os.path.dirname(os.path.abspath(__file__))


# images ======================================
primary_color_rect = pygame.Rect(640, 90, 50, 50)
secondary_color_rect = pygame.Rect(710, 90, 50, 50)

brush_image= pygame.image.load(r'images\brush.png').convert()
brush_rect = brush_image.get_rect()
brush_rect.x, brush_rect.y = 626, 510

fill_tool_image = pygame.image.load(r'images\fill.png').convert()
fill_tool_rect = fill_tool_image.get_rect()
fill_tool_rect.x, fill_tool_rect.y = 680, 510

eraser_image = pygame.image.load(r'images\eraser.png').convert()
eraser_rect = eraser_image .get_rect()
eraser_rect.x, eraser_rect.y = 734, 510

pick_tool_image = pygame.image.load(r'images\picker.png').convert()
pick_tool_rect = pick_tool_image.get_rect()
pick_tool_rect.x, pick_tool_rect.y = 626, 564

dither_tool_image = pygame.image.load(r'images\dither.png').convert()
dither_tool_rect = dither_tool_image.get_rect()
dither_tool_rect.x, dither_tool_rect.y = 680, 564

darken_tool_image = pygame.image.load(r'images\darken.png').convert()
darken_tool_rect = darken_tool_image.get_rect()
darken_tool_rect.x, darken_tool_rect.y = 734, 564

#color palette========================
palette_rect = pygame.Rect(610, 160, 180, 290)
color1_rect = pygame.Rect(618, 170, 25, 25)
color2_rect = pygame.Rect(653, 170, 25, 25)
color3_rect = pygame.Rect(688, 170, 25, 25)
color4_rect = pygame.Rect(723, 170, 25, 25)
color5_rect = pygame.Rect(758, 170, 25, 25)

color6_rect = pygame.Rect(618, 205, 25, 25)
color7_rect = pygame.Rect(653, 205, 25, 25)
color8_rect = pygame.Rect(688, 205, 25, 25)
color9_rect = pygame.Rect(723, 205, 25, 25)
color10_rect = pygame.Rect(758, 205, 25, 25)

color11_rect = pygame.Rect(618, 240, 25, 25)
color12_rect = pygame.Rect(653, 240, 25, 25)
color13_rect = pygame.Rect(688, 240, 25, 25)
color14_rect = pygame.Rect(723, 240, 25, 25)
color15_rect = pygame.Rect(758, 240, 25, 25)

color16_rect = pygame.Rect(618, 275, 25, 25)
color17_rect = pygame.Rect(653, 275, 25, 25)
color18_rect = pygame.Rect(688, 275, 25, 25)
color19_rect = pygame.Rect(723, 275, 25, 25)
color20_rect = pygame.Rect(758, 275, 25, 25)

color21_rect = pygame.Rect(618, 310, 25, 25)
color22_rect = pygame.Rect(653, 310, 25, 25)
color23_rect = pygame.Rect(688, 310, 25, 25)
color24_rect = pygame.Rect(723, 310, 25, 25)
color25_rect = pygame.Rect(758, 310, 25, 25)

color26_rect = pygame.Rect(618, 345, 25, 25)
color27_rect = pygame.Rect(653, 345, 25, 25)
color28_rect = pygame.Rect(688, 345, 25, 25)
color29_rect = pygame.Rect(723, 345, 25, 25)
color30_rect = pygame.Rect(758, 345, 25, 25)

color31_rect = pygame.Rect(618, 380, 25, 25)
color32_rect = pygame.Rect(653, 380, 25, 25)
color33_rect = pygame.Rect(688, 380, 25, 25)
color34_rect = pygame.Rect(723, 380, 25, 25)
color35_rect = pygame.Rect(758, 380, 25, 25)

color36_rect = pygame.Rect(618, 415, 25, 25)
color37_rect = pygame.Rect(653, 415, 25, 25)
color38_rect = pygame.Rect(688, 415, 25, 25)
color39_rect = pygame.Rect(723, 415, 25, 25)
color40_rect = pygame.Rect(758, 415, 25, 25)

new_rect = pygame.Rect(640, 650, 120, 40)
save_rect = pygame.Rect(640, 700, 120, 40)
load_rect = pygame.Rect(640, 750, 120, 40)


def make_grid():
	#make white grid
	_grid = []
	for i in range(0, CANVAS[0], TILESIZE):
		row = []
		for j in range(0, CANVAS[1], TILESIZE):
			row.append(WHITE)

		_grid.append(row)

	return _grid

def text(message, screen, color, size, x, y, center = None):
	font = pygame.font.SysFont("Calibri", size)
	text = font.render(message, True, color)
	if center:
		screen.blit(text,( x - text.get_width() // 2, y - text.get_height() // 2))
	else:
		screen.blit(text, (x, y))

def fill(grid, color, pos):
	#flood fill
	i, j = pos
	try:
		prev_color = grid[i][j]
		if color == prev_color:
			return
		grid[i][j] = color

		if i > 0:
			if grid[i-1][j] == prev_color:
				fill(grid, color , (i-1, j))

		if i < len(grid) - 1:
			if grid[i+1][j] == prev_color:
				fill(grid, color , (i+1, j))

		if j > 0:
			if grid[i][j-1] == prev_color:
				fill(grid, color , (i, j-1))

		if j < len(grid[0]) - 1:
			if grid[i][j+1] == prev_color:
				fill(grid, color , (i, j+1))
	except:
		pass

def dither(grid, color, pos):
	i, j = pos
	if (i + j) % 2 == 0:
		grid[i][j] = color

def darken(last_grid, grid, pos):
	i, j = pos
	color = last_grid[i][j]
	color = (int(color[0]*0.95), int(color[1]*0.95), int(color[2]*0.95))
	grid[i][j] = color


def brush(grid, size, color, pos):
	#brush paint
	mx, my = pos

	if size == 1:
		try:
			grid[mx][my] = color
		except:
			pass

	if size == 2:
		try:
			grid[mx+1][my] = color
			grid[mx][my] = color

			if my > 0:
				grid[mx+1][my-1] = color
				grid[mx][my-1] = color
		except:
			pass

	if size == 3:
		try:
			grid[mx][my] = color
			grid[mx+1][my] = color
			grid[mx+1][my+1] = color
			grid[mx][my+1] = color

			if mx > 0:
				grid[mx-1][my] = color
				grid[mx-1][my+1] = color

				if my > 0:
					grid[mx-1][my-1] = color

			if my > 0:
				grid[mx][my-1] = color
				grid[mx+1][my-1] = color

		except:
			pass

def set_slider(sliders, color):
	#set sliders potions cullectively
	for i in range(0, len(sliders)):
		sliders[i].set_pos(color[i])

def save(name):
	pygame.image.save(canvas, name)

class Slider:
	#SLider class
	def __init__(self, pos, length, min, max):
		self.length = length
		self.pos = pos
		self.spos = pos
		self.min = min
		self.max = max
		self.gap = (max - min) / length

	def draw(self, screen):
		pygame.draw.rect(screen, (100, 100, 100), (self.spos[0], self.spos[1], self.length , 5))

		pygame.draw.rect(screen, (255, 255, 255), (self.pos[0] , self.pos[1] - 3, 6 , 10))

		self.rect =  pygame.Rect(self.spos[0], self.spos[1] - 5, self.length + 1, 10)
		self.update()

	def update(self):
		if pygame.mouse.get_pressed()[0]:
			if self.rect.collidepoint(pygame.mouse.get_pos()):
				self.pos = (pygame.mouse.get_pos()[0], self.pos[1])

	def get_value(self):
		x = abs(self.spos[0] - self.pos[0])
		value = self.min + (x  * self.gap)
		return value

	def set_pos(self, value):
		self.pos = (((value - self.min) / self.gap) + self.spos[0], self.pos[1])


class load_screen():
	#loading screen =========================
	def __init__(self, super):
		self.run = True
		self.super = super
		self.items = [i for i in os.listdir(current_path) if '.png' in i ]
		self.rects = []
		self.select = None
		self.load_rect = pygame.Rect(640, 660, 120, 40)
		self.cancel_rect = pygame.Rect(640, 710, 120, 40)

		for i in range(len(self.items)):
			self.rects.append([pygame.Rect(100, 50*i+30, 400, 35), self.items[i], i])

	def update(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.super.running = False
				self.run = False

			if event.type == pygame.MOUSEBUTTONDOWN:
				if pygame.mouse.get_pressed()[0]:
					for rect in self.rects:
						if rect[0].collidepoint(pygame.mouse.get_pos()):
							self.select = rect

					if self.cancel_rect.collidepoint(pygame.mouse.get_pos()):
						self.run = False

					elif self.load_rect.collidepoint(pygame.mouse.get_pos()):
						self.super.name = self.select[1]
						self.load()
						self.run = False

	def draw(self):
		screen.fill((180,180,180))
		pygame.draw.rect(screen, WHITE, (0, 0, 600, 810))

		if self.select:
			pygame.draw.rect(screen, (130, 130, 130), (self.select[0].x + 2, self.select[0].y + 2, 402, 37))

		for rect in self.rects:
			pygame.draw.rect(screen, (200,200,200), rect[0])
			text(rect[1], screen, BLACK, 28, rect[0].x + 200, rect[0].y + 18 , True)

		pygame.draw.rect(screen , (210, 210, 210), self.load_rect)
		text('Load', screen, BLACK, 35, self.load_rect.x + 60, self.load_rect.y + 20, True)
		pygame.draw.rect(screen, (209, 26, 42), self.cancel_rect)
		text('Cancel', screen, BLACK, 35, self.cancel_rect.x + 60, self.cancel_rect.y + 20, True)

		pygame.display.update()

	def load(self):
		if self.select:
			image = pygame.image.load(self.select[1])
			_grid = []
			for i in range(0, CANVAS[0], TILESIZE):
				row = []
				for j in range(0, CANVAS[1], TILESIZE):
					row.append(image.get_at((i, j)))

				_grid.append(row)

			self.super.grid = _grid


class main():
	#main app
	def __init__(self):
		self.running = True
		self.name = str(datetime.now().strftime("%Y_%m_%d%H%M%S")) + '.png'
		self.grid = make_grid()
		self.drawing = False
		self.tooltype = 'brush'
		self.brushsize = 1
		self.primary_color = (0, 0 ,0)
		self.secondary_color = (255, 255, 255)
		self.selected_color = True
		self.last_drawing = [copy.deepcopy(self.grid)]

		self.slider1 = Slider((625, 20), 155, 0, 255 )
		self.slider2 = Slider((625, 40), 155, 0, 255 )
		self.slider3 = Slider((625, 60), 155, 0, 255 )
		self.slider_brushsize = Slider((675, 480), 105, 1, 3.4)


	def update(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.running = False

			if event.type == pygame.MOUSEBUTTONDOWN:
				self.last_drawing.append(copy.deepcopy(self.grid))
				if canvas.get_rect().collidepoint(pygame.mouse.get_pos()):
					self.drawing = True
					if self.tooltype == 'fill':
						if pygame.mouse.get_pressed()[0]:
							fill(self.grid, self.primary_color, (pygame.mouse.get_pos()[0] // TILESIZE, pygame.mouse.get_pos()[1] // TILESIZE))
						if pygame.mouse.get_pressed()[2]:
							fill(self.grid, self.secondary_color, (pygame.mouse.get_pos()[0] // TILESIZE, pygame.mouse.get_pos()[1] // TILESIZE))

					if self.tooltype == 'picktool':
						if pygame.mouse.get_pressed()[0]:
							_color = canvas.get_at((pygame.mouse.get_pos()))
							set_slider([self.slider1, self.slider2, self.slider3],_color)

				#check for collision ================
				if primary_color_rect.collidepoint(pygame.mouse.get_pos()):
					set_slider([self.slider1, self.slider2, self.slider3], self.primary_color)
					self.selected_color = True

				elif secondary_color_rect.collidepoint(pygame.mouse.get_pos()):
					set_slider([self.slider1, self.slider2, self.slider3], self.secondary_color)
					self.selected_color = False

				elif new_rect.collidepoint(pygame.mouse.get_pos()):
					# to make a new canvas
					self.name = str(datetime.now().strftime("%Y_%m_%d%H%M%S")) + '.png'
					self.grid = make_grid()

				elif save_rect.collidepoint(pygame.mouse.get_pos()):
					#to save the canvas
					save(self.name)

				elif load_rect.collidepoint(pygame.mouse.get_pos()):
					#to load a existing canvas
					load = load_screen(self)
					while load.run:
						load.update()
						load.draw()


				#collision with tools
				if brush_rect.collidepoint(pygame.mouse.get_pos()):
					self.tooltype = 'brush'
				elif fill_tool_rect.collidepoint(pygame.mouse.get_pos()):
					self.tooltype = 'fill'
				elif eraser_rect.collidepoint(pygame.mouse.get_pos()):
					self.tooltype = 'eraser'
				elif pick_tool_rect.collidepoint(pygame.mouse.get_pos()):
					self.tooltype = 'picktool'
				elif dither_tool_rect.collidepoint(pygame.mouse.get_pos()):
					self.tooltype = 'dithertool'
				elif darken_tool_rect.collidepoint(pygame.mouse.get_pos()):
					self.tooltype = 'darkentool'


				#collision with palette ================'
				if color1_rect.collidepoint(pygame.mouse.get_pos()):
					set_slider([self.slider1, self.slider2, self.slider3], color1)
				elif color2_rect.collidepoint(pygame.mouse.get_pos()):
					set_slider([self.slider1, self.slider2, self.slider3], color2)
				elif color3_rect.collidepoint(pygame.mouse.get_pos()):
					set_slider([self.slider1, self.slider2, self.slider3], color3)
				elif color4_rect.collidepoint(pygame.mouse.get_pos()):
					set_slider([self.slider1, self.slider2, self.slider3], color4)
				elif color5_rect.collidepoint(pygame.mouse.get_pos()):
					set_slider([self.slider1, self.slider2, self.slider3], color5)

				elif color6_rect.collidepoint(pygame.mouse.get_pos()):
					set_slider([self.slider1, self.slider2, self.slider3], color6)
				elif color7_rect.collidepoint(pygame.mouse.get_pos()):
					set_slider([self.slider1, self.slider2, self.slider3], color7)
				elif color8_rect.collidepoint(pygame.mouse.get_pos()):
					set_slider([self.slider1, self.slider2, self.slider3], color8)
				elif color9_rect.collidepoint(pygame.mouse.get_pos()):
					set_slider([self.slider1, self.slider2, self.slider3], color9)
				elif color10_rect.collidepoint(pygame.mouse.get_pos()):
					set_slider([self.slider1, self.slider2, self.slider3], color10)

				if color11_rect.collidepoint(pygame.mouse.get_pos()):
					set_slider([self.slider1, self.slider2, self.slider3], color11)
				elif color12_rect.collidepoint(pygame.mouse.get_pos()):
					set_slider([self.slider1, self.slider2, self.slider3], color12)
				elif color13_rect.collidepoint(pygame.mouse.get_pos()):
					set_slider([self.slider1, self.slider2, self.slider3], color13)
				elif color14_rect.collidepoint(pygame.mouse.get_pos()):
					set_slider([self.slider1, self.slider2, self.slider3], color14)
				elif color15_rect.collidepoint(pygame.mouse.get_pos()):
					set_slider([self.slider1, self.slider2, self.slider3], color15)

				elif color16_rect.collidepoint(pygame.mouse.get_pos()):
					set_slider([self.slider1, self.slider2, self.slider3], color16)
				elif color17_rect.collidepoint(pygame.mouse.get_pos()):
					set_slider([self.slider1, self.slider2, self.slider3], color17)
				elif color18_rect.collidepoint(pygame.mouse.get_pos()):
					set_slider([self.slider1, self.slider2, self.slider3], color18)
				elif color19_rect.collidepoint(pygame.mouse.get_pos()):
					set_slider([self.slider1, self.slider2, self.slider3], color19)
				elif color20_rect.collidepoint(pygame.mouse.get_pos()):
					set_slider([self.slider1, self.slider2, self.slider3], color20)

				elif color21_rect.collidepoint(pygame.mouse.get_pos()):
					set_slider([self.slider1, self.slider2, self.slider3], color21)
				elif color22_rect.collidepoint(pygame.mouse.get_pos()):
					set_slider([self.slider1, self.slider2, self.slider3], color22)
				elif color23_rect.collidepoint(pygame.mouse.get_pos()):
					set_slider([self.slider1, self.slider2, self.slider3], color23)
				elif color24_rect.collidepoint(pygame.mouse.get_pos()):
					set_slider([self.slider1, self.slider2, self.slider3], color24)
				elif color25_rect.collidepoint(pygame.mouse.get_pos()):
					set_slider([self.slider1, self.slider2, self.slider3], color25)

				elif color26_rect.collidepoint(pygame.mouse.get_pos()):
					set_slider([self.slider1, self.slider2, self.slider3], color26)
				elif color27_rect.collidepoint(pygame.mouse.get_pos()):
					set_slider([self.slider1, self.slider2, self.slider3], color27)
				elif color28_rect.collidepoint(pygame.mouse.get_pos()):
					set_slider([self.slider1, self.slider2, self.slider3], color28)
				elif color29_rect.collidepoint(pygame.mouse.get_pos()):
					set_slider([self.slider1, self.slider2, self.slider3], color29)
				elif color30_rect.collidepoint(pygame.mouse.get_pos()):
					set_slider([self.slider1, self.slider2, self.slider3], color30)

				elif color31_rect.collidepoint(pygame.mouse.get_pos()):
					set_slider([self.slider1, self.slider2, self.slider3], color31)
				elif color32_rect.collidepoint(pygame.mouse.get_pos()):
					set_slider([self.slider1, self.slider2, self.slider3], color32)
				elif color33_rect.collidepoint(pygame.mouse.get_pos()):
					set_slider([self.slider1, self.slider2, self.slider3], color33)
				elif color34_rect.collidepoint(pygame.mouse.get_pos()):
					set_slider([self.slider1, self.slider2, self.slider3], color34)
				elif color35_rect.collidepoint(pygame.mouse.get_pos()):
					set_slider([self.slider1, self.slider2, self.slider3], color35)

				elif color36_rect.collidepoint(pygame.mouse.get_pos()):
					set_slider([self.slider1, self.slider2, self.slider3], color36)
				elif color37_rect.collidepoint(pygame.mouse.get_pos()):
					set_slider([self.slider1, self.slider2, self.slider3], color37)
				elif color38_rect.collidepoint(pygame.mouse.get_pos()):
					set_slider([self.slider1, self.slider2, self.slider3], color38)
				elif color39_rect.collidepoint(pygame.mouse.get_pos()):
					set_slider([self.slider1, self.slider2, self.slider3], color39)
				elif color40_rect.collidepoint(pygame.mouse.get_pos()):
					set_slider([self.slider1, self.slider2, self.slider3], color40)


			if event.type == pygame.MOUSEBUTTONUP:
				self.drawing = False

			#keypressed events

			if event.type == pygame.KEYDOWN:
				keys = pygame.key.get_pressed()
				if keys[pygame.K_s] and keys[pygame.K_LCTRL]:
					save(self.name)

				if keys[pygame.K_z] and keys[pygame.K_LCTRL]:
					if self.last_drawing:
						self.grid = self.last_drawing[-1]
						self.last_drawing.pop(-1)


		if self.drawing:
			self.paint()

		self.slider1.update()
		self.slider2.update()
		self.slider2.update()
		self.slider_brushsize.update()

		#updating slider values

		if self.selected_color:
			self.primary_color = (int(self.slider1.get_value()), int(self.slider2.get_value()), int(self.slider3.get_value()))

		else:
			self.secondary_color = (int(self.slider1.get_value()), int(self.slider2.get_value()), int(self.slider3.get_value()))


		self.brushsize = int(self.slider_brushsize.get_value())


		if len(self.last_drawing) > 10:
			self.last_drawing.pop(0)



	def draw(self):
		#drawing everything into the window
		screen.fill((180,180,180))
		screen.blit(canvas, (0,0))
		clock.tick(60)
		for i in range(0, len(self.grid)):
			for j in range(0, len(self.grid[1])):
				pygame.draw.rect(canvas, self.grid[i][j], (i*TILESIZE, j*TILESIZE, TILESIZE, TILESIZE))


		#GUI ===============================
		if self.tooltype == 'brush':
			pygame.draw.rect(screen, (130, 130, 130), (brush_rect.x + 5, brush_rect.y + 5, 43, 43))

		elif self.tooltype == 'fill':
			pygame.draw.rect(screen, (130, 130, 130), (fill_tool_rect.x + 5, fill_tool_rect.y + 5, 43, 43))

		elif self.tooltype == 'eraser':
			pygame.draw.rect(screen, (130, 130, 130), (eraser_rect.x + 5, eraser_rect.y + 5, 43, 43))

		elif self.tooltype == 'picktool':
			pygame.draw.rect(screen, (130, 130, 130), (pick_tool_rect.x + 5, pick_tool_rect.y + 5, 43, 43))

		elif self.tooltype == 'dithertool':
			pygame.draw.rect(screen, (130, 130, 130), (dither_tool_rect.x + 5, dither_tool_rect.y + 5, 43, 43))

		elif self.tooltype == 'darkentool':
			pygame.draw.rect(screen, (130, 130, 130), (darken_tool_rect.x + 5, darken_tool_rect.y + 5, 43, 43))

		#sliders
		self.slider1.draw(screen)
		text('R:', screen, BLACK, 17, 615, 22, True)
		self.slider2.draw(screen)
		text('G:', screen, BLACK, 17, 615, 40, True)
		self.slider3.draw(screen)
		text('B:', screen, BLACK, 17, 615, 60, True)
		self.slider_brushsize.draw(screen)

		if self.selected_color:
			pygame.draw.rect(screen, (240,240,240), (primary_color_rect.x - 3, primary_color_rect.y - 3, 56, 56))

		else:
			pygame.draw.rect(screen, (240,240,240), (secondary_color_rect.x - 3, secondary_color_rect.y - 3, 56, 56))

		pygame.draw.rect(screen, self.primary_color, primary_color_rect)
		pygame.draw.rect(screen, self.secondary_color, secondary_color_rect)

		#draw GUI
		screen.blit(brush_image, brush_rect)
		screen.blit(fill_tool_image, fill_tool_rect)
		screen.blit(eraser_image, eraser_rect)
		screen.blit(pick_tool_image, pick_tool_rect)
		screen.blit(dither_tool_image, dither_tool_rect)
		screen.blit(darken_tool_image, darken_tool_rect)
		pygame.draw.rect(screen, (210,210,210), new_rect)
		text('New', screen, BLACK, 35, new_rect.x + 60, new_rect.y + 20, True)
		pygame.draw.rect(screen, (210,210,210), save_rect)
		text('Save', screen, BLACK, 35, save_rect.x + 60, save_rect.y + 20, True)
		pygame.draw.rect(screen, (210,210,210), load_rect)
		text('Load', screen, BLACK, 35, load_rect.x + 60, load_rect.y + 20, True)


		#draw color palette
		pygame.draw.rect(screen, (200, 200, 200), palette_rect)
		pygame.draw.rect(screen, color1, color1_rect)
		pygame.draw.rect(screen, color2, color2_rect)
		pygame.draw.rect(screen, color3, color3_rect)
		pygame.draw.rect(screen, color4, color4_rect)
		pygame.draw.rect(screen, color5, color5_rect)

		pygame.draw.rect(screen, color6, color6_rect)
		pygame.draw.rect(screen, color7, color7_rect)
		pygame.draw.rect(screen, color8, color8_rect)
		pygame.draw.rect(screen, color9, color9_rect)
		pygame.draw.rect(screen, color10, color10_rect)

		pygame.draw.rect(screen, color11, color11_rect)
		pygame.draw.rect(screen, color12, color12_rect)
		pygame.draw.rect(screen, color13, color13_rect)
		pygame.draw.rect(screen, color14, color14_rect)
		pygame.draw.rect(screen, color15, color15_rect)

		pygame.draw.rect(screen, color16, color16_rect)
		pygame.draw.rect(screen, color17, color17_rect)
		pygame.draw.rect(screen, color18, color18_rect)
		pygame.draw.rect(screen, color19, color19_rect)
		pygame.draw.rect(screen, color20, color20_rect)

		pygame.draw.rect(screen, color21, color21_rect)
		pygame.draw.rect(screen, color22, color22_rect)
		pygame.draw.rect(screen, color23, color23_rect)
		pygame.draw.rect(screen, color24, color24_rect)
		pygame.draw.rect(screen, color25, color25_rect)

		pygame.draw.rect(screen, color26, color26_rect)
		pygame.draw.rect(screen, color27, color27_rect)
		pygame.draw.rect(screen, color28, color28_rect)
		pygame.draw.rect(screen, color29, color29_rect)
		pygame.draw.rect(screen, color30, color30_rect)

		pygame.draw.rect(screen, color31, color31_rect)
		pygame.draw.rect(screen, color32, color32_rect)
		pygame.draw.rect(screen, color33, color33_rect)
		pygame.draw.rect(screen, color34, color34_rect)
		pygame.draw.rect(screen, color35, color35_rect)

		pygame.draw.rect(screen, color36, color36_rect)
		pygame.draw.rect(screen, color37, color37_rect)
		pygame.draw.rect(screen, color38, color38_rect)
		pygame.draw.rect(screen, color39, color39_rect)
		pygame.draw.rect(screen, color40, color40_rect)


		pygame.display.flip()


	def paint(self): #brush handling
		mx, my = pygame.mouse.get_pos()
		pos = (mx // TILESIZE, my // TILESIZE)

		if pygame.mouse.get_pressed()[0]:

			if self.tooltype == 'brush':
				brush(self.grid, self.brushsize, self.primary_color, pos)

			elif self.tooltype == 'eraser':
				brush(self.grid, self.brushsize, WHITE, pos)

			elif self.tooltype =='dithertool':
				dither(self.grid, self.primary_color, pos)

			elif self.tooltype == 'darkentool':
				darken(self.last_drawing[-1], self.grid, pos)

		if pygame.mouse.get_pressed()[2]:
			if self.tooltype == 'brush':
				brush(self.grid, self.brushsize, self.secondary_color, pos)
			elif self.tooltype =='dithertool':
				dither(self.grid, self.secondary_color, pos)

app = main()
while app.running:
	app.update()
	app.draw()
