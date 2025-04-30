- Understanding deeply nested list comprehension # is difficult. In this video, I will explain, # how to understand them by # comparing with traditional for loops, # and do stick around till the end for a performance tip

- Welcome to one minute python, where I try to explain python concepts in short video

- Step 1, always write the nested list comprehension on multiple lines
- Immediately, you can draw parallel to how similar it looks to the traditional for loop.
- In list comprehension, the expression is at the top, while in traditional for loop it's at the bottom.
- Ofcourse, in traditional for loop, you need to append the expression to a list to store the result for later use

- Similary, in list comprehension with if expression, write it on multiple lines
- Again, you can see how similar both look. With one having expression at the top while the other at the bottom
- Click pause
- Same is the case with nested for loops, nested inside if expressions. Write the for loop normally, and in the end place the expression at the top.

-- Now for the tip, you can see in this for loop, we are computing the square root twice.
-- We can avoid that using the walrus operator, and compute the square root only once.

--- That's all folks, thanks for watching, and don't forget to subscribe
