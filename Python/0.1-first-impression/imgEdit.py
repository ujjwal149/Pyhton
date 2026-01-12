from PIL import Image

img = Image.open("ChatGPT-portfolio image.png").convert("RGBA")
pixels = img.getdata()

new_pixels = []
for r, g, b, a in pixels:
    if a < 10:
        # transparent background
        new_pixels.append((0, 0, 0, 0))
    else:
        # visible logo pixel → pure black, keep alpha
        new_pixels.append((0, 0, 0, a))

img.putdata(new_pixels)
img.save("UJ_logo_black_transparent.png")
