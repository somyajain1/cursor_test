# Falling Stars Animation

This Python script creates a beautiful animation of falling stars using Pygame. Each star has a glowing tail and falls at a random angle across the screen.

## Overview

The program creates a window where multiple stars fall diagonally across the screen, each leaving behind a fading tail that creates a meteor-like effect.

## Dependencies
- Python 3.x
- Pygame

## Code Structure

### Initial Setup
```python
import pygame
import random
import math

pygame.init()
WIDTH = 800
HEIGHT = 600
```
The code begins by importing necessary libraries and initializing Pygame. It sets up a display window of 800x600 pixels.

### Star Class
The `Star` class is the main component of the animation. Each star has the following properties:

- Position (x, y)
- Tail length (random between 5-15 segments)
- Tail color (random bright colors)
- Speed (random between 3-7 units)
- Falling angle (random between -30 and -60 degrees)
- List of previous positions for the tail effect

Key methods:
1. `reset()`: Repositions the star at the top of the screen with a random x-coordinate
2. `move()`: Updates the star's position based on its angle and speed
3. `draw()`: Renders the star and its tail with a fading effect

### Animation Features

1. **Tail Effect**
   - Each star maintains a list of its previous positions
   - The tail is drawn using lines connecting these positions
   - The tail color fades out gradually from the star to the end of the tail

2. **Movement**
   - Stars move diagonally using trigonometric calculations
   - When a star goes off-screen, it's reset to the top with new random properties

3. **Controls**
   - Close window button or ESC key to exit
   - Runs at 60 FPS for smooth animation

## Main Loop
The main game loop:
1. Handles window events (closing, key presses)
2. Clears the screen
3. Updates and draws each star
4. Refreshes the display

## Visual Effects
- Black background for better visibility
- White stars with colorful tails
- Smooth motion and fading effects
- Multiple stars (20) moving simultaneously

## Running the Program
Simply run the Python script with Pygame installed. The animation will start automatically and continue until you close the window or press ESC. 