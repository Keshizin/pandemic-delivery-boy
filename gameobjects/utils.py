# Pandemic Delivery Game
# This code is released under MIT by Fabio Ishikawa

def blend_color(color1, color2, blend_factor):
    red1, green1, blue1 = color1
    red2, green2, blue2 = color2
    red   = red1 + (red2 - red1) * blend_factor
    green = green1 + (green2 - green1) * blend_factor
    blue  = blue1 + (blue2 - blue1) * blend_factor
    return int(red), int(green), int(blue)

# função de LERP
def interpolacao_linear(x, max):
	factor = x / max

# exemplo:
# x, y = pygame.mouse.get_pos()
# factor = x / 639.
# color = blend_color(color1, color2, factor)