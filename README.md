# Ping Pong Game

A classic 2-player ping pong game built with PyGame where players control paddles to bounce a ball back and forth.

![Ping Pong Game](https://via.placeholder.com/800x400?text=Ping+Pong+Game)

## Features

- Two-player local multiplayer gameplay
- Simple and intuitive keyboard controls
- Score tracking system
- Game ends when a player reaches 10 points
- Dynamic ball physics with slight randomization after paddle hits
- Clean visual design with center court line and score display
- Instructions screen at startup
- Winner announcement and game restart option

## Requirements

- Python 3.6 or higher
- PyGame 2.0.0 or higher

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/ping-pong-game.git
   cd ping-pong-game
   ```

2. Install the required dependencies:
   ```
   pip install pygame
   ```
   
   Or install from the requirements file:
   ```
   pip install -r requirements.txt
   ```

## How to Play

Run the game:
```
python ping_pong.py
```

### Controls

- **Player 1 (Left Paddle)**:
  - W: Move paddle up
  - S: Move paddle down

- **Player 2 (Right Paddle)**:
  - Up Arrow: Move paddle up
  - Down Arrow: Move paddle down

- **General Controls**:
  - SPACE: Start game / Restart after a win
  - ESC: Quit game

## Game Rules

1. Each player controls a paddle on their side of the screen
2. The ball bounces off paddles and the top/bottom walls
3. If a player misses the ball, the opponent scores a point
4. First player to reach 10 points wins the game
5. After a player wins, you can restart the game by pressing SPACE

## Code Structure

- `ping_pong.py`: Main game file containing all the game logic
  - `Paddle` class: Handles paddle creation, movement, and rendering
  - `Ball` class: Manages ball movement, collisions, and scoring
  - Helper functions for drawing the court, displaying scores, and showing game states

## Future Improvements

- Add sound effects for ball hits and scoring
- Implement difficulty levels with different ball speeds
- Add power-ups that temporarily modify gameplay
- Create an AI opponent for single-player mode
- Add customization options for paddles and ball

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- PyGame community for the excellent game development library
- Classic Pong game for the inspiration
