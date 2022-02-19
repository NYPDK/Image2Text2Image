import time
from PIL import Image

# encode image
def makefile(pixelSkip):
    with open("seq.txt", "w") as output:
        output.write("")
    img = Image.open("input.jpg")
    w, h = img.size
    pix = 0
    
    # get each pixel and store its data in seq.txt
    with open("seq.txt", "a") as output:
        for x in range(0, w, pixelSkip):
            for y in range(0, h, pixelSkip):
                color = img.getpixel((x, y))
                output.write(f"|{x}, {y}, {color[0]}, {color[1]}, {color[2]}")
                pix += 1
            print(f"{x}/{w - 1}")

# decode image
def readfile():
    pixels = []
    
    # parse data from seq.txt
    with open("seq.txt") as file:
        for line in file:
            seq = line.split("|")
        for i in range(1, len(seq)):
            pixels.append(tuple(map(int, seq[i].split(', '))))
    
    # create image from parsed data
    img = Image.new("RGB", (pixels[-1][0] + 1, pixels[-1][1] + 1))
    for pixel in pixels:
        img.putpixel((pixel[0], pixel[1]), (pixel[2], pixel[3], pixel[4]))
    img.save("output.png")

# run functions and prompt user input
if __name__ == "__main__":
    choice = input("[1] Make input.jpg into seq.txt\n[2] Make seq.txt into output.png\nChoice: ")
    if choice == "1":
        pixelSkip = input("Pixel scan interval (enter nothing for default 1): ")
        if pixelSkip:
            makefile(int(pixelSkip))
        else:
            makefile(1)
        print("Process finished!")
        time.sleep(1)
    elif choice == "2":
        readfile()
        print("Process finished!")
        time.sleep(1)
    else:
        print("Please choose a valid selection next time!")
        time.sleep(1)     