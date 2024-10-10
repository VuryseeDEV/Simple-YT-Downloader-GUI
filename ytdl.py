import yt_dlp
import tkinter as tk
from tkinter import filedialog, messagebox

def vid_download(url, save_path):
    try:
        ydl_opts = {
            'format': 'best',  # Download the best quality available
            'outtmpl': f'{save_path}/%(title)s.%(ext)s',  # Template for output file name
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])  # Starts the download
        print("Download was successful!")
        messagebox.showinfo("Success", "Download completed successfully!")  # Notify for success

    except Exception as e:
        print("An error occurred:")
        print(e)
        messagebox.showerror("Error", f"An error occurred: {str(e)}")  # Notify for error

def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        return folder 
    else:
        return None

def download_video():
    """Get the URL and folder, then initiate the video download."""
    video_url = url_entry.get()  # Gets the URL from the text entry
    save_dir = open_file_dialog()  # Opens folder dialog to select save location

    if save_dir:
        print("Started Download...")
        vid_download(video_url, save_dir)
    else:
        print("Invalid Location.")  # Notifies if no location is selected

if __name__ == "__main__":
    # Creates window
    root = tk.Tk()
    root.title("YouTube Video Downloader")
    root.geometry("400x150")

    # Create and pack the label and entry for URL input
    url_label = tk.Label(root, text="Enter YouTube URL:")
    url_label.pack(pady=10)

    url_entry = tk.Entry(root, width=50)  # Text entry for URL
    url_entry.pack(pady=5)

    # Create and pack the download button
    download_button = tk.Button(root, text="Download", command=download_video)
    download_button.pack(pady=20)

    root.mainloop() 
