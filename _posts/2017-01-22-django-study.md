---
title: Django
layout: post
date: '2017-01-22 12:44:09'
tags:
- python
- django
- framework
---

# Part 1

Tutorial 문서는 [이곳](https://docs.djangoproject.com/en/1.7/intro/tutorial01/)의 문서를 따라했다.

설치되어 있는 장고의 버전을 확인해 보자.

~~~
python -c "import django; print(django.get_version())"
-c option means "command"
~~~

장고 어플리케이션을 만들기 전에 **가상환경(virtualenv)** 을 만들어서 독립된 개발환경을 꾸려본다.

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

유의할 점은, 프로젝트를 만들 때 **django** 라는 네이밍이나 **test** 라는 네이밍을 쓰는 것을 추천하지 않는다. (파이썬의 내장 패키지와 충돌을 일으킬 수 있기 때문이다.)

### 프로젝트 생성하기.

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
- **manage.py** 는 명령어 유틸리티이다. 장고 프로젝트를 통해 다양한 방식으로 interaction할 수 있게 해준다.  좀 더 자세한 기능을 알고 싶다면 [이곳](https://docs.djangoproject.com/en/1.7/ref/django-admin/)을 보는 것을 추천한다.
- **mysite/** 디렉토리는 생성한 프로젝트의 파이썬 패키지가 실제로 들어가 있는 곳이다.
- **mysite/__init__.py** 는 파이썬이 이 디렉토리가 파이썬 패키지로 인식하게 끔 하는 파일이다.
- **mysite/settings.py** 는 장고 프로젝트의 설정이 들어가 있는 곳이다.
- **mysite/urls.py** 는 장고 프로젝트의 URL 선언이 들어가 있는 곳이다.  장고 URL이 어떤식으로 작동하는지 알고 싶다면 [이곳](https://docs.djangoproject.com/en/1.7/topics/http/urls/)을 보도록한다.
- **mysite/wsgi.py** 는 wsgi의 진입점이다. 웹서버가 한테 생성한 프로젝트를 제공할 수 있도록 한다.

---

### Database setup
데이터 베이스 셋업은 **mysite/settings.py** 에서 한다.
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
### 개발 서버 실행하기

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
### 모델 생성하기
**프로젝트와 앱의 차이는 무엇인가요?**
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

**polls**앱에 속해있는 **models.py** 에 2가지 모델을 생선한다.

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
### 모델 활성화 하기

- 또 뜬금포지만, 장고 앱의 철학은, 각 앱이 컨테이너(프로젝트에)에 **pulggable** 할 수 있도록 설계가 되어져 있다. 뜬금포를 꺼내는 이유는 polls앱을 프로젝트 내에 생성했다고, 바로 사용할 수 있는 것이 아니라, settings.py에서 설정을 해줘야 사용할 수 있기 때문이다.

**mysite/settings.py** 에 들어가서 **INSTALLED_APPS** 에서 **'polls'** 문자열을 추가해주자.

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
### API로 장고 가지고 놀기.

~~~
python manage.py shell
~~~

이 방식으로 하기가 싫다면, 다음과 같이 해보자. 이렇게 하면 **mysite/settings.py** 에 있는 설정 내용을 불러와서 프로젝트가 설정이된다.
ipython notebook에서 할때는 이런 방식으로 프로젝트와 앱을 로딩해서 가지고 놀 수 있다.

~~~
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

import django
django.setup()
~~~

---
# Part 2
### 최고 관리자 만들기

~~~
python manage.py createsuperuser
~~~

---
### 개발 서버 실행하기

~~~
python manage.py runserver
~~~

---
### 투표 앱을 관리자 화면에서 수정할 수 있게 하기
- **polls/admin.py** 파일을 연 후, 다음을 추가한 다음, **localhost:8000/admin/** 사이트를 들어가본다.

~~~
from django.contrib import admin
from polls.models import Question

admin.site.register(Question)
~~~

---
# Part 3

django에서 말하는 **view** 란 web page를 일컫는다. 이 web page는 특정한 함수와 특정한 템플릿을 통해 제공된다.  
django에서 웹 페이지와 컨텐츠는 뷰에 의해서 제공이 되는데, 각각의 뷰는 파이썬 함수에의해서 표현된다.(method, class-based-view).  

**polls/view.py** 에 다음과 같이 메소드를 만들어보자.

~~~
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello! this is poll index page!')
~~~

view를 보게 하기 위해서는 view를 url에 매핑 시켜주어야 한다.
**polls/urls.py** 파일을 생성해 보자. 생성한 파일에 다음 코드를 작성해 보자.

~~~
from django.conf.urls import patterns, url
from polls import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)
~~~

polls 앱에 view를 매핑 시켰으면, 이제 프로젝트 url에 다음 코드를 작성한다.
**mysite/urls.py** 파일을 연 후,

~~~
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^polls/', include('polls.urls')), # 이 부분을 작성한다.
    url(r'^admin/', include(admin.site.urls)),
)
~~~

이제 **http://localhost:8000/polls/** 를 통해 접속해 보면 다음과 같은 메시지가 나올 것이다.

~~~
Hello! this is poll index page!
~~~

이 메시지는 **polls/views.py** 에 작성한 **index** 메소드의
리턴 오브젝트 **(HttpResponse('Hello! this is poll index page!'))** 와 일치한다.

위 코드를 보면서 유심히 봐야할 점은 **url** 함수가 인자를 4개를 받는 다는 점이다. 이 중 2개는 필수고, 2개는 옵션이다.
- 필수
  - regex
  - view
- 옵션
  - kwargs
  - name

**view** 를 더 작성해 보도록 해보자.  
**polls/views.py** 에 다음과 같이 메소드를 추가로 작성해보자.

~~~
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
~~~

**polls/urls** 모듈에 다음과 같이 url을 추가로 작성해보자.

~~~
from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns('',
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<question_id>\d+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>\d+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
)
~~~

위와 같이 만들어 놓은 상태에서, 누군가가 이 웹사이트에 요청을 하는 상황을 가정해 보자.  
예를 들어서 **/polls/34/** 로 누군가가 **request** 를 보냈다고 하자.  
이 상황에서 일어나는 일련의 행위들은 다음과 같다.
- Django는 **mysite.urls** 파이썬 모듈을 로딩 한다. (왜냐하면 **ROOT_URLCONF** 에 해당모듈을 지정해 놓았기 때문이다. 실제로 그렇다.)
- 로딩한 파이썬 모듈에서 Django는 **urlpatterns** 라는 변수를 찾을 것이다. 그리고 정규표현식을 차례로 탐색할 것이다.
- **include()** 함수는 다른 URL 설정을 참조하게 된다.
  - 주의할 점은 **include** 함수는 **$(문자열 매칭의 끝을 알리는 기호)** 를 가지고 있지 않고, **/(슬래시)** 로 끝난다.
- Django가 **include()** 함수를 만나면, 그 지점까지 일치하는 URL 부분을 잘라서 버리고, 추가 처리를 위해 나머지 문자열(URL)을 URLconf로 보낸다.
- **include()** 함수의 아이디어는 URL들을 손쉽게 **plug-and-play** 할 수 있도록 한다는 점에 있다.
- **polls** 앱이 자신만의 **URLconf(polls/urls.py)** 를 가지고 있기 때문에, 이 설정내용은 다양한 경로 밑에 있다고 하더라도, 앱은 여전히 작동하게 된다.

**/polls/34/** 로 요청을 보냈을 때, Django에서 일어나는 일들을 한번 살펴보자.
- Django는 **'^polls/'** 를 찾은 다음, 매칭시킨다.
- Django는 일치하는 텍스트(**"polls/"**)를 벗겨낸 다음, 남은 텍스트(**34/**)를 **polls.urls** 의 URLconf 에 보내서 처리한다.
- **polls.urls** 에서는 남은 텍스트를 **r'^(?P<question_id>\d+)/$'** 와 일치여부를 비교한 후, **detail()** view 를 호출한다.

~~~
detail(request=<HttpRequest object>, question_id='34')
~~~

- 위와 같이 호출된 결과를 받아서 request를 보낸 사용자에게 결과를 보낸다.

django는 routing규칙이 상당히 복잡하다. part 3은 이런 복잡한 routing규칙에 대한 예시를 보여주고 있다.

---
### 행위를 하는 뷰를 작성해보기.
- 뷰는 둘 중 하나의 행위를 하게 되어 있다. 그 둘은 뭐냐 하면..
  - 요청한 페이지에 HttpResponse 객체를 담아서 반환한다.
  - 예외를 일으킨다. **Http404** 객체같은..

**polls/views.py** 에 있는 코드를 다음과 같이 수정해보자.

~~~
from django.http import HttpResponse

from polls.models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([p.question_text for p in latest_question_list])
    return HttpResponse(output)
~~~

그리고 위의 코드를 다음과 같이 고쳐보자. 변한게 있다면, index 메소드는 index.html 템플릿을 호출한 다음, context에 넘긴다.   

~~~
from django.http import HttpResponse
from django.template import RequestContext, loader

from polls.models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = RequestContext(request, {
        'latest_question_list': latest_question_list,
    })
    return HttpResponse(template.render(context))
~~~

그리고 **render()** 메소드를 사용해서 리팩토링을 해보자.

~~~
from django.shortcuts import render

from polls.models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
~~~    

**templates/polls** directory를 만들어 보자. Django는 템플릿을 이곳에서 찾게 될 것이다.  
Django의 TEMPLATE_LOADERS 세팅을 통해서 다양한 소스로 부터 템플릿을 import해서 쓸수 있게 한다.  
기본 설정은 **django.template.loaders.app_directories.Loader** 인데, **INSTALLED_APPS** 에 있는
**templates** subdirectory를 탐색한다. (이 설정 때문에 우리가 따로 **TEMPLATE_DIRS** 을 건드리지 않았다.)


이제 **polls/templates/polls/index.html** 을 다음과 같이 고쳐보자.


~~~
{% raw %} {% if latest_question_list %} {% endraw %}
{% raw %}     <ul> {% endraw %}
{% raw %}     {% for question in latest_question_list %} {% endraw %}
{% raw %}         <li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li> {% endraw %}
{% raw %}     {% endfor %} {% endraw %}
{% raw %}     </ul> {% endraw %}
{% raw %} {% else %} {% endraw %}
{% raw %}     <p>No polls are available.</p> {% endraw %}
{% raw %} {% endif %} {% endraw %}
~~~

view 함수를 통해서 넘어온 **latest_question_list** 객체를 템플릿에서 사용할 수 있게 되었다.

---

### 404 에러 발생시키기.

Question 객체에 데이터가 없을 수도 있으니 다음과 같이 고쳐보자.

~~~
from django.http import Http404
from django.shortcuts import render

from polls.models import Question

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})
~~~    

**try catch** 문으로 코드가 지저분해지는 것을 방지하기 위해서 django의 내장 객체 **get_object_or_404** 를 써보자.

~~~
from django.shortcuts import get_object_or_404, render
from polls.models import Question
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
~~~    

---
### 템플릿에 하드코딩으로 작성한 URL을 없애보자.

**polls/index.html** 템플릿에서 다음과 같은 코드가 있었다.

~~~
<li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
~~~

투표의 질문을 누르면 다른 웹페이지로 이동하는 코드였는데, 이 부분이 하드코딩 되어 있었다.  
이 부분을 다음과 같이 바꿔보자.

~~~
<li><a href="{% raw %}{% url 'detail' question.id %}{% endraw %}">{{ question.question_text }}</a></li>
~~~

**{% raw %}{% url %}{% endraw %}** 템플릿 테그를 이용해서 URL 설정에 정의되어 있는 특정 URL 경로의 의존성을 제거 할 수 있게 된다.

---

### URL 이름을 namespace화 하기.

예제 프로젝트는 **polls** 앱 하나밖에 없지만, 실제 장고 프로젝트에서는 수십개가 넘는 앱을 등록해서 사용할 수 있게 될 것이다.
장고는 어떻게 URL 이름들을 구별할 수 있을까?   
예를 들어서 **polls** 앱은 **detail** 뷰를 가지고 있다. 근데 만약에 **blog** 앱도 **detail** 뷰를 가지고 있다면 어떻게 될까?
Django는 **{% raw %}{% url %}{% endraw %}** 템플릿 테그를 사용할 때 어떤 앱의 view를 생성해서 만들어야할지 알까?  

답을 말하자면 최상의 URL설정에서 namespace를 더하면 된다. **mysite/urls.py** 에서 namespace를 더해보자.

~~~
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
)
~~~

그리고 네임스페이스가 필요한 템플릿(**polls/templates/polls/index.html**)을 다음과 같이 고쳐준다.

~~~
<li><a href="{% raw %}{% url 'polls:detail' question.id %}{% endraw %}">{{ question.question_text }}</a></li>
~~~

---

# Part 4

### Generic View 사용하기 : 적은 코드가 더 낫다!

Part 1~3에서 만들어 왔던 **detail(), results(), index()** 뷰들의 공통점이 있다.  
이런 뷰들은
- URL을 통해서 넘어온 인자(parameter)를 통해서 데이터베이스로부터 데이터를 가지고 오고,
- URL에 매핑하는 템플릿을 로딩한 다음
- 렌더링된 템플릿을 반환
하는 공통점을 가지고 있다. 이런 행위들이 꽤나 공통적으로 이루어지기 때문에, Django는 **generic views** 라는 시스템을 제공한다.

투표 앱을 **generic views system** 을 사용하는 형태로 바꿔보자. 바꿔가는 과정은 다음과 같다.
1. URLconf을 바꾼다.
2. views에서 필요없는 코드들을 지운다.
3. django의 generic views를 기반으로한 새로운 뷰를 만든다.

---

# Part 5

### 자동화된 테스트 만들기.

### 첫번째 테스트 작성해보기.

**shell** 에 접속한 후, 다음 코드를 작성해보자.

~~~
## shell login
python manage.py shell

>>> import datetime
>>> from django.utils import timezone
>>> from polls.models import Question
>>> # create a Question instance with pub_date 30 days in the future
>>> future_question = Question(pub_date=timezone.now() + datetime.timedelta(days=30))
>>> # was it published recently?
>>> future_question.was_published_recently()
True
~~~

코드를 보면 알다시피, 미래에 만든 질문은 **recent** 일 수 없다. 이제 이 버그를 고쳐보도록 하자.

**polls/tests.py** 에 다음 테스트 코드를 작성해보도록 하자.

~~~
import datetime

from django.utils import timezone
from django.test import TestCase

from polls.models import Question

class QuestionMethodTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() should return False for questions whose
        pub_date is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertEqual(future_question.was_published_recently(), False)
~~~

---

### 테스트 실행하기

~~~
python manage.py test polls
~~~

위 명령어를 실행하면 일어나는 일은

- **python manage.py test polls** 은 **polls** 어플리케이션에 있는 테스트를 찾는다.
- 테스트 프로그램은 **django.test.TestCase** 클래스를 상속받은 클래스를 찾는다.
- 테스트 프로그램은 테스트를 목적으로 하는 **특별한 데이터베이스** 를 생성한다.
- 테스트 프로그램은 **test methods** 들을 찾는다. 특히 **test** 로 시작하는 메소드들을 찾는다.
- 테스트 코드를 실행한 후, 통과여부를 말해준다.

---

### 버그 수정하기

**polls/models.py** 에 있는 코드를 수정한 다음 테스트 프로그램을 실행한다.

~~~
def was_published_recently(self):
    now = timezone.now()
    return now - datetime.timedelta(days=1) <= self.pub_date <= now
~~~

---

### 뷰 테스트하기

투표 어플리케이션은 사려깊게 작성하지 않았다. 누가 질문지를 미래에 게시한다고 설정을 해놓아도, 누구나 볼 수 있다.  
질문지가 게시가 되기 전날까지는 보이지 않도록 해야 한다. 이 상황을 고쳐보자.

---

### Django 테스트 클라이언트 생성하기.  

다시, shell환경에 접속해본 후, 환경설정을 해보자.

~~~
python manage.py shell

>>> from django.test.utils import setup_test_environment
>>> setup_test_environment()
~~~

테스트 클라이언트를 생성한 후, 각 url별로 테스트를 해보자.

~~~
>>> from django.test import Client
>>> # create an instance of the client for our use
>>> client = Client()
>>> # get a response from '/'
>>> response = client.get('/')
>>> # we should expect a 404 from that address
>>> response.status_code
404
>>> # on the other hand we should expect to find something at '/polls/'
>>> # we'll use 'reverse()' rather than a hardcoded URL
>>> from django.core.urlresolvers import reverse
>>> response = client.get(reverse('polls:index'))
>>> response.status_code
200
>>> response.content
'\n\n\n    <p>No polls are available.</p>\n\n'
>>> # note - you might get unexpected results if your ``TIME_ZONE``
>>> # in ``settings.py`` is not correct. If you need to change it,
>>> # you will also need to restart your shell session
>>> from polls.models import Question
>>> from django.utils import timezone
>>> # create a Question and save it
>>> q = Question(question_text="Who is your favorite Beatle?", pub_date=timezone.now())
>>> q.save()
>>> # check the response once again
>>> response = client.get('/polls/')
>>> response.content
'\n\n\n    <ul>\n    \n        <li><a href="/polls/1/">Who is your favorite Beatle?</a></li>\n    \n    </ul>\n\n'
>>> # If the following doesn't work, you probably omitted the call to
>>> # setup_test_environment() described above
>>> response.context['latest_question_list']
[<Question: Who is your favorite Beatle?>]
~~~

테스트 코드에 response객체의 property 값을 기준으로 테스트를 진행할 수 있다. 
