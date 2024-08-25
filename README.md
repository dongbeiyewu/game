# My Game Project

## Overview

This is a simple 2.5D dungeon-style game developed using the [Ursina Engine](https://www.ursinaengine.org/). In this game, the player can move a character using the WASD keys in a dungeon environment, with a camera that follows the player from a 2.5D perspective.

## Features

- **2.5D Camera**: The camera follows the player from an overhead angle, providing a clear view of the dungeon.
- **WASD Movement**: Control the player character using the WASD keys.
- **Simple Dungeon Map**: A basic dungeon environment with walls and a floor.

## Prerequisites

- Python 3.10+
- pip (Python package installer)

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/dongbeiyewu/game.git
   cd game
   ```

2. **Set up a virtual environment (optional but recommended)**:

   ```bash
   python -m venv venv
   ```

   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

3. **Install the required packages**:

   ```bash
   pip install -r requirements.txt
   ```

   If the `requirements.txt` file does not exist, you can manually install the dependencies:

   ```bash
   pip install ursina
   ```

## Running the Game

After setting up the environment, you can run the game with:

```bash
python main.py
```
