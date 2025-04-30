---
theme: default
background: https://source.unsplash.com/collection/94734566/1920x1080
class: text-center
highlighter: shiki
lineNumbers: true
drawings:
  persist: false
---

# The Dangers of Empty Lists as Default Parameters in Python

---

## The Problem

```python
def add_item(item, my_list=[]):
    my_list.append(item)
    return my_list

print(add_item(1))  # [1]
print(add_item(2))  # [1, 2] 😱
```

<arrow v-click="1" x1="420" y1="170" x2="330" y2="210" color="#564" width="3" arrowSize="1" />

<p v-click="1" class="text-red-500 absolute bottom-23 left-45">Wait, where did 1 come from?</p>

---

## What's Happening?

- Default parameters are evaluated **only once** at function definition time
- The empty list is created when the function is defined
- The same list object is reused for every call where a list isn't provided
- Modifications persist between function calls

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

```python
def add_item(item, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(item)
    return my_list

print(add_item(1))  # [1]
print(add_item(2))  # [2] ✅
```

---

## Why This Works

- `None` is immutable and safe to use as a default value
- A new empty list is created each time the function is called
- Each call gets its own unique list
- No more unexpected shared state between calls

---

## The Rule

Never use mutable objects as default parameters:

- ❌ Lists: `def func(param=[])`
- ❌ Dictionaries: `def func(param={})`
- ❌ Sets: `def func(param=set())`
- ✅ Immutable types are safe: `None`, `0`, `""`, `()`, etc.

---

## Bonus: Python Visualization

<div class="grid grid-cols-2 gap-4">
<div>

### First call
```python
add_item(1)
```
Creates output: `[1]`

</div>
<div>

### Second call
```python
add_item(2)
```
Creates output: `[1, 2]` 

Both calls reference the same list!

</div>
</div>

---

## Resources

- [Python documentation on default parameters](https://docs.python.org/3/reference/compound_stmts.html#function-definitions)
- [Common Gotchas in Python](https://docs.python-guide.org/writing/gotchas/#mutable-default-arguments)
- [Created with Slidev](https://sli.dev) 