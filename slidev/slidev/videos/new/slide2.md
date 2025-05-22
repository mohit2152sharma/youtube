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
class DatabaseConnector:
  """Connects to database"""

  def __init__(self, connectin_str: str):
    self.connectin_str = connectin_str
    self.connection = self.connect()

  def connect(self):
    ...

connector = DatabaseConnector('supersecretstring')
```

```python
class DatabaseConnector:
  """Connects to database"""

  def __init__(self, connectin_str: str):
    self.connectin_str = connectin_str
    self.connection = self.connect()

  def connect(self):
    ...

connector = DatabaseConnector('supersecretstring')
connector2 = DatabaseConnector('supersecretstring')
```

```python


class DatabaseConnector:
  """Connects to database"""

  def __init__(self, connectin_str: str):
    self.connectin_str = connectin_str
    self.connection = self.connect()

  def connect(self):
    ...

connector = DatabaseConnector('supersecretstring')
connector2 = DatabaseConnector('supersecretstring')
connector3 = DatabaseConnector('supersecretstring')
```

```python {*|*|*|*|*|*|*|*|19|1-5,7-9,19}
class DatabaseConnector:
  """Connects to database"""

  def __init__(self, connectin_str: str):
    self.connectin_str = connectin_str
    self.connection = self.connect()

  def connect(self):
    ...

connector = DatabaseConnector('supersecretstring')
connector1 = DatabaseConnector('supersecretstring')
connector2 = DatabaseConnector('supersecretstring')
connector3 = DatabaseConnector('supersecretstring')
connector4 = DatabaseConnector('supersecretstring')
connector5 = DatabaseConnector('supersecretstring')
connector6 = DatabaseConnector('supersecretstring')
connector7 = DatabaseConnector('supersecretstring')
connector8 = DatabaseConnector('supersecretstring')
```
````

</div>
</div>

<div v-click="[5,12]">
<img v-click="5" src="/too-many-clients-error.jpg" class="absolute top-1/2 left-1/2 -translate-x-1/2" width="400" height="400" />
<img v-click="6" src="/too-many-clients-error.jpg" class="absolute top-1/2 left-1/2 -translate-x-1/2 rotate-10" width="410" height="410" />
<img v-click="7" src="/too-many-clients-error.jpg" class="absolute top-1/2 left-1/2 -translate-x-1/2 rotate-20" width="420" height="420" />
<img v-click="8" src="/too-many-clients-error.jpg" class="absolute top-1/2 left-1/2 -translate-x-1/2 rotate-30" width="430" height="430" />
<img v-click="9" src="/too-many-clients-error.jpg" class="absolute top-1/2 left-1/2 -translate-x-1/2 rotate-40" width="440" height="440" />
<img v-click="10" src="/too-many-clients-error.jpg" class="absolute top-1/2 left-1/2 -translate-x-1/2 rotate-30" width="450" height="450" />
<img v-click="11" src="/too-many-clients-error.jpg" class="absolute top-1/2 left-1/2 -translate-x-1/2 rotate-20" width="460" height="460" />
</div>

<div v-click="[5,12]" class="absolute bottom-2 right-10"><p class="text-sm italic"><sup>*</sup>Though the error message mentions java, but same will happen in python also</p></div>
