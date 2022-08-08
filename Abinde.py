# Abinde python game-engine
# Copyright 2022 MIT License desvasicek

from PIL import Image as PILImage
import pygame
from pygame.locals import *
import time, random
import warnings
from pygame import mixer

pygame.init()
mixer.init()
pygame.font.init()

windows = []
players = []
drawings = []
_text = []
_objects = []

warnings.simplefilter("once")

enemies = pygame.sprite.Group()
objects = pygame.sprite.Group()

game_quit = False

class color:
    """All the colors"""
    ALICEBLUE = (240, 248, 255)
    ANTIQUEWHITE = (250, 235, 215)
    ANTIQUEWHITE1 = (255, 239, 219)
    ANTIQUEWHITE2 = (238, 223, 204)
    ANTIQUEWHITE3 = (205, 192, 176)
    ANTIQUEWHITE4 = (139, 131, 120)
    AQUA = (0, 255, 255)
    AQUAMARINE1 = (127, 255, 212)
    AQUAMARINE2 = (118, 238, 198)
    AQUAMARINE3 = (102, 205, 170)
    AQUAMARINE4 = (69, 139, 116)
    AZURE1 = (240, 255, 255)
    AZURE2 = (224, 238, 238)
    AZURE3 = (193, 205, 205)
    AZURE4 = (131, 139, 139)
    BANANA = (227, 207, 87)
    BEIGE = (245, 245, 220)
    BISQUE1 = (255, 228, 196)
    BISQUE2 = (238, 213, 183)
    BISQUE3 = (205, 183, 158)
    BISQUE4 = (139, 125, 107)
    BLACK = (0, 0, 0)
    BLANCHEDALMOND = (255, 235, 205)
    BLUE = (0, 0, 255)
    BLUE2 = (0, 0, 238)
    BLUE3 = (0, 0, 205)
    BLUE4 = (0, 0, 139)
    BLUEVIOLET = (138, 43, 226)
    BRICK = (156, 102, 31)
    BROWN = (165, 42, 42)
    BROWN1 = (255, 64, 64)
    BROWN2 = (238, 59, 59)
    BROWN3 = (205, 51, 51)
    BROWN4 = (139, 35, 35)
    BURLYWOOD = (222, 184, 135)
    BURLYWOOD1 = (255, 211, 155)
    BURLYWOOD2 = (238, 197, 145)
    BURLYWOOD3 = (205, 170, 125)
    BURLYWOOD4 = (139, 115, 85)
    BURNTSIENNA = (138, 54, 15)
    BURNTUMBER = (138, 51, 36)
    CADETBLUE = (95, 158, 160)
    CADETBLUE1 = (152, 245, 255)
    CADETBLUE2 = (142, 229, 238)
    CADETBLUE3 = (122, 197, 205)
    CADETBLUE4 = (83, 134, 139)
    CADMIUMORANGE = (255, 97, 3)
    CADMIUMYELLOW = (255, 153, 18)
    CARROT = (237, 145, 33)
    CHARTREUSE1 = (127, 255, 0)
    CHARTREUSE2 = (118, 238, 0)
    CHARTREUSE3 = (102, 205, 0)
    CHARTREUSE4 = (69, 139, 0)
    CHOCOLATE = (210, 105, 30)
    CHOCOLATE1 = (255, 127, 36)
    CHOCOLATE2 = (238, 118, 33)
    CHOCOLATE3 = (205, 102, 29)
    CHOCOLATE4 = (139, 69, 19)
    COBALT = (61, 89, 171)
    COBALTGREEN = (61, 145, 64)
    COLDGREY = (128, 138, 135)
    CORAL = (255, 127, 80)
    CORAL1 = (255, 114, 86)
    CORAL2 = (238, 106, 80)
    CORAL3 = (205, 91, 69)
    CORAL4 = (139, 62, 47)
    CORNFLOWERBLUE = (100, 149, 237)
    CORNSILK1 = (255, 248, 220)
    CORNSILK2 = (238, 232, 205)
    CORNSILK3 = (205, 200, 177)
    CORNSILK4 = (139, 136, 120)
    CRIMSON = (220, 20, 60)
    CYAN2 = (0, 238, 238)
    CYAN3 = (0, 205, 205)
    CYAN4 = (0, 139, 139)
    DARKGOLDENROD = (184, 134, 11)
    DARKGOLDENROD1 = (255, 185, 15)
    DARKGOLDENROD2 = (238, 173, 14)
    DARKGOLDENROD3 = (205, 149, 12)
    DARKGOLDENROD4 = (139, 101, 8)
    DARKGRAY = (169, 169, 169)
    DARKGREEN = (0, 100, 0)
    DARKKHAKI = (189, 183, 107)
    DARKOLIVEGREEN = (85, 107, 47)
    DARKOLIVEGREEN1 = (202, 255, 112)
    DARKOLIVEGREEN2 = (188, 238, 104)
    DARKOLIVEGREEN3 = (162, 205, 90)
    DARKOLIVEGREEN4 = (110, 139, 61)
    DARKORANGE = (255, 140, 0)
    DARKORANGE1 = (255, 127, 0)
    DARKORANGE2 = (238, 118, 0)
    DARKORANGE3 = (205, 102, 0)
    DARKORANGE4 = (139, 69, 0)
    DARKORCHID = (153, 50, 204)
    DARKORCHID1 = (191, 62, 255)
    DARKORCHID2 = (178, 58, 238)
    DARKORCHID3 = (154, 50, 205)
    DARKORCHID4 = (104, 34, 139)
    DARKSALMON = (233, 150, 122)
    DARKSEAGREEN = (143, 188, 143)
    DARKSEAGREEN1 = (193, 255, 193)
    DARKSEAGREEN2 = (180, 238, 180)
    DARKSEAGREEN3 = (155, 205, 155)
    DARKSEAGREEN4 = (105, 139, 105)
    DARKSLATEBLUE = (72, 61, 139)
    DARKSLATEGRAY = (47, 79, 79)
    DARKSLATEGRAY1 = (151, 255, 255)
    DARKSLATEGRAY2 = (141, 238, 238)
    DARKSLATEGRAY3 = (121, 205, 205)
    DARKSLATEGRAY4 = (82, 139, 139)
    DARKTURQUOISE = (0, 206, 209)
    DARKVIOLET = (148, 0, 211)
    DEEPPINK1 = (255, 20, 147)
    DEEPPINK2 = (238, 18, 137)
    DEEPPINK3 = (205, 16, 118)
    DEEPPINK4 = (139, 10, 80)
    DEEPSKYBLUE1 = (0, 191, 255)
    DEEPSKYBLUE2 = (0, 178, 238)
    DEEPSKYBLUE3 = (0, 154, 205)
    DEEPSKYBLUE4 = (0, 104, 139)
    DIMGRAY = (105, 105, 105)
    DIMGRAY = (105, 105, 105)
    DODGERBLUE1 = (30, 144, 255)
    DODGERBLUE2 = (28, 134, 238)
    DODGERBLUE3 = (24, 116, 205)
    DODGERBLUE4 = (16, 78, 139)
    EGGSHELL = (252, 230, 201)
    EMERALDGREEN = (0, 201, 87)
    FIREBRICK = (178, 34, 34)
    FIREBRICK1 = (255, 48, 48)
    FIREBRICK2 = (238, 44, 44)
    FIREBRICK3 = (205, 38, 38)
    FIREBRICK4 = (139, 26, 26)
    FLESH = (255, 125, 64)
    FLORALWHITE = (255, 250, 240)
    FORESTGREEN = (34, 139, 34)
    GAINSBORO = (220, 220, 220)
    GHOSTWHITE = (248, 248, 255)
    GOLD1 = (255, 215, 0)
    GOLD2 = (238, 201, 0)
    GOLD3 = (205, 173, 0)
    GOLD4 = (139, 117, 0)
    GOLDENROD = (218, 165, 32)
    GOLDENROD1 = (255, 193, 37)
    GOLDENROD2 = (238, 180, 34)
    GOLDENROD3 = (205, 155, 29)
    GOLDENROD4 = (139, 105, 20)
    GRAY = (128, 128, 128)
    GRAY1 = (3, 3, 3)
    GRAY10 = (26, 26, 26)
    GRAY11 = (28, 28, 28)
    GRAY12 = (31, 31, 31)
    GRAY13 = (33, 33, 33)
    GRAY14 = (36, 36, 36)
    GRAY15 = (38, 38, 38)
    GRAY16 = (41, 41, 41)
    GRAY17 = (43, 43, 43)
    GRAY18 = (46, 46, 46)
    GRAY19 = (48, 48, 48)
    GRAY2 = (5, 5, 5)
    GRAY20 = (51, 51, 51)
    GRAY21 = (54, 54, 54)
    GRAY22 = (56, 56, 56)
    GRAY23 = (59, 59, 59)
    GRAY24 = (61, 61, 61)
    GRAY25 = (64, 64, 64)
    GRAY26 = (66, 66, 66)
    GRAY27 = (69, 69, 69)
    GRAY28 = (71, 71, 71)
    GRAY29 = (74, 74, 74)
    GRAY3 = (8, 8, 8)
    GRAY30 = (77, 77, 77)
    GRAY31 = (79, 79, 79)
    GRAY32 = (82, 82, 82)
    GRAY33 = (84, 84, 84)
    GRAY34 = (87, 87, 87)
    GRAY35 = (89, 89, 89)
    GRAY36 = (92, 92, 92)
    GRAY37 = (94, 94, 94)
    GRAY38 = (97, 97, 97)
    GRAY39 = (99, 99, 99)
    GRAY4 = (10, 10, 10)
    GRAY40 = (102, 102, 102)
    GRAY42 = (107, 107, 107)
    GRAY43 = (110, 110, 110)
    GRAY44 = (112, 112, 112)
    GRAY45 = (115, 115, 115)
    GRAY46 = (117, 117, 117)
    GRAY47 = (120, 120, 120)
    GRAY48 = (122, 122, 122)
    GRAY49 = (125, 125, 125)
    GRAY5 = (13, 13, 13)
    GRAY50 = (127, 127, 127)
    GRAY51 = (130, 130, 130)
    GRAY52 = (133, 133, 133)
    GRAY53 = (135, 135, 135)
    GRAY54 = (138, 138, 138)
    GRAY55 = (140, 140, 140)
    GRAY56 = (143, 143, 143)
    GRAY57 = (145, 145, 145)
    GRAY58 = (148, 148, 148)
    GRAY59 = (150, 150, 150)
    GRAY6 = (15, 15, 15)
    GRAY60 = (153, 153, 153)
    GRAY61 = (156, 156, 156)
    GRAY62 = (158, 158, 158)
    GRAY63 = (161, 161, 161)
    GRAY64 = (163, 163, 163)
    GRAY65 = (166, 166, 166)
    GRAY66 = (168, 168, 168)
    GRAY67 = (171, 171, 171)
    GRAY68 = (173, 173, 173)
    GRAY69 = (176, 176, 176)
    GRAY7 = (18, 18, 18)
    GRAY70 = (179, 179, 179)
    GRAY71 = (181, 181, 181)
    GRAY72 = (184, 184, 184)
    GRAY73 = (186, 186, 186)
    GRAY74 = (189, 189, 189)
    GRAY75 = (191, 191, 191)
    GRAY76 = (194, 194, 194)
    GRAY77 = (196, 196, 196)
    GRAY78 = (199, 199, 199)
    GRAY79 = (201, 201, 201)
    GRAY8 = (20, 20, 20)
    GRAY80 = (204, 204, 204)
    GRAY81 = (207, 207, 207)
    GRAY82 = (209, 209, 209)
    GRAY83 = (212, 212, 212)
    GRAY84 = (214, 214, 214)
    GRAY85 = (217, 217, 217)
    GRAY86 = (219, 219, 219)
    GRAY87 = (222, 222, 222)
    GRAY88 = (224, 224, 224)
    GRAY89 = (227, 227, 227)
    GRAY9 = (23, 23, 23)
    GRAY90 = (229, 229, 229)
    GRAY91 = (232, 232, 232)
    GRAY92 = (235, 235, 235)
    GRAY93 = (237, 237, 237)
    GRAY94 = (240, 240, 240)
    GRAY95 = (242, 242, 242)
    GRAY97 = (247, 247, 247)
    GRAY98 = (250, 250, 250)
    GRAY99 = (252, 252, 252)
    GREEN = (0, 128, 0)
    GREEN1 = (0, 255, 0)
    GREEN2 = (0, 238, 0)
    GREEN3 = (0, 205, 0)
    GREEN4 = (0, 139, 0)
    GREENYELLOW = (173, 255, 47)
    HONEYDEW1 = (240, 255, 240)
    HONEYDEW2 = (224, 238, 224)
    HONEYDEW3 = (193, 205, 193)
    HONEYDEW4 = (131, 139, 131)
    HOTPINK = (255, 105, 180)
    HOTPINK1 = (255, 110, 180)
    HOTPINK2 = (238, 106, 167)
    HOTPINK3 = (205, 96, 144)
    HOTPINK4 = (139, 58, 98)
    INDIANRED = (176, 23, 31)
    INDIANRED = (205, 92, 92)
    INDIANRED1 = (255, 106, 106)
    INDIANRED2 = (238, 99, 99)
    INDIANRED3 = (205, 85, 85)
    INDIANRED4 = (139, 58, 58)
    INDIGO = (75, 0, 130)
    IVORY1 = (255, 255, 240)
    IVORY2 = (238, 238, 224)
    IVORY3 = (205, 205, 193)
    IVORY4 = (139, 139, 131)
    IVORYBLACK = (41, 36, 33)
    KHAKI = (240, 230, 140)
    KHAKI1 = (255, 246, 143)
    KHAKI2 = (238, 230, 133)
    KHAKI3 = (205, 198, 115)
    KHAKI4 = (139, 134, 78)
    LAVENDER = (230, 230, 250)
    LAVENDERBLUSH1 = (255, 240, 245)
    LAVENDERBLUSH2 = (238, 224, 229)
    LAVENDERBLUSH3 = (205, 193, 197)
    LAVENDERBLUSH4 = (139, 131, 134)
    LAWNGREEN = (124, 252, 0)
    LEMONCHIFFON1 = (255, 250, 205)
    LEMONCHIFFON2 = (238, 233, 191)
    LEMONCHIFFON3 = (205, 201, 165)
    LEMONCHIFFON4 = (139, 137, 112)
    LIGHTBLUE = (173, 216, 230)
    LIGHTBLUE1 = (191, 239, 255)
    LIGHTBLUE2 = (178, 223, 238)
    LIGHTBLUE3 = (154, 192, 205)
    LIGHTBLUE4 = (104, 131, 139)
    LIGHTCORAL = (240, 128, 128)
    LIGHTCYAN1 = (224, 255, 255)
    LIGHTCYAN2 = (209, 238, 238)
    LIGHTCYAN3 = (180, 205, 205)
    LIGHTCYAN4 = (122, 139, 139)
    LIGHTGOLDENROD1 = (255, 236, 139)
    LIGHTGOLDENROD2 = (238, 220, 130)
    LIGHTGOLDENROD3 = (205, 190, 112)
    LIGHTGOLDENROD4 = (139, 129, 76)
    LIGHTGOLDENRODYELLOW = (250, 250, 210)
    LIGHTGREY = (211, 211, 211)
    LIGHTPINK = (255, 182, 193)
    LIGHTPINK1 = (255, 174, 185)
    LIGHTPINK2 = (238, 162, 173)
    LIGHTPINK3 = (205, 140, 149)
    LIGHTPINK4 = (139, 95, 101)
    LIGHTSALMON1 = (255, 160, 122)
    LIGHTSALMON2 = (238, 149, 114)
    LIGHTSALMON3 = (205, 129, 98)
    LIGHTSALMON4 = (139, 87, 66)
    LIGHTSEAGREEN = (32, 178, 170)
    LIGHTSKYBLUE = (135, 206, 250)
    LIGHTSKYBLUE1 = (176, 226, 255)
    LIGHTSKYBLUE2 = (164, 211, 238)
    LIGHTSKYBLUE3 = (141, 182, 205)
    LIGHTSKYBLUE4 = (96, 123, 139)
    LIGHTSLATEBLUE = (132, 112, 255)
    LIGHTSLATEGRAY = (119, 136, 153)
    LIGHTSTEELBLUE = (176, 196, 222)
    LIGHTSTEELBLUE1 = (202, 225, 255)
    LIGHTSTEELBLUE2 = (188, 210, 238)
    LIGHTSTEELBLUE3 = (162, 181, 205)
    LIGHTSTEELBLUE4 = (110, 123, 139)
    LIGHTYELLOW1 = (255, 255, 224)
    LIGHTYELLOW2 = (238, 238, 209)
    LIGHTYELLOW3 = (205, 205, 180)
    LIGHTYELLOW4 = (139, 139, 122)
    LIMEGREEN = (50, 205, 50)
    LINEN = (250, 240, 230)
    MAGENTA = (255, 0, 255)
    MAGENTA2 = (238, 0, 238)
    MAGENTA3 = (205, 0, 205)
    MAGENTA4 = (139, 0, 139)
    MANGANESEBLUE = (3, 168, 158)
    MAROON = (128, 0, 0)
    MAROON1 = (255, 52, 179)
    MAROON2 = (238, 48, 167)
    MAROON3 = (205, 41, 144)
    MAROON4 = (139, 28, 98)
    MEDIUMORCHID = (186, 85, 211)
    MEDIUMORCHID1 = (224, 102, 255)
    MEDIUMORCHID2 = (209, 95, 238)
    MEDIUMORCHID3 = (180, 82, 205)
    MEDIUMORCHID4 = (122, 55, 139)
    MEDIUMPURPLE = (147, 112, 219)
    MEDIUMPURPLE1 = (171, 130, 255)
    MEDIUMPURPLE2 = (159, 121, 238)
    MEDIUMPURPLE3 = (137, 104, 205)
    MEDIUMPURPLE4 = (93, 71, 139)
    MEDIUMSEAGREEN = (60, 179, 113)
    MEDIUMSLATEBLUE = (123, 104, 238)
    MEDIUMSPRINGGREEN = (0, 250, 154)
    MEDIUMTURQUOISE = (72, 209, 204)
    MEDIUMVIOLETRED = (199, 21, 133)
    MELON = (227, 168, 105)
    MIDNIGHTBLUE = (25, 25, 112)
    MINT = (189, 252, 201)
    MINTCREAM = (245, 255, 250)
    MISTYROSE1 = (255, 228, 225)
    MISTYROSE2 = (238, 213, 210)
    MISTYROSE3 = (205, 183, 181)
    MISTYROSE4 = (139, 125, 123)
    MOCCASIN = (255, 228, 181)
    NAVAJOWHITE1 = (255, 222, 173)
    NAVAJOWHITE2 = (238, 207, 161)
    NAVAJOWHITE3 = (205, 179, 139)
    NAVAJOWHITE4 = (139, 121, 94)
    NAVY = (0, 0, 128)
    OLDLACE = (253, 245, 230)
    OLIVE = (128, 128, 0)
    OLIVEDRAB = (107, 142, 35)
    OLIVEDRAB1 = (192, 255, 62)
    OLIVEDRAB2 = (179, 238, 58)
    OLIVEDRAB3 = (154, 205, 50)
    OLIVEDRAB4 = (105, 139, 34)
    ORANGE = (255, 128, 0)
    ORANGE1 = (255, 165, 0)
    ORANGE2 = (238, 154, 0)
    ORANGE3 = (205, 133, 0)
    ORANGE4 = (139, 90, 0)
    ORANGERED1 = (255, 69, 0)
    ORANGERED2 = (238, 64, 0)
    ORANGERED3 = (205, 55, 0)
    ORANGERED4 = (139, 37, 0)
    ORCHID = (218, 112, 214)
    ORCHID1 = (255, 131, 250)
    ORCHID2 = (238, 122, 233)
    ORCHID3 = (205, 105, 201)
    ORCHID4 = (139, 71, 137)
    PALEGOLDENROD = (238, 232, 170)
    PALEGREEN = (152, 251, 152)
    PALEGREEN1 = (154, 255, 154)
    PALEGREEN2 = (144, 238, 144)
    PALEGREEN3 = (124, 205, 124)
    PALEGREEN4 = (84, 139, 84)
    PALETURQUOISE1 = (187, 255, 255)
    PALETURQUOISE2 = (174, 238, 238)
    PALETURQUOISE3 = (150, 205, 205)
    PALETURQUOISE4 = (102, 139, 139)
    PALEVIOLETRED = (219, 112, 147)
    PALEVIOLETRED1 = (255, 130, 171)
    PALEVIOLETRED2 = (238, 121, 159)
    PALEVIOLETRED3 = (205, 104, 137)
    PALEVIOLETRED4 = (139, 71, 93)
    PAPAYAWHIP = (255, 239, 213)
    PEACHPUFF1 = (255, 218, 185)
    PEACHPUFF2 = (238, 203, 173)
    PEACHPUFF3 = (205, 175, 149)
    PEACHPUFF4 = (139, 119, 101)
    PEACOCK = (51, 161, 201)
    PINK = (255, 192, 203)
    PINK1 = (255, 181, 197)
    PINK2 = (238, 169, 184)
    PINK3 = (205, 145, 158)
    PINK4 = (139, 99, 108)
    PLUM = (221, 160, 221)
    PLUM1 = (255, 187, 255)
    PLUM2 = (238, 174, 238)
    PLUM3 = (205, 150, 205)
    PLUM4 = (139, 102, 139)
    POWDERBLUE = (176, 224, 230)
    PURPLE = (128, 0, 128)
    PURPLE1 = (155, 48, 255)
    PURPLE2 = (145, 44, 238)
    PURPLE3 = (125, 38, 205)
    PURPLE4 = (85, 26, 139)
    RASPBERRY = (135, 38, 87)
    RAWSIENNA = (199, 97, 20)
    RED1 = (255, 0, 0)
    RED2 = (238, 0, 0)
    RED3 = (205, 0, 0)
    RED4 = (139, 0, 0)
    ROSYBROWN = (188, 143, 143)
    ROSYBROWN1 = (255, 193, 193)
    ROSYBROWN2 = (238, 180, 180)
    ROSYBROWN3 = (205, 155, 155)
    ROSYBROWN4 = (139, 105, 105)
    ROYALBLUE = (65, 105, 225)
    ROYALBLUE1 = (72, 118, 255)
    ROYALBLUE2 = (67, 110, 238)
    ROYALBLUE3 = (58, 95, 205)
    ROYALBLUE4 = (39, 64, 139)
    SALMON = (250, 128, 114)
    SALMON1 = (255, 140, 105)
    SALMON2 = (238, 130, 98)
    SALMON3 = (205, 112, 84)
    SALMON4 = (139, 76, 57)
    SANDYBROWN = (244, 164, 96)
    SAPGREEN = (48, 128, 20)
    SEAGREEN1 = (84, 255, 159)
    SEAGREEN2 = (78, 238, 148)
    SEAGREEN3 = (67, 205, 128)
    SEAGREEN4 = (46, 139, 87)
    SEASHELL1 = (255, 245, 238)
    SEASHELL2 = (238, 229, 222)
    SEASHELL3 = (205, 197, 191)
    SEASHELL4 = (139, 134, 130)
    SEPIA = (94, 38, 18)
    SGIBEET = (142, 56, 142)
    SGIBRIGHTGRAY = (197, 193, 170)
    SGICHARTREUSE = (113, 198, 113)
    SGIDARKGRAY = (85, 85, 85)
    SGIGRAY12 = (30, 30, 30)
    SGIGRAY16 = (40, 40, 40)
    SGIGRAY32 = (81, 81, 81)
    SGIGRAY36 = (91, 91, 91)
    SGIGRAY52 = (132, 132, 132)
    SGIGRAY56 = (142, 142, 142)
    SGIGRAY72 = (183, 183, 183)
    SGIGRAY76 = (193, 193, 193)
    SGIGRAY92 = (234, 234, 234)
    SGIGRAY96 = (244, 244, 244)
    SGILIGHTBLUE = (125, 158, 192)
    SGILIGHTGRAY = (170, 170, 170)
    SGIOLIVEDRAB = (142, 142, 56)
    SGISALMON = (198, 113, 113)
    SGISLATEBLUE = (113, 113, 198)
    SGITEAL = (56, 142, 142)
    SIENNA = (160, 82, 45)
    SIENNA1 = (255, 130, 71)
    SIENNA2 = (238, 121, 66)
    SIENNA3 = (205, 104, 57)
    SIENNA4 = (139, 71, 38)
    SILVER = (192, 192, 192)
    SKYBLUE = (135, 206, 235)
    SKYBLUE1 = (135, 206, 255)
    SKYBLUE2 = (126, 192, 238)
    SKYBLUE3 = (108, 166, 205)
    SKYBLUE4 = (74, 112, 139)
    SLATEBLUE = (106, 90, 205)
    SLATEBLUE1 = (131, 111, 255)
    SLATEBLUE2 = (122, 103, 238)
    SLATEBLUE3 = (105, 89, 205)
    SLATEBLUE4 = (71, 60, 139)
    SLATEGRAY = (112, 128, 144)
    SLATEGRAY1 = (198, 226, 255)
    SLATEGRAY2 = (185, 211, 238)
    SLATEGRAY3 = (159, 182, 205)
    SLATEGRAY4 = (108, 123, 139)
    SNOW1 = (255, 250, 250)
    SNOW2 = (238, 233, 233)
    SNOW3 = (205, 201, 201)
    SNOW4 = (139, 137, 137)
    SPRINGGREEN = (0, 255, 127)
    SPRINGGREEN1 = (0, 238, 118)
    SPRINGGREEN2 = (0, 205, 102)
    SPRINGGREEN3 = (0, 139, 69)
    STEELBLUE = (70, 130, 180)
    STEELBLUE1 = (99, 184, 255)
    STEELBLUE2 = (92, 172, 238)
    STEELBLUE3 = (79, 148, 205)
    STEELBLUE4 = (54, 100, 139)
    TAN = (210, 180, 140)
    TAN1 = (255, 165, 79)
    TAN2 = (238, 154, 73)
    TAN3 = (205, 133, 63)
    TAN4 = (139, 90, 43)
    TEAL = (0, 128, 128)
    THISTLE = (216, 191, 216)
    THISTLE1 = (255, 225, 255)
    THISTLE2 = (238, 210, 238)
    THISTLE3 = (205, 181, 205)
    THISTLE4 = (139, 123, 139)
    TOMATO1 = (255, 99, 71)
    TOMATO2 = (238, 92, 66)
    TOMATO3 = (205, 79, 57)
    TOMATO4 = (139, 54, 38)
    TURQUOISE = (64, 224, 208)
    TURQUOISE1 = (0, 245, 255)
    TURQUOISE2 = (0, 229, 238)
    TURQUOISE3 = (0, 197, 205)
    TURQUOISE4 = (0, 134, 139)
    TURQUOISEBLUE = (0, 199, 140)
    VIOLET = (238, 130, 238)
    VIOLETRED = (208, 32, 144)
    VIOLETRED1 = (255, 62, 150)
    VIOLETRED2 = (238, 58, 140)
    VIOLETRED3 = (205, 50, 120)
    VIOLETRED4 = (139, 34, 82)
    WARMGREY = (128, 128, 105)
    WHEAT = (245, 222, 179)
    WHEAT1 = (255, 231, 186)
    WHEAT2 = (238, 216, 174)
    WHEAT3 = (205, 186, 150)
    WHEAT4 = (139, 126, 102)
    WHITE = (255, 255, 255)
    WHITESMOKE = (245, 245, 245)
    WHITESMOKE = (245, 245, 245)
    YELLOW1 = (255, 255, 0)
    YELLOW2 = (238, 238, 0)
    YELLOW3 = (205, 205, 0)
    YELLOW4 = (139, 139, 0)

def pil_image_to_surface(pilImage):
    """
    Not for development use.
    """
    return pygame.image.fromstring(
        pilImage.tobytes(), pilImage.size, pilImage.mode).convert()

def LoadImage(path, mode="PIL"):
    """
    Load an image
    """
    if mode == "PIL":
        return pil_image_to_surface(PILImage.open(path))
    elif mode == "pygame":
        return pygame.image.load(path)
    else:
        raise error.SetModeError
        
        
class error:
    
    class TitleError(Exception):
        def __init__(self):
            super().__init__("Title must be single-line string.")

    class BackgroundError(Exception):
        def __init__(self):
            super().__init__("Background must be rgb tuple.")

    class SizeError(Exception):
        def __init__(self):
            super().__init__("Width and height must be integers.")
    class MultipleInstanceError(Exception):
        def __init__(self):
            super().__init__("You can only have 1 window open at once.")
    class ImageError(Exception):
        def __init__(self):
            super().__init__("Use Image class for sprite images.")
    class MultiplePlayerError(Exception):
        def __init__(self):
            super().__init__("You can only have 1 player object in use at once.")
    class SetModeError(Exception):
        def __init__(self):
            super().__init__("Only options 'PIL' and 'pygame' are supported.")
    class JumpError(Exception):
        def __init__(self):
            super().__init__("Jump height must be less than 150.")

class warn:
    
    class ImageWarning(DeprecationWarning):
        def __init__(self):
            warnings.warn("Using anything other than the Image class is highly advised against.", DeprecationWarning)
    

class Game(object):
    """
    Create the window object.
    """
    def __init__(self, title="New Abinde Instance", width=500, height=600, bg=color.BLACK):
        global windows
        try:
            if len(windows) <= 1:
                self.root = pygame.display.set_mode((width, height))
            else:
                raise error.MultipleInstanceError
        except:
            raise error.SizeError
        try:
            pygame.display.set_caption(title)
        except:
            raise error.TitleError
        self.fps = pygame.time.Clock()
        self.looping = True
        self.bg = bg
        self.root.fill(bg)
        windows.append(self)
        
    def loop(self):
        """
        Not for development use.
        """
        try:
            global game_quit
            while self.looping:
                if not game_quit:
                    try:
                        self.root.fill(self.bg)
                    except:
                        raise error.BackgroundError
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            game_quit = True
                            self.looping = False
                    for player in players:
                        player.move()
                        player.draw(self)
                    for drawing in drawings:
                        drawing.draw(self)
                    for _object in _objects:
                        _object.draw(self)
                    for text in _text:
                        text.draw(self)
                    pygame.display.flip()
                    self.fps.tick(60)
        except Exception as e:
             print(e)

    def mainloop(self):
        """
        Start the window
        """
        
        self.looping = True
        # To fix bug on mac run loop on Main Thread.
        self.loop()
        

class sprite:
    class Player(pygame.sprite.Sprite):
        """
        User-playable object
        """
        def __init__(self, image, pos=[20, 20], title="Sprite", FRIC=0.9, ACC=1, GRAV=1, jumpheight=10):
            super().__init__()
            global players
            players.append(self)
            if not len(players) <= 1:
                raise error.MultiplePlayerError
            try:
                self.image = image
            except:
                warn.ImageWarning()
            self.rect = self.image.get_rect()
            self.title = title
            self.VEL = [0, 0]
            self.ACC = ACC
            self.FRIC = FRIC
            self.GRAV = GRAV
            self.pos = pos
            if not jumpheight > 150:
                self.jumpheight = jumpheight
            else:
                raise error.JumpError
            self.rect.center = self.pos
            self.falling = True
            
        def move(self):
            """
            Not for development use.
            """
            self.k_pressed = pygame.key.get_pressed()
            if self.k_pressed[K_LEFT]:
                self.VEL[0] -= self.ACC
            if self.k_pressed[K_RIGHT]:
                self.VEL[0] += self.ACC
            if self.k_pressed[K_UP]:
                if not self.falling:
                    self.VEL[1] = -self.jumpheight
                    self.falling = True
            self.VEL[0] *= self.FRIC
            self.VEL[1] += self.GRAV
            if pygame.sprite.spritecollideany(self, objects):
                if self.VEL[1] > 0:
                    self.VEL[1] = 0
                    self.falling = False
            self.rect.move_ip(self.VEL[0], self.VEL[1])
            
        def draw(self, game):
            """
            Not for development use.
            """
            game.root.blit(self.image, self.rect)
                
        def kill(self):
            """
            Remove the sprite
            """
            players.remove(self)
            del self


         # DO NOT USE
         
    class Enemy(pygame.sprite.Sprite):
        """
        Enemy object that can hurt the player
        """
        def __init__(self, image, pos=[20, 20], title="Enemy", FRIC=0.9, ACC=1, GRAV=1, jumpheight=10):
            super().__init__()
            global enemies
            enemies.add(self)

        # END DO NOT USE

            
    class Object(pygame.sprite.Sprite):
        """
        Platforms.
        """
        def __init__(self, image, pos=[20, 20], title="Object"):
            super().__init__()
            global objects, _objects
            objects.add(self)
            _objects.append(self)
            self.image = image
            self.pos = pos
            self.title = title
            self.rect = self.image.get_rect()
            self.rect.center = self.pos
        def draw(self, game):
            game.root.blit(self.image, self.rect)

            
    class Rectangle(object):
        """
        Draw a rectangle
        """
        def __init__(self, pos=[40, 40], size=[50, 50], color=color.WHITE, title="Rectangle"):
            self._x = pos[0]
            self._y = pos[1]
            self._width = size[0]
            self._height = size[1]
            self.color = color
            self.title = title
            drawings.append(self)
            self.rect = pygame.Rect(self._x, self._y, self._width, self._height)
            
        def draw(self, game):
            pygame.draw.rect(game.root, self.color, self.rect)
        def returntitle(self):
            return self.title

            
    class Line(object):
        """
        Draw a line
        """
        def __init__(self, pos=[0, 0], length=[50, 50], color=color.WHITE, title="Line"):
            self._x = pos[0]
            self._y = pos[1]
            self._start = length[0]
            self._end = length[1]
            self.color = color
            self.title = title
            drawings.append(self)
            
        def draw(self, game):
            pygame.draw.line(game.root, self.color, [self._x, self._y], [self._start, self._end])
        def returntitle(self):
            return self.title

            
    class Ellipse(object):
        """
        Draw an ellipse
        """
        def __init__(self, pos=[80, 80], size=[50, 50], color=color.WHITE, title="Ellipse"):
            self._x = pos[0]
            self._y = pos[1]
            self._width = size[0]
            self._height = size[1]
            self.color = color
            self.title = title
            drawings.append(self)
            
        def draw(self, game):
            pygame.draw.ellipse(game.root, self.color, (self._x, self._y, self._width, self._height))
        def returntitle(self):
            return self.title

        
    class Text(object):
        def __init__(self, fontname, text, fontsize=30, pos=(10, 10), color=color.WHITE):
            global _text
            self.font = pygame.font.SysFont(fontname, fontsize)
            self.root = self.font.render(text, False, color)
            self.pos = pos
            _text.append(self)
            
        def draw(self, game):
            game.root.blit(self.root, self.pos)


class Audio:
    def __init__(self, file, volume=0.7):
        mixer.music.load(file)
        mixer.music.set_volume(volume)
    def play(self):
        mixer.music.play()
    def pause(self):
        mixer.music.pause()
    def unpause(self):
        mixer.music.unpause()



game = Game(width=1000, height=1000)
player = sprite.Player(LoadImage("Abinde.png"), jumpheight=150, ACC=6, FRIC=.9)
_object = sprite.Object(LoadImage("Abinde.png"), pos=[500, 1100])
game.mainloop()
