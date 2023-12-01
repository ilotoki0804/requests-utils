"""빌드를 자동화합니다."""
import os
import shutil
import subprocess
from pathlib import Path

try:
    shutil.rmtree('dist')
    shutil.rmtree('build')
except FileNotFoundError:
    os.mkdir('dist')
os.system(r'.\.venv312\Scripts\python.exe setup.py sdist bdist_wheel')
whl_file_name = os.listdir('dist')[0]
os.system(rf'.\.venv312\Scripts\python.exe -m pip install --force-reinstall dist/{whl_file_name}')  # --user를 추가하면 오류가 덜 날 수도 있음
if input('Submit changes? (y or not)') in ('y', 'Y', 'ㅛ'):
    token = Path('token.txt').read_text(encoding='utf-8')
    subprocess.run(["twine", "upload", "-u", '__token__', "-p", token, "dist/*"], check=False)
    os.system(r'.\.venv312\Scripts\python.exe -m pip show resoup')
