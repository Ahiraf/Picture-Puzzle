from PIL import Image  # "PIL.Image" is used to load and manipulate images (from the "Pillow" library).
import random # random is a built-in Python module used to shuffle the image chunks later.

PASSWORD = "secret"
seed = 0  # seed will be a number based on the password, used to make the shuffle reproducible.

for i in PASSWORD:
    # This ensures each different password gives a different total, leading to a different shuffle pattern.
    seed += ord(i) # Converts each letter of the password into its ASCII number (ord), adds them up to get a unique number.
  
random.seed(seed) # It sets the random module's "starting point" using the seed, so the shuffling is consistent for the same password.

img = Image.open("/Users/_kodiko_/Desktop/ Code/ButterflyFamilyTree.webp") # It Loads the image that will be scrambled.

#some functions for debugging 
#resized = img.resize((100,100))
#img.show()
#resized.show()

# Now the image will be divided into many small squares both horizantally and vertically.
# Decides how many chunks (small rectangles) the image will be cut into, horizontally and vertically.
chunks_x = 70  # how many chunks will be created in x-axis
chunks_y = 60  # how many chunks will be created in y-axis


width , height = img.size # Gets the original size of the image in pixels.
#print(height,width)


# Calculates how big each puzzle piece will be.
chunk_width = width // chunks_x
chunk_height = height // chunks_y


chunks = []  # List for storing all the chunks

# This double loop goes through the whole image and crops it into small rectangles ("chunks"), then stores them in a list.
for i in range(chunks_x): # range(4) -> [0,1,2,3]
    for j in range(chunks_y):
        #( left , upper , right , lower ) This four parametes are needed for img.crop() Method, which indicates positions
        # img.crop([0,1,chunk_width,chunk_height]).show()
        chunk = img.crop([chunk_width * i, chunk_height * j, chunk_width * (i + 1), chunk_height * (j + 1)])
        chunks.append(chunk)
        # chunk.show()


random.shuffle(chunks) # Shuffles the list of chunks randomly — but using the password-based seed.


# Image.new(mode, size, color=0) , Here mode = "RGB" , size is a tuple of 2 items(height,width),and color = 0 indicates background color which optional
canvas = Image.new("RGB",[chunk_width * chunks_x, chunk_height * chunks_y]) # Creates a blank new image (canvas) with the same size as the original image.


# It Puts the shuffled puzzle pieces one-by-one onto the blank canvas.
for i in range(chunks_x):
    for j in range(chunks_y):
        chunk = chunks.pop(0)
        canvas.paste(chunk, [chunk_width * i, chunk_height * j, chunk_width * (i + 1), chunk_height * (j + 1)])


canvas.save("scrambled.png") # Saves the new scrambled image as a PNG file and opens it.
canvas.show()



