# python3 solver_2-opt.py input_0.csv >output_0.csv  
# python3 solver_2-opt.py input_1.csv >output_1.csv  
# python3 solver_2-opt.py input_2.csv >output_2.csv  
# python3 solver_2-opt.py input_3.csv >output_3.csv  
# python3 solver_2-opt.py input_4.csv >output_4.csv  
# python3 solver_2-opt.py input_5.csv >output_5.csv 
# python3 solver_2-opt.py input_6.csv >output_6.csv 
import sys
import math

from common import print_tour, read_input


def distance(city1, city2):
  return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def solve(cities):
  N = len(cities)
  dist = [[0] * N for i in range(N)]
  for i in range(N):
      for j in range(i, N):
          dist[i][j] = dist[j][i] = distance(cities[i], cities[j])

  current_city = 0
  unvisited_cities = set(range(1, N))
  tour = [current_city]

  while unvisited_cities:
    next_city = min(unvisited_cities,
                    key=lambda city: dist[current_city][city])
    unvisited_cities.remove(next_city)
    tour.append(next_city)
    current_city = next_city
  # until here is the greedy approach
  
  while True:
    flag = True
    for i in range(N - 2):
      for j in range(i + 2, N):
        a, b, c, d = tour[i], tour[i + 1], tour[j], tour[(j + 1) % N]
        dist_a = dist[a][b] + dist[c][d] # old path
        dist_b = dist[a][c] + dist[b][d] # new path
        if (dist_a > dist_b): # If the old path is longer than the new one, swap b and c.
          tour[i + 1 : j + 1] = reversed(tour[i + 1 : j + 1])
          if flag:
            flag = False
    if flag: # If there is no points to swap, break the loop.
      break
  return tour


if __name__ == '__main__':
  assert len(sys.argv) > 1
  cities = read_input(sys.argv[1])
  tour = solve(cities)
  print_tour(tour)
