import os
import shutil
import logging
import pwnagotchi.plugins as plugins
from PIL import Image, ImageOps

class GrunkelStan(plugins.Plugin):
    __author__ = "Counter Chicken"
    __version__ = "1.2.0"
    __license__ = "GPL3"
    __description__ = "Face + Voice replacement for Pwnagotchi"

    def on_loaded(self):
        logging.info("Grunkel Stan: Plugin loaded – Setup begins...")
        self.faces_path = self.options.get('faces_path', '/c_grunkelstan')
        self.voice_path = self.options.get('voice_path', '/c_grunkelstan/voice.py')
        self.pos_x = self.options.get('position_x', 0)
        self.pos_y = self.options.get('position_y', 34)
        self.original_voice_py = "/home/pi/.pwn/lib/python3.11/site-packages/pwnagotchi/voice.py"
        self._replace_voice_file()

    def _replace_voice_file(self):
        if os.path.exists(self.voice_path):
            try:
                # Replace voice.py
                shutil.copy2(self.voice_path, self.original_voice_py)
                logging.info(f"Grunkel Stan: voice.py successfully replaced with {self.voice_path}")
            except Exception as e:
                logging.error(f"Grunkel Stan: Error while replacing voice.py: {e}")
        else:
            logging.warning(f"Grunkel Stan: Custom voice.py ({self.voice_path}) not found – no changes made.")

    def on_ui_setup(self, ui):
        import pwnagotchi.ui.faces as faces
        from pwnagotchi.ui import components

        logging.info("Grunkel Stan: Loading PNG faces...")
        face_config = {'png': True, 'position_x': self.pos_x, 'position_y': self.pos_y}
        if os.path.isdir(self.faces_path):
            face_names = [
                "look_r", "look_l", "look_r_happy", "look_l_happy", "sleep", "sleep2",
                "awake", "bored", "intense", "cool", "happy", "excited", "grateful",
                "motivated", "demotivated", "smart", "lonely", "sad", "angry", "friend",
                "broken", "debug", "upload", "upload1", "upload2"
            ]
            for name in face_names:
                file_path = os.path.join(self.faces_path, name.upper() + ".png")
                if os.path.exists(file_path):
                    face_config[name] = file_path
            faces.load_from_config(face_config)
            logging.info(f"Grunkel Stan: {len(face_config) - 3} PNG faces loaded.")
        else:
            logging.warning(f"Grunkel Stan: faces_path {self.faces_path} not found.")

        try:
            if hasattr(faces, 'PNG') and faces.PNG:
                original_draw = components.Text.draw

                def draw_with_png(self, canvas, drawer):
                    if self.value and isinstance(self.value, str) and self.value.endswith('.png') and os.path.isfile(self.value):
                        try:
                            img = Image.open(self.value).convert('RGBA')
                            pixels = img.load()
                            for y in range(img.height):
                                for x in range(img.width):
                                    if pixels[x, y][3] < 255:
                                        pixels[x, y] = (255, 255, 255, 255)
                            if self.color == 255:
                                img = ImageOps.colorize(img.convert('L'), black="white", white="black")
                            img = img.convert('1')
                            canvas.paste(img, self.xy)
                            return
                        except Exception as e:
                            logging.error(f"Grunkel Stan PNG drawing: {e}")
                    original_draw(self, canvas, drawer)

                components.Text.draw = draw_with_png
                logging.info("Grunkel Stan: PNG drawing enabled.")
        except Exception as e:
            logging.error(f"Grunkel Stan: Error while patching Text.draw: {e}")
