---
theme: dracula
background: https://source.unsplash.com/collection/94734566/1920x1080
class: text-center
highlighter: shiki
lineNumbers: true
drawings:
    persist: false
transition: slide-up
addons:
    - fancy-arrow
mdc: true
---

<div class="absolute top-10 left-1/2 -translate-x-1/2 w-full" data-id="title">
  <p class="text-5xl leading-8 font-mono mb-4 pb-4">What are triple </p>
  <p class="text-5xl leading-8 font-mono">dots in Python?</p>
</div>
<FancyArrow q2="[data-id=ellipsis]" arc="0.2" q1="[data-id=title]" pos1="bottom"  color="lime" roughness="2" pos2="top"></FancyArrow>


<div class="flex flex-col items-center justify-center h-full mb-2 gap-y-2">
  <div class="text-3xl font-mono position z-20">
  <pre><code><span style="color: #C678DC;">def</span><span style="color: #61AFEE;"> f</span>(<span style="color: #D19A66;">param1</span>):<span style="color: #D19A66;" data-id="ellipsis"> ...</span></code></pre>
  </div>
  </div>

<img src="/python.png" class="absolute bottom-10 left-10" width="200" height="200" />

<div class="absolute bottom-18 left-90 h-[250px] w-[200px] bg-[#15161D] position z-10"></div>
<img src="/soyjak.png" class="absolute bottom-20 right-40" width="400" height="400" />

---

<div class="flex flex-col items-center justify-center h-full mb-2 gap-y-2">
  <div class="text-3xl font-mono">Triple Dots</div>
  <img v-click="1" v-motion 
    :initial="{ opacity: 0 }"
    :enter="{ opacity: 1 }"
  src="/ellipsis.png" class="w-3/4 rounded-lg" />
</div>

---

<div class="flex flex-col items-center justify-center h-full mb-2 gap-y-2">
<p class="text-5xl font-mono">one minute python</p>
<p v-click="1" v-motion :initial="{ opacity: 0}" :enter="{ opacity: 1 }" :leave="{ opacity: 0 }" class="text-2xl font-mono">by saral.club</p>

</div>

---

## Triple dots

<ul>
<li
v-click="1"
v-motion
:initial="{ opacity: 0 }"
:enter="{ opacity: 1 }"
:duration="300"
>
<div 
class="mt-5"
>Formally <code>...</code> are known as <code>Ellipsis</code></div>
</li>
<li
v-click="2"
v-motion
:initial="{ opacity: 0 }"
:enter="{ opacity: 1 }"
:duration="300"
>
<div 
class="my-5"
><code>Ellipsis</code> is a built-in constant in python namespace </div>
</li>
</ul>

<div v-click="3">

````md magic-move
```python {none|none|none|*}
... is Ellipsis
```

```python
... is Ellipsis
# True
```

```python
... is Ellipsis
# True

type(...)
# <class 'ellipsis'>
```
````

</div>

---

## How to use `Ellipsis`

<div v-click="1" class="w-full mt-40">

````md magic-move
```python {none|*}
def my_function(param1, param2):
```

```python
def my_function(param1, param2):
  # TODO: Implement later
  ...
```

```python
class MyClass(ABC):

  @abstractmethod
  def my_method(self):
    pass
```

```python
class MyClass(ABC):

  @abstractmethod
  def my_method(self):
    ...
```

```python {1|3} //[!code hl]
from typing import Callable

Handler = Callable[..., None]

```

```python {5} //[!code hl]
from typing import Callable

Handler = Callable[..., None]

Integers = Tuple[int, ...]

```

```python
from pydantic import BaseModel, Field

class User(BaseModel):
  name: str = Field(..., description="User's name")
  age: int = Field(..., description="User's age")
```

```python
from pydantic import BaseModel, Field

class User(BaseModel):
  name: str = Field(..., description="User's name")
  age: int = Field(..., description="User's age")
```

```python
from pydantic import BaseModel, Field

class User(BaseModel):
  name: str = Field(default=..., description="User's name")
  age: int = Field(default=..., description="User's age")
```

```python
from pydantic import BaseModel, Field

class User(BaseModel):
  name: str = Field(default=..., description="User's name")
  age: int = Field(default=..., description="User's age")

  # Simplified version

  if default is Ellipsis:
    self.default = None
    self.required = True
```
````

</div>

<FancyArrow v-motion :initial="{ opacity: 0}" :enter="{ opacity: 1}" :duration="300" v-click="[9, 10]" arc="0.2" pos1="left" q1="[data-id=arc-end]" y2="340" x2="230" color="lime" roughness="2"></FancyArrow>

<div v-motion :initial="{ opacity: 0}" :enter="{ opacity: 1}" :duration="300" v-click="[9, 10]" class="absolute bottom-20 left-1/2 -translate-x-1/2 text-2xl" data-id="arc-end">Makes the parameter required</div>

---

<div class="flex flex-col items-center justify-center h-full mb-2 gap-y-2"
>
Thanks for watching!
</div>
