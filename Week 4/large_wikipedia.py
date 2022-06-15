import queue
import random

# python3 large_wikipedia.py

# ------ import datasets ----- #
def main():
  pages = {}
  links = {}

  with open('data/pages.txt') as f:
    for data in f.read().splitlines():
      page = data.split('\t')
      # page[0]: id, page[1]: title
      pages[page[0]] = page[1]

  with open('data/links.txt') as f:
    for data in f.read().splitlines():
      link = data.split('\t')
      # link[0]: id (from), links[1]: id (to)
      if link[0] in links:
        links[link[0]].append(link[1])
      else:
        links[link[0]] = []
        links[link[0]].append(link[1])


  # --------------------------- #

  # Find the minimum step from google to a random word.

  def minimumStepFromGoogle(start_id, target_id):
    """
    start_id: ID of the starting page. Initially Google's page id is passed.
    target_id: ID of the target page. 
    """

    Q = queue.Queue()
    Q.put(start_id)
    dist = {start_id: 0} # Using hashmap just because the pairs of a page id and a step can be beneficial for further use.

    # Breadth First Search
    while not Q.empty():
      node = Q.get()

      if node == target_id:
        return "{step} step(s) needed to access {target} from {start}!".format(step = dist[node],
          target = pages[target_id], start = pages[start_id] )

      if node in links: # Check if it's a leaf node.
        for adjacency_node in links[node]:
          if adjacency_node not in dist:
            dist[adjacency_node] = dist[node] + 1
            Q.put(adjacency_node)

    return "No, {target} is not accessible from {start}.".format(step = dist[node],
          target = pages[target_id], start = pages[start_id])


  pages_list = list(pages.keys())
  Google_id = "457783"
  random_word_id = random.choice(pages_list)

  print("Is {word} accessible from Google?".format(word = pages[random_word_id]))
  ans = minimumStepFromGoogle(Google_id, random_word_id)
  print(ans)

if __name__ == '__main__':
  main()