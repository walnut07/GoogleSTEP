# python3 test.py
# --- test data --- #

pages = {"10": "Apple" , "40": "Meta", "50": "Google"}
links = {"10": ["40"], "40":["50"], "50": ["40"]}

# ----------------- #

def findMinimumStep(node_id, prev_distance):
  dist[node_id] = prev_distance + 1
  print("current: ", pages[node_id])

  if node_id == target_id:
    print("Yes, it takes {step} step(s) from Google!".format(step = dist[node_id]))
    return "Yes, it takes {step} step(s) from Google!".format(step = dist[node_id])

  for adjacency_node_id in links[node_id]:
    if adjacency_node_id not in dist:
      findMinimumStep(str(adjacency_node_id), dist[node_id])

  return "No you can't go there"

  # ------------------- #

dist = {} 
Google_id = "50"
target_id = "30"

print(findMinimumStep(Google_id,-1))

