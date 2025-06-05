# [
# 
# Script made by CrazyH2 (https://github.com/crazyh2)
# © Copyright 2025 CrazyH2. All rights reserved.
# 
# ]


def require(name, package = None):
    if package == None:
        package = name
    import os
    try:
        return __import__(name, fromlist=[''])
        print(f"""module '{name}' is installed""")
    except ModuleNotFoundError:
        print(f"""module '{name}' is not installed""")
        os.system(f"""pip install {package}""")
        try:
            return __import__(name, fromlist=[''])
            print(f"""module '{name}' is now installed""")
        except ModuleNotFoundError:
            print(f"""module '{name}' is not installing""")

require("tkinter")
require("pynput")

import pathlib, os
from pynput import keyboard

import tkinter as Tk
from tkinter import *
import tkinter.messagebox as messagebox
import tkinter.filedialog as filedialog
import tkinter.simpledialog as simpledialog

class Main:
    def __init__(self):
        self.fps = 30
        self.current_image_index = 0
        self.bottomText = '''Animat-a-background
An animated wallpaper engine.

Use ctrl + alt + w to remove wallpaper

Licensed under CC BY-NC-ND 4.0
Made by CrazyH2 (https://github.com/crazyh2)
© Copyright 2025 CrazyH2. All rights reserved.'''

        self.root = Tk()
        self.root.title('Animat-a-background - CrazyH2 (github.com/crazyh2)')
        self.root.iconbitmap(os.path.join(os.path.dirname(os.path.realpath(__file__)), './favicon.ico'))
        self.root.withdraw()

        self.screenWidth, self.screenHeight = self.root.winfo_screenwidth(), self.root.winfo_screenheight()

        self.root.wm_attributes("-disabled", True)
        self.root.wm_attributes("-topmost", False)
        self.root.wm_attributes("-fullscreen", False)
        self.root.geometry('%dx%d+0+0' % (self.screenWidth, self.screenHeight - 2))
        self.root.overrideredirect(True)
        self.root.resizable(False, False)
        
        self.agreed = messagebox.askokcancel("Animat-a-background", """By using this software beyond this point you have agreed to not modify, distribute, edit, adapt, sell, steal, or take credit for this code in any form.
                    
Breaking any of these would be a copyright infringement even if you dont agree to the above.
                               
You are also agreeding that you are liable for any harm/damage cause by this program.

Licensed under CC BY-NC-ND 4.0
Made by CrazyH2 (https://github.com/crazyh2)
© Copyright 2025 CrazyH2. All rights reserved.""")
        if self.agreed == False:
            messagebox.showinfo("Animat-a-background", """You have stopped the software from going any futher.
                                
Licensed under CC BY-NC-ND 4.0
Made by CrazyH2 (https://github.com/crazyh2)
© Copyright 2025 CrazyH2. All rights reserved.""")
            exit()

        messagebox.showwarning("Animat-a-background", r"""Use https://motionbgs.com for finding live wallpapers.
Then use https://ezgif.com/video-to-png for converting the video to png frames.

Licensed under CC BY-NC-ND 4.0
Made by CrazyH2 (https://github.com/crazyh2)
© Copyright 2025 CrazyH2. All rights reserved.""")

        self.backgroundPath = self.chooseFile()
        self.fps = self.chooseFPS()

        self.backgroundFrames = self.load_images()
        self.renderer = self.render()

    def chooseFPS(self):
        chosenFPS = simpledialog.askinteger("Animat-a-background", "Enter an FPS:", parent = self.root)
        if chosenFPS == None:
            exit()
        return chosenFPS

    def chooseFile(self):
        filename = filedialog.askdirectory(initialdir="/", title="Select A Wallpaper  |  Animat-a-background - CrazyH2 (github.com/crazyh2)")
        if filename == False:
            exit()
        return filename

    def render(self):
        #bgImg = PhotoImage(file = f"""{pathlib.Path(__file__).parent.resolve()}\\background.png""")
        #bgImg = PhotoImage(file = self.backgroundPath)
        #bg = Label(self.root, image = bgImg) 
        #bg.place(x = (self.screenWidth / 2) - (bgImg.width() / 2), y = (self.screenHeight / 2) - (bgImg.height() / 2))

        self.label = Label(self.root)
        self.label.pack()

        grey_text = Label(self.root, text=self.bottomText, fg="grey", bg="#121212", font = ("Helvetica", 8), justify = "left")
        grey_text.pack()
        grey_text.pack(side = BOTTOM, anchor = 'sw', padx = 10, pady = 60)

        self.root.deiconify()

        keyboard.GlobalHotKeys({'<ctrl>+<alt>+w': self.on_activate_w}).start()

        self.root.lower()
        self.root.after(10, self.update_image)
        self.root.mainloop()

    def load_images(self):
        ezgif = [f for f in sorted(os.listdir(self.backgroundPath)) if f.startswith('ezgif-frame-') and f.endswith('.png')]
        if not ezgif:
            return [f for f in sorted(os.listdir(self.backgroundPath)) if f.startswith('frame_') and f.endswith('.png')]
        else:
            return ezgif
    
    def update_image(self):
        if not self.backgroundFrames:
            print("No images found!")
            return

        image_path = os.path.join(self.backgroundPath, self.backgroundFrames[self.current_image_index])
        photo = PhotoImage(file = image_path)

        self.label.config(image=photo)
        self.label.image = photo
        self.label.place(x = (self.screenWidth / 2) - (photo.width() / 2), y = (self.screenHeight / 2) - (photo.height() / 2))

        self.current_image_index = (self.current_image_index + 1) % len(self.backgroundFrames)

        self.root.after(int(1000 / self.fps), self.update_image)

        mainself = self

    def on_activate_w(self):
        print("Detected w hotkey")
        agreed = messagebox.askokcancel("Animat-a-background", """Are you sure you want to remove the animated wallpaper?

Licensed under CC BY-NC-ND 4.0
Made by CrazyH2 (https://github.com/crazyh2)
© Copyright 2025 CrazyH2. All rights reserved.""")
        if agreed == True:
            self.root.quit()
            os._exit(0)                                

if __name__ == "__main__":
    Main()
