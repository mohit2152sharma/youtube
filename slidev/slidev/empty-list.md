---
theme: vuetiful
background: https://source.unsplash.com/collection/94734566/1920x1080
class: text-center
highlighter: shiki
lineNumbers: true
drawings:
  persist: false
---

# Empty lists??? Think Again!

---

## The Problem

````md magic-move {at: 1, lines: true}
```python
def add_item(item, my_list=[]):
    my_list.append(item)
    return my_list
```

```python
def add_item(item, my_list=[]):
    my_list.append(item)
    return my_list

add_item(1)
# [1]
```

```python
def add_item(item, my_list=[]):
    my_list.append(item)
    return my_list

add_item(1)
# [1]

add_item(2)
# [1, 2]
```
````

<Arrow v-click="3" x1="210" y1="400" x2="120" y2="260" />

<p v-click="3" class="text-xl absolute bottom-23 left-45"> Where does this 1 come from? </p>


--- 

<p class="text-3xl absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2">https://saral.club</p>
<p class="text-sm absolute left-1/2 -translate-x-1/2 top-[55%] -translate-y-1/6">Convert your chatGPT conversations into memorable notes</p>


---

## What's Happening?

<ul>
<li v-click> Default parameters are evaluated <span class="font-bold">only once</span> at function definition time</li>
<li v-click> The empty list is created when the function is defined</li>
<li v-click> The same list object is reused for every call where a list isn't provided</li>
<li v-click> Modifications persist between function calls</li>
</ul>

---

## The Explanation

When Python loads the function definition:

```python
def add_item(item, my_list=[]):
    ...
```

1. It creates an empty list object in memory
2. It binds the parameter `my_list` to reference this object
3. This happens **just once** when the module loads
4. All calls to `add_item()` without a second argument will use the same list object

---

## The Solution: Use None as Default

````md magic-move {lines: true}
```python
def add_item(item, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(item)
    return my_list
```

```python
def add_item(item, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(item)
    return my_list

print(add_item(1))  # [1]
```

```python
def add_item(item, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(item)
    return my_list

print(add_item(1))  # [1]
print(add_item(2))  # [2] ✅
```
````

---

## Why This Works

<ul>
<li v-click> <code>None</code> is immutable and safe to use as a default value</li>
<li v-click> A new empty list is created each time the function is called</li>
<li v-click> Each call gets its own unique list</li>
<li v-click> No more unexpected shared state between calls</li>
</ul>

---

## The Rule

Never use mutable objects as default parameters:

- ❌ Lists: `def func(param=[])`
- ❌ Dictionaries: `def func(param={})`
- ❌ Sets: `def func(param=set())`
- ✅ Immutable types are safe: `None`, `0`, `""`, `()`, etc.

---

## Resources

- [Python documentation on default parameters](https://docs.python.org/3/reference/compound_stmts.html#function-definitions)
- [Common Gotchas in Python](https://docs.python-guide.org/writing/gotchas/#mutable-default-arguments)
- [Created with Slidev](https://sli.dev)
