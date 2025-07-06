import os
import environ
from django.conf import settings
from threading import Lock


class EnvConfig:
    _instance = None
    _lock = Lock()  # pour thread safety

    @classmethod
    def get_env(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:  # double-checked locking
                    env = environ.Env(DEBUG=(bool, False))
                    env_path = os.path.join(settings.BASE_DIR, ".env")
                    if os.path.exists(env_path):
                        environ.Env.read_env(env_path)
                    cls._instance = env
        return cls._instance
