# 🧩 Picture-Puzzle 

### 🧠 Goal of the Program
This program takes an image and scrambles it like a puzzle by cutting it into small squares, shuffling them, and putting them back together in a new random order. A specific password controls the random shuffling, so using the same password will always produce the same scrambled image. So, anyone can share the password and chunk size with their friends and challenge them to solve the scrambled image. It's a fun and creative way to share secret messages or memories through pictures!

### 📁 Project Structure

- `puzzle.py` – Takes an image, cuts it into chunks, scrambles the pieces using a password, and saves the output.
- `solution.py` – Takes the scrambled image and reassembles it back into the original form using the same password and chunk settings.
