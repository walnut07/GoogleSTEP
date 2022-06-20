# **The program description of cache.py** 

## Summary of the program
`cache.py` records a cache and print the cache out starting with the most recently accessed page and ending with the least recently accessed one. The time complexity of updating a cache is mostly done in O(1) time. This is because a doubly linked list, which requires only O(1) time to add or delete element, stores a cache. The nodes of the doubly linked list are a hashmap type. A node has an url as a key and other information (url, contents, previous node, next node) as a value.<br>

This is a big picture that illustrates what a cache looks like after accessing “a.com”, “b.com”, and “c.com”
![Picture of a cache]

***
## How the program works
`cache.py` is composed of three parts.
1. Initializing a cache.
2. `access_page(url, contents)`: Stores the most recently accessed N pages where N is a given number. 
3. `get_pages()`: Returns the cache starting with the most recently accessed page and ending with the least recently accessed one.<br>
 ![Picture of a cache.The A variable `head`, urls "c.com", "b.com", and "a.com", and a variable `tail` are mutually linked.](https://user-images.githubusercontent.com/90857923/169695892-f395c63b-39fb-405f-a739-618fdff3da75.png) <br>
![Picture of a cache. It has a psuedocode that prints out the nodes from left to right.](https://user-images.githubusercontent.com/90857923/169696062-59215dc6-91f5-4852-8d54-8082adef26cc.png)


Let's take a close look at how each part works.

### 1. Initializing a cache
   `head`: Marks the head of a doubly linked list.
   `tail`: Marks the tail of a doubly linked list.
```python
self.head = {"url": "", "contents": "", "prev": None, "next": None}
self.tail = {"url": "", "contents": "", "prev": None, "next": None}
```
   Nextly, make both `head` and `tail` as mutually linked by changing the `prev` and `next` keys in each hashmap.
```python
self.head["next"] = self.tail
self.tail["prev"] = self.head
```
   Then, initialize other variables.<br>
   `n` : The size of the cache.
   `count` : Counts the number of items in `url_to_node`.
   `url_to_node`: Stores urls as keys and nodes as values. The length is never longer than `n`.
   ```python
    self.n = n
    self.url_to_node = {}
    self.count = 0 
   ```

### 2. `access_page(url, contens)`
`access_page` accesses a page and update the cache so that it stores the most recently accessed N pages. It has three processes.
 
1. Assign `node`. It should have an url if input url exists in the cache. If the url is NOT none, meaning input url is foung in the cache, change prev and next of the node to make the previous and next node of the node as linked. <br>
    ```python
    node = self.url_to_node.get(url, None)
    if node != None:
        node["prev"]["next"] = node["next"]
        node["next"]["prev"] = node["prev"]
    ```
2. If input url is NOT found, examine if `count` is going to be bigger than `n`. This checks if the length of the cache is longer than `n`.
   1. If so, delete the previous node of `tail`, which is the least accessed page in the cache. Otherwise, do nothing.<br>
    ```python
    else:
        if self.count >= self.n:
            last_node = self.tail["prev"]
            del self.url_to_node[last_node["url"]]
            last_node["prev"]["next"] = self.tail
            self.tail["prev"] = last_node["prev"]
            self.count -= 1
    ```
   2. In either case (`count` is going to be bigger than `n` or not), it initializes a new node and add it to the doubly linked list.
   ```python
   node = {"url": url, "contents": contents, "prev": None, "next": None}
        self.url_to_node[url] = node
        self.count += 1
    ```
3. Finally, it makes the node exist after `head` because we want to make the most recently accessed page be after `head`.
    ```python
    node["next"] = self.head["next"]
    node["prev"] = self.head 
    self.head["next"]["prev"] = node
    self.head["next"] = node
    ```
### 2. `get_pages()`
`get_pages()` works so simply; It firstly initialize variables. Then, returns an arrray of urls.<br>
To begin with, initialize the variables.<br>
`urls` : Stores urls of nodes. The most recently accessed one comes first. The least recently accessed one comes last.
`node` : Current node.
`count` : Counts how many noded are added to `urls`.
```python
 urls = []
 node = self.head["next"]
 count = 0
```



