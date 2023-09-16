import re
from pathlib import Path

from setuptools import setup, find_packages

from requests_utils import __version__

long_description = '이 설명은 최신 버전이 아닐 수 있습니다. 만약 최신 버전을 확인하고 싶으시다면 [여기](https://github.com/ilotoki0804/requests-utils)를 참고하세요.\n'
long_description += Path('README.md').read_text(encoding='utf-8')
# 사진 대체
repl = r'![\g<1>](https://raw.githubusercontent.com/ilotoki0804/requests-utils/master/\g<2>)'
long_description = re.sub(r'!\[(.+?)\]\((images\/.+?)\)', repl, long_description)

setup(
    name='requests-utils',
    version='.'.join(map(str, __version__)),
    description='Various convenient features about requests.',
    author='ilotoki0804',
    author_email='ilotoki0804@gmail.com',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    url='https://github.com/ilotoki0804/requests-utils',
    install_requires=Path('requirements.txt').read_text(encoding='utf-8').split(),
    packages=find_packages(exclude=[]),
    package_data={
        # "": ["*.pyi", 'py.typed'],
        "": ["*.pyi"],
    },
    keywords=['requests', 'bs4', 'BeautifulSoup', 'async', 'caching', 'cache'],
    python_requires='>=3.10',
    # package_data={},
    zip_safe=False,
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
)
