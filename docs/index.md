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

_Not Documented Yet._