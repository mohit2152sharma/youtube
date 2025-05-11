# Advantages

<div class="grid grid-cols-3 gap-x-2 items-start justify-center h-full"
v-click="1"
v-motion
:initial="{ opacity: 0 }"
:enter="{ opacity: 1}"
:duration="1000"
>

<div class="h-full space-y-5">

<div>

## Memory

</div>

<div
    v-click="2"
    v-motion
    :initial="{ opacity: 0 }"
    :enter="{ opacity: 1}"
    :duration="500"
    class=""
>

````md magic-move {lines: false, at: 3}
```python

class A:
  def __init__(self):
    self.a = "A"

a = A()

sys.getsizeof(a)
# 56
```

```python
class A:
  def __init__(self):
    self.a = "A"

a = A()

sys.getsizeof(a)
# 56

class B:
  __slots__ = ["a"]
  def __init__(self):
    self.a = "A"

b = B()

sys.getsizeof(b)
# 40
```
````

</div>

</div>

<div 
    v-click="4"
    v-motion
    :initial="{ opacity: 0 }"
    :enter="{ opacity: 1}"
    :duration="500"
    class="h-full space-y-5">

<div>

## Speed

</div>

<div 
    v-click="5"
    v-motion
    :initial="{ opacity: 0 }"
    :enter="{ opacity: 1}"
    :duration="500"
    class=""
>

````md magic-move {lines: false, at: 4}
```python

class A:
    def __init__(self):
        self.a = "A"
class B:
    __slots__ = ["a"]
    def __init__(self):
        self.a = "A"

timeit(
  stmt="A()",
  setup="from __main__ import A;",
  number=1_000_000
)
# 0.06412366696167737
timeit(
  stmt="B()",
  setup="from __main__ import B;",
  number=1_000_000
)
# 0.05365570797584951
```
````

</div>
  </div>

<div 
    v-click="6"
    v-motion
    :initial="{ opacity: 0 }"
    :enter="{ opacity: 1}"
    :duration="500"
    class="h-full space-y-5">

<div>

## Accidental Typos

</div>

<div 
    v-click="7"
    v-motion
    :initial="{ opacity: 0 }"
    :enter="{ opacity: 1}"
    :duration="500"
    class=""
>

````md magic-move {lines: false, at: 7}
```python {all|all}{at: 7}
class Person:
  def __init__(self):
    self.name = "A"

a = A()
a.naame = "B"
```

```python
class Person:
  def __init__(self):
    self.name = "A"

a = A()
a.naame = "B"

class Person:
  __slots__ = ["name"]
  def __init__(self):
    self.name = "A"

a = A()
a.naame = "B"
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# AttributeError: 'A' object
# has no attribute 'naame'
```
````

</div>
  </div>
</div>
