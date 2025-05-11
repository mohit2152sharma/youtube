Can you spot the difference between these two code snippets?
Let me help you, what's this slots for?

Welcome to one minute python
and today I am talking about slots
and it's advantages

Usually when you create a class
the instance attributes are stored in a dictionary
But in the case of slots
the instance attributes
are stored in a fixed sized array
In fact if you try to access the dictionary attribute, you will get an error

In a usual class, since the attributes are stored in a dynamic dictionary
It allows us to add new instance attributes at run time
but you can't do the same with slots, because the attributes are stored in a fixed sized array

So what are the advantages
First, is memory
Since we are not storing the attributes in a dynamic dictionary
we can avoid it's overheads and save memory by using slots

Second is speed
Slots speeds up your class related operations but it only becomes attractive when you are creating millions of instances

Last one and probably the most practical one is, it helps avoid typos
In a usual dictionary, you can accidentally create new attributes
which you can't do that with slots
