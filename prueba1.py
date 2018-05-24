from tkinter import *
tk=Tk()
canvas =Canvas(tk, width=800,height=400)
canvas.pack()

my_arco=PhotoImage(file="arco.gif")
canvas.create_image(500,20,anchor=NW,image=my_arco)

my_ball=PhotoImage(file="ball.gif")
canvas.create_image(50,150,anchor=NW,image=my_ball)


def moveball(event):
        canvas.move(2,2,0)

canvas.bind_all('<KeyPress-Right>',moveball)
print("david")



tk.mainloop()