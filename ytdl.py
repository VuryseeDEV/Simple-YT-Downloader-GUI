import yt_dlp
import tkinter as tk
from tkinter import filedialog, messagebox

def vid_download(url, save_path):
    try:
        ydl_opts = {
            'format': 'best',
            'outtmpl': f'{save_path}/%(title)s.%(ext)s',
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Download was successful!")
        messagebox.showinfo("Success", "Download completed successfully!")
    except Exception as e:
        print("An error occurred:")
        print(e)
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        return folder
    else:
        return None

def download_video():
    video_url = url_entry.get()
    save_dir = open_file_dialog()

    if save_dir:
        print("Started Download...")
        vid_download(video_url, save_dir)
    else:
        print("Invalid Location.")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("YouTube Video Downloader")
    root.geometry("400x150")

    url_label = tk.Label(root, text="Enter YouTube URL:")
    url_label.pack(pady=10)

    url_entry = tk.Entry(root, width=50)
    url_entry.pack(pady=5)

    download_button = tk.Button(root, text="Download", command=download_video)
    download_button.pack(pady=20)

    root.mainloop()

    
