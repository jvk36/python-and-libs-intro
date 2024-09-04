from PIL import Image

print("CHECKOUT OFFICIAL TUTORIAL FOR MORE: https://pillow.readthedocs.io/en/stable/handbook/tutorial.html")

# OPENING AND DISPLAYING IMAGES
print("\nOPENING AND DISPLAYING IMAGES:\n")
# Open an image file
image = Image.open('images/background.png')
print("Open and image file: image = Image.open('images/background.png')")
# Display the image
# image.show()
print("Display the image file: image.show()")

# GETTING IMAGE INFORMATON
print("\nGETTING IMAGE INFORMATON:\n")
# Get image size
width, height = image.size
print("width, height = image.size:")
print(f"Width: {width}, Height: {height}")
# Get image format
format = image.format
print("format = image.format")
print(f"Format: {format}")
# Get image mode
mode = image.mode
print("mode = image.mode")
print(f"Mode: {mode}")

# CREATING A THUMBNAIL
print("\nCREATE A THUMNAIL FROM AN IMAGE:\n")
img_copy = image.copy()
print("1. Copy image: img_copy = image.copy()")
img_copy.thumbnail((128, 128))
print("2. Create Thumnail: img_copy.thumbnail((128, 128))")
# img_copy.show()


# CONVERTING IMAGES TO DIFFERENT FORMATS THAT SUPPORT RGBA
print("\nCONVERTING IMAGES TO DIFFERENT FORMATS THAT SUPPORT RGBA:\n")
image.save('images/background.webp')
print("image.save('images/background.webp')")
image2 = Image.open('images/background.webp')
# image2.show()

# CONVERTING FROM AN RGBA FORMAT TO RGB ONLY FILE TYPE (JPG)
print("\nCONVERTING FROM AN RGBA FORMAT TO RGB ONLY FILE TYPE (JPG):\n")
image_rgb = image.convert('RGB')
image_rgb.save('images/background.jpg')
print("image_rgb = image.convert('RGB')")
print("image_rgb.save('images/background.jpg')")
image2 = Image.open('images/background.jpg')
# image2.show()

# RESIZING AN IMAGE
print("\nRESIZING AN IMAGE:\n")
# Resize the image to a new width and height
new_image = image.resize((800, 600))
print("new_image = image.resize((800, 600))")
# new_image.show()

# CROPPING AN IMAGE
print("\nCROPPING AN IMAGE:\n")
# Define the cropping box (left, upper, right, lower)
cropped_image = image.crop((100, 100, 400, 400))
print("cropped_image = image.crop((100, 100, 400, 400))")
# cropped_image.show()

# ROTATING AN IMAGE
print("\nROTATING AN IMAGE:\n")
# Rotate the image by 90 degrees
normal_image = Image.open('images/brilliance-insanity.png')
rotated_image = normal_image.rotate(90)
print("rotated_image = normal_image.rotate(90)")
# rotated_image.show()

# APPLYING FILTERS
print("\nAPPLYING FILTERS:\n")
from PIL import ImageFilter
# Apply a blur filter
blurred_image = normal_image.filter(ImageFilter.BLUR)
print("blurred_image = normal_image.filter(ImageFilter.BLUR)")
# blurred_image.show()

# ADDING TEXT TO AN IMAGE
print("\nADDING TEXT TO AN IMAGE:\n")
from PIL import ImageDraw, ImageFont
# Create a drawing context
draw = ImageDraw.Draw(image)
print("1. Create a drawing context: draw = ImageDraw.Draw(image)")
# Define a font and size
# font = ImageFont.load_default()
font = ImageFont.truetype("arial.ttf", 36)
print("2. Define a font and size: font = ImageFont.truetype('arial.ttf', 36)")
# Define text position and color
position = (50, 50)
color = (0, 0, 0)  # black
print("3. Define text position and color: a) position = (50, 50), b) color = (0, 0, 0)")
# Add text to image
print('4. Add text to the image: draw.text(position, "Hello, Pillow!", fill=color, font=font)')
draw.text(position, "Hello, Pillow!", fill=color, font=font)
# image.show()

# COMBINING IMAGES
print("\nCOMBINE TWO IMAGES:\n")
# Combine images side by side
combined_width = image.width + normal_image.width
combined_height = max(image.height, normal_image.height)
print("1. Set the width and height of the combined image:")
print("1a. combined_width = image.width + normal_image.width")
print("1b. combined_height = max(image.height, normal_image.height)")
combined_image = Image.new('RGB', (combined_width, combined_height))
print("2. Create a new image with the required dimensions: combined_image = Image.new('RGB', (combined_width, combined_height))")
combined_image.paste(image, (0, 0))
combined_image.paste(normal_image, (image.width, 0))
print("3. Past the two images side-by-side on to the new image")
print("3a. combined_image.paste(image, (0, 0))")
print("3b. combined_image.paste(normal_image, (image.width, 0))")
# combined_image.show()

# CHANGE IMAGE MODE
print("CHANGE IMAGE MODE:")
# Convert image to grayscale
grayscale_image = image.convert('L')
print("Convert image to grayscale: grayscale_image = image.convert('L')")
# grayscale_image.show()
