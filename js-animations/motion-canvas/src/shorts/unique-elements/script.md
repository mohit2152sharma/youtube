Suppose you have a list original_list <br description="create a list with repeated elements">
and you need to find <br description="highlight unique elements"> unique elements in it
A naive way to do this to use <br description="create a for loop which finds unique elements in a list"> for loop.
Create a new list <br description="highlight new list">, iterate through each element of our original list <br description="highlight loop iteration">
check if the elment is alread y in our new list <br description="highlight if condition">, if not then add it <br description="highlight append section">

A much better way to do this is to use <br description="show new solution with sets">
A set is a ddata structure in python <br description="highlight set"> that contains unique elements.
We can pass the list to set function <br description="highlight passing the original list to set">. this will return a set of unique elements
Then we can pass it to list <br  description="highlight passing the set to list"> to get our new list.
