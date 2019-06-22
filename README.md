# python-playground

Python Playground

## virtualenv

구성

```sh
sudo pip install virtualenv
cd ~/my/project/dir
virutalenv .env
```

실행

```bash
#!/bin/bash
source ".env/bin/activate"
```

확인

```sh
which python
```

## requirements

```sh
.env/bin/pip freeze > requirements.txt
.env/bin/pip install -r requirements.txt
```
