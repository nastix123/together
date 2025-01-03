import os
from pathlib import Path

import environ

env = environ.Env(DEBUG=bool, default=False)

BASE_DIR = Path(__file__).resolve().parent.parent

environ.Env.read_env(os.path.join(BASE_DIR.parent, ".env"))
