# 🚀 Asteroids (Pygame)

A classic **Asteroids-style arcade game** built with **Python** and **Pygame**.  
The player controls a spaceship in open space, shoots incoming asteroids, and survives as long as possible while asteroids split into smaller, faster fragments.

This project focuses on, **object-oriented design**, and **game-loop fundamentals**.

---

## 🎮 Gameplay Overview

- Control a spaceship positioned at the center of the screen  
- Rotate and move the ship using momentum-based movement  
- Shoot asteroids to destroy them  
- Large asteroids split into smaller ones when shot  
- Smaller asteroids eventually disappear  
- Collision with an asteroid ends the game  

---

## 🛠️ Built With

- **Python 3**
- **Pygame**
- Basic vector-based physics using `pygame.Vector2`
- Sprite groups for efficient updates, drawing, and collision handling

---

## 🧠 Key Concepts Implemented

- Game loop with delta time (`dt`)
- Sprite-based architecture (`pygame.sprite.Sprite`)
- Automatic sprite group management
- Circle-based collision detection
- Asteroid splitting logic with velocity rotation
- Event logging for gameplay actions
- Scalable and extensible design

---

## 📁 Project Structure

```text
.
├── main.py              # Game loop and collision handling
├── player.py            # Player movement and shooting
├── asteroid.py          # Asteroid behavior and splitting logic
├── asteroidfield.py     # Asteroid spawning system
├── shot.py              # Projectile logic
├── circleshape.py       # Base class for circular game objects
├── constants.py         # Game constants
├── logger.py            # Event and state logging
```

---

## ▶️ How to Run

1. Make sure Python 3 is installed
2. Install Pygame:
   ```bash
   pip install pygame
3. Run the game:
   ```bash
   python main.py

---

## 🧪 Current Features

- Basic movement  
- Shooting mechanics  
- Asteroid spawning  
- Asteroid splitting with randomized trajectories  
- Collision detection between ship, asteroids, and shots   

---

## 🔮 Future Upgrade Ideas

The project was designed to be easily extensible. Planned or potential upgrades include:

- Add a scoring system  
- Implement multiple lives and respawning  
- Add an explosion effect for the asteroids  
- Add acceleration to the player movement  
- Make the objects wrap around the screen instead of disappearing  
- Add a background image  
- Create different weapon types  
- Make the asteroids lumpy instead of perfectly round  
- Make the ship have a triangular hit box instead of a circular one  
- Add a shield power-up  
- Add a speed power-up  
- Add bombs that can be dropped  

