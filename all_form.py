import pygame
import tkinter

app = tkinter.Tk()
app.geometry("400x200")
app.title("Formes")

COLORS = ["red" , "blue" , "green" , "black" , "white", "gray"]
RED = (255,0,0)
def draw(lis): 
	app.destroy()
	WIDTH,HEIGHT = 800,600
	jeu = pygame.display.set_mode((WIDTH,HEIGHT))
	pygame.display.set_caption("My project before going to school")


	run = True
	while run: 
		for event in pygame.event.get(): 
			if event.type == pygame.QUIT: 
				run= False
		jeu.fill((255,255,255))
		if lis[0] == "rect": 
			lis[3],lis[4], lis[1], lis[2] = int(lis[3]),int(lis[4]), int(lis[1]), int(lis[2])
			rectangle = pygame.Rect(lis[3],lis[4], lis[1], lis[2]) 
			if lis[5] == "blue" : 
				color = (0,0,255)
				pygame.draw.rect(jeu,color, rectangle)
			if lis[5] == "green" : 
				color = (0,255,0)
				pygame.draw.rect(jeu,color, rectangle)
			if lis[5] == "red" : 
				color = (255,0,0)
				pygame.draw.rect(jeu,color, rectangle)
			if lis[5] == "black" : 
				color = (0,0,0)
				pygame.draw.rect(jeu,color, rectangle)
			if lis[5] == "white" : 
				color = (255,255,255)
				pygame.draw.rect(jeu,color, rectangle)
			if lis[5] == "gray" : 
				color = (110,110,110)
				pygame.draw.rect(jeu,color, rectangle)

		if lis[0] == "circle": 
			lis[1], lis[2], lis[3] = int(lis[1]), int(lis[2]), int(lis[3]) 
			pygame.draw.circle(jeu , RED ,[lis[2], lis[3]], lis[1])

		if lis[0] == "square":
			lis[1], lis[2], lis[3] = int(lis[1]), int(lis[2]), int(lis[3])
			rectangle = pygame.Rect(lis[2],lis[3], lis[1], lis[1])
			pygame.draw.rect(jeu, RED, rectangle)
		if lis[0] == "line": 
			lis[1], lis[2], lis[3], lis[4] = int(lis[1]), int(lis[2]), int(lis[3]), int(lis[4])
			pygame.draw.line(jeu , RED,(lis[1], lis[2]), (lis[3], lis[4]), 7) 
		pygame.display.flip()

def Update_form(value):
	top = tkinter.Toplevel()
	color = tkinter.StringVar()
	color.set(COLORS[0])
	if value == "rect": 
		W_label  = tkinter.Label(top ,text="Width")
		W_entry = tkinter.Entry(top)
		H_label  = tkinter.Label(top ,text="Height")
		H_entry = tkinter.Entry(top)
		X_label  = tkinter.Label(top ,text="cord x")
		X_entry = tkinter.Entry(top)
		Y_label  = tkinter.Label(top ,text="cord y")
		Y_entry = tkinter.Entry(top)

		color_menu = tkinter.OptionMenu(top , color , *COLORS)

		W_label.grid(row=0, column=0 ,padx=5, pady=(10,0))
		W_entry.grid(row=0, column=1 ,padx=5, pady=(10,0))
		H_label.grid(row=1, column=0 ,padx=5, pady=(10,0))
		H_entry.grid(row=1, column=1 ,padx=5, pady=(10,0))
		X_label.grid(row=2, column=0 ,padx=5, pady=(10,0))
		X_entry.grid(row=2, column=1 ,padx=5, pady=(10,0))
		Y_label.grid(row=3, column=0 ,padx=5, pady=(10,0))
		Y_entry.grid(row=3, column=1 ,padx=5, pady=(10,0))
		color_menu.grid(row=4 , column=0 , padx=5 , pady = 5)

		b = tkinter.Button(top , text="Submit" , command = lambda : draw(["rect", W_entry.get(), H_entry.get(), X_entry.get(), Y_entry.get() , color.get()])) 
		b.grid(row=5, column= 0, columnspan=2 , ipadx=50)
		
	elif value == "circle" :

		R_label = tkinter.Label(top ,text="Radious")
		R_entry = tkinter.Entry(top)
		X_label = tkinter.Label(top ,text="cord x")
		X_entry = tkinter.Entry(top)
		Y_label  = tkinter.Label(top ,text="cord y")
		Y_entry = tkinter.Entry(top)

		
		R_label.grid(row=0, column=0 ,padx=5, pady=(10,0))
		R_entry.grid(row=0, column=1 ,padx=5, pady=(10,0))
		X_label.grid(row=1, column=0 ,padx=5, pady=(10,0))
		X_entry.grid(row=1, column=1 ,padx=5, pady=(10,0))
		Y_label.grid(row=2, column=0 ,padx=5, pady=(10,0))
		Y_entry.grid(row=2, column=1 ,padx=5, pady=(10,0))

		b = tkinter.Button(top , text="Submit" , command = lambda : draw(["circle", R_entry.get(), X_entry.get(), Y_entry.get()])) 
		b.grid(row=3 , column= 0, columnspan=2 , ipadx=50)
	

	elif value == "square" :
		C_label = tkinter.Label(top ,text="Cote")
		C_entry = tkinter.Entry(top)
		X_label = tkinter.Label(top ,text="cord x")
		X_entry = tkinter.Entry(top)
		Y_label  = tkinter.Label(top ,text="cord y")
		Y_entry = tkinter.Entry(top)

		C_label.grid(row=0, column=0 ,padx=5, pady=(10,0))
		C_entry.grid(row=0, column=1 ,padx=5, pady=(10,0))
		X_label.grid(row=1, column=0 ,padx=5, pady=(10,0))
		X_entry.grid(row=1, column=1 ,padx=5, pady=(10,0))
		Y_label.grid(row=2, column=0 ,padx=5, pady=(10,0))
		Y_entry.grid(row=2, column=1 ,padx=5, pady=(10,0))
		
		b = tkinter.Button(top , text="Submit" , command = lambda : draw(["square",C_entry.get() , X_entry.get(), Y_entry.get()])) 
		b.grid(row=3 , column= 0, columnspan=2 , ipadx=50)

	elif value == "line" :
		X_label = tkinter.Label(top ,text="first point x")
		X_entry = tkinter.Entry(top)
		Y_label  = tkinter.Label(top ,text="first point y")
		Y_entry = tkinter.Entry(top)
		X2_label = tkinter.Label(top ,text="second point x")
		X2_entry = tkinter.Entry(top)
		Y2_label  = tkinter.Label(top ,text="second point y")
		Y2_entry = tkinter.Entry(top)


		X_label.grid(row=0, column=0 ,padx=5, pady=(10,0))
		X_entry.grid(row=0, column=1 ,padx=5, pady=(10,0))
		Y_label.grid(row=1, column=0 ,padx=5, pady=(10,0))
		Y_entry.grid(row=1, column=1 ,padx=5, pady=(10,0))
		X2_label.grid(row=2, column=0 ,padx=5, pady=(10,0))
		X2_entry.grid(row=2, column=1 ,padx=5, pady=(10,0))
		Y2_label.grid(row=3, column=0 ,padx=5, pady=(10,0))
		Y2_entry.grid(row=3, column=1 ,padx=5, pady=(10,0))

		b = tkinter.Button(top , text="Submit" , command = lambda : draw(["line", X_entry.get() , Y_entry.get(), X2_entry.get(), Y2_entry.get()])) 
		b.grid(row=4 , column= 0, columnspan=2 , ipadx=50)


		
FORM = [("rectangle", "rect"),
		("circle", "circle"),
		("square","square"),
		("line", "line"),
		]
form = tkinter.StringVar()
form.set('rectangle')
for text , value in FORM: 
	tkinter.Radiobutton(app , text = text, variable = form , value= value).pack(anchor = "w")

tkinter.Button(app , text="Choose form" , command = lambda : Update_form(form.get())).pack() 

app.mainloop()
