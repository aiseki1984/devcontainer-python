# Python Devcontainer

- python
- mysql
- phpmyadmin
- mailpit

# venv

```shell
$ python -m venv venv
$ source venv/bin/activate

# requirements.txt
$ pip install -r requirements.txt
$ pip freeze > requirements.txt
```

# find でのディレクトリの削除

https://qiita.com/mtakahashi-ivi/items/a678b6514674350c05a3

```shell
# venvを検索
$ find . -type d -name venv
# venvを削除
$ find . -type d -name venv -exec rm -rf {} +


$ find . -type d -name <DIR_NAME> -prune -exec rm -rf {};
$ find . -type d -name .svn -prune -exec rm -rf {};
$ find . -type d -name <DIR_NAME> -prune -exec rm -rf {} +
$ find . -type d -name .svn -prune -exec rm -rf {} +
```

## **pycache**削除

```shell
$ find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf
```

# よく使う pip コマンド

https://qiita.com/Masaaki_Inaba/items/fe4a246a7e6fcd9c4726

## ライブラリがあるか確認

```shell
# 例えばuvicornがあるか確認したいとき
$ pip freeze | grep "uvicorn"
uvicorn==0.15.0
```

## jupyter lab

```shell
$ jupyter lab --no-browser --allow-root --port=8888 --ip=0.0.0.0
```

## vscode remote container で ssh で git push

https://wonwon-eater.com/vscode-remote-containers-git/
https://qiita.com/frozenbonito/items/5bb6f30f1e8df8e02317

# devcontainer を使いたくないときは

```
$ docker-compose -f .decontainer/docker-compose.yml up -d
```

```shell
$ uvicorn blog.main:app --host 0 --reload
$ uvicorn app.api.main:app --host 0 --reload
http://localhost:8000/docs
```
