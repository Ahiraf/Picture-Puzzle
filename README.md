# 🧩 Picture-Puzzle 

### 🧠 Goal of the Program
This program takes an image and scrambles it like a puzzle by cutting it into small squares, shuffling them, and putting them back together in a new random order. A specific password controls the random shuffling, so using the same password will always produce the same scrambled image. So, anyone can share the password and chunk size with their friends and challenge them to solve the scrambled image. It's a fun and creative way to share secret messages or memories through pictures!

### 📁 Project Structure

- `puzzle.py` – Takes an image, cuts it into chunks, scrambles the pieces using a password, and saves the output.
- `solution.py` – Takes the scrambled image and reassembles it back into the original form using the same password and chunk settings.

### 🛠️ How to Use

1. **Install Pillow** (if you haven’t already) :
  
  ``` pip install Pillow ```
  <img width="1269" alt="19701841-5D7E-4CC4-B76F-015ED097EF8C" src="https://github.com/user-attachments/assets/78754bd4-e874-48fb-902c-4aea51fc4e78" />

  
2. **Scramble an image with puzzle.py :**
To run this python file use this command on your terminal 

``` python ./puzzle.py ```
<img width="1265" alt="Screenshot 2025-04-08 at 8 03 55 PM" src="https://github.com/user-attachments/assets/0df20e1b-1b20-4b18-88c0-2f2a3e89ba86" />


3. **Reconstruct the image using solution.py :**

``` python ./PuzzleSolution.py ```
<img width="1265" alt="Screenshot 2025-04-08 at 8 04 56 PM" src="https://github.com/user-attachments/assets/3fceaea6-71f9-4ed2-b148-70d0a2c63d09" />


4. **Make sure to :**
    Use the same password and Use the same chunk size (chunks_x and chunks_y) to recover the original image.

5. **🔐 Why Password?**
  The password is converted into a seed that controls how the image is shuffled. This means:
  The same password = same scrambled pattern.
  Different passwords = completely different puzzles.

### 💡 Example Use Cases
Share secret photos with friends by just giving a password.


### 📸 Sample Output
  I have added,
 => **The main picture =**  ``` ButterflyFamilyTree.webp ``` 
 => **The scrambled picture =** ``` scrambled.png ```
 => **The unscrambled picture =** ``` unscrambled.png ``` , which should be same as the main picture.


📜 License
MIT License – Feel free to use and remix!


