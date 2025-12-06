#!/usr/bin/env python3
"""Generate a simple circular favicon for Fighting Balls game."""

from PIL import Image, ImageDraw

# Create a 32x32 image with transparent background
size = 32
img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
draw = ImageDraw.Draw(img)

# Colors - two contrasting colors representing the teams
color1 = '#d4ddd6'  # sage/day
color2 = '#2d4a4a'  # teal/night

# Draw circular background - left half (semicircle)
draw.pieslice([0, 0, size, size], 90, 270, fill=color1)

# Draw circular background - right half (semicircle)
draw.pieslice([0, 0, size, size], 270, 90, fill=color2)

# Draw ball 1 (dark ball on light side)
ball1_center = (size//4, size//2)
ball1_radius = 5
draw.ellipse([
    ball1_center[0] - ball1_radius,
    ball1_center[1] - ball1_radius,
    ball1_center[0] + ball1_radius,
    ball1_center[1] + ball1_radius
], fill=color2)

# Draw ball 2 (light ball on dark side)
ball2_center = (3*size//4, size//2)
ball2_radius = 5
draw.ellipse([
    ball2_center[0] - ball2_radius,
    ball2_center[1] - ball2_radius,
    ball2_center[0] + ball2_radius,
    ball2_center[1] + ball2_radius
], fill=color1)

# Create a perfect circular mask to ensure clean edges
# Calculate pixel-perfect circle mask
mask = Image.new('L', (size, size), 0)
center = size / 2 - 0.5  # Center point accounting for pixel centers
radius = size / 2

# Create mask pixel by pixel for perfect circular boundary
pixels = mask.load()
for y in range(size):
    for x in range(size):
        # Calculate distance from center
        dx = x - center
        dy = y - center
        distance = (dx * dx + dy * dy) ** 0.5
        # If pixel is inside or on the circle boundary, make it opaque
        if distance <= radius:
            pixels[x, y] = 255

# Apply the mask to the alpha channel - this ensures everything outside circle is transparent
img.putalpha(mask)

# Save as ICO
img.save('favicon.ico', format='ICO', sizes=[(32, 32)])

# Also save as PNG for browsers that prefer it
img.save('favicon.png', format='PNG')

print("Created favicon.ico and favicon.png")

