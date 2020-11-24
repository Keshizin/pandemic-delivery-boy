from math import *

def format_number(n, accuracy=6):
    """Formats a number in a friendly manner
    (removes trailing zeros and unneccesary point."""

    fs = "%."+str(accuracy)+"f"
    str_n = fs%float(n)
    if '.' in str_n:
        str_n = str_n.rstrip('0').rstrip('.')
    if str_n == "-0":
        str_n = "0"
    #str_n = str_n.replace("-0", "0")
    return str_n


def lerp(a, b, i):
    """Linear enterpolate from a to b."""
    return a+(b-a)*i


def range2d(range_x, range_y):

    """Creates a 2D range."""

    range_x = list(range_x)
    return [ (x, y) for y in range_y for x in range_x ]


def xrange2d(range_x, range_y):

    """Iterates over a 2D range."""

    range_x = list(range_x)
    for y in range_y:
        for x in range_x:
            yield (x, y)


def saturate(value, low, high):
    return min(max(value, low), high)


def is_power_of_2(n):
    """Returns True if a value is a power of 2."""
    return log(n, 2) % 1.0 == 0.0


def next_power_of_2(n):
    """Returns the next power of 2 that is >= n"""
    return int(2 ** ceil(log(n, 2)))

if __name__ == "__main__":

    print(list( xrange2d(range(3), range(3)) ))
    print(range2d(range(3), range(3)))
    print(is_power_of_2(7))
    print(is_power_of_2(8))
    print(is_power_of_2(9))

    print(next_power_of_2(7))

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

# def getMovementIntention(Monster monster):
#   intetion = Vector2(0., 0.)

#   # persegue o jogador
#   for player in player_list:
#       direction = get_direction(monster, player)
#       distance = get_distance(monster, player)

#       target_distance = 1.
#       spring_strength = (distance - target_distance)
#       intention += direction = spring_strength # pull towards the player

#   # evita obstaculos
#   for obstacle in obstacle_list:
#       direction = get_direction(monster, obstacle)
#       distance = get_distance(monster, obstacle)

#       spring_strength = 1. / (1. + distance * distance * distance) # inverse cube of distance
#       intention -= direction * spring_strength # push away from the obstacle

#   # spread out
#   for other_monster in monster_list:
#       if monster == other_monster:
#           continue

#       direction = get_direction(monster, other_monster)
#       distance = get_distance(monster, other_monster)

#       spring_strength = 1. / (1. + distance * distance * distance) # inverse cube of distance
#       intention -= direction * spring_strength # push away from the obstacle

#   # check above cutoff threshold
#   if (intention.magnitude < 0.5):
#       return Vector2.zero

#   return intention.normalized