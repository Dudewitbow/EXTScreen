import tkinter as tk
from PIL import Image, ImageTk

class mainWindow:
    def __init__(self, master=None):
        self.master = master
        master.title("Image Display Client")

        imageFrame = Image.new("RGB", "black")
        animation = Image.open('patrick.gif', 'r')
        frames= []

        try:
            while 1:
                frames.append(animation.copy())
                animation.seek(len(frames))
        except EOFError:
            pass

        for i in frames:
            imageFrame.paste(i)
            imageFrame.show()


def main():
    root = tk.Tk()
    root.configure(bg="black")
    server = mainWindow(master=root)
    root.mainloop()


if __name__ == "__main__":
    main()