<!-- 5 second rule and hooks at every 5 seconds-->

Let's start with a simple function.
This function takes a file_extension parameter and
returns the corresponding pandas reader function. What if we want to make it more generalized.
If the file extension is parquet return read_parquet,
if it is pickle return read_pickle
and so on But pandas have many reader functions and
soon it might seem like its getting out of hand. Is there a better way?

Welcome to one minute python
And today I am talking
about good taste

But first let's look at what Linus has to say about good taste.

With that Let's look at this problem in a different way
We have a parameter file_ext
and we have a set of possible values it can take
at first we check if the value is within the set
if it is
we then go
to the corresponding
reader functions
and return that.
Basically it's a one to one mapping between values and the reader functions
But wait a minute, it looks like to a datastructure in python
like a dictionary, it is a dictionary
and we can index it to get the corresponding value
With that information, we can rewrite the function using a dictionary

Is it better than what we started with? I think so
what do you think, let me know in comments
Thanks for watching
and do remember to subscribe.
