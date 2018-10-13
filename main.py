import time, keyboard
from tkinter import filedialog
def Build(struct):
    global blockBuffer
    print("Starting build in" ,sleepBuffer, "seconds...")
    time.sleep(sleepBuffer)
    print("Building...")
    for i in struct:
        time.sleep(blockBuffer)
        x = '/tp @p ~'+str(len(i)*-1)+' ~ ~1'
        keyboard.press_and_release('t')
        time.sleep(blockBuffer)
        keyboard.write(x)
        time.sleep(blockBuffer)
        keyboard.press_and_release('enter')
        time.sleep(blockBuffer)
        for i in i:
            y = '/setblock ~ ~-2 ~ '+i
            keyboard.press_and_release('t')
            time.sleep(blockBuffer)
            keyboard.write('/tp @p ~1 ~ ~')
            time.sleep(blockBuffer)
            keyboard.press_and_release('enter')
            time.sleep(blockBuffer)
            keyboard.press_and_release('t')
            time.sleep(blockBuffer)
            keyboard.write(y)
            time.sleep(blockBuffer)
            keyboard.press_and_release('enter')
            time.sleep(blockBuffer)

def SelectFile():
    filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("TXT files","*.txt"),("all files","*.*")))
    return filename
            
def ParseTXT(txtfile):
    print("Parsing Text File...")
    txt = open(txtfile)
    contents = txt.readlines()
    parse = []
    for i in contents:
        x = i.split(',')
        del x[len(x)-1]
        parse.append(x)
    print(parse)
    return parse
blockBuffer = 0.1
sleepBuffer = 10
filename = SelectFile()
txt = ParseTXT(filename)
Build(txt)

