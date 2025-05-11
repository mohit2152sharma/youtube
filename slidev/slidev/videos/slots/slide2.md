# Slots vs No Slots

<FancyArrow v-click="7" pos1="bottom" q1="[data-id=list]" x2="154" y2="335" arc="0.5" roughness="2" width="2" color="orange" class="z-10"></FancyArrow>

<div v-click="[3, 6]"
  v-motion
  :initial="{ opacity: 0 }"
  :enter="{ opacity: 1}"
  :exit="{ opacity: 0 }"
  :duration="1000"
  class="absolute bottom-5 right-10">
<YoutubeSubscribe />
</div>

<div v-click="7" data-id="list" class="absolute top-60 left-90 z-20">It's not a list</div>

<div class="flex flex-col items-center justify-center h-[50vh] w-4/5"
v-click="1"
v-motion
:initial="{ opacity: 0 }"
:enter="{ opacity: 1}"
:duration="1000"
>

````md magic-move {at: 1, lines: false}
```python
class Dummy:
  def __init__(self):
    self.a = "A"
    self.b = "B"
```

```python
class Dummy:

  def __init__(self):
    self.a = "A"
    self.b = "B"

dummy = Dummy()
```

```python
class Dummy:

  def __init__(self):
    self.a = "A"
    self.b = "B"

dummy = Dummy()

print(dummy.__dict__)
# {'a': 'A', 'b': 'B'}
```

```python
class Dummy:

  __slots__ = ["a", "b"]
  def __init__(self):
    self.a = "A"
    self.b = "B"
```

```python
class Dummy:

  __slots__ = ["a", "b"]
  def __init__(self):
    self.a = "A"
    self.b = "B"

dummy = Dummy()
```

```python
class Dummy:

  __slots__ = ["a", "b"]
  def __init__(self):
    self.a = "A"
    self.b = "B"

dummy = Dummy()

print(dummy.__slots__)
# ['a', 'b']
```

```python
class Dummy:

  __slots__ = ["a", "b"]
  def __init__(self):
    self.a = "A"
    self.b = "B"

dummy = Dummy()

print(dummy.__slots__)
# ['a', 'b']

print(dummy.__dict__)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'Dummy' object has no attribute '__dict__'. Did you mean: '__dir__'?
```
````

</div>
