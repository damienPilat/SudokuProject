import tkinter

window = tkinter.Tk()
window.title("Sudoku")
label = tkinter.Label(window, text="1st Tinker").pack()
window.mainloop()

def create_grid(size):
    for x in range(size):
        current = "0"
        for y in range(size-1):
            current += " 0"
        print(current)

# create_grid(9)