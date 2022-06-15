import sys
# python3 homework3.py

# Cache is a data structure that stores the most recently accessed N pages.
# See the below test cases to see how it should work.
#
# Note: Please do not use a library (e.g., collections.OrderedDict).
#       Implement the data structure yourself.
class Cache:
  # Initializes the cache.
  # |n|: The size of the cache.
  def __init__(self, n):
    # |head| is the index of the url/contents that is least recently added to the cache.
    # |tail| is the index of the url/contents that is most recently added to the cache. 
    self.n = n
    self.list = [ None ] * self.n
    self.head = 0  
    self.tail = 0

  # Access a page and update the cache so that it stores the most
  # recently accessed N pages. This needs to be done with mostly O(1).
  # |url|: The accessed URL
  # |contents|: The contents of the URL
  def access_page(self, url, contents):
    self.url = url
    self.contents = contents
    # If the url is already in the list, 
    # replace the older one with None and add the url in the index of |tail|.
    if [url, contents] in self.list:
        # Find where the older one is. It takes O(N) time.
        index = self.list.index([url, contents]) 
        self.list[index] = None
        self.list[self.tail] = [url, contents]

        # Update |head| and |tail|.
        # If the head is equal to index, add one if |head| isn't in the end 
        # and set |head| to zero otherwise.
        if self.head == index:
            if self.head != (self.n - 1):
                self.head += 1
            else:
                self.head = 0
                
        if self.tail != (self.n - 1):
            self.tail += 1
        else:
            self.tail = 0
    else:
    # If the url isn't in the list, add the url and contents into the tail index.
    # Add one to |tail| if |tail| isn't in the end. 
    # Otherwise set |head| to zero.
    # Update |head| when the indices of |head| and |tail| were the same.
        self.list[self.tail] = [url, contents]
        if self.tail != (self.n - 1):
            self.tail += 1
        else:
            self.tail = 0

        if self.tail == self.head:
            if self.tail != (self.n - 1):
                self.head += 1
            else:
                self.head = 0

    return self.list

# ----- get_pages still has bugs! ----- #
  # Return the URLs stored in the cache. The URLs are ordered
  # in the order in which the URLs are mostly recently accessed.
  def get_pages(self):
    # |ordered_list|: The list where most recently accessed url/contents come first and 
    #                   least recently accessed are in the end.
    # |count|: Counts how many times it has done the operation.
    ordered_list = []
    count = 0
    current = self.tail

    # Append the url/contents, starting from the index of |tail| 
    # and ending in the index of |head|.
    # Loop this operation for |tail - head| times. 
    # e.g., 2 times where |tail| is 2 and |head| is 0.
    while count <= abs(self.tail - self.head):
        # |current| : Which index of url/contents it appends to |ordered_list|.
        # Descend from the index of |tail| to that of |head|. 
        # If |current| is in the index of zero, it goes to the end of the list nextly.
        # Otherwise |current| descends, which means one extracted from |current|.

        ordered_list.append(self.list[current][0])

        if current == 0:
            current = (self.n - 1)
        else:
            current -= 1
        count += 1

    return ordered_list


# -- test cases -- #
"""
cache = Cache(4)  
print("tail", cache.tail) 
print("head", cache.head)
print(cache.access_page("a.com", "AAA"))
print(cache.tail)
print(cache.head)
print(cache.access_page("b.com", "BBB"))
print(cache.tail) 
print(cache.head)
print(cache.access_page("c.com", "CCC"))
print(cache.tail) 
print(cache.head)
print(cache.access_page("a.com", "AAA"))
print(cache.tail) 
print(cache.head)
"""

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
