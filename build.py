"""빌드를 자동화합니다."""
import os
import shutil
from pathlib import Path

try:
    shutil.rmtree('dist')
    shutil.rmtree('build')
except FileNotFoundError:
    os.mkdir('dist')

os.system('poetry build')
os.system(f'poetry publish -u __token__ -p {Path("_token.txt").read_text("utf-8")}')
