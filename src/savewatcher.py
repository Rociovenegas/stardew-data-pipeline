import time
import shutil
import os
from pathlib import Path
from datetime import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class OnMyWatch:

    def __init__(self, watch_directory, destination_path):
        self.observer = Observer()
        self.watch_directory = watch_directory
        self.destination_path = destination_path

    def run(self):
        event_handler = StardewSaveHandler(self.destination_path)
        self.observer.schedule(event_handler, self.watch_directory, recursive = True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Observer Stopped")

        self.observer.join()

def make_backup(event, destination_path):
    try:

        src_path = Path(event.src_path)  
        file_name = src_path.name      
        
        # Carpeta destino usando el nombre del archivo (sin extensión)
        save_directory = Path(destination_path) / src_path.stem
        if not save_directory.is_dir():
            save_directory.mkdir(parents=True, exist_ok=True)

        # Crear nombre único con timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
        backup_name = f"{file_name}_{timestamp}"

        # Copiar archivo
        shutil.copy2(src_path, os.path.join(save_directory, backup_name))


    except IOError as e:
        print(f"Error copying file {src_path}: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")




class StardewSaveHandler(FileSystemEventHandler):
    def __init__(self, destination_path):
        self.destination_path = destination_path  

    
    def on_moved(self, event):
        if event.is_directory:
            return None
        else:
            file_name = Path(event.src_path)
            folder_file = file_name.parent.name
            if (folder_file == file_name.name):
                make_backup(event, self.destination_path)
                print(f"{time.time()}: {event.event_type} → {event.src_path}")
                


            

if __name__ == '__main__':
    user_home = Path.home()

    # Construye las rutas de las carpetas de forma dinámica
    watch_directory = user_home / ".config" / "StardewValley" / "Saves"
    destination_path = user_home / "StardewValleyDashboard" / "Saves"
    watch = OnMyWatch(watch_directory, destination_path)
    watch.run()