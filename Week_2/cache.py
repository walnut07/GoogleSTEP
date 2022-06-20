import sys
# how to run
# python3 cache.py

# Cache is a data structure that stores the most recently accessed N pages.
# See the below test cases to see how it should work.
class Cache:
  # Initializes the cache.
  # `n`: The size of the cache.
  def __init__(self, n):
    self.n = n
    self.head = {"url": "", "contents": "", "prev": None, "next": None}
    self.tail = {"url": "", "contents": "", "prev": None, "next": None}
    # Make `head` and `tail` as doubly linked.
    self.head["next"] = self.tail
    self.tail["prev"] = self.head
    # `url_to_node`: Stores urls as keys and nodes as values. The length is never longer than `n`.
    # `count`: Counts the number of items in `url_to_node`.
    self.url_to_node = {}
    self.count = 0 
    assert(n >= 1)

  # Access a page and update the cache so that it stores the most
  # recently accessed N pages. This needs to be done with mostly O(1).
  # `url`: The accessed URL
  # `contents`: The contents of the URL
  def access_page(self, url, contents):
    node = self.url_to_node.get(url, None)
    # If an user has already visited the page, 
    # change the order of prev and next node of the node.
    if node != None:
        node["prev"]["next"] = node["next"]
        node["next"]["prev"] = node["prev"]
    else:
        # If `url_to_node` is going to be longer than `n`,
        # delete the least recently used cache.
        if self.count >= self.n:
            last_node = self.tail["prev"]
            del self.url_to_node[last_node["url"]]
            last_node["prev"]["next"] = self.tail
            self.tail["prev"] = last_node["prev"]
            self.count -= 1
        # Initialize a node.
        node = {"url": url, "contents": contents, "prev": None, "next": None}
        self.url_to_node[url] = node
        self.count += 1
    # Make the node be after `head`.
    node["next"] = self.head["next"]
    node["prev"] = self.head 
    self.head["next"]["prev"] = node
    self.head["next"] = node

    return self.url_to_node

  # Return the URLs stored in the cache. The URLs are ordered
  # in the order in which the URLs are mostly recently accessed.
  def get_pages(self):
    # `urls` : It stores the urls.
    urls = []
    node = self.head["next"]
    count = 0
    while node["next"] != None:
      urls.append(node["url"])
      node = node["next"]
      count += 1
    assert(count == len(self.url_to_node))
    return urls

# Does your code pass all test cases? :)
def cache_test():
  # Set the size of the cache to 4.
  cache = Cache(4)
  # Initially, no page is cached.
  equal(cache.get_pages(), [])
  # Access "a.com".
  cache.access_page("a.com", "AAA")
  # "a.com" is cached.
  equal(cache.get_pages(), ["a.com"])
  # Access "b.com".
  cache.access_page("b.com", "BBB")
  # The cache is updated to:
  #   (most recently accessed)<-- "b.com", "a.com" -->(least recently accessed)
  equal(cache.get_pages(), ["b.com", "a.com"])
  # Access "c.com".
  cache.access_page("c.com", "CCC")
  # The cache is updated to:
  #   (most recently accessed)<-- "c.com", "b.com", "a.com" -->(least recently accessed)
  equal(cache.get_pages(), ["c.com", "b.com", "a.com"])
  # Access "d.com".
  cache.access_page("d.com", "DDD")
  # The cache is updated to:
  #   (most recently accessed)<-- "d.com", "c.com", "b.com", "a.com" -->(least recently accessed)
  equal(cache.get_pages(), ["d.com", "c.com", "b.com", "a.com"])
  # Access "d.com" again.
  cache.access_page("d.com", "DDD")
  # The cache is updated to:
  #   (most recently accessed)<-- "d.com", "c.com", "b.com", "a.com" -->(least recently accessed)
  equal(cache.get_pages(), ["d.com", "c.com", "b.com", "a.com"])
  # Access "a.com" again.
  cache.access_page("a.com", "AAA")
  # The cache is updated to:
  #   (most recently accessed)<-- "a.com", "d.com", "c.com", "b.com" -->(least recently accessed)
  equal(cache.get_pages(), ["a.com", "d.com", "c.com", "b.com"])
  cache.access_page("c.com", "CCC")
  equal(cache.get_pages(), ["c.com", "a.com", "d.com", "b.com"])
  cache.access_page("a.com", "AAA")
  equal(cache.get_pages(), ["a.com", "c.com", "d.com", "b.com"])
  cache.access_page("a.com", "AAA")
  equal(cache.get_pages(), ["a.com", "c.com", "d.com", "b.com"])
  # Access "e.com".
  cache.access_page("e.com", "EEE")
  # The cache is full, so we need to remove the least recently accessed page "b.com".
  # The cache is updated to:
  #   (most recently accessed)<-- "e.com", "a.com", "c.com", "d.com" -->(least recently accessed)
  equal(cache.get_pages(), ["e.com", "a.com", "c.com", "d.com"])
  # Access "f.com".
  cache.access_page("f.com", "FFF")
  # The cache is full, so we need to remove the least recently accessed page "c.com".
  # The cache is updated to:
  #   (most recently accessed)<-- "f.com", "e.com", "a.com", "c.com" -->(least recently accessed)
  equal(cache.get_pages(), ["f.com", "e.com", "a.com", "c.com"])
  # Access "e.com".
  cache.access_page("e.com", "EEE")
  # The cache is updated to:
  #   (most recently accessed)<-- "e.com", "f.com", "a.com", "c.com" -->(least recently accessed)
  equal(cache.get_pages(), ["e.com", "f.com", "a.com", "c.com"])
  # Access "a.com".
  cache.access_page("a.com", "AAA")
  # The cache is updated to:
  #   (most recently accessed)<-- "a.com", "e.com", "f.com", "c.com" -->(least recently accessed)
  equal(cache.get_pages(), ["a.com", "e.com", "f.com", "c.com"])
  print("OK!")

# A helper function to check if the contents of the two lists is the same.
def equal(list1, list2):
  assert(list1 == list2)

if __name__ == "__main__":
  cache_test()