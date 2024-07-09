from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import os
import subprocess

class RebuildHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith(".md") or event.src_path.endswith(".ipynb"):
            print(f"Detected change in {event.src_path}. Rebuilding the book...")
            subprocess.run(["jupyter-book", "build", "."])

if __name__ == "__main__":
    event_handler = RebuildHandler()
    observer = Observer()
    observer.schedule(event_handler, path='.', recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
