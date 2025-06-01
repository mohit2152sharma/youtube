Pythons call feature

In this video I want to talk about call method in python classes what it is? how to use it? and when you should you use it?

To put it simply, it makes an instance callable, so instead of calling the method, you can directly call an instance. In terms of how, you simply use the dunder call method and define what you need to do inside it.

This is useful when you want to have a stateful function. Like in this example, whenever I create an instance of counter, it will start with a count 0 and every time i call the instance it will increment the count by 1, thus remembering how many times the instance was called.

Another example, is when you want instances which behave like functions. Like this class Multiplier, which takes a factor when you create an instance and whenever you call that instance, it multiplies your input with the factor. With this you can easily create factory functions pattern.

That's all for this video, thanks for watching and if you like the video, do remember to subscribe.
