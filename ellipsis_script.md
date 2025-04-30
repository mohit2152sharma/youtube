In many places, you may have seen these three dots. What are these?

Welcome to one minute python [font-mono, write-character-animation]
And today we are talking about these three dots.

Formally, these are called Ellipses.

In fact, python has a built-in singleton object called Ellipsis, which is the same as the three dots.

And if you compare them with is operator, you will get true.

<code>
  ... is Ellipsis 
  # True
</code>

How To use this ellipsis?

There are three many ways or places where you would use the ellipsis.

1. As a placeholder for todo. Suppose you define a function, but you don't want to implement the whole logic yet.

```def my_function():
      ...
```

This is similar to how people use `pass` keyword. And you will find it a lot in abstract classes. Where the class is placeholder to be implemented by the subclass.

```
class MyClass:
    ...
```

2. Next is in type hints.
