# Abinde Docs

## Before You Continue

Please note this project is still under __heavy development__, which means it will probably change __a lot__. However, all of the versions will be available to install on [__PyPI__](https://pypi.org/project/Abinde).

This project is stable on Debian Linux, Raspberry Pi, and Mac.

Want to be a tester? take a look at [__this__](https://github.com/orgs/Abinde-Game-Dev/teams/testers/)!

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


<li><b>ALICEBLUE</b></li>
<li><b>ANTIQUEWHITE</b></li>
<li><b>ANTIQUEWHITE1</b></li>
<li><b>ANTIQUEWHITE2</b></li>
<li><b>ANTIQUEWHITE3</b></li>
<li><b>ANTIQUEWHITE4</b></li>
<li><b>AQUA</b></li>
<li><b>AQUAMARINE1</b></li>
<li><b>AQUAMARINE2</b></li>
<li><b>AQUAMARINE3</b></li>
<li><b>AQUAMARINE4</b></li>
<li><b>AZURE1</b></li>
<li><b>AZURE2</b></li>
<li><b>AZURE3</b></li>
<li><b>AZURE4</b></li>
<li><b>BANANA</b></li>
<li><b>BEIGE</b></li>
<li><b>BISQUE1</b></li>
<li><b>BISQUE2</b></li>
<li><b>BISQUE3</b></li>
<li><b>BISQUE4</b></li>
<li><b>BLACK</b></li>
<li><b>BLANCHEDALMOND</b></li>
<li><b>BLUE</b></li>
<li><b>BLUE2</b></li>
<li><b>BLUE3</b></li>
<li><b>BLUE4</b></li>
<li><b>BLUEVIOLET</b></li>
<li><b>BRICK</b></li>
<li><b>BROWN</b></li>
<li><b>BROWN1</b></li>
<li><b>BROWN2</b></li>
<li><b>BROWN3</b></li>
<li><b>BROWN4</b></li>
<li><b>BURLYWOOD</b></li>
<li><b>BURLYWOOD1</b></li>
<li><b>BURLYWOOD2</b></li>
<li><b>BURLYWOOD3</b></li>
<li><b>BURLYWOOD4</b></li>
<li><b>BURNTSIENNA</b></li>
<li><b>BURNTUMBER</b></li>
<li><b>CADETBLUE</b></li>
<li><b>CADETBLUE1</b></li>
<li><b>CADETBLUE2</b></li>
<li><b>CADETBLUE3</b></li>
<li><b>CADETBLUE4</b></li>
<li><b>CADMIUMORANGE</b></li>
<li><b>CADMIUMYELLOW</b></li>
<li><b>CARROT</b></li>
<li><b>CHARTREUSE1</b></li>
<li><b>CHARTREUSE2</b></li>
<li><b>CHARTREUSE3</b></li>
<li><b>CHARTREUSE4</b></li>
<li><b>CHOCOLATE</b></li>
<li><b>CHOCOLATE1</b></li>
<li><b>CHOCOLATE2</b></li>
<li><b>CHOCOLATE3</b></li>
<li><b>CHOCOLATE4</b></li>
<li><b>COBALT</b></li>
<li><b>COBALTGREEN</b></li>
<li><b>COLDGREY</b></li>
<li><b>CORAL</b></li>
<li><b>CORAL1</b></li>
<li><b>CORAL2</b></li>
<li><b>CORAL3</b></li>
<li><b>CORAL4</b></li>
<li><b>CORNFLOWERBLUE</b></li>
<li><b>CORNSILK1</b></li>
<li><b>CORNSILK2</b></li>
<li><b>CORNSILK3</b></li>
<li><b>CORNSILK4</b></li>
<li><b>CRIMSON</b></li>
<li><b>CYAN2</b></li>
<li><b>CYAN3</b></li>
<li><b>CYAN4</b></li>
<li><b>DARKGOLDENROD</b></li>
<li><b>DARKGOLDENROD1</b></li>
<li><b>DARKGOLDENROD2</b></li>
<li><b>DARKGOLDENROD3</b></li>
<li><b>DARKGOLDENROD4</b></li>
<li><b>DARKGRAY</b></li>
<li><b>DARKGREEN</b></li>
<li><b>DARKKHAKI</b></li>
<li><b>DARKOLIVEGREEN</b></li>
<li><b>DARKOLIVEGREEN1</b></li>
<li><b>DARKOLIVEGREEN2</b></li>
<li><b>DARKOLIVEGREEN3</b></li>
<li><b>DARKOLIVEGREEN4</b></li>
<li><b>DARKORANGE</b></li>
<li><b>DARKORANGE1</b></li>
<li><b>DARKORANGE2</b></li>
<li><b>DARKORANGE3</b></li>
<li><b>DARKORANGE4</b></li>
<li><b>DARKORCHID</b></li>
<li><b>DARKORCHID1</b></li>
<li><b>DARKORCHID2</b></li>
<li><b>DARKORCHID3</b></li>
<li><b>DARKORCHID4</b></li>
<li><b>DARKSALMON</b></li>
<li><b>DARKSEAGREEN</b></li>
<li><b>DARKSEAGREEN1</b></li>
<li><b>DARKSEAGREEN2</b></li>
<li><b>DARKSEAGREEN3</b></li>
<li><b>DARKSEAGREEN4</b></li>
<li><b>DARKSLATEBLUE</b></li>
<li><b>DARKSLATEGRAY</b></li>
<li><b>DARKSLATEGRAY1</b></li>
<li><b>DARKSLATEGRAY2</b></li>
<li><b>DARKSLATEGRAY3</b></li>
<li><b>DARKSLATEGRAY4</b></li>
<li><b>DARKTURQUOISE</b></li>
<li><b>DARKVIOLET</b></li>
<li><b>DEEPPINK1</b></li>
<li><b>DEEPPINK2</b></li>
<li><b>DEEPPINK3</b></li>
<li><b>DEEPPINK4</b></li>
<li><b>DEEPSKYBLUE1</b></li>
<li><b>DEEPSKYBLUE2</b></li>
<li><b>DEEPSKYBLUE3</b></li>
<li><b>DEEPSKYBLUE4</b></li>
<li><b>DIMGRAY</b></li>
<li><b>DIMGRAY</b></li>
<li><b>DODGERBLUE1</b></li>
<li><b>DODGERBLUE2</b></li>
<li><b>DODGERBLUE3</b></li>
<li><b>DODGERBLUE4</b></li>
<li><b>EGGSHELL</b></li>
<li><b>EMERALDGREEN</b></li>
<li><b>FIREBRICK</b></li>
<li><b>FIREBRICK1</b></li>
<li><b>FIREBRICK2</b></li>
<li><b>FIREBRICK3</b></li>
<li><b>FIREBRICK4</b></li>
<li><b>FLESH</b></li>
<li><b>FLORALWHITE</b></li>
<li><b>FORESTGREEN</b></li>
<li><b>GAINSBORO</b></li>
<li><b>GHOSTWHITE</b></li>
<li><b>GOLD1</b></li>
<li><b>GOLD2</b></li>
<li><b>GOLD3</b></li>
<li><b>GOLD4</b></li>
<li><b>GOLDENROD</b></li>
<li><b>GOLDENROD1</b></li>
<li><b>GOLDENROD2</b></li>
<li><b>GOLDENROD3</b></li>
<li><b>GOLDENROD4</b></li>
<li><b>GRAY</b></li>
<li><b>GRAY1</b></li>
<li><b>GRAY10</b></li>
<li><b>GRAY11</b></li>
<li><b>GRAY12</b></li>
<li><b>GRAY13</b></li>
<li><b>GRAY14</b></li>
<li><b>GRAY15</b></li>
<li><b>GRAY16</b></li>
<li><b>GRAY17</b></li>
<li><b>GRAY18</b></li>
<li><b>GRAY19</b></li>
<li><b>GRAY2</b></li>
<li><b>GRAY20</b></li>
<li><b>GRAY21</b></li>
<li><b>GRAY22</b></li>
<li><b>GRAY23</b></li>
<li><b>GRAY24</b></li>
<li><b>GRAY25</b></li>
<li><b>GRAY26</b></li>
<li><b>GRAY27</b></li>
<li><b>GRAY28</b></li>
<li><b>GRAY29</b></li>
<li><b>GRAY3</b></li>
<li><b>GRAY30</b></li>
<li><b>GRAY31</b></li>
<li><b>GRAY32</b></li>
<li><b>GRAY33</b></li>
<li><b>GRAY34</b></li>
<li><b>GRAY35</b></li>
<li><b>GRAY36</b></li>
<li><b>GRAY37</b></li>
<li><b>GRAY38</b></li>
<li><b>GRAY39</b></li>
<li><b>GRAY4</b></li>
<li><b>GRAY40</b></li>
<li><b>GRAY42</b></li>
<li><b>GRAY43</b></li>
<li><b>GRAY44</b></li>
<li><b>GRAY45</b></li>
<li><b>GRAY46</b></li>
<li><b>GRAY47</b></li>
<li><b>GRAY48</b></li>
<li><b>GRAY49</b></li>
<li><b>GRAY5</b></li>
<li><b>GRAY50</b></li>
<li><b>GRAY51</b></li>
<li><b>GRAY52</b></li>
<li><b>GRAY53</b></li>
<li><b>GRAY54</b></li>
<li><b>GRAY55</b></li>
<li><b>GRAY56</b></li>
<li><b>GRAY57</b></li>
<li><b>GRAY58</b></li>
<li><b>GRAY59</b></li>
<li><b>GRAY6</b></li>
<li><b>GRAY60</b></li>
<li><b>GRAY61</b></li>
<li><b>GRAY62</b></li>
<li><b>GRAY63</b></li>
<li><b>GRAY64</b></li>
<li><b>GRAY65</b></li>
<li><b>GRAY66</b></li>
<li><b>GRAY67</b></li>
<li><b>GRAY68</b></li>
<li><b>GRAY69</b></li>
<li><b>GRAY7</b></li>
<li><b>GRAY70</b></li>
<li><b>GRAY71</b></li>
<li><b>GRAY72</b></li>
<li><b>GRAY73</b></li>
<li><b>GRAY74</b></li>
<li><b>GRAY75</b></li>
<li><b>GRAY76</b></li>
<li><b>GRAY77</b></li>
<li><b>GRAY78</b></li>
<li><b>GRAY79</b></li>
<li><b>GRAY8</b></li>
<li><b>GRAY80</b></li>
<li><b>GRAY81</b></li>
<li><b>GRAY82</b></li>
<li><b>GRAY83</b></li>
<li><b>GRAY84</b></li>
<li><b>GRAY85</b></li>
<li><b>GRAY86</b></li>
<li><b>GRAY87</b></li>
<li><b>GRAY88</b></li>
<li><b>GRAY89</b></li>
<li><b>GRAY9</b></li>
<li><b>GRAY90</b></li>
<li><b>GRAY91</b></li>
<li><b>GRAY92</b></li>
<li><b>GRAY93</b></li>
<li><b>GRAY94</b></li>
<li><b>GRAY95</b></li>
<li><b>GRAY97</b></li>
<li><b>GRAY98</b></li>
<li><b>GRAY99</b></li>
<li><b>GREEN</b></li>
<li><b>GREEN1</b></li>
<li><b>GREEN2</b></li>
<li><b>GREEN3</b></li>
<li><b>GREEN4</b></li>
<li><b>GREENYELLOW</b></li>
<li><b>HONEYDEW1</b></li>
<li><b>HONEYDEW2</b></li>
<li><b>HONEYDEW3</b></li>
<li><b>HONEYDEW4</b></li>
<li><b>HOTPINK</b></li>
<li><b>HOTPINK1</b></li>
<li><b>HOTPINK2</b></li>
<li><b>HOTPINK3</b></li>
<li><b>HOTPINK4</b></li>
<li><b>INDIANRED</b></li>
<li><b>INDIANRED</b></li>
<li><b>INDIANRED1</b></li>
<li><b>INDIANRED2</b></li>
<li><b>INDIANRED3</b></li>
<li><b>INDIANRED4</b></li>
<li><b>INDIGO</b></li>
<li><b>IVORY1</b></li>
<li><b>IVORY2</b></li>
<li><b>IVORY3</b></li>
<li><b>IVORY4</b></li>
<li><b>IVORYBLACK</b></li>
<li><b>KHAKI</b></li>
<li><b>KHAKI1</b></li>
<li><b>KHAKI2</b></li>
<li><b>KHAKI3</b></li>
<li><b>KHAKI4</b></li>
<li><b>LAVENDER</b></li>
<li><b>LAVENDERBLUSH1</b></li>
<li><b>LAVENDERBLUSH2</b></li>
<li><b>LAVENDERBLUSH3</b></li>
<li><b>LAVENDERBLUSH4</b></li>
<li><b>LAWNGREEN</b></li>
<li><b>LEMONCHIFFON1</b></li>
<li><b>LEMONCHIFFON2</b></li>
<li><b>LEMONCHIFFON3</b></li>
<li><b>LEMONCHIFFON4</b></li>
<li><b>LIGHTBLUE</b></li>
<li><b>LIGHTBLUE1</b></li>
<li><b>LIGHTBLUE2</b></li>
<li><b>LIGHTBLUE3</b></li>
<li><b>LIGHTBLUE4</b></li>
<li><b>LIGHTCORAL</b></li>
<li><b>LIGHTCYAN1</b></li>
<li><b>LIGHTCYAN2</b></li>
<li><b>LIGHTCYAN3</b></li>
<li><b>LIGHTCYAN4</b></li>
<li><b>LIGHTGOLDENROD1</b></li>
<li><b>LIGHTGOLDENROD2</b></li>
<li><b>LIGHTGOLDENROD3</b></li>
<li><b>LIGHTGOLDENROD4</b></li>
<li><b>LIGHTGOLDENRODYELLOW</b></li>
<li><b>LIGHTGREY</b></li>
<li><b>LIGHTPINK</b></li>
<li><b>LIGHTPINK1</b></li>
<li><b>LIGHTPINK2</b></li>
<li><b>LIGHTPINK3</b></li>
<li><b>LIGHTPINK4</b></li>
<li><b>LIGHTSALMON1</b></li>
<li><b>LIGHTSALMON2</b></li>
<li><b>LIGHTSALMON3</b></li>
<li><b>LIGHTSALMON4</b></li>
<li><b>LIGHTSEAGREEN</b></li>
<li><b>LIGHTSKYBLUE</b></li>
<li><b>LIGHTSKYBLUE1</b></li>
<li><b>LIGHTSKYBLUE2</b></li>
<li><b>LIGHTSKYBLUE3</b></li>
<li><b>LIGHTSKYBLUE4</b></li>
<li><b>LIGHTSLATEBLUE</b></li>
<li><b>LIGHTSLATEGRAY</b></li>
<li><b>LIGHTSTEELBLUE</b></li>
<li><b>LIGHTSTEELBLUE1</b></li>
<li><b>LIGHTSTEELBLUE2</b></li>
<li><b>LIGHTSTEELBLUE3</b></li>
<li><b>LIGHTSTEELBLUE4</b></li>
<li><b>LIGHTYELLOW1</b></li>
<li><b>LIGHTYELLOW2</b></li>
<li><b>LIGHTYELLOW3</b></li>
<li><b>LIGHTYELLOW4</b></li>
<li><b>LIMEGREEN</b></li>
<li><b>LINEN</b></li>
<li><b>MAGENTA</b></li>
<li><b>MAGENTA2</b></li>
<li><b>MAGENTA3</b></li>
<li><b>MAGENTA4</b></li>
<li><b>MANGANESEBLUE</b></li>
<li><b>MAROON</b></li>
<li><b>MAROON1</b></li>
<li><b>MAROON2</b></li>
<li><b>MAROON3</b></li>
<li><b>MAROON4</b></li>
<li><b>MEDIUMORCHID</b></li>
<li><b>MEDIUMORCHID1</b></li>
<li><b>MEDIUMORCHID2</b></li>
<li><b>MEDIUMORCHID3</b></li>
<li><b>MEDIUMORCHID4</b></li>
<li><b>MEDIUMPURPLE</b></li>
<li><b>MEDIUMPURPLE1</b></li>
<li><b>MEDIUMPURPLE2</b></li>
<li><b>MEDIUMPURPLE3</b></li>
<li><b>MEDIUMPURPLE4</b></li>
<li><b>MEDIUMSEAGREEN</b></li>
<li><b>MEDIUMSLATEBLUE</b></li>
<li><b>MEDIUMSPRINGGREEN</b></li>
<li><b>MEDIUMTURQUOISE</b></li>
<li><b>MEDIUMVIOLETRED</b></li>
<li><b>MELON</b></li>
<li><b>MIDNIGHTBLUE</b></li>
<li><b>MINT</b></li>
<li><b>MINTCREAM</b></li>
<li><b>MISTYROSE1</b></li>
<li><b>MISTYROSE2</b></li>
<li><b>MISTYROSE3</b></li>
<li><b>MISTYROSE4</b></li>
<li><b>MOCCASIN</b></li>
<li><b>NAVAJOWHITE1</b></li>
<li><b>NAVAJOWHITE2</b></li>
<li><b>NAVAJOWHITE3</b></li>
<li><b>NAVAJOWHITE4</b></li>
<li><b>NAVY</b></li>
<li><b>OLDLACE</b></li>
<li><b>OLIVE</b></li>
<li><b>OLIVEDRAB</b></li>
<li><b>OLIVEDRAB1</b></li>
<li><b>OLIVEDRAB2</b></li>
<li><b>OLIVEDRAB3</b></li>
<li><b>OLIVEDRAB4</b></li>
<li><b>ORANGE</b></li>
<li><b>ORANGE1</b></li>
<li><b>ORANGE2</b></li>
<li><b>ORANGE3</b></li>
<li><b>ORANGE4</b></li>
<li><b>ORANGERED1</b></li>
<li><b>ORANGERED2</b></li>
<li><b>ORANGERED3</b></li>
<li><b>ORANGERED4</b></li>
<li><b>ORCHID</b></li>
<li><b>ORCHID1</b></li>
<li><b>ORCHID2</b></li>
<li><b>ORCHID3</b></li>
<li><b>ORCHID4</b></li>
<li><b>PALEGOLDENROD</b></li>
<li><b>PALEGREEN</b></li>
<li><b>PALEGREEN1</b></li>
<li><b>PALEGREEN2</b></li>
<li><b>PALEGREEN3</b></li>
<li><b>PALEGREEN4</b></li>
<li><b>PALETURQUOISE1</b></li>
<li><b>PALETURQUOISE2</b></li>
<li><b>PALETURQUOISE3</b></li>
<li><b>PALETURQUOISE4</b></li>
<li><b>PALEVIOLETRED</b></li>
<li><b>PALEVIOLETRED1</b></li>
<li><b>PALEVIOLETRED2</b></li>
<li><b>PALEVIOLETRED3</b></li>
<li><b>PALEVIOLETRED4</b></li>
<li><b>PAPAYAWHIP</b></li>
<li><b>PEACHPUFF1</b></li>
<li><b>PEACHPUFF2</b></li>
<li><b>PEACHPUFF3</b></li>
<li><b>PEACHPUFF4</b></li>
<li><b>PEACOCK</b></li>
<li><b>PINK</b></li>
<li><b>PINK1</b></li>
<li><b>PINK2</b></li>
<li><b>PINK3</b></li>
<li><b>PINK4</b></li>
<li><b>PLUM</b></li>
<li><b>PLUM1</b></li>
<li><b>PLUM2</b></li>
<li><b>PLUM3</b></li>
<li><b>PLUM4</b></li>
<li><b>POWDERBLUE</b></li>
<li><b>PURPLE</b></li>
<li><b>PURPLE1</b></li>
<li><b>PURPLE2</b></li>
<li><b>PURPLE3</b></li>
<li><b>PURPLE4</b></li>
<li><b>RASPBERRY</b></li>
<li><b>RAWSIENNA</b></li>
<li><b>RED1</b></li>
<li><b>RED2</b></li>
<li><b>RED3</b></li>
<li><b>RED4</b></li>
<li><b>ROSYBROWN</b></li>
<li><b>ROSYBROWN1</b></li>
<li><b>ROSYBROWN2</b></li>
<li><b>ROSYBROWN3</b></li>
<li><b>ROSYBROWN4</b></li>
<li><b>ROYALBLUE</b></li>
<li><b>ROYALBLUE1</b></li>
<li><b>ROYALBLUE2</b></li>
<li><b>ROYALBLUE3</b></li>
<li><b>ROYALBLUE4</b></li>
<li><b>SALMON</b></li>
<li><b>SALMON1</b></li>
<li><b>SALMON2</b></li>
<li><b>SALMON3</b></li>
<li><b>SALMON4</b></li>
<li><b>SANDYBROWN</b></li>
<li><b>SAPGREEN</b></li>
<li><b>SEAGREEN1</b></li>
<li><b>SEAGREEN2</b></li>
<li><b>SEAGREEN3</b></li>
<li><b>SEAGREEN4</b></li>
<li><b>SEASHELL1</b></li>
<li><b>SEASHELL2</b></li>
<li><b>SEASHELL3</b></li>
<li><b>SEASHELL4</b></li>
<li><b>SEPIA</b></li>
<li><b>SGIBEET</b></li>
<li><b>SGIBRIGHTGRAY</b></li>
<li><b>SGICHARTREUSE</b></li>
<li><b>SGIDARKGRAY</b></li>
<li><b>SGIGRAY12</b></li>
<li><b>SGIGRAY16</b></li>
<li><b>SGIGRAY32</b></li>
<li><b>SGIGRAY36</b></li>
<li><b>SGIGRAY52</b></li>
<li><b>SGIGRAY56</b></li>
<li><b>SGIGRAY72</b></li>
<li><b>SGIGRAY76</b></li>
<li><b>SGIGRAY92</b></li>
<li><b>SGIGRAY96</b></li>
<li><b>SGILIGHTBLUE</b></li>
<li><b>SGILIGHTGRAY</b></li>
<li><b>SGIOLIVEDRAB</b></li>
<li><b>SGISALMON</b></li>
<li><b>SGISLATEBLUE</b></li>
<li><b>SGITEAL</b></li>
<li><b>SIENNA</b></li>
<li><b>SIENNA1</b></li>
<li><b>SIENNA2</b></li>
<li><b>SIENNA3</b></li>
<li><b>SIENNA4</b></li>
<li><b>SILVER</b></li>
<li><b>SKYBLUE</b></li>
<li><b>SKYBLUE1</b></li>
<li><b>SKYBLUE2</b></li>
<li><b>SKYBLUE3</b></li>
<li><b>SKYBLUE4</b></li>
<li><b>SLATEBLUE</b></li>
<li><b>SLATEBLUE1</b></li>
<li><b>SLATEBLUE2</b></li>
<li><b>SLATEBLUE3</b></li>
<li><b>SLATEBLUE4</b></li>
<li><b>SLATEGRAY</b></li>
<li><b>SLATEGRAY1</b></li>
<li><b>SLATEGRAY2</b></li>
<li><b>SLATEGRAY3</b></li>
<li><b>SLATEGRAY4</b></li>
<li><b>SNOW1</b></li>
<li><b>SNOW2</b></li>
<li><b>SNOW3</b></li>
<li><b>SNOW4</b></li>
<li><b>SPRINGGREEN</b></li>
<li><b>SPRINGGREEN1</b></li>
<li><b>SPRINGGREEN2</b></li>
<li><b>SPRINGGREEN3</b></li>
<li><b>STEELBLUE</b></li>
<li><b>STEELBLUE1</b></li>
<li><b>STEELBLUE2</b></li>
<li><b>STEELBLUE3</b></li>
<li><b>STEELBLUE4</b></li>
<li><b>TAN</b></li>
<li><b>TAN1</b></li>
<li><b>TAN2</b></li>
<li><b>TAN3</b></li>
<li><b>TAN4</b></li>
<li><b>TEAL</b></li>
<li><b>THISTLE</b></li>
<li><b>THISTLE1</b></li>
<li><b>THISTLE2</b></li>
<li><b>THISTLE3</b></li>
<li><b>THISTLE4</b></li>
<li><b>TOMATO1</b></li>
<li><b>TOMATO2</b></li>
<li><b>TOMATO3</b></li>
<li><b>TOMATO4</b></li>
<li><b>TURQUOISE</b></li>
<li><b>TURQUOISE1</b></li>
<li><b>TURQUOISE2</b></li>
<li><b>TURQUOISE3</b></li>
<li><b>TURQUOISE4</b></li>
<li><b>TURQUOISEBLUE</b></li>
<li><b>VIOLET</b></li>
<li><b>VIOLETRED</b></li>
<li><b>VIOLETRED1</b></li>
<li><b>VIOLETRED2</b></li>
<li><b>VIOLETRED3</b></li>
<li><b>VIOLETRED4</b></li>
<li><b>WARMGREY</b></li>
<li><b>WHEAT</b></li>
<li><b>WHEAT1</b></li>
<li><b>WHEAT2</b></li>
<li><b>WHEAT3</b></li>
<li><b>WHEAT4</b></li>
<li><b>WHITE</b></li>
<li><b>WHITESMOKE</b></li>
<li><b>WHITESMOKE</b></li>
<li><b>YELLOW1</b></li>
<li><b>YELLOW2</b></li>
<li><b>YELLOW3</b></li>
<li><b>YELLOW4</b></li>


</details>