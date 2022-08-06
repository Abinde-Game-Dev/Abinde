# Abinde Docs

## Before You Continue

Please note this project is still under __heavy development__, which means it will probably change __a lot__. However, all of the versions will be available to install on [__PyPI__](https://pypi.org/project/Abinde).

This project is stable on Debian Linux, Raspberry Pi, and Mac.

Want to be a tester? take a look at [__this__](https://github.com/desvasicek/Abinde/discussions/6)!

## About

Abinde is an open-source wrapper around pygame.

## Install

To install Abinde, you can open your shell and run:

```sh
pip install Abinde
```

### or

```sh
pip3 install Abinde
```

Make sure you have python and pip installed!

## Import

To import Abinde, open your IDE for python and add:

```python
import Abinde as ab
```

## Making a Game

To make the game object you can add:

```python
game = ab.Game(<title>, <width>, <height>, <background-color>)
```
You can replace the parameters with what you want. None of them are neccesary. 

<details><summary>Parameters</summary>
Title is a string for the title of the window, width is an integer for the width of the window, height is also an integer for the height of the window, background-color is an rgb tuple or color object for the background of the window.
</details>

For built in colors, you can see the [colors section](#colors).

## Adding Objects

### Rectangle

You can start with a rectangle, since it is very simple:

```python
my_rect = ab.sprite.Rectangle(<pos>, <size>, <color> <title>)
```

<details><summary>Parameters</summary>
Pos is an int list for the the position of the rectangle, size is an int list for the size of the rectange, color is an rgb tuple or color object, title is a string for the name of the object.
</details>

For built in colors, you can see the [colors section](#colors).

## Simple Drawing

To make a simple drawing:

```python
game = Game()
ellipse = sprite.Ellipse()
line = sprite.Line()
rect = sprite.Rectangle()
game.mainloop()
```

## Loading Images

_Not Documented Yet._

## Colors

<details><summary>All Colors (ABC Order)</summary>


- __ALICEBLUE__
- __ANTIQUEWHITE__
- __ANTIQUEWHITE1__
- __ANTIQUEWHITE2__
- __ANTIQUEWHITE3__
- __ANTIQUEWHITE4__
- __AQUA__
- __AQUAMARINE1__
- __AQUAMARINE2__
- __AQUAMARINE3__
- __AQUAMARINE4__
- __AZURE1__
- __AZURE2__
- __AZURE3__
- __AZURE4__
- __BANANA__
- __BEIGE__
- __BISQUE1__
- __BISQUE2__
- __BISQUE3__
- __BISQUE4__
- __BLACK__
- __BLANCHEDALMOND__
- __BLUE__
- __BLUE2__
- __BLUE3__
- __BLUE4__
- __BLUEVIOLET__
- __BRICK__
- __BROWN__
- __BROWN1__
- __BROWN2__
- __BROWN3__
- __BROWN4__
- __BURLYWOOD__
- __BURLYWOOD1__
- __BURLYWOOD2__
- __BURLYWOOD3__
- __BURLYWOOD4__
- __BURNTSIENNA__
- __BURNTUMBER__
- __CADETBLUE__
- __CADETBLUE1__
- __CADETBLUE2__
- __CADETBLUE3__
- __CADETBLUE4__
- __CADMIUMORANGE__
- __CADMIUMYELLOW__
- __CARROT__
- __CHARTREUSE1__
- __CHARTREUSE2__
- __CHARTREUSE3__
- __CHARTREUSE4__
- __CHOCOLATE__
- __CHOCOLATE1__
- __CHOCOLATE2__
- __CHOCOLATE3__
- __CHOCOLATE4__
- __COBALT__
- __COBALTGREEN__
- __COLDGREY__
- __CORAL__
- __CORAL1__
- __CORAL2__
- __CORAL3__
- __CORAL4__
- __CORNFLOWERBLUE__
- __CORNSILK1__
- __CORNSILK2__
- __CORNSILK3__
- __CORNSILK4__
- __CRIMSON__
- __CYAN2__
- __CYAN3__
- __CYAN4__
- __DARKGOLDENROD__
- __DARKGOLDENROD1__
- __DARKGOLDENROD2__
- __DARKGOLDENROD3__
- __DARKGOLDENROD4__
- __DARKGRAY__
- __DARKGREEN__
- __DARKKHAKI__
- __DARKOLIVEGREEN__
- __DARKOLIVEGREEN1__
- __DARKOLIVEGREEN2__
- __DARKOLIVEGREEN3__
- __DARKOLIVEGREEN4__
- __DARKORANGE__
- __DARKORANGE1__
- __DARKORANGE2__
- __DARKORANGE3__
- __DARKORANGE4__
- __DARKORCHID__
- __DARKORCHID1__
- __DARKORCHID2__
- __DARKORCHID3__
- __DARKORCHID4__
- __DARKSALMON__
- __DARKSEAGREEN__
- __DARKSEAGREEN1__
- __DARKSEAGREEN2__
- __DARKSEAGREEN3__
- __DARKSEAGREEN4__
- __DARKSLATEBLUE__
- __DARKSLATEGRAY__
- __DARKSLATEGRAY1__
- __DARKSLATEGRAY2__
- __DARKSLATEGRAY3__
- __DARKSLATEGRAY4__
- __DARKTURQUOISE__
- __DARKVIOLET__
- __DEEPPINK1__
- __DEEPPINK2__
- __DEEPPINK3__
- __DEEPPINK4__
- __DEEPSKYBLUE1__
- __DEEPSKYBLUE2__
- __DEEPSKYBLUE3__
- __DEEPSKYBLUE4__
- __DIMGRAY__
- __DIMGRAY__
- __DODGERBLUE1__
- __DODGERBLUE2__
- __DODGERBLUE3__
- __DODGERBLUE4__
- __EGGSHELL__
- __EMERALDGREEN__
- __FIREBRICK__
- __FIREBRICK1__
- __FIREBRICK2__
- __FIREBRICK3__
- __FIREBRICK4__
- __FLESH__
- __FLORALWHITE__
- __FORESTGREEN__
- __GAINSBORO__
- __GHOSTWHITE__
- __GOLD1__
- __GOLD2__
- __GOLD3__
- __GOLD4__
- __GOLDENROD__
- __GOLDENROD1__
- __GOLDENROD2__
- __GOLDENROD3__
- __GOLDENROD4__
- __GRAY__
- __GRAY1__
- __GRAY10__
- __GRAY11__
- __GRAY12__
- __GRAY13__
- __GRAY14__
- __GRAY15__
- __GRAY16__
- __GRAY17__
- __GRAY18__
- __GRAY19__
- __GRAY2__
- __GRAY20__
- __GRAY21__
- __GRAY22__
- __GRAY23__
- __GRAY24__
- __GRAY25__
- __GRAY26__
- __GRAY27__
- __GRAY28__
- __GRAY29__
- __GRAY3__
- __GRAY30__
- __GRAY31__
- __GRAY32__
- __GRAY33__
- __GRAY34__
- __GRAY35__
- __GRAY36__
- __GRAY37__
- __GRAY38__
- __GRAY39__
- __GRAY4__
- __GRAY40__
- __GRAY42__
- __GRAY43__
- __GRAY44__
- __GRAY45__
- __GRAY46__
- __GRAY47__
- __GRAY48__
- __GRAY49__
- __GRAY5__
- __GRAY50__
- __GRAY51__
- __GRAY52__
- __GRAY53__
- __GRAY54__
- __GRAY55__
- __GRAY56__
- __GRAY57__
- __GRAY58__
- __GRAY59__
- __GRAY6__
- __GRAY60__
- __GRAY61__
- __GRAY62__
- __GRAY63__
- __GRAY64__
- __GRAY65__
- __GRAY66__
- __GRAY67__
- __GRAY68__
- __GRAY69__
- __GRAY7__
- __GRAY70__
- __GRAY71__
- __GRAY72__
- __GRAY73__
- __GRAY74__
- __GRAY75__
- __GRAY76__
- __GRAY77__
- __GRAY78__
- __GRAY79__
- __GRAY8__
- __GRAY80__
- __GRAY81__
- __GRAY82__
- __GRAY83__
- __GRAY84__
- __GRAY85__
- __GRAY86__
- __GRAY87__
- __GRAY88__
- __GRAY89__
- __GRAY9__
- __GRAY90__
- __GRAY91__
- __GRAY92__
- __GRAY93__
- __GRAY94__
- __GRAY95__
- __GRAY97__
- __GRAY98__
- __GRAY99__
- __GREEN__
- __GREEN1__
- __GREEN2__
- __GREEN3__
- __GREEN4__
- __GREENYELLOW__
- __HONEYDEW1__
- __HONEYDEW2__
- __HONEYDEW3__
- __HONEYDEW4__
- __HOTPINK__
- __HOTPINK1__
- __HOTPINK2__
- __HOTPINK3__
- __HOTPINK4__
- __INDIANRED__
- __INDIANRED__
- __INDIANRED1__
- __INDIANRED2__
- __INDIANRED3__
- __INDIANRED4__
- __INDIGO__
- __IVORY1__
- __IVORY2__
- __IVORY3__
- __IVORY4__
- __IVORYBLACK__
- __KHAKI__
- __KHAKI1__
- __KHAKI2__
- __KHAKI3__
- __KHAKI4__
- __LAVENDER__
- __LAVENDERBLUSH1__
- __LAVENDERBLUSH2__
- __LAVENDERBLUSH3__
- __LAVENDERBLUSH4__
- __LAWNGREEN__
- __LEMONCHIFFON1__
- __LEMONCHIFFON2__
- __LEMONCHIFFON3__
- __LEMONCHIFFON4__
- __LIGHTBLUE__
- __LIGHTBLUE1__
- __LIGHTBLUE2__
- __LIGHTBLUE3__
- __LIGHTBLUE4__
- __LIGHTCORAL__
- __LIGHTCYAN1__
- __LIGHTCYAN2__
- __LIGHTCYAN3__
- __LIGHTCYAN4__
- __LIGHTGOLDENROD1__
- __LIGHTGOLDENROD2__
- __LIGHTGOLDENROD3__
- __LIGHTGOLDENROD4__
- __LIGHTGOLDENRODYELLOW__
- __LIGHTGREY__
- __LIGHTPINK__
- __LIGHTPINK1__
- __LIGHTPINK2__
- __LIGHTPINK3__
- __LIGHTPINK4__
- __LIGHTSALMON1__
- __LIGHTSALMON2__
- __LIGHTSALMON3__
- __LIGHTSALMON4__
- __LIGHTSEAGREEN__
- __LIGHTSKYBLUE__
- __LIGHTSKYBLUE1__
- __LIGHTSKYBLUE2__
- __LIGHTSKYBLUE3__
- __LIGHTSKYBLUE4__
- __LIGHTSLATEBLUE__
- __LIGHTSLATEGRAY__
- __LIGHTSTEELBLUE__
- __LIGHTSTEELBLUE1__
- __LIGHTSTEELBLUE2__
- __LIGHTSTEELBLUE3__
- __LIGHTSTEELBLUE4__
- __LIGHTYELLOW1__
- __LIGHTYELLOW2__
- __LIGHTYELLOW3__
- __LIGHTYELLOW4__
- __LIMEGREEN__
- __LINEN__
- __MAGENTA__
- __MAGENTA2__
- __MAGENTA3__
- __MAGENTA4__
- __MANGANESEBLUE__
- __MAROON__
- __MAROON1__
- __MAROON2__
- __MAROON3__
- __MAROON4__
- __MEDIUMORCHID__
- __MEDIUMORCHID1__
- __MEDIUMORCHID2__
- __MEDIUMORCHID3__
- __MEDIUMORCHID4__
- __MEDIUMPURPLE__
- __MEDIUMPURPLE1__
- __MEDIUMPURPLE2__
- __MEDIUMPURPLE3__
- __MEDIUMPURPLE4__
- __MEDIUMSEAGREEN__
- __MEDIUMSLATEBLUE__
- __MEDIUMSPRINGGREEN__
- __MEDIUMTURQUOISE__
- __MEDIUMVIOLETRED__
- __MELON__
- __MIDNIGHTBLUE__
- __MINT__
- __MINTCREAM__
- __MISTYROSE1__
- __MISTYROSE2__
- __MISTYROSE3__
- __MISTYROSE4__
- __MOCCASIN__
- __NAVAJOWHITE1__
- __NAVAJOWHITE2__
- __NAVAJOWHITE3__
- __NAVAJOWHITE4__
- __NAVY__
- __OLDLACE__
- __OLIVE__
- __OLIVEDRAB__
- __OLIVEDRAB1__
- __OLIVEDRAB2__
- __OLIVEDRAB3__
- __OLIVEDRAB4__
- __ORANGE__
- __ORANGE1__
- __ORANGE2__
- __ORANGE3__
- __ORANGE4__
- __ORANGERED1__
- __ORANGERED2__
- __ORANGERED3__
- __ORANGERED4__
- __ORCHID__
- __ORCHID1__
- __ORCHID2__
- __ORCHID3__
- __ORCHID4__
- __PALEGOLDENROD__
- __PALEGREEN__
- __PALEGREEN1__
- __PALEGREEN2__
- __PALEGREEN3__
- __PALEGREEN4__
- __PALETURQUOISE1__
- __PALETURQUOISE2__
- __PALETURQUOISE3__
- __PALETURQUOISE4__
- __PALEVIOLETRED__
- __PALEVIOLETRED1__
- __PALEVIOLETRED2__
- __PALEVIOLETRED3__
- __PALEVIOLETRED4__
- __PAPAYAWHIP__
- __PEACHPUFF1__
- __PEACHPUFF2__
- __PEACHPUFF3__
- __PEACHPUFF4__
- __PEACOCK__
- __PINK__
- __PINK1__
- __PINK2__
- __PINK3__
- __PINK4__
- __PLUM__
- __PLUM1__
- __PLUM2__
- __PLUM3__
- __PLUM4__
- __POWDERBLUE__
- __PURPLE__
- __PURPLE1__
- __PURPLE2__
- __PURPLE3__
- __PURPLE4__
- __RASPBERRY__
- __RAWSIENNA__
- __RED1__
- __RED2__
- __RED3__
- __RED4__
- __ROSYBROWN__
- __ROSYBROWN1__
- __ROSYBROWN2__
- __ROSYBROWN3__
- __ROSYBROWN4__
- __ROYALBLUE__
- __ROYALBLUE1__
- __ROYALBLUE2__
- __ROYALBLUE3__
- __ROYALBLUE4__
- __SALMON__
- __SALMON1__
- __SALMON2__
- __SALMON3__
- __SALMON4__
- __SANDYBROWN__
- __SAPGREEN__
- __SEAGREEN1__
- __SEAGREEN2__
- __SEAGREEN3__
- __SEAGREEN4__
- __SEASHELL1__
- __SEASHELL2__
- __SEASHELL3__
- __SEASHELL4__
- __SEPIA__
- __SGIBEET__
- __SGIBRIGHTGRAY__
- __SGICHARTREUSE__
- __SGIDARKGRAY__
- __SGIGRAY12__
- __SGIGRAY16__
- __SGIGRAY32__
- __SGIGRAY36__
- __SGIGRAY52__
- __SGIGRAY56__
- __SGIGRAY72__
- __SGIGRAY76__
- __SGIGRAY92__
- __SGIGRAY96__
- __SGILIGHTBLUE__
- __SGILIGHTGRAY__
- __SGIOLIVEDRAB__
- __SGISALMON__
- __SGISLATEBLUE__
- __SGITEAL__
- __SIENNA__
- __SIENNA1__
- __SIENNA2__
- __SIENNA3__
- __SIENNA4__
- __SILVER__
- __SKYBLUE__
- __SKYBLUE1__
- __SKYBLUE2__
- __SKYBLUE3__
- __SKYBLUE4__
- __SLATEBLUE__
- __SLATEBLUE1__
- __SLATEBLUE2__
- __SLATEBLUE3__
- __SLATEBLUE4__
- __SLATEGRAY__
- __SLATEGRAY1__
- __SLATEGRAY2__
- __SLATEGRAY3__
- __SLATEGRAY4__
- __SNOW1__
- __SNOW2__
- __SNOW3__
- __SNOW4__
- __SPRINGGREEN__
- __SPRINGGREEN1__
- __SPRINGGREEN2__
- __SPRINGGREEN3__
- __STEELBLUE__
- __STEELBLUE1__
- __STEELBLUE2__
- __STEELBLUE3__
- __STEELBLUE4__
- __TAN__
- __TAN1__
- __TAN2__
- __TAN3__
- __TAN4__
- __TEAL__
- __THISTLE__
- __THISTLE1__
- __THISTLE2__
- __THISTLE3__
- __THISTLE4__
- __TOMATO1__
- __TOMATO2__
- __TOMATO3__
- __TOMATO4__
- __TURQUOISE__
- __TURQUOISE1__
- __TURQUOISE2__
- __TURQUOISE3__
- __TURQUOISE4__
- __TURQUOISEBLUE__
- __VIOLET__
- __VIOLETRED__
- __VIOLETRED1__
- __VIOLETRED2__
- __VIOLETRED3__
- __VIOLETRED4__
- __WARMGREY__
- __WHEAT__
- __WHEAT1__
- __WHEAT2__
- __WHEAT3__
- __WHEAT4__
- __WHITE__
- __WHITESMOKE__
- __WHITESMOKE__
- __YELLOW1__
- __YELLOW2__
- __YELLOW3__
- __YELLOW4__


</details>