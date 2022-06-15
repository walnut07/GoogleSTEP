# **The program description of homework3.py** 

## Summary of the feature
`homework3.py` records cache. Cache is a data structure that stores the most recently accessed N pages where N is a given number. The time complexity of updating cache is O(1).

## Why is the time complexity O(1)?
The time complexity of updating cache is mostly done in O(1) time because the program is built based on the idea of circular buffer. 

[Image of circular buffer](/Week%202/1200px-Circular_buffer.png)

Circular buffer is implemented with one-dimentional array in the program. The variable *head* indicates where the least recently accessed page is, and the variable *tail* indiates where the most recently accessed page is. 

Every time an user visits a new URL/contents, one is added to |tail|. If |tail| goes beyond the end of the array, it is reset as zero.

> e.g., Suppose an user visited ["aaa.com", "AAA"].
> 
> The cache gets ["aaa.com", "AAA"].
> 
> The variable | tail | is set as 1 after the operation above.
> The variable | head | is kept as 0.

***

## Issues not fixed yet
### 1. The time complexity is O(N) when an user visit a URL/contents that they have already visited before. 
  
This program examins whether the user has visited the page before in the `access_page` function.

`if [url, contents] in self.list:`

If this conditional statement returns true, it nextly finds where in the circular buffer the older URL/contents is saved. And set it as *none*.

However, the problem here is; the worst running time of finding the index of older URL/contents is **O(N)**

> Suppose an user visit ["aaa.com", "AAA"] for the second time.
> 
> The cache looks like this, supposing they already visited "aaa.com" and "bbb.com".
> 
> [["aaa.com", "AAA"], ["bbb.com", "BBB], ["aaa.com", "AAA"]]
>
> By looking for the index of the older version of ["aaa.com", "AAA"] which is zero,
> the program will set it as *none*.
> 
> [None, ["bbb.com", "BBB], ["aaa.com", "AAA"]]

### 2. It is quit complicated to print the array out in a supposed order.
The function `get_pages` must return the cache starting with most recently accessed and ending with least recently accessed.

> In the example above, `get_pages` should return
> 
> ["aaa.com", "bbb.com"]
> 
> (<- most recently accessed --- least reacently accessed ->)

However, I found it very complicated to implement this. 
Therefore, now I'm doubting if using a circular buffer is a correct way to solve this problem.