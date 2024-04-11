# pythondevpractice

Practice of Python development environment.

# Setup
0. Install VSCode, Python, Rust, and Rye in that order. It is essential to install Rust before Rye. If Rye is installed before Rust on Windows, you should delete the Users/.rye folders.
1. ```>>> git clone [this url]```
2. Install recommended extensions of VSCode (written in extensions.json)
3. ```>>> rye sync```
4. ```>>> rye run pre-commit install``` (If you use pre-commit)

# Structure
Version control system: Git  
Source-code editor: VSCode  
Language: Python  
Package manager: Rye (uv) by Rust  
Spell check: Code Spell Checker in VSCode
Linter: Ruff by Rust  
Formatter: Ruff by Rust  
Type Checking: Pylance in VSCode & mypy in CUI  
Python docstring style: Numpy style 
Test process: pytest  
Container virtualization: Docker & DevContainer in VSCode

VSCode extensions;
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

## Docker
- [Docker 概要](https://qiita.com/etaroid/items/b1024c7d200a75b992fc)

# To do
https://sogo.dev/posts/2023/11/rye-with-docker
https://zenn.dev/daifukuninja/articles/f2997585867f7b
https://zenn.dev/tk_resilie/articles/python_my_best_project  
pytest  
bandit  
logging: https://qiita.com/knknkn1162/items/87b1153c212b27bd52b4  

mypy が ipynb を見ない。 pre-commit 時も見れていない。
