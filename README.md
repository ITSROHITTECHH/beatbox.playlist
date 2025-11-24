<p align="center">
  <img src="/mnt/data/banner.png" alt="Beatbox Banner" width="100%">
</p>

# 🎧 Beatbox — YouTube Music Player (Python + Tkinter + VLC + yt-dlp)

Beatbox is a modern **desktop music player app** built in Python that lets you:

- 🔍 Search YouTube  
- 🎵 Stream audio-only playback (no video)  
- 📻 Load a default playlist  
- 🎚️ Control playback (Play / Pause / Resume / Stop)  
- 🔊 Adjust volume  
- 🖼️ View track thumbnails  
- 🎨 Enjoy a smooth purple-themed UI with a dynamic background  

This project evolved from a simple playlist OOP project into a **full music player app**.

---

## 🚀 Features

### 🔍 **YouTube Search**
- Search any song directly using YouTube keywords  
- Uses `yt-dlp` to fetch metadata  
- Extracts thumbnails & channel details  
- Handles both URLs + search terms

### 🎧 **Music Playback Engine**
- Built using **VLC Python bindings**  
- Audio-only playback → lightweight & faster  
- Supports Play / Pause / Resume / Stop  
- Auto-updates currently playing song info

### 🎨 **Purple Modern UI**
- Built with Tkinter  
- Resizable layout  
- Dynamic background scaling  
- Modern purple theme  
- Separate panels:
  - **Search Bar**
  - **Results List**
  - **Now Playing Panel**
  - **Playback Controls**

### 📁 **Default Playlist Loader**
Loads your built-in playlist JSON to instantly test the UI.

---

## 📸 Screenshots Preview

### 🎼 Default Playlist  

![Beatbox Banner](beatbox.playlist/default-playlist.png)
![alt text](<ChatGPT Image Nov 24, 2025, 07_20_45 PM.png>)


---

## 🛠️ Technologies Used

| Component | Library |
|----------|----------|
| GUI | Tkinter |
| Streaming | VLC Python (`python-vlc`) |
| YouTube Search | yt-dlp |
| Image Handling | Pillow (PIL) |
| HTTP Requests | requests |

---

## 📦 Installation


pip install yt-dlp python-vlc pillow requests

---

## 🧾 Sample Code Snippet

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

### Want me to also generate:
✅ A cleaner **project description**  
✅ A **requirements.txt**  
✅ A **GitHub release summary**  
✅ A better **repository structure**  
?

Just dm me on  x , linkdinn , email !




