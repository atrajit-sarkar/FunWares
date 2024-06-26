import PIL.Image

# Load an image
img_path = input(r"CountdownWare\hacker.jpeg")
try:
    img = PIL.Image.open(img_path)
except FileNotFoundError:
    print(f"Unable to find image at {img_path}")
    exit(1)

# Resize the image (adjust width and height as needed)
new_width = 120
aspect_ratio = img.height / img.width
new_height = aspect_ratio * new_width * 0.55
img = img.resize((new_width, int(new_height)))

# Convert the image to grayscale
img = img.convert('L')

# Define ASCII characters (customize as desired)
chars = ["@", "J", "D", "%", "*", "P", "+", "Y", "$", ",", "."]

# Convert pixels to ASCII art
pixels = img.getdata()
new_pixels = [chars[pixel // 25] for pixel in pixels]
new_pixels = ''.join(new_pixels)

# Split the string into lines of equal width
ascii_image = [new_pixels[i:i + new_width] for i in range(0, len(new_pixels), new_width)]
ascii_image = "\n".join(ascii_image)

# Print the ASCII art
print(ascii_image)

# Save the result to a text file
with open("sample_ascii_image.txt", "w") as f:
    f.write(ascii_image)
