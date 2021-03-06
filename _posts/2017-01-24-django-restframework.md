---
title: Django-restframework
layout: post
date: '2017-01-24 01:00:32'
tags:
- django
- restful
---

**shell** 에서 여러가지 실험을 하기 위해서, notebook을 설치한다. 문서는 [이곳](https://opensourcehacker.com/2014/08/13/turbocharge-your-python-prompt-and-django-shell-with-ipython-notebook/)을 참조한다.

~~~
# after entering virtualenv
pip install django_extensions

# add settings.py
INSTALLED_APPS = (
  ...
  'django_extensions'
)

# after finishing configuration, start notebook in the Terminal
python manage.py shell_plus --notebook
~~~

---

# Tutorial 1

**django restframework** 을 쓰기 위해서는 다음 요구사항을 만족시켜야 한다.

- Python (2.7, 3.2, 3.3, 3.4, 3.5)
- Django (1.8, 1.9, 1.10)

다음 dependency들을 설치한다.

~~~
pip install django
pip install djangorestframework
pip install pygments
~~~

프로젝트 설정을 한 다음. web api를 만들어 보자.

~~~
django-admin.py startproject tutorial
cd tutorial

python manage.py startapp snippets
~~~

**INSTALLED_APPS** 에 rest_framework을 추가한다. **tutorials/settings.py** 에 추가해보자.

~~~
INSTALLED_APPS = (
    ...
    'rest_framework',
    'snippets.apps.SnippetsConfig',
)
~~~

### 모델 생성하기.

**snippets/models.py** 에 다음 모델을 생성하자.

~~~
from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    class Meta:
        ordering = ('created',)
~~~

django한테 생성한 모델을 데이터베이스에 반영시키도록 하자.

~~~
python manage.py makemigrations snippets
python manage.py migrate
~~~

---

###  Serializer class 생성하기.

**snippets/serializers.py** 에 다음 코드를 추가해 보자.

~~~
from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


class SnippetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance
~~~

- serializer 클래스의 첫번째 부분은 field들이 serialized/deserialized 되는지 정의한다.
- **create() update()** 메소드는 fully fledged instance가 serializer.save()를 호출했을 때 어떻게 수정되는지를 보여준다.

---

### Serializers 가지고 놀아보기.

Serializer에 대한 내용을 자세히 알아보고 싶다면 [이곳](http://www.django-rest-framework.org/api-guide/serializers/)을 참조한다.
Serializer의 역할은 다음과 같다.
- 복잡한 데이터(Querysets, model instances, ...)들을 native Python datatype으로 쉽게 변환시켜 준다.
- 또한, JSON, XML 같은 데이터 형식으로 쉽게 변환을 시켜준다.
- Serialization 에 대칭 되는 기능, Deserialization 또한 기능을 제공해 준다.

Django의 Form class, ModelForm class 에 대응되는 개념으로  
Rest framework에서는 Serializer, ModelSerializer등을 제공한다.

**ModelSerializers** 의 기능 또한 눈여겨 볼 필요 있다.
대단한 기능은 아니지만, model에 대한 define을 할 때, 조금이라도 덜 타이핑 할 수 있게 한다.

**Meta class** 가 어떤 역할을 하는지 알고 싶으면 [다음](http://stackoverflow.com/questions/10344197/how-does-djangos-meta-class-work)
문서를 읽어보는 것이 좋다.

---

# Tutorial 2

### Request & Response

- Request object
- Response object
- Status code
- Wrapping API views
  - **@api_vew**  decorator는 function-based view에 쓰인다.
  - **APIView** 클래스는 class-based view에 쓰인다.
- 접미사 옵션을 붙여서 URL에서 처리하도록 하기.

---

# Tutorial 3

### Class-based views

function-based views를 class-based views로 바꾸는 작업을 진행한다.

**mixins (multiple inheritance)** 개념을 통해서 기존의 class-based view를 refactoring 하는 과정을 보여준다.

> **구현상속(Implementation Inheritance)**
> 이미 어느 정도 구현이 되어 있는 객체를 상속시키는 방법.
> java extends 혹은 implements interface

이 쪽 분야의 오래된 논쟁거리 중 하나는 Inheritance가 좋냐, Composite가 좋냐.. 뭐 이런 논쟁거리가 있다고 한다.
[이곳](https://www.facebook.com/groups/django/permalink/971113676258465)을 참조한다.


---

# Tutorial 4

### Authentication & Permissions

요청에 인증을 붙이는 방법을 다룬다.

---

# Tutorial 5

### Relationships & Hyperlinked APIs

---

# Tutorial 6

### ViewSets & Routers

- 아직 쓰고 있지 않고 있다고 한다.

viewset을 활용하며 추상성을 획득해서 일관성을 높일수 있다.  
반대로 정확히 어떤일을 하는지 추적하기가 힘들어진다.

---

# Tutorial 7

### Schemas & client libraries
