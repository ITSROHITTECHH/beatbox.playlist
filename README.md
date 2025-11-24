# 🎧 Python beatbox Playlist Manager

A beginner-friendly Python project demonstrating core Object-Oriented Programming (OOP) concepts using a custom **Song** and **Playlist** class. This project showcases the power of Python's *dunder methods* (`__init__`, `__str__`, `__len__`, `__getitem__`, `__add__`) to create a flexible and intuitive playlist system.

---
## 🎵 Songs Folder

All song data used in this project is stored in the `songs` {} `beats_archive.json` directory for better organization and scalability.

---

## 📌 Features

- 🎵 Create songs with title, artist, and duration
- 📂 Build playlists and add songs easily
- ➕ Combine playlists using the `+` operator
- 🔢 Get total songs using `len()`
- 🔍 Access songs via index like a list
- 🖨️ Display formatted playlist info

---
## 📌 Overview

This project is designed to replicate basic features of a playlist application using Python classes. It's perfect for students or learners who are exploring Python OOP concepts such as:

- Class design
- Constructor methods
- Dunder methods like `__str__`, `__len__`, `__getitem__`, and `__add__`
- Data abstraction and encapsulation

---

## 🧠 What You Will Learn

- How to create and use custom Python classes
- How to manage lists of objects
- How to implement and override built-in Python methods
- How to structure a basic Python application
---

## 💡 Key Concepts Demonstrated

| Method        | Description                                                |
|---------------|------------------------------------------------------------|
| `__init__`    | Initializes Song and Playlist objects                      |
| `__str__`     | Custom string representation for songs and playlists       |
| `__len__`     | Enables use of `len()` on playlists                        |
| `__getitem__` | Enables indexing, e.g. `playlist[0]`                        |
| `__add__`     | Allows combining playlists using `playlist1 + playlist2`   |

---

# screenshot of terminal output

![Terminal Output](default-playlist.png)

---

# 👨‍💻 Author: Rohit Kumar Srivastava
---

🎓 BCA Student | 💻 turning errors into experience ..... | 🧠 Python Learner

🔗 LinkedIn: https://www.linkedin.com/in/rohit-kumar-srivastava-39a74b372?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app

📬 Feel free to connect !


---

## 🧾 Code Example

```python
song1 = Song("angreji beat", "yoyo honey singh", 200)
pop_hits = Playlist("Pop Hits")
pop_hits.add_song(song1)

print(pop_hits)            # __str__ in action
print(len(pop_hits))       # __len__ in action
print(pop_hits[0])         # __getitem__ in action

