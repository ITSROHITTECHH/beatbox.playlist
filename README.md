# 🎧 Python beatbox Playlist Manager

A beginner-friendly Python project demonstrating core Object-Oriented Programming (OOP) concepts using a custom **Song** and **Playlist** class. This project showcases the power of Python's *dunder methods* (`__init__`, `__str__`, `__len__`, `__getitem__`, `__add__`) to create a flexible and intuitive playlist system.

---

## 📌 Features

- 🎵 Create songs with title, artist, and duration
- 📂 Build playlists and add songs easily
- ➕ Combine playlists using the `+` operator
- 🔢 Get total songs using `len()`
- 🔍 Access songs via index like a list
- 🖨️ Display formatted playlist info

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

## 🧾 Code Example

```python
song1 = Song("Blinding Lights", "The Weeknd", 200)
pop_hits = Playlist("Pop Hits")
pop_hits.add_song(song1)

print(pop_hits)            # __str__ in action
print(len(pop_hits))       # __len__ in action
print(pop_hits[0])         # __getitem__ in action




# ===========================================
# 👨‍💻 Author: Rohit Kumar Srivastava
# ===========================================
# 🎓 BCA Student | 💻 Developer & Designer | 🧠 Python Learner
# 🔗 LinkedIn: https://www.linkedin.com/in/rohit-kumar-srivastava-39a74b372?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app
# 📬 Feel free to connect and collaborate!
# ===========================================


