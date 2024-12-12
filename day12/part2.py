from typing import List, Set, Tuple

grid = [list(l.strip()) for l in open('sample3.txt').readlines()]

directions = [(-1,0), (0,1), (1,0), (0, -1)]

def findRegions(g) -> List[List[Tuple[int, int]]]:
  regions = []
  seen: Set[Tuple[int, int]] = set()

  def floodfill(x: int, y: int) -> List[Tuple[int, int]]:
    seen.add((x, y))
    region = [(x, y)]
    for xdir, ydir in directions:
      x2, y2 = x + xdir, y + ydir
      if (x2, y2) not in seen and x2 in range(len(g[0])) and y2 in range(len(g)) and g[y2][x2] == g[y][x]:
        region += floodfill(x2, y2)
    return region
  
  for i, row in enumerate(g):
    for j in range(len(row)):
      if (j,i) in seen:
        continue
      regions.append(floodfill(j,i))
  
  return regions

def findEdges(region: List[Tuple[int, int]], g, searchRegion = None) -> Set[Tuple[int, int]]:
  edges = set()
  for x, y in region:
    for xdir, ydir in directions:
      x2, y2 = x + xdir, y + ydir
      if searchRegion == None:
        if not (y2 in range(len(g)) and x2 in range(len(g[0]))) or g[y2][x2] != g[y][x]:
          edges.add((x2, y2))
      elif y2 in range(len(g)) and x2 in range(len(g[0])) and (x2, y2) in searchRegion:
          edges.add((x2,y2))
  return edges

def groupEdges(edges: Set[Tuple[int, int]]) -> List[Set[Tuple[int, int]]]:
  seen = set()

  def floodfill(x: int, y: int) -> List[Tuple[int, int]]:
    seen.add((x, y))
    group = [(x,y)]
    for xdir, ydir in directions:
      cord = (x + xdir, y + ydir)
      if cord in edges and cord not in seen:
        group += floodfill(*cord)
    return group
  
  return [floodfill(*edge) for edge in edges if edge not in seen]

res = 0
regions = findRegions(grid) # Vind all regions
for region in regions:
  sides = 0
  edges = findEdges(region, grid) # Find all cells (edges), including off grid, toucing the region
  edgeGroups = groupEdges(edges) # Find all regions of these edges and group them
  for edgeGroup in edgeGroups:
    touchingSides = findEdges(edgeGroup, grid, region) # Find all the cells of the original region that touch this region of edges
    sides += len(groupEdges(touchingSides)) # Group these original cells
  res += sides * len(region)

print(res)

# 854340 too low