from PIL import Image
import random

PASSWORD = "secret"
seed = sum(ord(i) for i in PASSWORD)
random.seed(seed)

# Load the scrambled image
scrambled_img = Image.open("/Users/_kodiko_/Desktop/ Code/scrambled.png")

chunks_x = 70
chunks_y = 60

width, height = scrambled_img.size
chunk_width = width // chunks_x
chunk_height = height // chunks_y

# Extract the chunks from the image
chunks = []
for i in range(chunks_x):
    for j in range(chunks_y):
        chunk = scrambled_img.crop((
            chunk_width * i,
            chunk_height * j,
            chunk_width * (i + 1),
            chunk_height * (j + 1)
        ))
        chunks.append(chunk)

# Generate the same shuffle order as in the original code
indices = list(range(len(chunks)))
random.shuffle(indices)  # This creates the same shuffle as in the original code

# Create a list to store the original positions
original_order = [0] * len(indices)
for new_pos, original_pos in enumerate(indices):
    original_order[original_pos] = new_pos

# Reconstruct the original image by putting chunks back in their original positions
solved = Image.new("RGB", (width, height))
for idx, pos in enumerate(original_order):
    # Correctly calculate i and j based on chunks_y
    i = idx // chunks_y  # Row index
    j = idx % chunks_y   # Column index
    solved.paste(chunks[pos], (i * chunk_width, j * chunk_height))

# Save and show the result
solved.save("/Users/_kodiko_/Desktop/ Code/unscrambled.png")
solved.show()