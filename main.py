# Animation Box Program
# 1. Importing Modules
import tkinter

# Defining Dimentions
left,top,width,height=0,0,100,100

# Functions
def runTk():
    global left, top, width, height
    strPosition="{0}x{1}+{2}+{3}".format(width,height,left,top)
    # strPosition = str(width) + "x" + str(height) + "+" + str(left) + "+" + str(top)
    window.geometry(strPosition)
    #"200x200+100+50"
    left+=5
    top+=5
    width+=5
    height+=5
    # Condition for animation till 600
    if left>=600:
        return
    window.after(100,runTk) # to mainloop

# window
window=tkinter.Tk()
window.title("Box Animation Tkinter")
window.after(100,runTk) # from here to runTk func after 100sec
window.mainloop()
