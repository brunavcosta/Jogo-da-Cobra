## JOGO DA COBRINHA (SNAKE GAME)
This is a simple implementation of the classic Snake game, written in Python using the Pygame library.

### 🎮 HOW TO PLAY
Use the arrow keys (UP, DOWN, LEFT, RIGHT) to control the snake's direction.

The goal is to eat the red food. Each time the snake eats the food, it grows longer.

The game ends if the snake hits the edge of the screen or collides with its own body.

### 💻 REQUIREMENTS
To run this game, you'll need to have Python and the Pygame library installed.

Python 3.x

Pygame: You can install it using pip:

pip install pygame

### ▶️ HOW TO RUN
Make sure you have all the requirements installed.

Save the provided code as a Python file (e.g., cobrinha.py).

Run the file from your terminal:

python cobrinha.py

### 🧠 CODE EXPLANATION
The code is structured as a basic game loop:

- Initialization: The pygame.init() function initializes all the necessary Pygame modules. A window is created with a size of 600x400 pixels.

- Game Objects: The snake is represented by a list of tuples, cobra, where each tuple is a coordinate (x, y). The food, comdida, is also a tuple of coordinates.

- Game Loop (while rodando): The main loop of the game.

- Event Handling: It checks for user input, such as quitting the game or pressing an arrow key to change the snake's direcao (direction).

- Movement Logic: A nova_cabeca (new head) is calculated based on the current direction, and it's inserted at the beginning of the cobra list.

- Food Logic: It checks if the snake's head is at the same position as the food.

If it is, the food is moved to a new random location.

If not, the last segment of the snake is removed using cobra.pop(), which makes the snake appear to move without growing.

- Game Over Conditions: The game ends (rodando = False) if the snake's head goes off-screen or if it collides with any part of its body.

- Drawing: The desenhar() function clears the screen and redraws the snake and the food at their new positions.

- Game Speed: relogio.tick(15) controls the frame rate, setting the game speed to 15 frames per second.

✍️ AUTHOR
This code was created with the help of a tiktok video by Leandro Hirt. I just followed along and made some changes.
