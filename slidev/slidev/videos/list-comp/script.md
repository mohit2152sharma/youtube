<div v-click="0"
  v-motion
  :initial="{ opacity: 0 }"
  :enter="{ opacity: 1 }"
  :duration="2000"
  class="flex flex-col items-center justify-center h-full mb-2 gap-y-2"
  >

````md magic-move {lines: false}
```python
[x for x in range(10)]
```

```python
[x*y for x in range(10) for y in range(10)]
```

```python
[x*y*z for x in range(10) for y in range(10) for z in range(10)]
```

```python
[x*y*z*k for x in range(10) for y in range(10) for z in range(10) for k in range(10)]
```

```python
[x*y*z*k*l for x in range(10) for y in range(10) for z in range(10) for k in range(10) for l in range(10)]
```
````

</div>

---
src: ../one-minute-slide.md
---
---

<div class="flex flex-col h-full justify-center items-center">
<div class="flex flex-col items-center justify-center w-full mb-2 gap-y-2">
<div v-click="0" 
      v-motion
      :initial="{ opacity: 0 }"
      :enter="{ opacity: 1 }"
      :duration="2000"
      class="w-3/4">

````md magic-move {lines: false}
```python
[x*y*z for x in range(10) for y in range(10) for z in range(10)]
```

```python {all|all|3-5}{at: 3}
[
  x*y*z
  for x in range(10)
    for y in range(10)
      for z in range(10)
]
```
````

</div>

<div v-click="2" 
      v-motion
      :initial="{ opacity: 0 }"
      :enter="{ opacity: 1 }"
      :duration="2000"
      class="w-3/4">

````md magic-move {lines: false}
```python {1-3}{at: 3}
for x in range(10):
  for y in range(10):
    for z in range(10):
      x*y*z
```

```python
container = []
for x in range(10):
  for y in range(10):
    for z in range(10):
    container.append(x*y*z)
```
````

</div>
</div>
</div>

---
---

<div class="flex flex-col h-full justify-center items-center">
<div class="flex flex-col z-20 w-full gap-y-2 gap-x-2 justify-center items-center">
<div v-click="0" 
      v-motion
      :initial="{ opacity: 0 }"
      :enter="{ opacity: 1 }"
      :duration="2000"
      class="w-3/4">

````md magic-move {lines: false}
```python
[x for x in range(10) if x % 2 == 0]
```

```python {all|all|3-4}{at: 3}
[
  x
  for x in range(10)
    if x % 2 == 0
]
```

```python
[
  'even' if x % 2 == 0 else 'odd'
  for x in range(10)
]
```

```python {all|3-6}{at: 6}
[
  x*j
  for x in range(10)
    if x % 5 == 0
      for j in range(10)
        if j % 2 == 0
]
```

```python
[x*j for x in range(10) if x % 5 == 0 for j in range(10) if j % 2 == 0]
```
````

</div>

<div v-click="2" 
      v-click.hide="+7"
      v-motion
      :initial="{ opacity: 0 }"
      :enter="{ opacity: 1 }"
      :duration="2000"
      class="w-3/4">

````md magic-move {at: 2, lines: false}
```python {all|all|1-2}{at: 3}
for x in range(10):
  if x % 2 == 0:
    x
```

```python
for x in range(10):
  'even' if x % 2 == 0 else 'odd'
```

```python {all|1-4}{at: 6}
for x in range(10):
  if x % 5 == 0:
    for j in range(10):
      if j % 2 == 0:
        print(x*j)
```
````

</div>
</div>
</div>

---

# Bonus Performance Trick

<div class="flex flex-col h-4/5 justify-center items-center">
<div v-click="0" 
      v-motion
      :initial="{ opacity: 0 }"
      :enter="{ opacity: 1 }"
      :duration="2000"
      class="w-full">

````md magic-move {lines: false}
```python {all|2,4}
[
  (n, math.sqrt(n))
  for n in range(100)
  if math.sqrt(n) > 2
]
```

```python {all|2,4}
[
  (n, root)
  for n in range(100)
    if (root := math.sqrt(n)) > 2
]
```
````

</div>
</div>

---
src: ../ending.md
---
