#Rogue-Python Engine 0.0.2

#####A Simple ray-casting engine built with Python and PyGame.

Designed to be used for writing retro-styled FPP roguelike dungeon crawler games, like *[Dungeon Master](http://www.dungeon-master.com/)* series or the newer *[Legend of Grimrock](http://www.grimrock.net/)*.

Currently the engine intentionally only allows grid-based movement.

##Credits:

[mlambir's PygameFPS](https://github.com/mlambir/Pygame-FPS)

[raycasting tutorial on lodev.org](http://lodev.org/cgtutor/raycasting.html)

[raycasting tutorial on permadi.com](http://www.permadi.com/tutorial/raycast/index.html)

##Dependencies:

* CPython 2.7.5
* PyGame 1.9.2pre

##Current version features:

* **Raycasting**
* **Movement and roation**
* **Collision detection**
* **Loading maps from textfiles**

##Keys:

Movement keys are hardcoded (as long as anything is hardcoded in Python's code) and go like this:

* **W, S, A, D** - move and rotate
* **Q, E** - strafe
* **Esc** - quit