#
# The code below uses a linear
# scan to find the unfinished node
# with the smallest distance from
# the source.
#
# Modify it to use a heap instead
#

import heapq

def dijkstra(HG, v):
	dist_so_far = {v: 0}
	final_dist = {}
	heap = [(0, v)]
	while dist_so_far:
		(w, k) = heapq.heappop(heap)
		if k in final_dist or (k in dist_so_far and w > dist_so_far[k]):
			continue
		else:
			del dist_so_far[k]
			final_dist[k] = w
		for neighbor in [nb for nb in HG[k] if nb not in final_dist]:
			nw = final_dist[k]+ HG[k][neighbor]
			if neighbor not in dist_so_far or nw < dist_so_far[neighbor]:
				dist_so_far[neighbor] = nw
				heapq.heappush(heap, (nw, neighbor))
	return final_dist

############
#
# Test

def make_link(G, node1, node2, w):
	if node1 not in G:
		G[node1] = {}
	if node2 not in G[node1]:
		(G[node1])[node2] = 0
	(G[node1])[node2] += w
	if node2 not in G:
		G[node2] = {}
	if node1 not in G[node2]:
		(G[node2])[node1] = 0
	(G[node2])[node1] += w
	return G

def test():
	# shortcuts
	(a,b,c,d,e,f,g) = ('A', 'B', 'C', 'D', 'E', 'F', 'G')
	triples = ((a,c,3),(c,b,10),(a,b,15),(d,b,9),(a,d,4),(d,f,7),(d,e,3),
			   (e,g,1),(e,f,5),(f,g,2),(b,f,1))
	G = {}
	for (i,j,k) in triples:
		make_link(G, i, j, k)

	dist = dijkstra(G, a)
	assert dist[g] == 8 #(a -> d -> e -> g)
	assert dist[b] == 11 #(a -> d -> e -> g -> f -> b)

if __name__ == '__main__':
	test()
	print "Test passes"