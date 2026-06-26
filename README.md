# 🏓 Ping Pong AI

A classic **Ping Pong** game built using Python's **Turtle Graphics**. The game features an AI-controlled opponent with multiple difficulty levels, a customizable winning score, and an interactive menu.

---

## Features

-  Single-player Ping Pong
-  AI opponent with three difficulty levels:
  - Easy
  - Medium
  - Hard
-  Select the winning score before starting:
  - 5
  - 7
  - 10
-  Interactive menu
-  Live scoreboard
-  Ball speed increases after each paddle hit
-  Built entirely using Python's Turtle module

---

## Controls

### Menu

| Key | Action |
|-----|--------|
| a | Decrease Difficulty |
| d | Increase Difficulty |
| s | Decrease Winning Score |
| w | Increase Winning Score |
| Enter | Start Game |
| q | Quit |

### Gameplay

| Key | Action |
|-----|--------|
| ↑ | Move Paddle Up |
| ↓ | Move Paddle Down |

---

## Difficulty Levels

The AI difficulty changes three parameters:

| Difficulty | Paddle Speed | Reaction Delay | Tracking Error |
|------------|--------------|----------------|----------------|
| Easy | Slow | High | Large |
| Medium | Medium | Medium | Medium |
| Hard | Fast | Low | Small |

As the difficulty increases:
- The AI reacts more quickly.
- The paddle moves faster.
- The AI makes fewer aiming mistakes.

---

## Project Structure

```
ping_pong/
│
├── main.py          # Main game loop
├── menu.py          # Game menu
├── paddle.py        # Paddle class
├── ball.py          # Ball movement and collision
├── ai.py            # AI controller
├── scoreboard.py    # Score display
└── README.md
```

---

## How the AI Works

The AI continuously tracks the vertical position of the ball.
Every few milliseconds (depending on the selected difficulty), it:

1. Reads the ball's current Y-coordinate.
2. Adds a random error to simulate imperfect gameplay.
3. Moves its paddle toward the target position.
4. Waits for the configured reaction delay before moving again.

---

## Scoring

- If the ball passes the AI paddle, the **Player** scores.
- If the ball passes the Player paddle, the **AI** scores.
- The first player to reach the selected winning score wins the match.

---

## Technologies Used

- Python 3
- Turtle Graphics
- Object-Oriented Programming (OOP)



```bash
python main.py
