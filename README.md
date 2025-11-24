
# 🎧 Beatbox — YouTube Music Player (Python + Tkinter + VLC + yt-dlp)

Beatbox is a modern **desktop music player** built in Python.  
It lets you:

- 🔍 Search YouTube  
- 🎵 Stream audio-only playback  
- 📻 Load a built-in playlist  
- 🎚️ Control playback  
- 🔊 Adjust volume  
- 🖼️ View thumbnails  
- 🎨 Enjoy a clean purple UI  

Originally a small OOP playlist project — now a **full YouTube-powered music player**.

---

## 🚀 Features

### 🔍 **YouTube Search**
- Search any song using keywords  
- Uses `yt-dlp` to fetch YouTube metadata  
- Extracts thumbnails, channels & duration  
- Supports both direct URLs & search queries  

### 🎧 **Music Playback Engine**
- Built with **python-vlc**  
- Audio-only → faster & smooth  
- Supports:
  - ▶️ Play  
  - ⏸️ Pause  
  - 🔁 Resume  
  - ⏹️ Stop  
- Auto-updates Now Playing info  

### 🎨 **Purple Modern UI**
- Tkinter-based clean layout  
- Responsive window  
- Dynamic background scaling  
- UI Sections:
  - Search Bar  
  - Results List  
  - Now Playing  
  - Player Controls  

### 📁 **Default Playlist Loader**
Loads your JSON playlist instantly for testing.

---

## 📸 Screenshots Preview

### 🎼 Default Playlist

(beatbox.playlist/default-playlist.png)


---

🛠️ Technologies Used

Component	Library
GUI	Tkinter
Playback	python-vlc
YouTube Search	yt-dlp
Images	Pillow (PIL)
Network Requests	requests

---

📦 Installation

pip install yt-dlp python-vlc pillow requests


---

🧾 Sample yt-dlp Options

ydl_opts = {
    "quiet": True,
    "no_warnings": True,
    "skip_download": True,
    "extract_flat": True,
    "default_search": "ytsearch10"
}

---
👨‍💻 Author: Rohit Kumar Shrivastava
BCA Student | Python Developer | UI & Music App Enthusiast

🔗 LinkedIn:
https://www.linkedin.com/in/rohit-kumar-srivastava-39a74b372

🔗 X (Twitter):
https://x.com/itsrohit_tech?t=8Pzh0VeKL4d_ZVCQQuyODQ&s=09

---

Need More?
I can generate :

✅ Cleaner project description
✅ requirements.txt file
✅ GitHub release summary
✅ Improved repo structure

Just ping me on X, LinkedIn, or Email!

If you want the **banner** to be clickable or want a **dark README theme**, I can update it too — just tell me!






