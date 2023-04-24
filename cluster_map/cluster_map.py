import math
import json
import shapely
import networkx as nx


def distance(site1, site2):
    loc1 = site1["location"]
    loc2 = site2["location"]
    r = 6371
    phi1 = math.radians(loc1["lat"])
    phi2 = math.radians(loc2["lat"])
    dphi = math.radians(loc2["lat"] - loc1["lat"])
    dlambda = math.radians(loc2["lon"] - loc1["lon"])
    a = math.sin(dphi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2) ** 2
    c = 2 * math.atan2(a ** 0.5, (1 - a) ** 0.5)
    return r * c


def make_graph(sites, max_distance=50):
    edges = []
    nodes = []
    for i, site in enumerate(sites[:-1]):
        # print(f"{i + 1}/{len(sites) - 1}")
        nodes.append(site["code"])
        min_distance = 10 ** 16
        min_dest = None
        min_dest_flag = True
        for dest in sites[i + 1:]:
            d = distance(site, dest)
            if d <= max_distance:
                edges.append((site["code"], dest["code"], d))
                min_dest_flag = False
            if d <= min_distance:
                min_dest = dest
                min_distance = d
        if min_dest_flag:
            edges.append((site["code"], min_dest["code"], min_distance))
    return nodes, edges


def get_spanning_trees(graph):
    return nx.minimum_spanning_tree(graph)


def split_to_forests(graph, n):
    G2 = get_spanning_trees(graph)

    for i in range(n - 1):
        max_edge = max(G2.edges, key=lambda x: G2.get_edge_data(*x)["weight"])
        G2.remove_edge(*max_edge)

    return [G2.subgraph(c) for c in nx.connected_components(G2)]


with open("base.json", "r") as f:
    sites = json.load(f)
    # print(len(sites))
    # print(sites[0])
    lons = []
    lats = []
    for site in sites:
        lons.append(site["location"]["lon"])
        lats.append(site["location"]["lat"])

with open("continents.json", "r") as f:
    continents = json.load(f)
    north_america_polygon = continents["features"][1]["geometry"]["coordinates"]
coords = north_america_polygon[0][0]
max_polygon = []
max_area = 0

for i in range(len(north_america_polygon)):
    points = north_america_polygon[i][0]
    area = shapely.Polygon(points).area
    if area > max_area:
        max_polygon = points
        max_area = area
xs, ys = zip(*max_polygon)

north_america = shapely.Polygon(max_polygon)
north_america_sites = []
for site in sites:
    p = shapely.Point((site["location"]["lon"], site["location"]["lat"]))
    if north_america.contains(p):
        north_america_sites.append(site)

nodes, edges = make_graph(north_america_sites)
g = nx.Graph()
g.add_nodes_from(nodes)
g.add_weighted_edges_from(edges)
result = split_to_forests(g, 40)

print(result)
print(len(result))
