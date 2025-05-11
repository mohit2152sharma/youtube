<div class="flex flex-row justify-center items-center h-full gap-x-10">

  <div 
    v-click="1"
    v-motion
    :initial="{ opacity: 0 }"
    :enter="{ opacity: 1}"
    :duration="500"
    class="w-1/3">

```python {*|*|none}{lines: false, at: 1}
class Dummy:


  def __init__(self):

    self.a = "A"
    self.b = "B"
```

  </div>
<div 
    v-click="1"
    v-motion
    :initial="{ opacity: 0 }"
    :enter="{ opacity: 1}"
    :duration="500"
    class="w-1/3">

```python {*|*|3}{lines: false, at: 1}
class Dummy:

  __slots__ = ["a", "b"]

  def __init__(self):
    self.a = "A"
    self.b = "B"
```

  </div>

</div>
