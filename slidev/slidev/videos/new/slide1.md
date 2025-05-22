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

```

```python
class DatabaseConnector:
  """Connects to database"""

  def __init__(self, connectin_str: str):
    self.connectin_str = connectin_str
    self.connection = self.connect()

  def connect(self):
    ... # connect to database

```

```python {*|6}
class DatabaseConnector:
  """Connects to database"""

  def __init__(self, connectin_str: str):
    self.connectin_str = connectin_str
    self.connection = self.connect()

  def connect(self):
    ... # connect to database

connector = DatabaseConnector('supersecretstring')
```
````

</div>
</div>
