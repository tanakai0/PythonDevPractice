# pythondevpractice

Practice of Python development environment.

# Setup
0. Install VSCode, Python, Rust, and Rye in that order. It is essential to install Rust before Rye. If Rye is installed before Rust on Windows, you should delete the Users/.rye folders.
1. ```>>> git clone [this url]```
2. Install recommended extensions of VSCode (written in extensions.json)
3. ```>>> rye sync```
4. ```>>> rye run pre-commit install``` (If you use pre-commit)

# Structure
## Methods
Version control system: Git  
Source-code editor: VSCode  
Language: Python  
Package manager: Rye (uv) by Rust  
Spell check: Code Spell Checker in VSCode  
Logging: logging package in Python  
Linter: Ruff by Rust  
Formatter: Ruff by Rust  
Type Checking: Pylance in VSCode & mypy in CUI  
Python docstring style: Numpy style  
Test process: pytest  
Container virtualization: Docker & DevContainer in VSCode

### VSCode extensions
- ms-python.python
- ms-toolsai.jupyter
- ms-python.vscode-pylance
- njpwerner.autodocstring
- ms-azuretools.vscode-docker
- ms-vscode-remote.remote-containers
- sdras.night-owl
- usernamehw.errorlens
- streetsidesoftware.code-spell-checker
- mhutchie.git-graph

## Folder hierarchy
Package programs: /package_name  
Test programs: /tests  
Scripts for analysis: /experiments  
VSCode extensions and settings: .vscode

# To do
- https://sogo.dev/posts/2023/11/rye-with-docker
- https://zenn.dev/daifukuninja/articles/f2997585867f7b  
- [【Rye \+ uv \+ Ruff】Docker で VS Code の Dev Container 上に快適な Python 環境を構築する](https://zenn.dev/dena/articles/rye_python_in_devcontainer)  
- [VSCode と devcontainer で始める開発環境構築 \#Docker \- Qiita](https://qiita.com/haruhikonyan/items/291e1e5413a827fc6d9a)  
- [Dev Containers入門～Dev Containersってなんだ編～ \#VSCode \- Qiita](https://qiita.com/dagamun/items/e8e856f0ee6cf8a457e0)  
- bandit  
- rope  
- GitHub actions  

# Guide
- Activate a .venv: ```>>> .\.venv\Scripts\activate``` for Windows, and ```>>> source .venv/bin/activate``` for Unix-like OS 
- Add a library for development: ```>>> rye add --dev library_name```
- ```>>> pytest``` search functions titled as test\_\* and classes titled as Test* in test\_\*.py or \*\_test.py. 
- Add a local dependency by Rye: ```>>> rye add packagename --path path/to/packagename```
- Test a docstring by Pytest: ```>>> rye run pytest --doctest-modules```  
- Store functions and test data used in tests as fixtures in tests/conftest.py. Fixtures defined in a conftest.py file can be used without import in files within the same or deeper directory levels.  
- rye scripts is prepared in [tool.rye.scripts] in pyproject.html. ```>>> rye fmt```, ```>>> rye lint```, and ```>>> rye test``` can be used.

# Troubleshooting
- To ensure the correct syntax analysis in VSCode for `import packagename` from the `tests` folder, I added `${workspaceFolder}` to the `python.analysis.extraPaths` in the VSCode's `settings.json`. 
- If you encounter a `ModuleNotFoundError: No module named 'pythondevpractice'`, execute them like `python -m tests.test_base` to force Python to run the scripts with the project's root directory in its path. Additionally, using `rye add packagename --path .` may add the project's root to the path persistently.  
- Mypy does not check .ipynb files. It is neither to check them during pre-commit.  
- Initially, I thought using a /src/packagename structure would allow for mimicking the production package environment by using pip install -e or rye add packagename --path ./src/packagename. However, VSCode unexpectedly adds src/ to the PYTHONPATH, which results in direct references to src/packagename. Consequently, I decided to place the package directly under the project root at /packagename.   
- Be aware that README.md uses trailing whitespace for line breaks. Depending on the editor settings, these trailing spaces might be automatically removed.  


# Reference

## Git
- [Setting up Git & Authenticating with GitHub from Git](https://docs.github.com/en/get-started/getting-started-with-git/set-up-git)
- [Git まとめ](https://qiita.com/gold-kou/items/7f6a3b46e2781b0dd4a0)


## VSCode
- [json 設定ファイルの優先度について](https://qiita.com/tabo_dev/items/df7e5b1b0d7c336af124)
- [Workspace recommended extensions](https://code.visualstudio.com/docs/editor/extension-marketplace#_workspace-recommended-extensions)
- [VSCode に Code Spell Checker を導入して typo と戦う \#VSCode \- Qiita](https://qiita.com/diescake/items/98c5a099e85775cd917d)  
- [VSCode で Python 書くのにおすすめな拡張機能](https://qiita.com/nanato12/items/ddf26487eb30714251c3)  

## Python
- [Python](https://www.python.org/)
- [Status of Python versions](https://devguide.python.org/versions/)
- [Pythonの相対パスimportを理解する \#Python \- Qiita](https://qiita.com/u943425f/items/bd94a30b52c9296e942d)

## Rust
- [Installing Rust for Windows](https://www.rust-lang.org/tools/install)

## Rye/uv
- [Rye](https://github.com/astral-sh/rye)
- [Installing Rye for Windows](https://rye-up.com/guide/installation/#installing-rye)
- [【Pythonのパッケージ管理に悩む方へ】パッケージ管理ツールRyeを使ってみた](https://dev.classmethod.jp/articles/get-start-rye-python/)
- [pythonパッケージ管理ツールryeを使う - 肉球でキーボード](https://nsakki55.hatenablog.com/entry/2023/05/29/013658)

## Ruff
- [Ruff](https://github.com/astral-sh/ruff)
- [Configuring Ruff（default はかなり black に近い）](https://docs.astral.sh/ruff/configuration/)

## pre-commit
- [pre-commit で Python コードをキレイに管理してみた](https://zenn.dev/fikastudio/articles/73c226000f9a0a)
- [pre-commit + Ruff](https://zenn.dev/nowa0402/articles/79aaeb8db5731c)
- [pre\-commitでコミット時にコードの整形やチェックを行う](https://zenn.dev/yiskw713/articles/3c3b4022f3e3f22d276d)

## project
- [Python プロジェクトテンプレート](https://zenn.dev/tk_resilie/articles/python_my_best_project)
- [\[2023年最新版:rye対応\]Python案件で汎用的に使えるモダンなプロジェクトテンプレート](https://zenn.dev/tk_resilie/articles/python_my_best_project)  

## Docker
- [Docker 概要](https://qiita.com/etaroid/items/b1024c7d200a75b992fc)

# Pytest
- [pytest: helps you write better programs — pytest documentation](https://docs.pytest.org/en/8.0.x/)
- [pytest ヘビー🐍ユーザーへの第一歩 \- エムスリーテックブログ](https://www.m3tech.blog/entry/pytest-summary)

# Logging
- [Logging HOWTO — Python 3\.12\.3 documentation](https://docs.python.org/3/howto/logging.html)  
- [logging入門 \#Python \- Qiita](https://qiita.com/knknkn1162/items/87b1153c212b27bd52b4)  
