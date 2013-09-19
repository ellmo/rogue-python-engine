#Rogue-Python Engine 0.0.3

#####A Simple ray-casting engine built with Python and PyGame.

Designed to be used for writing retro-styled FPP roguelike dungeon crawler games, like *[Dungeon Master](http://www.dungeon-master.com/)* series or the newer *[Legend of Grimrock](http://www.grimrock.net/)*.

This program is mainly written for educational purposes. The raycasting algorithm has been rewritten in a more *Object-Oriented* fashion, where a **Renderer-class** object throws **Ray-class** objects in front of the **Camera-class** object. I think thanks to the *Object-Oriented* approach it's easier to understand what is actually happening during the rendering process – even if you plan to implement it in a procedural fashion.

The engine intentionally allows grid-based movement only! If you're looking for a more Wolf3D-like movement look no further than [mlambir's PygameFPS](https://github.com/mlambir/Pygame-FPS).

##Legal:
This code is distributed under GPL v3 License.

##Credits:

* [mlambir's PygameFPS](https://github.com/mlambir/Pygame-FPS)
* [raycasting tutorial on lodev.org](http://lodev.org/cgtutor/raycasting.html)
* [raycasting tutorial on permadi.com](http://www.permadi.com/tutorial/raycast/index.html)

##Dependencies:
*__May__ work with older versions, but these are what I used:*

* CPython 2.7.5
* PyGame 1.9.2pre
* PyGame itslef depends on [SDL](http://www.libsdl.org/) so you need to have development libraries istalled for it to run.

===

####Current version features:

* **Raycasting**
* **Movement and roation**
* **Collision detection**
* **Loading maps from textfiles**

####Keys:

Movement keys are hardcoded (as long as anything is hardcoded in Python's code) and go like this:

* **W, S, A, D** - move and rotate
* **Q, E** - strafe
* **Esc** - quit

######-- ellmo 2013