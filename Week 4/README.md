# Is that page accesible from Google? Check it by BFS!

## Task
## Find something interesting from the graph of Wikipedia.


## My work
`minimumStepFromGoogle(start_id, target_id)` returns the minimum step from Google's Wikipedia page to a random Wikipedia page. If it is impossible to reach the random page from Google's page.

## How to run
Download [wikipedia_data.zip](https://drive.google.com/file/d/1zqtjSb-ZoR4rzVUWZrjNSES5GKJhYmmH/view?usp=sharing)  and make a directory like below.
```shell
step_wikipedia-graph
├── data
│   ├── graph_small.png
│   ├── links_small.txt
│   ├── links.txt
│   ├── pages_small.txt
│   └── pages.txt
├── .gitignore
├── README.md 
└── large_wikipedia.py
```

Test environment: Python 3.9.2

```shell
python3 wikipedia_bfs.py
```
It takes a few minutes to open data files. After that, a message `Is [random word] accessible from Google?` appear. It takes from a few minutes to approximately 15 minutes to do BFS. Finally the step required to reach the target page appears.

## Algorithm
The main part in the program is the Breadth First Search algorithm.
I use hashmap to store a distance from Google's page.

- Initialize a queue .
- Push Google's page id to the queue.
- While queue it not empty, repeat these operations:
  - Pop an item from the queue. Let it be called `node`.
  - If `node` is the word we are looking for, return true!
  - Otherwise, push `node`'s adjacency nodes to the queue if we haven't visited the adjacency node.
- If we haven't returned true in the while loop, return false. It's impossible to go to the page from Google's page.

### Example
This is the demonstration of the breadth first search. Suppose you want to visit a page called "coffee".
![Untitled presentation (4)](https://user-images.githubusercontent.com/90857923/171433098-d4085320-ba5f-401b-ad85-270b257d5cc1.jpg)
![Untitled presentation (1)](https://user-images.githubusercontent.com/90857923/171433050-8afef1f4-3ddc-4836-b986-2191537425ee.jpg)
![Untitled presentation (2)](https://user-images.githubusercontent.com/90857923/171433055-061c18c1-457d-491d-8082-1bbc2051d238.jpg)
![Untitled presentation (5)](https://user-images.githubusercontent.com/90857923/171433994-282c076b-0787-491c-87c6-771118682548.jpg)
![Untitled presentation (6)](https://user-images.githubusercontent.com/90857923/171434007-1ba17aa6-3730-4f47-b53e-427c8f7adf0f.jpg)
![Untitled presentation (7)](https://user-images.githubusercontent.com/90857923/171434013-744d0dec-d8d4-47d1-b69d-182a42d318bf.jpg)



