<div class="absolute top-2 left-2" v-click="[0,12]">
<p class="text-4xl">Singleton Design Pattern</p>
<p v-click="1" class="text-sm">"A class has only one instance and that instance is globally accessible"</p>
</div>
<div class="flex flex-row justify-start w-4/5 items-center h-full gap-x-10 text-sm">

  <div 
    v-click="2"
    v-motion
    :initial="{ opacity: 0 }"
    :enter="{ opacity: 1}"
    :duration="500"
    class="w-full text-sm">

````md magic-move {at:2, lines: false}
```python {*|*|3|3}
class Singleton:

  def __init__(self, name: str):
    self.name = name
```

```python {*|3}
class Singleton:

  def __new__(cls):
    ...

  def __init__(self, name: str):
    self.name = name

```

```python {*|3|6|7|8}
class Singleton:

  _instance = None

  def __new__(cls, *args, **kwargs):
    if cls._instance is None:
      cls._instance = super().__new__(cls)
    return cls._instance

  def __init__(self, name: str):
    self.name = name

```

```python {*|2|3|6|7|8|10|20|20-23,9,14,18|25|25,26,14|28,29}
class DatabaseConnector:
  _instance = None
  _connection = None

  def __new__(cls, *args, **kwargs):
    if cls._instance is None:
      cls._instance = super().__new__(cls)
      cls._connection = cls._instance.connect()
      print('instance created and connected')
    return cls._instance

  def __init__(self, connectin_str: str):
    self.connectin_str = connectin_str
    print('instance initialised')

  def connect(self):
    if self._connection:
      print('reusing connection')

Db1 = DatabaseConnector('secret')
# connected successfully
# instance created and connected
# instance initialised

Db2 = DatabaseConnector('secret2')
# instance initialised

print(Db1 is Db2)
# True
```

```python {*|2|2,6|10-12}
class Singleton:
  def __new__(cls, *args, **kwargs):
    print(f"args from new method: {args}")
    return super().__new__(cls)

  def __init__(self, *args, **kwargs):
    print(f"args from init method: {args}")


s = Singleton("hello world")
# args from new method: ('hello world',)
# args from init method: ('hello world',)
```
````

</div>

<div v-click="[3,5]" data-id="init" class="top-20 right-40 absolute bg-red p-2 rounded">
  <span v-click="3">Initialises the instance and</span> <span v-click="3">sets up the attribute</span>
</div>

<div 
    v-motion
    :initial="{ opacity: 0 }"
    :enter="{ opacity: 1 }"
    :leave="{ opacity: 0 }"
    :duration="300"
    data-id="new" v-click="[5,7]" class="top-40 right-40 absolute bg-green p-2 rounded">
  Creates a new instance in memory
</div>
<FancyArrow pos1="bottom" v-click="[3,5]" x2="300" y2="280" color="lime" class="z-10" arc="0.2" q1="[data-id='init']"/>
<FancyArrow
    v-motion
    :initial="{ opacity: 0 }"
    :enter="{ opacity: 1 }"
    :leave="{ opacity: 0 }"
    :duration="1000"
    pos1="bottom" v-click="[5,7]" x2="200" y2="260" color="lime" class="z-10" arc="0.2" q1="[data-id='new']"/>
</div>

<img src="/index-finger.png" width=40 height=40  class="absolute top-50 left-8" v-click="[8,24]" 
    v-motion 
    :initial="{ opacity: 0, x: 0, y: 0 }" 
    :enter="{ opacity: 1 }" 
    :leave="{ opacity: 0 }" 
    :duration="1000" 
    :click-9="{x: 8, y: 55, transition: {duration: 500, type: 'keyframes', ease: 'easeInOut'}}"
    :click-10="{x: 8, y: 75, transition: {duration: 500, type: 'keyframes', ease: 'easeInOut'}}"
    :click-11="{x: 8, y: 95, transition: {duration: 500, type: 'keyframes', ease: 'easeInOut'}}" 
    :click-12="{x: 8, y: -175, transition: {duration: 500, type: 'keyframes', ease: 'easeInOut'}}" 
    :click-14="{x: 8, y: -155, transition: {duration: 500, type: 'keyframes', ease: 'easeInOut'}}" 
    :click-15="{x: 8, y: -105, transition: {duration: 500, type: 'keyframes', ease: 'easeInOut'}}" 
    :click-16="{x: 8, y: -85, transition: {duration: 500, type: 'keyframes', ease: 'easeInOut'}}" 
    :click-17="{x: 8, y: -65, transition: {duration: 500, type: 'keyframes', ease: 'easeInOut'}}" 
    :click-18="{x: 8, y: -30, transition: {duration: 500, type: 'keyframes', ease: 'easeInOut'}}" 
    :click-19="{x: -10, y: 150, transition: {duration: 500, type: 'keyframes', ease: 'easeInOut'}}" 
    :click-21="{x: -10, y: 240, transition: {duration: 500, type: 'keyframes', ease: 'easeInOut'}}" 
    :click-23="{x: -10, y: 295, transition: {duration: 500, type: 'keyframes', ease: 'easeInOut'}}" 
/>

<div class="absolute bottom-2 right-10"
v-click="[12,16]"
v-motion
:inital="{ opacity: 0 }"
:enter="{ opacity: 1 }"
:duration="400" >
<YoutubeSubscribe />
</div>
