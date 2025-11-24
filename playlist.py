"""
Beatbox.playlist YouTube Streaming Player
- Search YouTube or paste full URL
- Results list (double-click to play)
- Now-playing panel with thumbnail
- Bottom controls: Play / Pause / Resume / Stop / Volume
- Uses yt_dlp + python-vlc to stream audio
"""

import threading
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import yt_dlp
import vlc
import requests
import io
import os
import re
import traceback

# ---------------------------
# CONFIG - change path if needed
# ---------------------------
# If your background image lives in a folder called `tryitbeatbox` inside your project,
# keep this as-is. If you uploaded the image to the sandbox, you may need to use the
# full path (e.g. "/mnt/data/bg.png"). This variable is only used by the background loader.
DEFAULT_BG = "beatbox.playlist/bg.png"

# Theme colors used across the UI. Tweak these for a different look.
BG = "#1B0032"
PANEL = "#210022"
ACCENT = "#7C3AED"
TEXT = "#FFFFFF"
SUB = "#cfc6e8"


# --------------------------------------------
# Default 50 Bollywood Songs Playlist
# NOTE: kept as a list of dicts with title, url, thumb, channel
# --------------------------------------------

default_songs = [
    {"title": "Baharon Phool Barsao", "url": "https://youtu.be/P6p45E3lxb4?si=Z2W6dOX5TtUdEs7G", "thumb": None, "channel": "Mohammed Rafi"},
    {"title": "Awaara Hoon", "url": "https://youtu.be/fi-OKRuBbI8?si=spqjZNs6jWNSLtPF", "thumb": None, "channel": "Raj Kapoor"},
    {"title": "Tujhe Dekha To", "url": "https://youtu.be/ay6pwhXPNvo?si=FLLM_A9GfyoHYcyN", "thumb": None, "channel": "Kumar Sanu"},
    {"title": "Ajeeb Dastan Hai Yeh", "url": "https://youtu.be/niSarMZ2t7g?si=sQMK2vjLa8hm8YeF", "thumb": None, "channel": "Lata Mangeshkar"},
    {"title": "Kabhi Kabhie Mere Dil Mein", "url": "https://youtu.be/-W2dagktUp0?si=GnBuBztsV24U1SJw", "thumb": None, "channel": "Mukesh"},
    {"title": "Tere Liye", "url": "https://youtu.be/AlvUuGJccKs?si=xMhtCJ9JkE10-6lA", "thumb": None, "channel": "Shreya Ghosal"},
    {"title": "Yeh Dosti", "url": "https://youtu.be/qfCt1UZAXMQ?si=EgmiFXX3RUFXC_Jx", "thumb": None, "channel": "Kishore Kumar"},
    {"title": "Pyar Kiya To Darna Kya", "url": "https://youtu.be/uASs1_CrBnE?si=8sHckRL-qmxjjz3-", "thumb": None, "channel": "Kishore Kumar"},
    {"title": "Chaiyya Chaiyya", "url": "https://youtu.be/K-pX4qwtAxA?si=7IysSGk9UWCpAgTT", "thumb": None, "channel": "Sukhwinder Singh"},
    {"title": "Chalte Chalte", "url": "https://youtu.be/rkOakcMqJ-8?si=RGnainr6OlU_DG0j", "thumb": None, "channel": "Asha Bhosle"},
    {"title": "Lag Ja Gale", "url": "https://youtu.be/y2fgw1Oqz28?si=AEMzvMUtyXUEYBQk", "thumb": None, "channel": "Lata Mangeshkar"},
    {"title": "Pal Pal Dil Ke Paas", "url": "https://youtu.be/AMuRRXCuy-4?si=kmFe_IjhXXGIp-zH", "thumb": None, "channel": "Kishore Kumar"},
    {"title": "Piya Tu Ab To Aaja", "url": "https://youtu.be/46GGxF_Bwhg?si=A2v9_2X6iz2vJFKR", "thumb": None, "channel": "Asha Bhosle"},
    {"title": "Mere Sapno Ki Rani", "url": "https://youtu.be/9PdSmDRGIwM?si=MDN3L4mDmgT57nND", "thumb": None, "channel": "Kishore Kumar"},
    {"title": "Yeh Shaam Mastani", "url": "https://youtu.be/lbfWsIpXsCA?si=ga5ixu4iiBm3pezF", "thumb": None, "channel": "Kishore Kumar"},
    {"title": "Mere Samne Wali Khidki Mein", "url": "https://youtu.be/S0WPSYFm7iE?si=t1KXm1bJO8pV7Rnm", "thumb": None, "channel": "Kishore Kumar"},
    {"title": "Udein Jab Jab Zulfen Teri", "url": "https://youtu.be/xdh0VaKi2jQ?si=-XbaHgYf3pwYmAPT", "thumb": None, "channel": "Kishore Kumar"},
    {"title": "In Ankhon Ki Masti", "url": "https://youtu.be/yjYE41bYnUM?si=hJmVgsBIezuusGo0", "thumb": None, "channel": "Asha Bhosle"},
    {"title": "Tere Bina Zindagi Se", "url": "https://youtu.be/8-HnmVg0-O8?si=mbJfyV_NNOwn3Wnu", "thumb": None, "channel": "Lata Mangeshkar"},
    {"title": "Ae Mere Humsafar", "url": "https://youtu.be/AMuRRXCuy-4?si=KbIzHcN3qKiKU7ZX", "thumb": None, "channel": "Udit Narayan"},
    {"title": "Pehla Nasha", "url": "https://youtu.be/ODu7OyAqK-Q?si=qKWsab0jvVy4Hsg_", "thumb": None, "channel": "Udit Narayan"},
    {"title": "Kuch Kuch Hota Hai", "url": "https://youtu.be/bKZTnnFU9HA?si=VgjH7QKB9FhzmUq0", "thumb": None, "channel": "Udit Narayan"},
    {"title": "Kal Ho Naa Ho", "url": "https://youtu.be/g0eO74UmRBs?si=F4fJNiSKajakDslv", "thumb": None, "channel": "Sonu Nigam"},
    {"title": "Mauja Hi Mauja", "url": "https://youtu.be/PaDaoNnOQaM?si=eibCL6K6qceXxTvb", "thumb": None, "channel": "Sukhwinder Singh"},
    {"title": "Tum Hi Ho", "url": "https://youtu.be/Umqb9KENgmk?si=fBY3sRrmp9qJtrt2", "thumb": None, "channel": "Arijit Singh"},
    {"title": "Channa Mereya", "url": "https://youtu.be/284Ov7ysmfA?si=BJp2NcW0VYB9aHEu", "thumb": None, "channel": "Arijit Singh"},
    {"title": "Galliyan", "url": "https://youtu.be/FxAG_11PzCk?si=Ab3UF8I0TVVrxvF-", "thumb": None, "channel": "Ankit Tiwari"},
    {"title": "Raabta", "url": "https://youtu.be/zlt38OOqwDc?si=7xdE-2YJsg7xBqDP", "thumb": None, "channel": "Arijit Singh"},
    {"title": "Dil Diyan Gallan", "url": "https://youtu.be/SAcpESN_Fk4?si=C96gPcUJHWd9YJkx", "thumb": None, "channel": "Atif Aslam"},
    {"title": "Hawayein", "url": "https://youtu.be/cYOB941gyXI?si=MyetKA7put9jDxp-", "thumb": None, "channel": "Arijit Singh"},
    {"title": "Jeene Laga Hoon", "url": "https://youtu.be/pkzOBl1p7y4?si=dzoQe4_OCnbhEa8P", "thumb": None, "channel": "Atif Aslam"},
    {"title": "Janam Janam", "url": "https://youtu.be/pIBoAh4OXhQ?si=YfZMliNnq79FclOM", "thumb": None, "channel": "Arijit Singh"},
]








# --------------------------------------------
# Helpers
# --------------------------------------------
def is_youtube_url(s: str) -> bool:
    if not s:
        return False
    return bool(re.search(r"(youtube\.com/watch\?v=|youtu\.be/)", s))

def safe_fetch_thumbnail(url, max_size=(240, 140)):
    try:
        r = requests.get(url, timeout=6)
        r.raise_for_status()
        img = Image.open(io.BytesIO(r.content)).convert("RGBA")
        img.thumbnail(max_size, Image.LANCZOS)
        return ImageTk.PhotoImage(img)
    except Exception:
        return None

# --------------------------------------------
# YouTube search (uses yt-dlp)
# --------------------------------------------
def youtube_search(query: str):
    ydl_opts = {
        "quiet": True,
        "no_warnings": True,
        "skip_download": True,
        "extract_flat": True,
        "default_search": "ytsearch10",
        "extractor_args": {"youtube": {"player_client": ["default"]}}
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        data = ydl.extract_info(query, download=False)

    results = []
    for v in data.get("entries", []):
        vid = v.get("id")
        title = v.get("title") or v.get("title_plain") or "Unknown"
        results.append({
            "title": title,
            "url": f"https://www.youtube.com/watch?v={vid}" if vid else (v.get("webpage_url") or ""),
            "thumb": f"https://img.youtube.com/vi/{vid}/hqdefault.jpg" if vid else None,
            "channel": v.get("channel") or v.get("uploader") or "Unknown",
        })
    return results

# --------------------------------------------
# Main App
# --------------------------------------------
class BeatboxPurple:
    def __init__(self, root):
        self.root = root
        self.root.title("Beatbox.playlist")
        self.root.geometry("980x640")
        self.root.minsize(860, 540)

        # prefer audio-only VLC
        try:
            self.vlc_inst = vlc.Instance("--no-video")
        except Exception:
            self.vlc_inst = vlc.Instance()

        self.player = None
        self.search_results = []
        self.thumb_cache = {}

        # background image resources
        self._bg_orig = None   # PIL Image
        self._bg_photo = None  # ImageTk.PhotoImage

        # create background canvas first so it's behind other widgets
        self._create_background_canvas()

        # build UI on top
        self._build_ui()
        self._apply_theme()

        # update bg after UI is placed
        self._load_background_image(DEFAULT_BG)

        # handle resizing so background scales
        self.root.bind("<Configure>", self._on_root_configure)

        # cleanup
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    # -------------------------
    # Background: canvas, loader, resize handler
    # -------------------------
    def _create_background_canvas(self):
        # use place so other widgets (packed/placed) appear above
        self.canvas_bg = tk.Canvas(self.root, highlightthickness=0, bd=0)
        self.canvas_bg.place(x=0, y=0, relwidth=1, relheight=1)

    def _load_background_image(self, path):
        try:
            if not path or not os.path.exists(path):
                raise FileNotFoundError(path)
            self._bg_orig = Image.open(path).convert("RGBA")
            self._resize_bg_to_root()
        except Exception as e:
            print("Background load failed:", e)
            # leave canvas empty on error

    def _resize_bg_to_root(self):
        try:
            if self._bg_orig is None:
                return
            w = max(1, self.root.winfo_width())
            h = max(1, self.root.winfo_height())
            resized = self._bg_orig.resize((w, h), Image.LANCZOS)
            self._bg_photo = ImageTk.PhotoImage(resized)
            # remove any previous bg image by tag and add new
            self.canvas_bg.delete("bg_image")
            self.canvas_bg.create_image(0, 0, image=self._bg_photo, anchor="nw", tags=("bg_image",))
            # ensure the bg image is at the bottom of the canvas's stacking order
            self.canvas_bg.tag_lower("bg_image")
        except Exception as e:
            print("Failed resizing background:", e)

    def _on_root_configure(self, event):
        # skip if geometry not initialized
        # resize background when window size changes
        self._resize_bg_to_root()

    # -------------------------
    # UI
    # -------------------------
    def _build_ui(self):
        # top area (search)
        top = tk.Frame(self.root, bg=BG, pady=8)
        top.place(relx=0, rely=0, relwidth=1, height=48)

        tk.Label(top, text="Search or paste URL:", bg=BG, fg=TEXT,
                 font=("Segoe UI", 11)).pack(side=tk.LEFT, padx=(12, 6))

        self.search_var = tk.StringVar()
        self.search_entry = ttk.Entry(top, textvariable=self.search_var, width=50)
        self.search_entry.pack(side=tk.LEFT, padx=(0, 8))
        self.search_entry.bind("<Return>", lambda e: self._start_search_or_url())

        ttk.Button(top, text="Search / Play URL", command=self._start_search_or_url).pack(side=tk.LEFT, padx=4)
        ttk.Button(top, text="Load Default Playlist", command=self.load_default_playlist).pack(side=tk.LEFT, padx=4)

        self.status_label = tk.Label(top, text="", bg=BG, fg=SUB)
        self.status_label.pack(side=tk.RIGHT, padx=(0, 12))

        # middle body
        middle = tk.Frame(self.root, bg=BG)
        middle.place(relx=0, rely=0.07, relwidth=1, relheight=0.78)

        # left (results)
        left = tk.Frame(middle, bg=BG)
        left.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        tk.Label(left, text="Results", bg=BG, fg=TEXT,
                 font=("Segoe UI", 12, "bold")).pack(anchor="w", padx=4)

        self.results_listbox = tk.Listbox(
            left, bg=PANEL, fg=TEXT, font=("Segoe UI", 11),
            selectbackground=ACCENT, activestyle="none"
        )
        self.results_listbox.pack(fill=tk.BOTH, expand=True, padx=4, pady=4)
        self.results_listbox.bind("<Double-1>", lambda e: self._on_result_double())

        # right (now playing)
        right = tk.Frame(middle, bg=BG, width=340)
        right.pack(side=tk.RIGHT, fill=tk.Y)

        tk.Label(right, text="Now Playing", bg=BG, fg=TEXT,
                 font=("Segoe UI", 12, "bold")).pack(anchor="nw", pady=4)

        self.now_title = tk.Label(right, text="None", bg=PANEL, fg=TEXT,
                                  font=("Segoe UI", 11, "bold"), wraplength=300)
        self.now_title.pack(fill=tk.X, padx=6, pady=4)

        self.now_sub = tk.Label(right, text="", bg=PANEL, fg=SUB,
                                font=("Segoe UI", 9))
        self.now_sub.pack(fill=tk.X, padx=6)

        self.thumb_label = tk.Label(right, bg=PANEL)
        self.thumb_label.pack(padx=6, pady=8)

        # bottom controls
        bottom = tk.Frame(self.root, bg=BG, pady=8)
        bottom.place(relx=0, rely=0.88, relwidth=1, height=64)

        btns = tk.Frame(bottom, bg=BG)
        btns.pack()

        ttk.Button(btns, text="Play", command=self.play_selected).grid(row=0, column=0, padx=6)
        ttk.Button(btns, text="Pause", command=self.pause).grid(row=0, column=1, padx=6)
        ttk.Button(btns, text="Resume", command=self.resume).grid(row=0, column=2, padx=6)
        ttk.Button(btns, text="Stop", command=self.stop).grid(row=0, column=3, padx=6)

        self.volume = tk.Scale(bottom, from_=0, to=100, orient=tk.HORIZONTAL,
                               bg=BG, fg=TEXT, highlightthickness=0,
                               command=self._set_volume)
        self.volume.set(80)
        self.volume.pack()

    # -------------------------
    def _apply_theme(self):
        style = ttk.Style()
        try:
            style.theme_use("clam")
        except Exception:
            pass
        style.configure("TButton", background=ACCENT, foreground="white",
                        padding=6, font=("Segoe UI", 10))
        style.map("TButton", background=[("active", "#6D28D9")])

    # -------------------------
    def load_default_playlist(self):
        self.search_results = default_songs.copy()
        self.results_listbox.delete(0, tk.END)
        for s in self.search_results:
            self.results_listbox.insert(tk.END, s["title"])
        self.status_label.config(text=f"{len(self.search_results)} songs loaded ✔")

    # -------------------------
    def _start_search_or_url(self):
        q = self.search_var.get().strip()
        if not q:
            return
        if is_youtube_url(q):
            threading.Thread(target=self._play_by_url, args=(q, None), daemon=True).start()
            return
        self.status_label.config(text="Searching...")
        threading.Thread(target=self._do_search, args=(q,), daemon=True).start()

    def _do_search(self, q):
        try:
            results = youtube_search(q) or []
        except Exception:
            results = []
            self.root.after(0, lambda: self.status_label.config(text="Search failed"))
            return

        def update_ui():
            self.search_results = results
            self.results_listbox.delete(0, tk.END)
            for r in results:
                self.results_listbox.insert(tk.END, r.get("title") or "Unknown title")
            self.status_label.config(text=f"{len(results)} results")
        self.root.after(0, update_ui)

    # -------------------------
    def _on_result_double(self):
        sel = self.results_listbox.curselection()
        if not sel:
            return
        idx = sel[0]
        song = self.search_results[idx]
        threading.Thread(target=self._play_by_url, args=(song.get("url"), song), daemon=True).start()

    def play_selected(self):
        self._on_result_double()

    # -------------------------
    def _play_by_url(self, url, data=None):
        try:
            if not url:
                raise RuntimeError("No URL provided to play.")
            if self.player:
                try:
                    self.player.stop()
                except Exception:
                    pass

            ydl_opts = {
                "quiet": True,
                "no_warnings": True,
                "format": "bestaudio/best",
                "extractor_args": {"youtube": {"player_client": ["default"]}}
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)

            # find stream url
            stream = info.get("url")
            if not stream:
                for f in reversed(info.get("formats") or []):
                    if f.get("acodec") and f.get("acodec") != "none":
                        stream = f.get("url")
                        break

            if not stream:
                raise RuntimeError("Could not obtain a direct stream URL from yt-dlp.")

            media = self.vlc_inst.media_new(stream)
            self.player = self.vlc_inst.media_player_new()
            self.player.set_media(media)
            self.player.play()

            try:
                self.player.audio_set_volume(int(self.volume.get()))
            except Exception:
                pass

            def ui_update():
                try:
                    title = info.get("title") or (data.get("title") if data else "Unknown")
                    channel = info.get("uploader") or info.get("channel") or (data.get("channel") if data else "")
                    self.now_title.config(text=title)
                    self.now_sub.config(text=channel or "")

                    vid = info.get("id")
                    if vid:
                        thumb = f"https://img.youtube.com/vi/{vid}/hqdefault.jpg"
                        if thumb in self.thumb_cache:
                            img = self.thumb_cache[thumb]
                        else:
                            img = safe_fetch_thumbnail(thumb)
                            if img:
                                self.thumb_cache[thumb] = img
                        if img:
                            self.thumb_label.config(image=img)
                            self.thumb_label.image = img
                except Exception:
                    traceback.print_exc()
            self.root.after(0, ui_update)

        except Exception as e:
            self.root.after(0, lambda: messagebox.showerror("Error", f"Failed to play video.\n{e}"))

    # -------------------------
    def pause(self):
        if self.player:
            try:
                self.player.pause()
            except Exception:
                pass

    def resume(self):
        if self.player:
            try:
                self.player.play()
            except Exception:
                pass

    def stop(self):
        if self.player:
            try:
                self.player.stop()
            except Exception:
                pass

    def _set_volume(self, v):
        if self.player:
            try:
                self.player.audio_set_volume(int(v))
            except Exception:
                pass

    def on_close(self):
        try:
            if self.player:
                self.player.stop()
        except Exception:
            pass
        try:
            self.root.destroy()
        except Exception:
            pass

# --------------------------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = BeatboxPurple(root)
    root.mainloop()