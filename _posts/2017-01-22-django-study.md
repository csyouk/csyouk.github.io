---
title: Django
layout: post
date: '2017-01-22 12:44:09'
tags:
- python
- django
- framework
---

Tutorial 문서는 [이곳](https://docs.djangoproject.com/en/1.7/intro/tutorial01/)의 문서를 따라했다.

설치되어 있는 장고의 버전을 확인해 보자.
~~~
python -c "import django; print(django.get_version())"
-c option means "command"
~~~
장고 어플리케이션을 만들기 전에 **가상환경(virtualenv)**을 만들어서 독립된 개발환경을 꾸려본다.
~~~
python3.4 -m venv venv
-m option means "module name"
~~~
가상환경을 만든 폴더내에서 명령어를 실행시켜서 가상환경을 실행시킨다.
~~~
. venv/bin/activate
~~~
가상환경을 다 만들었으면, 이제 장고를 설치한다. MMT에서는 django를 1.7로 사용한다고 했으니, 1.7 버전으로 설치한다.
~~~
pip install django==1.7
~~~

---

이제 장고 프로젝트를 실행하기 위한 준비가 끝났다. 본격적으로 장고로 투표 시스템을 만들어보자.

유의할 점은, 프로젝트를 만들 때 **django**라는 네이밍이나 **test**라는 네이밍을 쓰는 것을 추천하지 않는다. (파이썬의 내장 패키지와 충돌을 일으킬 수 있기 때문이다.)

## 프로젝트 생성하기.
~~~
django-admin.py startproject mysite
~~~
위의 명령어를 치면 다음과 같이 폴더가 생성이 된다.
~~~
mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        wsgi.py
~~~				
하나씩 까보면,
- **mysite/** 루트 디렉토리는 프로젝트의 컨테이너일 뿐이다. 이 컨테이너의 이름은 다르게 바꿔도 된다.
- **manage.py**는 명령어 유틸리티이다. 장고 프로젝트를 통해 다양한 방식으로 interaction할 수 있게 해준다.  좀 더 자세한 기능을 알고 싶다면 [이곳](https://docs.djangoproject.com/en/1.7/ref/django-admin/)을 보는 것을 추천한다.
- **mysite/** 디렉토리는 생성한 프로젝트의 파이썬 패키지가 실제로 들어가 있는 곳이다.
- **mysite/__init__.py**는 파이썬이 이 디렉토리가 파이썬 패키지로 인식하게 끔 하는 파일이다.
- **mysite/settings.py**는 장고 프로젝트의 설정이 들어가 있는 곳이다.
- **mysite/urls.py**는 장고 프로젝트의 URL 선언이 들어가 있는 곳이다.  장고 URL이 어떤식으로 작동하는지 알고 싶다면 [이곳](https://docs.djangoproject.com/en/1.7/topics/http/urls/)을 보도록한다.
- **mysite/wsgi.py**는 wsgi의 진입점이다. 웹서버가 한테 생성한 프로젝트를 제공할 수 있도록 한다.

---

## Database setup
데이터 베이스 셋업은 **mysite/settings.py**에서 한다.
tutorial 에서는 SQLite를 사용한다.

db table을 생성시키기 위해서 다음 명령어를 사용한다.
~~~
python manage.py migrate
~~~
sqlite에 접속하기 위해서는
~~~
sqlite3 db.sqlite3
~~~
sqlite 의 shell command를 알고 싶다면 [이곳](https://sqlite.org/cli.html)을 참조할 것!

---
## 개발 서버 실행하기
~~~
python manage.py runserver
~~~
포트를 설정하려면
~~~
python manage.py runserver 8080
~~~
server machine이외에 다른 machine이 접속이 가능하게 하려면
~~~
python manage.py runserver 0.0.0.0:8080
~~~

---
## 모델 생성하기
** 프로젝트와 앱의 차이는 무엇인가요? **
- 앱 : 앱은 웹 어플리케이션을 일컫는다. (weblog system, database, ...)
- 프로젝트 : 앱의 상위개념이다. 설정과 앱들의 모음이다. 그렇다고, 앱이 프로젝트에 종속적으로 포함된 관계는 아니다. 물론 하나의 프로젝트는 여러개의 앱을 가지고 있지만, 앱은 복수 개의 프로젝트에 포함되어 있을 수 있다. (Microservice architecture를 생각해보라.)

이제 앱을 한번 만들어 보자.
~~~
python manage.py startapp polls
~~~
위 명령어를 실행하면 이제 프로젝트 구조는 다음과 같다.
~~~
mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        wsgi.py
    polls/
        __init__.py
        admin.py
        migrations/
            __init__.py
        models.py
        tests.py
        views.py
~~~
보다 시피, mysite라는 앱과 polls라는 앱이 존재하는 것을 알 수 있다.

뜬금포지만, django의 디자인 철학을 잠시 짚고 넘어가자면, [이곳](https://docs.djangoproject.com/en/1.7/misc/design-philosophies/#dry)을 참조하면 된다.

**polls**앱에 속해있는 **models.py**에 2가지 모델을 생선한다.
~~~
from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
~~~    

---
## 모델 활성화 하기

- 또 뜬금포지만, 장고 앱의 철학은, 각 앱이 컨테이너(프로젝트에)에 **pulggable**할 수 있도록 설계가 되어져 있다. 뜬금포를 꺼내는 이유는 polls앱을 프로젝트 내에 생성했다고, 바로 사용할 수 있는 것이 아니라, settings.py에서 설정을 해줘야 사용할 수 있기 때문이다.

**mysite/settings.py**에 들어가서 **INSTALLED_APPS**에서 **'polls'**문자열을 추가해주자.
~~~
mysite/settings.py

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'polls',
)
~~~

이제 장고한테 polls앱을 사용할 수 있게 되었다고 알려주자.
~~~
python manage.py makemigrations polls
~~~

마이그레이션을 하는 절차는 다음과 같다.
- 모델을 변경한다.
- **python manage.py makemigrations** 명령어를 실행해서 마이그레이션을 한다.
- **python manage.py migration** 명령어를 적용시켜 데이터베이스의 내용들을 변경한다.

---
## API로 장고 가지고 놀기.

~~~
python manage.py shell
~~~

이 방식으로 하기가 싫다면, 다음과 같이 해보자. 이렇게 하면 **mysite/settings.py**에 있는 설정 내용을 불러와서 프로젝트가 설정이된다.
ipython notebook에서 할때는 이런 방식으로 프로젝트와 앱을 로딩해서 가지고 놀 수 있다.
~~~
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

import django
django.setup()
~~~
