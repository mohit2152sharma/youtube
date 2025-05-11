# Slots vs No Slots 


<div class="flex flex-row justify-start w-4/5 items-center h-full gap-x-10">

  <div 
    v-click="1"
    v-motion
    :initial="{ opacity: 0 }"
    :enter="{ opacity: 1}"
    :duration="500"
    class="w-full">

````md magic-move {at:2, lines: false}
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

d1 = Dummy()
d1.c = "C"

```

```python
class Dummy:

  __slots__ = ["a", "b"]

  def __init__(self):
    self.a = "A"
    self.b = "B"

d1 = Dummy()
d1.c = "C"
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# AttributeError: 'Dummy' object has no attribute 'c'

```
````

</div>
</div>
