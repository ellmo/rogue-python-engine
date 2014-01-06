

#Rogue-Python Engine 0.0.4
![RPE](http://i.imgur.com/T8KXqKn.png) ![RPEss](https://i.imgur.com/KS6GHWY.png)

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

* **Raycasting Textured Walls**
* **Raycasting Transparent Sprites**
* **Movement and roation**
* **Collision detection**
* **Loading maps from textfiles**

####Keys:

Movement keys are hardcoded (as long as anything is hardcoded in Python's code) and go like this:

* **W, S, A, D** - move and rotate
* **Q, E** - strafe
* **Esc** - quit

======

## Installing PyGame on OSX

Based on: [python 3.3 with pygame under mac os lion / mountain lion / mavericks](http://www.albrecht.lt/2012/06/python-3-2-with-pygame-under-mac-os-lion-10-7/) post, on [albrecht.LT](http://www.albrecht.lt/)

1. **Download and Install Xcode from AppStore**
2. **Install [homebrew](http://brew.sh/)**:

	`ruby -e "$(curl -fsSL https://raw.github.com/Homebrew/homebrew/go/install)"`
3. **Update your brew**: `brew update`
4. **Install Python** (optional)

	You can now install a desired version of Python from homebrew, but a more _version-managing-oriented_ approach is reccomended. I myself use [Pyenv](https://github.com/yyuu/pyenv), which is an exact rbenv clone, but for Python. That said, the described method should work with whichever version your system has installed (OSX 10.8 and 10.9 come with 2.7.5) if you don't want to install different versions.
5. **You need few tools to compile PyGame**

	```
	brew install hg
	brew install sdl sdl_image sdl_mixer sdl_ttf portmidi
	brew install --HEAD smpeg
	```
	
    if you get an error:
    
    `Error: No available formula for smpeg`
    
    use the command:
    
	`brew install --HEAD https://raw.github.com/Homebrew/homebrew-headonly/master/smpeg.rb`
	
    *(Sometimes the server is slow. You may have to repeat the command if you get a connection reset error.)*

6. **Install pip**: `easy_install3 pip`

	_(if you installed Python via PythonBrew and VirtualEnv you should have the `pip` command working, so you can skip this step):_
	
7. **Install PyGame:**
	1. Try to install *normally*:
	
		`pip install pygame`
	
		Most probably you'll get this error:
	
		`src/scale_mmx64.c:424:27: error: invalid instruction mnemonic 'movsxl'`
	
		Which you will need to fix manually in the cloned PyGame's repository. If you didn't and PyGame installed succesfully... well... lucky you!
	
	2. Clone the repository.
	
		`hg clone https://bitbucket.org/pygame/pygame`
		
		*(It's best to clone while in `~/Downloads`)*
	
	3. Enter the repo directory and replace the file `pygame/src/scale_mmx64.c` with Albrecht's [`scale_mmx64`](https://gist.github.com/ellmo/7974837)

	4. Install pygame
	
		`pip3 install ~/Downloads/pygame`

=====

######-- ellmo 2013