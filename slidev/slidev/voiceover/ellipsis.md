Ever stumbled upon these three little dots ... in Python code and wondered what they are for?

Welcome to one minute python and today we'll be talking about Ellipsis.

These dots ... are formally called Ellipsis.

It's a unique, built-in constant object. Think of it like True, False, or None – there's only one instance of it.

You can compare triple dots with Ellipsis object using is operator. It evaluates to True.
And checking its type with type function reveals it belongs to the ellipsis class.

Now, How do you actually use it?

One common place is as a placeholder in function or method definitions. It is used to create an empty block similar to pass keyword. using ellipsis can sometimes serve as a more explicit signal that 'real code implementation is pending here', especially useful in stubs or abstract methods.

Ellipsis are also used in type hinting. In the first example, ellipsis acts as a wildcard for arguments. It signifies a callable (like a function or method) that can accept any number or type of parameters.

Similarly, it's used with generic types like tuples. In the second example, it defines a tuple that must start with an integer, but can then be followed by any number of additional integers. It's a concise way to annotate variable-length sequences where you know the type of the elements.

Finally, you will see this a lot when working with pydantic library. When defining fields or parameters, using ellipsis tells the library that this field or parameter is mandatory. It must be provided when creating an object. This is the same as assigning ellipsis to default parameter. Internally, pydantic checks if a default value is the Ellipsis object, and if so, they mark the field as required.

If you found this useful, please hit the like button and subscribe to Saral Club for more Python insights. We'd love to hear in the comments if you use Ellipsis in other interesting ways!

