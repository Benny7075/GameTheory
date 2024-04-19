import pygame
import sys
import math
import time
import random
from AI import *

pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 500, 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LLGREY = [200,200,200]
LGREY = [120,120,120]
DGREY = [50,50,50]
DDGREY = [30,30,30]
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
DGREEN = (2, 117, 29)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GYELLOW = (247, 242, 145)
ORANGE = (253, 113, 4)
BROWN = (147, 66, 3)

# Initialize Pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("GameTheory")

# Define screen sizes and positions
center_screen_rect = pygame.Rect(0, 0, WIDTH, HEIGHT // 2)
bottom_left_screen_rect = pygame.Rect(0, HEIGHT // 2, WIDTH // 2, HEIGHT // 2)
bottom_right_screen_rect = pygame.Rect(WIDTH // 2, HEIGHT // 2, WIDTH // 2, HEIGHT // 2)

# Define font
font = pygame.font.Font(None, 36)

# Define rotation state
rotation_state = 0  # 0: Center on top, 1: Bottom left, 2: Bottom right

# HACKENBUSH starting positions:
# One big structure
greenL1 = [((268, 246), (264, 185), (0, 255, 0)), ((308, 175), (311, 240), (0, 255, 0)), ((348, 174), (387, 180), (0, 255, 0)), ((387, 180), (392, 242), (0, 255, 0)), ((348, 174), (347, 249), (0, 255, 0)), ((422, 174), (424, 239), (0, 255, 0)), ((472, 172), (469, 237), (0, 255, 0)), ((469, 237), (422, 174), (0, 255, 0)), ((264, 185), (308, 175), (0, 255, 0)), ((308, 175), (348, 174), (0, 255, 0)), ((387, 180), (422, 174), (0, 255, 0)), ((422, 174), (472, 172), (0, 255, 0)), ((308, 175), (361, 48), (0, 255, 0)), ((361, 48), (422, 174), (0, 255, 0))]
greenN1 = [(268, 246), (264, 185), (308, 175), (311, 240), (348, 174), (387, 180), (392, 242), (347, 249), (422, 174), (472, 172), (424, 239), (469, 237), (361, 48)]
greenRN1 = [(268, 246), (311, 240), (392, 242), (347, 249), (424, 239), (469, 237)]
# 2 structures 1 root and a 2 root
greenL2 = [((318, 250), (306, 142), (0, 255, 0)), ((306, 142), (366, 120), (0, 255, 0)), ((306, 142), (328, 56), (0, 255, 0)), ((306, 142), (268, 55), (0, 255, 0)), ((268, 55), (328, 56), (0, 255, 0)), ((268, 55), (264, 116), (0, 255, 0)), ((328, 56), (374, 38), (0, 255, 0)), ((401, 245), (407, 154), (0, 255, 0)), ((407, 154), (451, 154), (0, 255, 0)), ((451, 154), (446, 243), (0, 255, 0))]
greenN2 = [(318, 250), (306, 142), (366, 120), (328, 56), (268, 55), (264, 116), (374, 38), (401, 245), (407, 154), (451, 154), (446, 243)]
greenRN2 = [(318, 250), (401, 245), (446, 243)]
# 3 structures
greenL3 = [((295, 239), (295, 147), (0, 255, 0)), ((334, 246), (327, 154), (0, 255, 0)), ((327, 154), (353, 137), (0, 255, 0)), ((353, 137), (313, 118), (0, 255, 0)), ((313, 118), (327, 154), (0, 255, 0)), ((411, 252), (414, 181), (0, 255, 0)), ((414, 181), (395, 198), (0, 255, 0)), ((414, 181), (415, 153), (0, 255, 0)), ((415, 153), (429, 171), (0, 255, 0)), ((415, 153), (416, 80), (0, 255, 0)), ((416, 80), (390, 50), (0, 255, 0)), ((416, 80), (415, 50), (0, 255, 0)), ((416, 80), (445, 57), (0, 255, 0))]
greenN3 = [(295, 239), (295, 147), (334, 246), (327, 154), (353, 137), (313, 118), (411, 252), (414, 181), (395, 198), (415, 153), (429, 171), (416, 80), (390, 50), (415, 50), (445, 57)]
greenRN3 = [(295, 239), (334, 246), (411, 252)]

# green tree SG value 5
greenL4 = [((365, 247), (363, 192), (0, 255, 0)), ((363, 192), (314, 170), (0, 255, 0)), ((314, 170), (293, 129), (0, 255, 0)), ((293, 129), (258, 89), (0, 255, 0)), ((293, 129), (299, 83), (0, 255, 0)), ((363, 192), (363, 121), (0, 255, 0)), ((363, 121), (341, 87), (0, 255, 0)), ((341, 87), (313, 53), (0, 255, 0)), ((313, 53), (341, 24), (0, 255, 0)), ((363, 121), (396, 89), (0, 255, 0)), ((396, 89), (399, 44), (0, 255, 0)), ((363, 192), (431, 144), (0, 255, 0)), ((431, 144), (438, 90), (0, 255, 0)), ((438, 90), (475, 68), (0, 255, 0)), ((431, 144), (470, 146), (0, 255, 0))]
greenN4 = [(365, 247), (363, 192), (314, 170), (293, 129), (258, 89), (299, 83), (363, 121), (341, 87), (313, 53), (341, 24), (396, 89), (399, 44), (431, 144), (438, 90), (475, 68), (470, 146)]
greenRN4 = [(365, 247)]

greenL5 = [((297, 257), (293, 201), (0, 255, 0)), ((293, 201), (289, 163), (0, 255, 0)), ((289, 163), (267, 149), (0, 255, 0)), ((289, 163), (285, 124), (0, 255, 0)), ((285, 124), (312, 99), (0, 255, 0)), ((285, 124), (280, 34), (0, 255, 0)), ((312, 99), (309, 62), (0, 255, 0)), ((312, 99), (328, 75), (0, 255, 0)), ((312, 99), (343, 97), (0, 255, 0)), ((409, 244), (408, 186), (0, 255, 0)), ((408, 186), (379, 162), (0, 255, 0)), ((408, 186), (382, 202), (0, 255, 0)), ((408, 186), (432, 157), (0, 255, 0)), ((408, 186), (445, 201), (0, 255, 0)), ((408, 186), (407, 128), (0, 255, 0)), ((407, 128), (404, 78), (0, 255, 0)), ((404, 78), (421, 56), (0, 255, 0)), ((421, 56), (438, 34), (0, 255, 0)), ((438, 34), (460, 21), (0, 255, 0)), ((404, 78), (375, 57), (0, 255, 0)), ((375, 57), (357, 40), (0, 255, 0))]
greenN5 = [(297, 257), (293, 201), (289, 163), (267, 149), (285, 124), (312, 99), (280, 34), (309, 62), (328, 75), (343, 97), (409, 244), (408, 186), (379, 162), (382, 202), (432, 157), (445, 201), (407, 128), (404, 78), (421, 56), (438, 34), (460, 21), (375, 57), (357, 40)]
greenRN5 = [(297, 257), (409, 244)]

greenL6 = [((282, 247), (279, 212), (0, 255, 0)), ((279, 212), (279, 169), (0, 255, 0)), ((279, 169), (277, 125), (0, 255, 0)), ((277, 125), (277, 80), (0, 255, 0)), ((277, 80), (267, 27), (0, 255, 0)), ((343, 241), (343, 206), (0, 255, 0)), ((343, 206), (315, 203), (0, 255, 0)), ((343, 206), (341, 172), (0, 255, 0)), ((343, 206), (368, 206), (0, 255, 0)), ((402, 243), (395, 135), (0, 255, 0)), ((395, 135), (361, 92), (0, 255, 0)), ((361, 92), (341, 57), (0, 255, 0)), ((341, 57), (336, 29), (0, 255, 0)), ((395, 135), (406, 109), (0, 255, 0)), ((406, 109), (417, 80), (0, 255, 0)), ((417, 80), (426, 47), (0, 255, 0)), ((426, 47), (449, 29), (0, 255, 0)), ((449, 29), (460, 52), (0, 255, 0)), ((460, 52), (464, 95), (0, 255, 0))]
greenN6 = [(282, 247), (279, 212), (279, 169), (277, 125), (277, 80), (267, 27), (343, 241), (343, 206), (315, 203), (341, 172), (368, 206), (402, 243), (395, 135), (361, 92), (341, 57), (336, 29), (406, 109), (417, 80), (426, 47), (449, 29), (460, 52), (464, 95)]
greenRN6 = [(282, 247), (343, 241), (402, 243)]

greenL7 = [((365, 247), (363, 192), (0, 255, 0)), ((363, 192), (314, 170), (0, 255, 0)), ((314, 170), (293, 129), (0, 255, 0)), ((293, 129), (258, 89), (0, 255, 0)), ((293, 129), (299, 83), (0, 255, 0)), ((363, 192), (363, 121), (0, 255, 0)), ((363, 121), (341, 87), (0, 255, 0)), ((341, 87), (313, 53), (0, 255, 0)), ((313, 53), (341, 24), (0, 255, 0)), ((363, 121), (396, 89), (0, 255, 0)), ((396, 89), (399, 44), (0, 255, 0)), ((363, 192), (431, 144), (0, 255, 0)), ((431, 144), (438, 90), (0, 255, 0)), ((438, 90), (475, 68), (0, 255, 0)), ((431, 144), (470, 146), (0, 255, 0)), ((258, 89), (299, 83), (0, 255, 0)), ((341, 24), (399, 44), (0, 255, 0)), ((475, 68), (470, 146), (0, 255, 0))]
greenN7 = [(365, 247), (363, 192), (314, 170), (293, 129), (258, 89), (299, 83), (363, 121), (341, 87), (313, 53), (341, 24), (396, 89), (399, 44), (431, 144), (438, 90), (475, 68), (470, 146)]
greenRN7 = [(365, 247)]

greenL8 = [((365, 247), (363, 192), (0, 255, 0)), ((363, 192), (314, 170), (0, 255, 0)), ((314, 170), (293, 129), (0, 255, 0)), ((293, 129), (258, 89), (0, 255, 0)), ((293, 129), (299, 83), (0, 255, 0)), ((363, 192), (363, 121), (0, 255, 0)), ((363, 121), (341, 87), (0, 255, 0)), ((341, 87), (313, 53), (0, 255, 0)), ((313, 53), (341, 24), (0, 255, 0)), ((363, 121), (396, 89), (0, 255, 0)), ((396, 89), (399, 44), (0, 255, 0)), ((363, 192), (431, 144), (0, 255, 0)), ((431, 144), (438, 90), (0, 255, 0)), ((438, 90), (475, 68), (0, 255, 0)), ((431, 144), (470, 146), (0, 255, 0)), ((258, 89), (299, 83), (0, 255, 0)), ((341, 24), (399, 44), (0, 255, 0)), ((475, 68), (470, 146), (0, 255, 0)), ((438, 90), (396, 89), (0, 255, 0)), ((341, 87), (299, 83), (0, 255, 0)), ((363, 121), (431, 144), (0, 255, 0))]
greenN8 = [(365, 247), (363, 192), (314, 170), (293, 129), (258, 89), (299, 83), (363, 121), (341, 87), (313, 53), (341, 24), (396, 89), (399, 44), (431, 144), (438, 90), (475, 68), (470, 146)]
greenRN8 = [(365, 247)]

start_positions = [[[(290, 246), (335, 244), (374, 243), (411, 237), (454, 241)], [(290, 246), (289, 197), (264, 167), (303, 164), (308, 122), (335, 244), (335, 205), (332, 168), (331, 125), (374, 243), (372, 198), (410, 194), (411, 237), (373, 146), (392, 105), (454, 241), (454, 194), (433, 162), (468, 156), (443, 128)],
[((290, 246), (289, 197), (0, 0, 255)), ((289, 197), (264, 167), (0, 0, 255)), ((289, 197), (303, 164), (255, 0, 0)), ((303, 164), (308, 122), (0, 0, 255)), ((335, 244), (335, 205), (255, 0, 0)), ((335, 205), (332, 168), (255, 0, 0)), ((332, 168), (331, 125), (0, 0, 255)), ((374, 243), (372, 198), (0, 0, 255)), ((372, 198), (410, 194), (0, 0, 255)), ((410, 194), (411, 237), (255, 0, 0)), ((372, 198), (373, 146), (255, 0, 0)), ((373, 146), (392, 105), (0, 255, 0)), ((308, 122), (331, 125), (0, 255, 0)), ((454, 241), (454, 194), (0, 0, 255)), ((454, 194), (433, 162), (255, 0, 0)), ((454, 194), (468, 156), (255, 0, 0)), ((454, 194), (443, 128), (255, 0, 0))]
],
     [[(268, 246), (311, 240), (392, 242), (347, 249), (424, 239), (469, 237)],[(268, 246), (264, 185), (284, 156), (308, 175), (323, 132), (311, 240), (348, 174), (367, 136), (396, 141), (372, 99), (441, 123), (387, 180), (392, 242), (347, 249), (422, 174), (472, 172), (424, 239), (469, 237)]
,[((268, 246), (264, 185), (0, 255, 0)), ((264, 185), (284, 156), (0, 255, 0)), ((264, 185), (308, 175), (0, 0, 255)), ((308, 175), (323, 132), (0, 0, 255)), ((284, 156), (323, 132), (255, 0, 0)), ((308, 175), (311, 240), (0, 255, 0)), ((308, 175), (348, 174), (255, 0, 0)), ((348, 174), (367, 136), (0, 255, 0)), ((367, 136), (396, 141), (255, 0, 0)), ((367, 136), (372, 99), (0, 0, 255)), ((323, 132), (372, 99), (0, 255, 0)), ((372, 99), (441, 123), (0, 0, 255)), ((372, 99), (396, 141), (0, 255, 0)), ((396, 141), (387, 180), (0, 0, 255)), ((348, 174), (387, 180), (0, 255, 0)), ((387, 180), (392, 242), (0, 255, 0)), ((348, 174), (347, 249), (0, 255, 0)), ((387, 180), (422, 174), (255, 0, 0)), ((422, 174), (472, 172), (0, 0, 255)), ((441, 123), (472, 172), (255, 0, 0)), ((422, 174), (424, 239), (0, 255, 0)), ((472, 172), (469, 237), (0, 255, 0)), ((469, 237), (422, 174), (0, 255, 0)), ((422, 174), (441, 123), (0, 255, 0))]
],

[[(286, 253), (435, 248), (359, 240)], [(286, 253), (288, 111), (435, 248), (421, 110), (358, 54), (359, 240), (359, 178), (330, 165), (359, 136), (389, 129), (329, 199), (399, 158)]
, [((286, 253), (288, 111), (0, 0, 255)), ((435, 248), (421, 110), (255, 0, 0)), ((421, 110), (358, 54), (0, 0, 255)), ((358, 54), (288, 111), (255, 0, 0)), ((288, 111), (421, 110), (0, 255, 0)), ((359, 240), (359, 178), (0, 255, 0)), ((359, 178), (330, 165), (0, 255, 0)), ((359, 178), (359, 136), (0, 255, 0)), ((359, 136), (389, 129), (0, 255, 0)), ((330, 165), (329, 199), (0, 255, 0)), ((389, 129), (399, 158), (0, 255, 0))]
],

[[(315, 250), (388, 238), (437, 238)], [(315, 250), (314, 187), (333, 167), (343, 202), (284, 219), (279, 160), (312, 90), (339, 85), (358, 58), (296, 63), (314, 32), (278, 110), (265, 25), (388, 238), (387, 189), (386, 136), (437, 238), (434, 188), (431, 137), (347, 117), (457, 108), (406, 76), (405, 33), (457, 54)]
, [((315, 250), (314, 187), (0, 255, 0)), ((314, 187), (333, 167), (0, 255, 0)), ((314, 187), (343, 202), (0, 255, 0)), ((314, 187), (284, 219), (0, 255, 0)), ((314, 187), (279, 160), (0, 255, 0)), ((314, 187), (312, 90), (0, 255, 0)), ((312, 90), (339, 85), (0, 255, 0)), ((339, 85), (358, 58), (0, 255, 0)), ((312, 90), (296, 63), (0, 255, 0)), ((296, 63), (314, 32), (0, 255, 0)), ((296, 63), (278, 110), (0, 255, 0)), ((296, 63), (265, 25), (0, 255, 0)), ((388, 238), (387, 189), (0, 255, 0)), ((387, 189), (386, 136), (0, 255, 0)), ((437, 238), (434, 188), (0, 255, 0)), ((434, 188), (431, 137), (0, 255, 0)), ((386, 136), (347, 117), (0, 0, 255)), ((431, 137), (457, 108), (0, 0, 255)), ((386, 136), (406, 76), (255, 0, 0)), ((406, 76), (431, 137), (255, 0, 0)), ((406, 76), (405, 33), (255, 0, 0)), ((347, 117), (339, 85), (0, 0, 255)), ((457, 108), (457, 54), (0, 0, 255))]
],

[[(281, 239), (341, 238), (309, 237), (378, 236), (408, 238), (462, 240)], [(281, 239), (292, 195), (330, 192), (332, 149), (357, 126), (375, 150), (341, 238), (309, 237), (378, 236), (407, 159), (360, 59), (437, 159), (408, 238), (386, 57), (462, 240), (451, 36), (299, 36), (278, 66), (320, 65), (277, 99), (315, 106)]
, [((281, 239), (292, 195), (0, 0, 255)), ((292, 195), (330, 192), (0, 0, 255)), ((330, 192), (332, 149), (0, 0, 255)), ((332, 149), (357, 126), (0, 0, 255)), ((357, 126), (375, 150), (255, 0, 0)), ((330, 192), (341, 238), (255, 0, 0)), ((292, 195), (309, 237), (255, 0, 0)), ((378, 236), (407, 159), (255, 0, 0)), ((407, 159), (360, 59), (255, 0, 0)), ((407, 159), (437, 159), (255, 0, 0)), ((437, 159), (408, 238), (0, 0, 255)), ((437, 159), (386, 57), (0, 0, 255)), ((462, 240), (451, 36), (0, 255, 0)), ((451, 36), (299, 36), (0, 255, 0)), ((299, 36), (278, 66), (0, 255, 0)), ((299, 36), (320, 65), (0, 255, 0)), ((278, 66), (277, 99), (0, 0, 255)), ((320, 65), (315, 106), (255, 0, 0)), ((277, 99), (315, 106), (0, 255, 0))]
]]



start_pos = random.choice(start_positions)
start_lines = start_pos[2]
start_nodes = start_pos[1]
start_roots = start_pos[0]


start_lines = greenL8
start_nodes = greenN8
start_roots = greenRN8

#FROG GAME ########################
box_size = 50
smaller_box_size = 40
frog_size = 20
smaller_frog = 16
#frog_grid = [[0,0,2,0,1],[2,0,1,0,0],[2,2,0,1,1],[2,0,0,0,1]]
frog_grid = [[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0],[0,0,0,0,0]]
for i in range(5):
    for j in range(5):
        rand_num = random.randint(0, 99)
        if rand_num < 10:
            frog_grid[i][j] = 2
frog_grid[0][4] = 1
def draw_grid(rotation_state, frog_grid):
    if rotation_state == 0:
        for j in range(5):
            for i in range(5):
                x = WIDTH/4 + i * (box_size)
                y = HEIGHT // 4 - 50*j + 70
                box_center = (x + box_size // 2, y + box_size // 2)

                if frog_grid[j][i] == 1:
                    pygame.draw.circle(screen, WHITE, box_center, frog_size)
                if frog_grid[j][i] == 2:
                    pygame.draw.circle(screen, BLACK, box_center, frog_size)
                if frog_grid[j][i] == 3:
                    square_x = box_center[0] - frog_size
                    square_y = box_center[1] - frog_size
                    pygame.draw.rect(screen, BLACK, (square_x, square_y, 2*frog_size, 2*frog_size))
                    pygame.draw.circle(screen, WHITE, box_center, frog_size)
                if cheat_mode:
                    grundy_grid = calculate_wyt_posiions(frog_grid)
                    grundy_value = grundy_grid[j][i]
                    text_surface = font.render(str(grundy_value), True, BLACK)
                    text_rect = text_surface.get_rect(center=box_center)
                    screen.blit(text_surface, text_rect)
                pygame.draw.rect(screen, BLACK, (x, y, box_size, box_size), 5)
    if rotation_state == 1:
        for j in range(5):
            for i in range(5):
                x = WIDTH/2 + i * (smaller_box_size) + 20
                y = HEIGHT // 2 - 40*j + 220
                box_center = (x + smaller_box_size // 2, y + smaller_box_size // 2)

                if frog_grid[j][i] == 1:
                    pygame.draw.circle(screen, WHITE, box_center, smaller_frog)
                if frog_grid[j][i] == 2:
                    pygame.draw.circle(screen, BLACK, box_center, smaller_frog)
                pygame.draw.rect(screen, BLACK, (x, y, smaller_box_size, smaller_box_size), 5)
    if rotation_state == 2:
        for j in range(5):
            for i in range(5):
                x = i * (smaller_box_size) + 20
                y = HEIGHT // 2 - 40*j + 220
                box_center = (x + smaller_box_size // 2, y + smaller_box_size // 2)

                if frog_grid[j][i] == 1:
                    pygame.draw.circle(screen, WHITE, box_center, smaller_frog)
                if frog_grid[j][i] == 2:
                    pygame.draw.circle(screen, BLACK, box_center, smaller_frog)
                pygame.draw.rect(screen, BLACK, (x, y, smaller_box_size, smaller_box_size), 5)



def which_frog_box(click_position):
    for j in range(5):
        for i in range(5):
            x = WIDTH / 4 + i * (box_size)
            y = HEIGHT // 4 - 50 * j + 70
            box_rect = pygame.Rect(x, y, box_size, box_size)

            # Check if the click position is within the current box
            if box_rect.collidepoint(click_position):
                return j, i  # Return the row and column indices

    return None, None  # Return None if no box is selected
highlighted = False
def highlight_piece(i, j):
    if frog_grid[i][j] == 1:
        frog_grid[i][j] = 3
    highlighted = True

def unhighlight():
    for i in range(5):
        for j in range(5):
            if frog_grid[i][j] == 3:
                frog_grid[i][j] = 1
    highlighted = False

def perform_frog_moves(i, j, turn):
    for n in range(5):
        for m in range(5):
            if frog_grid[n][m] == 3:
                if i == n and j < m:
                    blocked = False
                    for k in range(j + 1, m):
                        if frog_grid[n][k] != 0:  # Check for obstacles (1 or 2)
                            blocked = True
                    if not blocked and frog_grid[i][j] == 0:
                        frog_grid[i][j] = 1
                        frog_grid[n][m] = 0
                        turn = change_turn(turn)
                elif j == m and i > n:
                    blocked = False
                    for k in range(n + 1, i):
                        if frog_grid[k][m] != 0:  # Check for obstacles (1 or 2)
                            blocked = True
                    if not blocked and frog_grid[i][j] == 0:
                        frog_grid[i][j] = 1
                        frog_grid[n][m] = 0
                        turn = change_turn(turn)
                elif (abs(i - n) == abs(j - m) and i >= n and j <= m) and frog_grid[i][j] == 0:
                    blocked = False
                    for k in range(1, abs(i-n)):
                        if frog_grid[i - k][j + k] != 0:  # Check for obstacles (1 or 2)
                            blocked = True
                    if not blocked and frog_grid[i][j] == 0:
                        frog_grid[i][j] = 1
                        frog_grid[n][m] = 0
                        turn = change_turn(turn)
    return turn



# NIM #################################
nim_grid = [random.randint(1, 12) for _ in range(4)]
#nim_grid = [0,0,0,0]
def draw_nim(rotation_state, nim_grid):
    if rotation_state == 1:
        rect_width = 70
        rect_height = 20
        rect_x = 15
        rect_y = 250
        tower_spacing = 10
        for i in nim_grid:
            rect_x += rect_width + 10
            for _ in range(i):
                pygame.draw.rect(screen, ORANGE, (rect_x, rect_y, rect_width, rect_height))
                pygame.draw.rect(screen, BROWN, (rect_x, rect_y, rect_width, rect_height), 2)
                if playing == False and _ == i-1 and i < 12:
                    pygame.draw.rect(screen, BROWN, (rect_x, rect_y - rect_height, rect_width, rect_height), 2)
                # Update position for the next rectangle
                rect_y -= rect_height

            # Reset position and size for the next tower
            rect_y = 250
        if not playing:
            pygame.draw.circle(screen, ORANGE, (30, 30), frog_size)
    if rotation_state == 0:
        rect_width = 40
        rect_height = 15
        rect_x = -20
        rect_y = 550
        tower_spacing = 10
        nim_sum = 0
        for i in nim_grid:
            nim_sum ^= i
            rect_x += rect_width + 10
            for _ in range(i):
                pygame.draw.rect(screen, ORANGE, (rect_x, rect_y, rect_width, rect_height))
                pygame.draw.rect(screen, BROWN, (rect_x, rect_y, rect_width, rect_height), 2)
                # Update position for the next rectangle
                rect_y -= rect_height
            if cheat_mode:
                font = pygame.font.Font(None, 28)
                text_surface = font.render(str(i), True, ORANGE)
                text_rect = text_surface.get_rect(center=(rect_x + rect_width / 2, rect_y))
                screen.blit(text_surface, text_rect)
            # Reset position and size for the next tower
            rect_y = 550
        if cheat_mode:
            font = pygame.font.Font(None, 40)
            text_surface = font.render(str(nim_sum), True, ORANGE)
            text_rect = text_surface.get_rect(center=(WIDTH // 4, HEIGHT // 2 + 40))
            screen.blit(text_surface, text_rect)

    if rotation_state == 2:
        rect_width = 40
        rect_height = 15
        rect_x = 230
        rect_y = 550
        tower_spacing = 10
        for i in nim_grid:
            rect_x += rect_width + 10
            for _ in range(i):
                pygame.draw.rect(screen, ORANGE, (rect_x, rect_y, rect_width, rect_height))
                pygame.draw.rect(screen, BROWN, (rect_x, rect_y, rect_width, rect_height), 2)
                # Update position for the next rectangle
                rect_y -= rect_height

            # Reset position and size for the next tower
            rect_y = 550

def which_nim_block(click_position):
    rect_width = 70
    rect_height = 20
    rect_x = 15
    rect_y = 250
    tower_spacing = 10
    tower = 0
    for i in nim_grid:
        tower += 1
        rect_x += rect_width + 10
        for _ in range(i + 1):
            box_rect = pygame.Rect(rect_x, rect_y, rect_width, rect_height)

            # Check if the click position is within the current box
            if box_rect.collidepoint(click_position):
                return tower, _  # Return the row and column indices
            # Update position for the next rectangle
            rect_y -= rect_height

        # Reset position and size for the next tower
        rect_y = 250
    return None, None

def remove_and_add_blocks(tower, block):
    global nim_grid
    if block > nim_grid[tower-1] - 1 and not playing:
        nim_grid[tower-1] = nim_grid[tower-1] + 1
    else:
        nim_grid[tower - 1] = block

# HACKENBUSHHHH ############
def intersect(line1, line2):
    x1, y1 = line1[0]
    x2, y2 = line1[1]
    x3, y3 = line2[0]
    x4, y4 = line2[1]

    # Calculate the orientation of three points (p, q, r)
    def orientation(p, q, r):
        val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
        if val == 0:
            return 0  # Collinear
        return 1 if val > 0 else 2  # Clockwise or Counterclockwise

    # Check if two line segments intersect
    def on_segment(p, q, r):
        return (q[0] <= max(p[0], r[0]) and q[0] >= min(p[0], r[0]) and
                q[1] <= max(p[1], r[1]) and q[1] >= min(p[1], r[1]))

    o1 = orientation((x1, y1), (x2, y2), (x3, y3))
    o2 = orientation((x1, y1), (x2, y2), (x4, y4))
    o3 = orientation((x3, y3), (x4, y4), (x1, y1))
    o4 = orientation((x3, y3), (x4, y4), (x2, y2))

    # General case
    if o1 != o2 and o3 != o4:
        return True

    # Special cases
    if o1 == 0 and on_segment((x1, y1), (x3, y3), (x2, y2)):
        return True
    if o2 == 0 and on_segment((x1, y1), (x4, y4), (x2, y2)):
        return True
    if o3 == 0 and on_segment((x3, y3), (x1, y1), (x4, y4)):
        return True
    if o4 == 0 and on_segment((x3, y3), (x2, y2), (x4, y4)):
        return True

    return False

nodes = start_nodes
def remove_unconnected_nodes(nodes, lines, roots):
    # Create an adjacency list representation of the graph
    graph = {node: [] for node in nodes}
    for line in lines:
        graph[line[0]].append(line[1])
        graph[line[1]].append(line[0])

    # Perform DFS starting from each root node
    visited = set()
    for root in roots:
        if root not in visited:
            dfs(graph, root, visited)

    # Filter nodes and lines based on visited nodes
    connected_nodes = [node for node in nodes if node in visited]
    connected_lines = [line for line in lines if line[0] in visited and line[1] in visited]

    return connected_nodes, connected_lines

def dfs(graph, node, visited):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


def is_line_ok(coords):
    if distance(coords[0], coords[1]) > 22 and WIDTH - 10 > coords[0][0] > WIDTH // 2 and\
            10 < coords[0][1] < HEIGHT // 2 and WIDTH - 10 > coords[1][0] > WIDTH // 2 and \
            10 < coords[1][1] < HEIGHT // 2:
        return True
    else:
        return False

def check_two_roots(line):
    ground = pygame.Rect(WIDTH // 2, -70 + HEIGHT // 2, WIDTH // 2, HEIGHT // 10)
    if ground.collidepoint(line[0]) and ground.collidepoint(line[1]):
        return True
    return False

def convert_line_to_center(line):
    return ((line[0][0] - WIDTH//4, line[0][1]), (line[1][0]- WIDTH//4, line[1][1]))

root_nodes = start_roots
def update_root_nodes():
    global root_nodes
    for line in drawn_lines:
        ground = pygame.Rect(WIDTH // 2, -70 + HEIGHT // 2, WIDTH // 2, HEIGHT // 10)
        if ground.collidepoint(line[0]) and line[0] not in root_nodes:
            root_nodes.append(line[0])
        if ground.collidepoint(line[1]) and line[1] not in root_nodes:
            root_nodes.append(line[1])
    for root in root_nodes:
        found = False
        for line in drawn_lines:
            if root == line[0] or root == line[1]:
                found = True
        if found == False:
            root_nodes.remove(root)

def update_nodes():
    global nodes
    for line in drawn_lines:
        if line[0] not in nodes:
            nodes.append(line[0])
        if line[1] not in nodes:
            nodes.append(line[1])
    for node in nodes:
        found = False
        for line in drawn_lines:
            if node == line[0] or node == line[1]:
                found = True
        if found == False:
            nodes.remove(node)


def check_if_line_joins(drawn_lines, line):
    point1 = line[0]
    point2 = line[1]
    for l in drawn_lines:
        if distance(l[0], line[0]) < 10:
            point1 = l[0]
        elif distance(l[1], line[0]) < 10:
            point1 = l[1]
        elif distance(l[0], line[1]) < 10:
            point2 = l[0]
        elif distance(l[1], line[1]) < 10:
            point2 = l[1]

    return point1, point2

def draw_hacken_background(rotation_state):
    if rotation_state == 2:
        if not playing:
            pygame.draw.rect(screen, WHITE, (WIDTH // 2, 0, WIDTH // 2, HEIGHT // 2))
            pygame.draw.rect(screen, GYELLOW, (WIDTH // 2, -70 + HEIGHT // 2, WIDTH // 2, HEIGHT // 10 ))
        if playing:
            pygame.draw.rect(screen, WHITE, (0, 0, WIDTH, HEIGHT // 2))
            pygame.draw.rect(screen, GYELLOW, (0, -70 + HEIGHT // 2, WIDTH, HEIGHT // 10))
    if rotation_state == 0:
        pygame.draw.rect(screen, WHITE, (WIDTH // 2, HEIGHT // 2, WIDTH // 2, HEIGHT // 2))
        pygame.draw.rect(screen, GYELLOW, (WIDTH // 2, -70 + HEIGHT, WIDTH // 2, HEIGHT // 10 ))
    if rotation_state == 1:
        pygame.draw.rect(screen, WHITE, (0, HEIGHT // 2, WIDTH // 2, HEIGHT // 2))
        pygame.draw.rect(screen, GYELLOW, (0 , HEIGHT - 70, WIDTH // 2, HEIGHT // 10 ))

I_colour = 0
def draw_hackenbush(rotation_state):
    # Draw previously drawn lines
    global icol
    if rotation_state == 2 and not playing:
        if highlight == BLUE:
            pygame.draw.circle(screen, YELLOW, (80, HEIGHT // 6), 35)
        if highlight == RED:
            pygame.draw.circle(screen, YELLOW, (180, HEIGHT // 6), 35)
        if highlight == GREEN:
            pygame.draw.circle(screen, YELLOW, (80, 100 +HEIGHT // 6), 35)
        if highlight == 666:
            pygame.draw.circle(screen, YELLOW, (180, 100 +HEIGHT // 6), 35)
        pygame.draw.circle(screen, BLUE, (80, HEIGHT // 6), 30)
        pygame.draw.circle(screen, RED, (180, HEIGHT // 6), 30)
        pygame.draw.circle(screen, GREEN, (80, 100 + HEIGHT // 6), 30)
        pygame.draw.circle(screen, DGREY, (180, 100 + HEIGHT // 6), 30)
        pygame.draw.circle(screen, LLGREY, (130, 50 + HEIGHT // 6), 20)
        # AI logo
        if I_colour==0:
            icol = GREEN
        if I_colour==1:
            icol = BLUE
        if I_colour==2:
            icol = RED
        pygame.draw.rect(screen, DGREY, (100, -40 + HEIGHT//10 + 210, 60, 80))
        pygame.draw.circle(screen, icol, (130, -18 + HEIGHT//10 + 210), 10)
        pygame.draw.rect(screen, icol, (121, 6 +HEIGHT // 10 +210, 18, 34))
        for line in drawn_lines:
            pygame.draw.line(screen, line[2], line[0], line[1], 4)
            pygame.draw.circle(screen, line[2], line[0], 6)
            pygame.draw.circle(screen, line[2], line[1], 6)
        for node in root_nodes:
            pygame.draw.circle(screen, BLACK, node, 6)

    if rotation_state == 2 and playing:
        for line in drawn_lines:
            pygame.draw.line(screen, line[2], (line[0][0] - WIDTH//4, line[0][1]), (line[1][0]- WIDTH//4, line[1][1]), 4)
            pygame.draw.circle(screen, line[2], (line[0][0] - WIDTH//4, line[0][1]), 6)
            pygame.draw.circle(screen, line[2], (line[1][0] - WIDTH//4, line[1][1]), 6)
        for node in root_nodes:
            pygame.draw.circle(screen, BLACK, (node[0] - WIDTH//4, node[1]), 6)
    if rotation_state == 0:
        for line in drawn_lines:
            pygame.draw.line(screen, line[2], (line[0][0], line[0][1] + HEIGHT//2), (line[1][0], line[1][1] + HEIGHT//2), 4)
            pygame.draw.circle(screen, line[2], (line[0][0], line[0][1] + HEIGHT//2), 6)
            pygame.draw.circle(screen, line[2], (line[1][0], line[1][1] + HEIGHT//2), 6)
        for node in root_nodes:
            pygame.draw.circle(screen, BLACK, (node[0], node[1] + HEIGHT // 2), 6)
        if cheat_mode:
            pictures = seperate_into_componants(drawn_lines, nodes, root_nodes)
            hack_sum = 0
            for picture in pictures:
                grund = compute_grundies(picture[0], picture[1], picture[2])
                hack_sum ^= grund[0]
                font = pygame.font.Font(None, 26)
                text_surface = font.render(str(grund[0]), True, BLACK)
                text_rect = text_surface.get_rect(center=(picture[2][0][0], picture[2][0][1] + HEIGHT // 2 + 20))
                screen.blit(text_surface, text_rect)
            # hack gruns
            font = pygame.font.Font(None, 40)
            text_surface = font.render(str(hack_sum), True, GREEN)
            text_rect = text_surface.get_rect(center=(WIDTH//2 + 30, HEIGHT//2 + 30))
            screen.blit(text_surface, text_rect)
            # total
            SGval = hack_sum
            for pile in nim_grid:
                SGval ^= pile
            grundy_grid = calculate_wyt_posiions(frog_grid)
            for i in range(5):
                for j in range(5):
                    if frog_grid[i][j] == 1 or frog_grid[i][j] == 3:
                        SGval ^= grundy_grid[i][j]
            font = pygame.font.Font(None, 40)
            text_surface = font.render(str(SGval), True, WHITE)
            text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            screen.blit(text_surface, text_rect)

    if rotation_state == 1:
        for line in drawn_lines:
            pygame.draw.line(screen, line[2], (line[0][0] - WIDTH // 2, line[0][1] + HEIGHT//2), (line[1][0] - WIDTH // 2, line[1][1] + HEIGHT//2), 4)
            pygame.draw.circle(screen, line[2], (line[0][0] - WIDTH // 2, line[0][1] + HEIGHT//2), 6)
            pygame.draw.circle(screen, line[2], (line[1][0] - WIDTH // 2, line[1][1] + HEIGHT//2), 6)
        for node in root_nodes:
            pygame.draw.circle(screen, BLACK, (node[0] - WIDTH//2, node[1] + HEIGHT // 2), 6)



playing = False
turn = 0
def draw_screens():
    global center_screen_rect, bottom_left_screen_rect, bottom_right_screen_rect, rotation_state,\
        frog_grid, nim_grid, redscore, bluescore
    screen.fill(LGREY)
    if not playing:
        screenedge = DGREY
    else:
        if turn == 0:
            screenedge = BLUE
        else:
            screenedge = RED
    draw_hacken_background(rotation_state)
    pygame.draw.rect(screen, screenedge, center_screen_rect, 10)
    pygame.draw.rect(screen, screenedge, bottom_left_screen_rect, 10)
    pygame.draw.rect(screen, screenedge, bottom_right_screen_rect, 10)
    pygame.draw.circle(screen, DDGREY, (WIDTH/2, HEIGHT/2), 20)
    #pygame.draw.circle(screen, ORANGE, (WIDTH / 2, HEIGHT - 25), 25)
    draw_grid(rotation_state, frog_grid)
    draw_nim(rotation_state, nim_grid)
    draw_hackenbush(rotation_state)
    if not playing:
        pygame.draw.circle(screen, BLUE, (20, HEIGHT / 2), 20)
        pygame.draw.circle(screen, RED, (WIDTH - 20, HEIGHT / 2), 20)
        draw_score(redscore, bluescore)
    if playing:
        pygame.draw.circle(screen, DDGREY, (WIDTH//2, HEIGHT), 20)
    if rotation_state == 0:
        pygame.draw.circle(screen, DDGREY, (0, 0), 20)


def rotate_screens():
    global rotation_state
    if rotation_state == 0:
        rotation_state = 1
    elif rotation_state == 1:
        rotation_state = 2
    elif rotation_state == 2:
        rotation_state = 0

# Function to calculate distance between two points
def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def change_turn(turn):
    return 1 - turn

def no_frog_moves(frog_grid):
    for i in range(5):
        for j in range(5):
            if (frog_grid[i][j] == 1 or frog_grid[i][j] == 3) and can_piece_move(frog_grid, i, j):
                return False
    return True


def no_blue_or_green(drawn_lines):
    for line in drawn_lines:
        if line[2] == BLUE or line[2] == GREEN:
            return False
    return True

def no_red_or_green(drawn_lines):
    for line in drawn_lines:
        if line[2] == RED or line[2] == GREEN:
            return False
    return True

def check_winning_move(frog_grid, nim_grid, drawn_lines, turn):
    global playing, redscore, bluescore
    if sum(nim_grid) == 0 and no_frog_moves(frog_grid):
        if turn == 0 and no_blue_or_green(drawn_lines):
            redscore += 1
            unhighlight()
            playing = False
            return True
        if turn == 1 and no_red_or_green(drawn_lines):
            bluescore += 1
            unhighlight()
            playing = False
            return True
    return False
redscore = 0
bluescore = 0
def draw_score(redscore, bluescore):
    # Draw blue score on the left
    blue_text = font.render(str(bluescore), True, BLUE)
    blue_rect = blue_text.get_rect()
    blue_rect.topleft = (50, HEIGHT // 2 - blue_rect.height // 2)
    screen.blit(blue_text, blue_rect)

    # Draw red score on the right
    red_text = font.render(str(redscore), True, RED)
    red_rect = red_text.get_rect()
    red_rect.topright = (WIDTH - 50, HEIGHT // 2 - red_rect.height // 2)
    screen.blit(red_text, red_rect)


cheat_mode = False
def change_cheat_mode():
    global cheat_mode
    if not cheat_mode:
        cheat_mode = True
    else:
        cheat_mode = False


# Main game loop
drawing = False
highlight = BLUE
drawn_lines = start_lines
AI_on = True
while True:
    goneround1 = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            radius = 20  # Specify the radius here
            bigrad = 30
            click_position = pygame.mouse.get_pos()
            center_position = (WIDTH // 2, HEIGHT // 2)
            if distance(click_position, center_position) < radius:
                unhighlight()
                rotate_screens()
            if distance(click_position, (20, HEIGHT//2)) < radius:
                unhighlight()
                playing = True
                goneround1 = False
                turn = 0
            if distance(click_position, (WIDTH-20, HEIGHT//2)) < radius:
                playing = True
                goneround1 = False
                turn = 1
            if playing:
                if distance(click_position, (WIDTH // 2, HEIGHT)) < radius:
                    playing = False
                    unhighlight()
            if distance(click_position, (0, 0)) < radius and rotation_state == 0:
                change_cheat_mode()
            if rotation_state == 2 and not playing:
                drawing = True
                start_pos = event.pos
                if distance(click_position, (80, HEIGHT // 6)) < bigrad:
                    highlight = BLUE
                if distance(click_position, (180, HEIGHT // 6)) < bigrad:
                    highlight = RED
                if distance(click_position, (80,100 + HEIGHT // 6)) < bigrad:
                    highlight = GREEN
                if distance(click_position, (180,100 + HEIGHT // 6)) < bigrad:
                    highlight = 666
                if distance(click_position, (130,50 + HEIGHT // 6)) < radius:
                    #drawn_lines = []
                    #root_nodes = []
                    drawn_lines, nodes, root_nodes = perform_fusion_principle2(drawn_lines, nodes, root_nodes, False)
                # Check if the click is inside the AI button
                if pygame.Rect(100, -40 + HEIGHT // 10 + 210, 60, 80).collidepoint(click_position):
                    # Rotate I_colour between 0, 1, and 2
                    I_colour = (I_colour + 1) % 3
            elif rotation_state == 2 and playing:
                start_pos = event.pos
            elif rotation_state == 0 and not playing:
                i, j = which_frog_box(click_position)
                if i is not None and j is not None:
                    if frog_grid[i][j] == 0:
                        frog_grid[i][j] = 1
                    elif frog_grid[i][j] == 1:
                        frog_grid[i][j] = 2
                    elif frog_grid[i][j] == 2:
                        frog_grid[i][j] = 0
            elif rotation_state == 0 and playing:
                i, j = which_frog_box(click_position)
                if i is not None and j is not None:
                    if highlighted == True:
                        turn = perform_frog_moves(i, j, turn)
                        unhighlight()
                        highlighted = False
                    elif highlighted == False and can_piece_move(frog_grid, i, j):
                        highlight_piece(i, j)
                        highlighted = True
                    check_winning_move(frog_grid, nim_grid, drawn_lines, turn)
            elif rotation_state == 1 and not playing:
                if distance(click_position, (30, 30)) < frog_size:
                    nim_grid = [random.randint(1, 12) for _ in range(4)]
                i, j = which_nim_block(click_position)
                if i is not None and j is not None:
                    remove_and_add_blocks(i, j)
            elif rotation_state == 1 and playing:
                i, j = which_nim_block(click_position)
                if i is not None and j is not None:
                    remove_and_add_blocks(i, j)
                    turn = change_turn(turn)
                    check_winning_move(frog_grid, nim_grid, drawn_lines, turn)
            if playing:
                if I_colour == 1 and turn == 0 and not check_winning_move(frog_grid, nim_grid, drawn_lines, turn):
                    turn = 1 - turn
                    frog_grid, nim_grid, drawn_lines, nodes, root_nodes = play_AI_move(frog_grid, nim_grid, drawn_lines, nodes, root_nodes)
                    check_winning_move(frog_grid, nim_grid, drawn_lines, turn)
                if I_colour == 2 and turn == 1 and not check_winning_move(frog_grid, nim_grid, drawn_lines, turn):
                    turn = 1 - turn
                    frog_grid, nim_grid, drawn_lines, nodes, root_nodes = play_AI_move(frog_grid, nim_grid, drawn_lines, nodes, root_nodes)
                    check_winning_move(frog_grid, nim_grid, drawn_lines, turn)


        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # Left mouse button released
                end_pos = event.pos
                if drawing and not highlight == 666:
                    if is_line_ok((start_pos, end_pos)):
                        news, newe = check_if_line_joins(drawn_lines, (start_pos, end_pos))
                        current_colour = highlight
                        if not check_two_roots((news, newe)):
                            drawn_lines.append((news, newe, current_colour))

                        update_root_nodes()
                        update_nodes()
                        nodes, drawn_lines = remove_unconnected_nodes(nodes, drawn_lines, root_nodes)

                      #  print(drawn_lines)
                       # print(nodes)
                       # print(root_nodes)
                    drawing = False
                if highlight == 666 and rotation_state == 2 and not playing:
                    lines_to_remove = []
                    for line in drawn_lines:
                        if intersect(line, (start_pos, end_pos)):
                            if line not in lines_to_remove:
                                lines_to_remove.append(line)
                    for line in lines_to_remove:
                        drawn_lines.remove(line)
                        update_root_nodes()
                        update_nodes()
                        nodes, drawn_lines = remove_unconnected_nodes(nodes, drawn_lines, root_nodes)
                if rotation_state == 2 and playing and goneround1:
                    lines_to_remove = []
                    for line in drawn_lines:
                        linec = convert_line_to_center(line)
                        if intersect(linec, (start_pos, end_pos)):
                            if line not in lines_to_remove:
                                lines_to_remove.append(line)
                    for line in lines_to_remove:
                        if line in drawn_lines and len(lines_to_remove)==1 and line[2] != BLUE and turn == 1:
                            drawn_lines.remove(line)
                            turn = change_turn(turn)
                        if line in drawn_lines and len(lines_to_remove)==1 and line[2] != RED and turn == 0:
                            drawn_lines.remove(line)
                            turn = change_turn(turn)
                        update_root_nodes()
                        update_nodes()
                        nodes, drawn_lines = remove_unconnected_nodes(nodes, drawn_lines, root_nodes)
                        check_winning_move(frog_grid, nim_grid, drawn_lines, turn)
                    if I_colour == 1 and turn == 0 and not check_winning_move(frog_grid, nim_grid, drawn_lines, turn):
                        turn = 1 - turn
                        frog_grid, nim_grid, drawn_lines, nodes, root_nodes = play_AI_move(frog_grid, nim_grid, drawn_lines, nodes, root_nodes)
                        check_winning_move(frog_grid, nim_grid, drawn_lines, turn)
                    if I_colour == 2 and turn == 1 and not check_winning_move(frog_grid, nim_grid, drawn_lines, turn):
                        turn = 1 - turn
                        frog_grid, nim_grid, drawn_lines, nodes, root_nodes = play_AI_move(frog_grid, nim_grid, drawn_lines, nodes, root_nodes)
                        check_winning_move(frog_grid, nim_grid, drawn_lines, turn)



    draw_screens()

    pygame.display.flip()
    pygame.time.Clock().tick(30)
