# Voiceover Script: The Dangers of Empty Lists as Default Parameters in Python

## Title Slide
Welcome to this presentation on "The Dangers of Empty Lists as Default Parameters in Python." This is a common pitfall that even experienced Python developers can encounter, and understanding it will help you write more predictable and bug-free code.

## The Problem
Let's start by looking at what appears to be a simple function. We have an `add_item` function that takes an item and a list, appends the item to the list, and returns the updated list. The list parameter has a default value of an empty list.

When we first call this function with the value 1, we get back a list containing 1, which seems correct. But when we call it again with the value 2, instead of getting a new list with just 2, we get a list with both 1 and 2. This is surprising behavior! Where did that 1 come from? This unexpected result happens because of how Python handles default parameters.

Before I jump into the explanation, if you use ChatGPT for learning then do checkout saral.club, it organises your conversations into memorable notes and automatically generates flash cards using space repetition.

## What's Happening?
Here's what's actually going on: Default parameters in Python are evaluated only once, at the time when the function is defined—not each time the function is called. This means the empty list is created just once when the function is first defined.

Every time you call the function without providing a list argument, it uses that same list object. Any modifications to this list persist between function calls, which is why we see values accumulating unexpectedly.

## The Explanation
Let's break down exactly what happens when Python loads this function definition. First, Python creates an empty list in memory. Then, it binds the parameter `my_list` to reference this object.

The crucial point is that this happens just once, when the module containing the function is loaded. After that, all calls to `add_item()` without a second argument will use that same list object. This is why modifications to the list are visible across different function calls.

## The Solution: Use None as Default
The solution is straightforward: use `None` as your default parameter instead of an empty list. In this revised version of the function, we check if `my_list` is `None`, and if it is, we create a new empty list inside the function body.

With this change, when we call `add_item(1)` and then `add_item(2)`, we get [1] and [2] respectively, which is the behavior most people expect.

## Why This Works
This approach works because `None` is immutable, making it safe to use as a default value. When the function is called, a new empty list is created each time within the function body.

This means each function call gets its own unique list, and there's no more shared state between calls. This pattern produces the behavior most developers intuitively expect from a function.

## The Rule
Based on this understanding, we can establish a general rule: never use mutable objects as default parameters in Python. This includes lists, dictionaries, sets, and other mutable containers.

Instead, use immutable types like `None`, integers, strings, or tuples as default values. Then, initialize your mutable objects inside the function body. This ensures that each function call starts with a fresh object.

## Bonus: Python Visualization
Let's visualize what's happening. In the first call to `add_item(1)`, we get a list with just the number 1. In the second call to `add_item(2)`, instead of getting a fresh list with just 2, we get [1, 2] because both calls are referencing and modifying the same list object in memory.

This shared state is usually not what you want and can lead to hard-to-debug issues, especially in larger codebases where functions might be called from many different places.

## Resources
If you'd like to learn more about this topic, here are some excellent resources. The Python documentation covers default parameters in detail, and the "Common Gotchas" section of the Python Guide specifically mentions mutable default arguments as a common trap for new and experienced Python developers alike.

Thank you for your attention, and I hope this helps you avoid this subtle but important pitfall in your Python code! 