import os
import shutil
import logging
import pwnagotchi.plugins as plugins

class ResetVoice(plugins.Plugin):
    __author__ = "Dein Name"
    __version__ = "1.0.0"
    __license__ = "MIT"
    __description__ = "Reset voice to original from /c_resetcharacter"

    def on_loaded(self):
        logging.info("[ResetVoice] Plugin loaded – restoring original voice.py...")
        voice_src = "/c_resetcharacter/voice.py"
        voice_dst = "/home/pi/.pwn/lib/python3.11/site-packages/pwnagotchi/voice.py"

        if os.path.exists(voice_src):
            try:
                shutil.copy2(voice_src, voice_dst)
                logging.info("[ResetVoice] voice.py restored successfully.")
            except Exception as e:
                logging.error(f"[ResetVoice] Failed to restore voice.py: {e}")
        else:
            logging.warning("[ResetVoice] Source voice.py not found, nothing restored.")
