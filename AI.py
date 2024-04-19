import pygame
import networkx as nx
import random
from copy import copy

RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
WIDTH, HEIGHT = 500, 600

# One big structure
greenL1 = [((268, 246), (264, 185), (0, 255, 0)), ((308, 175), (311, 240), (0, 255, 0)), ((348, 174), (387, 180), (0, 255, 0)), ((387, 180), (392, 242), (0, 255, 0)), ((348, 174), (347, 249), (0, 255, 0)), ((422, 174), (424, 239), (0, 255, 0)), ((472, 172), (469, 237), (0, 255, 0)), ((469, 237), (422, 174), (0, 255, 0)), ((264, 185), (308, 175), (0, 255, 0)), ((308, 175), (348, 174), (0, 255, 0)), ((387, 180), (422, 174), (0, 255, 0)), ((422, 174), (472, 172), (0, 255, 0)), ((308, 175), (361, 48), (0, 255, 0)), ((361, 48), (422, 174), (0, 255, 0))]
greenN1 = [(268, 246), (264, 185), (308, 175), (311, 240), (348, 174), (387, 180), (392, 242), (347, 249), (422, 174), (472, 172), (424, 239), (469, 237), (361, 48)]
greenRN1 = [(268, 246), (311, 240), (392, 242), (347, 249), (424, 239), (469, 237)]
# 2 structures 1 root and a 2 root
greenL2 = [((318, 250), (306, 142), (0, 255, 0)), ((306, 142), (366, 120), (0, 255, 0)), ((306, 142), (328, 56), (0, 255, 0)), ((306, 142), (268, 55), (0, 255, 0)), ((268, 55), (328, 56), (0, 255, 0)), ((268, 55), (264, 116), (0, 255, 0)), ((328, 56), (374, 38), (0, 255, 0)), ((401, 245), (407, 154), (0, 255, 0)), ((407, 154), (451, 154), (0, 255, 0)), ((451, 154), (446, 243), (0, 255, 0))]
greenN2 = [(318, 250), (306, 142), (366, 120), (328, 56), (268, 55), (264, 116), (374, 38), (401, 245), (407, 154), (451, 154), (446, 243)]
greenRN2 = [(318, 250), (401, 245), (446, 243)]
# 3 structures
greenL3 = [((295, 239), (295, 147), (0, 255, 0)), ((334, 246), (327, 154), (0, 255, 0)), ((327, 154), (353, 137), (0, 255, 0)), ((353, 137), (313, 118), (0, 255, 0)), ((313, 118), (327, 154), (0, 255, 0)), ((411, 252), (414, 181), (0, 255, 0)), ((414, 181), (395, 198), (0, 255, 0)), ((414, 181), (415, 153), (0, 255, 0)), ((415, 153), (429, 171), (0, 255, 0)), ((415, 153), (416, 80), (0, 255, 0)), ((416, 80), (390, 50), (0, 255, 0)), ((416, 80), (415, 50), (0, 255, 0)), ((416, 80), (445, 57), (0, 255, 0))]
greenN3 = [(295, 239), (295, 147), (334, 246), (327, 154), (353, 137), (313, 118), (411, 252), (414, 181), (395, 198), (415, 153), (429, 171), (416, 80), (390, 50), (415, 50), (445, 57)]
greenRN3 = [(295, 239), (334, 246), (411, 252)]

# green tree SG value 5
greenL4 = [((365, 247), (363, 192), (0, 255, 0)), ((363, 192), (314, 170), (0, 255, 0)), ((314, 170), (293, 129), (0, 255, 0)), ((293, 129), (258, 89), (0, 255, 0)), ((293, 129), (299, 83), (0, 255, 0)), ((363, 192), (363, 121), (0, 255, 0)), ((363, 121), (341, 87), (0, 255, 0)), ((341, 87), (313, 53), (0, 255, 0)), ((313, 53), (341, 24), (0, 255, 0)), ((363, 121), (396, 89), (0, 255, 0)), ((396, 89), (399, 44), (0, 255, 0)), ((363, 192), (431, 144), (0, 255, 0)), ((431, 144), (438, 90), (0, 255, 0)), ((438, 90), (475, 68), (0, 255, 0)), ((431, 144), (470, 146), (0, 255, 0))]
greenN4 = [(365, 247), (363, 192), (314, 170), (293, 129), (258, 89), (299, 83), (363, 121), (341, 87), (313, 53), (341, 24), (396, 89), (399, 44), (431, 144), (438, 90), (475, 68), (470, 146)]
greenRN4 = [(365, 247)]

# 2 trees SG 7, 4
greenL5 = [((297, 257), (293, 201), (0, 255, 0)), ((293, 201), (289, 163), (0, 255, 0)), ((289, 163), (267, 149), (0, 255, 0)), ((289, 163), (285, 124), (0, 255, 0)), ((285, 124), (312, 99), (0, 255, 0)), ((285, 124), (280, 34), (0, 255, 0)), ((312, 99), (309, 62), (0, 255, 0)), ((312, 99), (328, 75), (0, 255, 0)), ((312, 99), (343, 97), (0, 255, 0)), ((409, 244), (408, 186), (0, 255, 0)), ((408, 186), (379, 162), (0, 255, 0)), ((408, 186), (382, 202), (0, 255, 0)), ((408, 186), (432, 157), (0, 255, 0)), ((408, 186), (445, 201), (0, 255, 0)), ((408, 186), (407, 128), (0, 255, 0)), ((407, 128), (404, 78), (0, 255, 0)), ((404, 78), (421, 56), (0, 255, 0)), ((421, 56), (438, 34), (0, 255, 0)), ((438, 34), (460, 21), (0, 255, 0)), ((404, 78), (375, 57), (0, 255, 0)), ((375, 57), (357, 40), (0, 255, 0))]
greenN5 = [(297, 257), (293, 201), (289, 163), (267, 149), (285, 124), (312, 99), (280, 34), (309, 62), (328, 75), (343, 97), (409, 244), (408, 186), (379, 162), (382, 202), (432, 157), (445, 201), (407, 128), (404, 78), (421, 56), (438, 34), (460, 21), (375, 57), (357, 40)]
greenRN5 = [(297, 257), (409, 244)]

greenL6 = [((282, 247), (279, 212), (0, 255, 0)), ((279, 212), (279, 169), (0, 255, 0)), ((279, 169), (277, 125), (0, 255, 0)), ((277, 125), (277, 80), (0, 255, 0)), ((277, 80), (267, 27), (0, 255, 0)), ((343, 241), (343, 206), (0, 255, 0)), ((343, 206), (315, 203), (0, 255, 0)), ((343, 206), (341, 172), (0, 255, 0)), ((343, 206), (368, 206), (0, 255, 0)), ((402, 243), (395, 135), (0, 255, 0)), ((395, 135), (361, 92), (0, 255, 0)), ((361, 92), (341, 57), (0, 255, 0)), ((341, 57), (336, 29), (0, 255, 0)), ((395, 135), (406, 109), (0, 255, 0)), ((406, 109), (417, 80), (0, 255, 0)), ((417, 80), (426, 47), (0, 255, 0)), ((426, 47), (449, 29), (0, 255, 0)), ((449, 29), (460, 52), (0, 255, 0)), ((460, 52), (464, 95), (0, 255, 0))]
greenN6 = [(282, 247), (279, 212), (279, 169), (277, 125), (277, 80), (267, 27), (343, 241), (343, 206), (315, 203), (341, 172), (368, 206), (402, 243), (395, 135), (361, 92), (341, 57), (336, 29), (406, 109), (417, 80), (426, 47), (449, 29), (460, 52), (464, 95)]
greenRN6 = [(282, 247), (343, 241), (402, 243)]

greenL7 = [((365, 247), (363, 192), (0, 255, 0)), ((363, 192), (314, 170), (0, 255, 0)), ((314, 170), (293, 129), (0, 255, 0)), ((293, 129), (258, 89), (0, 255, 0)), ((293, 129), (299, 83), (0, 255, 0)), ((363, 192), (363, 121), (0, 255, 0)), ((363, 121), (341, 87), (0, 255, 0)), ((341, 87), (313, 53), (0, 255, 0)), ((313, 53), (341, 24), (0, 255, 0)), ((363, 121), (396, 89), (0, 255, 0)), ((396, 89), (399, 44), (0, 255, 0)), ((363, 192), (431, 144), (0, 255, 0)), ((431, 144), (438, 90), (0, 255, 0)), ((438, 90), (475, 68), (0, 255, 0)), ((431, 144), (470, 146), (0, 255, 0)), ((258, 89), (299, 83), (0, 255, 0)), ((341, 24), (399, 44), (0, 255, 0)), ((475, 68), (470, 146), (0, 255, 0))]
greenN7 = [(365, 247), (363, 192), (314, 170), (293, 129), (258, 89), (299, 83), (363, 121), (341, 87), (313, 53), (341, 24), (396, 89), (399, 44), (431, 144), (438, 90), (475, 68), (470, 146)]
greenRN7 = [(365, 247)]

greenL8 = [((365, 247), (363, 192), (0, 255, 0)), ((363, 192), (314, 170), (0, 255, 0)), ((314, 170), (293, 129), (0, 255, 0)), ((293, 129), (258, 89), (0, 255, 0)), ((293, 129), (299, 83), (0, 255, 0)), ((363, 192), (363, 121), (0, 255, 0)), ((363, 121), (341, 87), (0, 255, 0)), ((341, 87), (313, 53), (0, 255, 0)), ((313, 53), (341, 24), (0, 255, 0)), ((363, 121), (396, 89), (0, 255, 0)), ((396, 89), (399, 44), (0, 255, 0)), ((363, 192), (431, 144), (0, 255, 0)), ((431, 144), (438, 90), (0, 255, 0)), ((438, 90), (475, 68), (0, 255, 0)), ((431, 144), (470, 146), (0, 255, 0)), ((258, 89), (299, 83), (0, 255, 0)), ((341, 24), (399, 44), (0, 255, 0)), ((475, 68), (470, 146), (0, 255, 0)), ((438, 90), (396, 89), (0, 255, 0)), ((341, 87), (299, 83), (0, 255, 0)), ((363, 121), (431, 144), (0, 255, 0))]
greenN8 = [(365, 247), (363, 192), (314, 170), (293, 129), (258, 89), (299, 83), (363, 121), (341, 87), (313, 53), (341, 24), (396, 89), (399, 44), (431, 144), (438, 90), (475, 68), (470, 146)]
greenRN8 = [(365, 247)]

def min_length_list(list_of_lists):
    min_length = float('inf')
    min_length_list = None

    for sublist in list_of_lists:
        length = len(sublist)
        if length < min_length:
            min_length = length
            min_length_list = sublist

    return min_length_list

def can_piece_move(frog_grid, i, j):
    if i == 4 and j == 0:
        return False
    if i == 4 and frog_grid[i][j-1] != 0:
        return False
    if j == 0 and frog_grid[i+1][j] != 0:
        return False
    if frog_grid[i][j-1] != 0 and frog_grid[i+1][j] != 0 and frog_grid[i+1][j-1] != 0:
        return False
    return True


def find_all_moves_for_piece(frog_grid, n, m):
    good_moves = []
    for i in range(5):
        for j in range(5):
            if i == n and j < m:
                blocked = False
                for k in range(j + 1, m):
                    if frog_grid[n][k] != 0:  # Check for obstacles (1 or 2)
                        blocked = True
                if not blocked and frog_grid[i][j] == 0:
                    good_moves.append([i,j])
            elif j == m and i > n:
                blocked = False
                for k in range(n + 1, i):
                    if frog_grid[k][m] != 0:  # Check for obstacles (1 or 2)
                        blocked = True
                if not blocked and frog_grid[i][j] == 0:
                    good_moves.append([i,j])
            elif (abs(i - n) == abs(j - m) and i >= n and j <= m) and frog_grid[i][j] == 0:
                blocked = False
                for k in range(1, abs(i - n)):
                    if frog_grid[i - k][j + k] != 0:  # Check for obstacles (1 or 2)
                        blocked = True
                if not blocked and frog_grid[i][j] == 0:
                    good_moves.append([i,j])
    if [n,m] in good_moves:
        good_moves.remove([n,m])
    return good_moves


def mex(nums):
    num_set = set(nums)
    i = 0
    while i in num_set:
        i += 1
    return i


def calculate_wyt_posiions(frog_grid):
    grundy_grid = [[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1]]
    for i in range(5):
        for j in range(5):
            if not can_piece_move(frog_grid, i, j):
                grundy_grid[i][j] = 0
    for _ in range(5):
        for i in range(5):
            for j in range(5):
                moves_from_here = find_all_moves_for_piece(frog_grid, i, j)
                mex_values = [grundy_grid[x][y] for x, y in moves_from_here]
                grundy_grid[i][j] = mex(mex_values)  # Calculate mex value
    return grundy_grid


def get_current_wyt_grund(frog_grid):
    grundy_grid = calculate_wyt_posiions(frog_grid)
    for i in range(5):
        for j in range(5):
            if frog_grid[i][j] == 1:
                return grundy_grid[i][j]


def find_wyt_move(xor_result, frog_grid):
    grundy_grid = calculate_wyt_posiions(frog_grid)
    for i in range(5):
        for j in range(5):
            if frog_grid[i][j] == 1:
                moves = find_all_moves_for_piece(frog_grid, i, j)
    for move in moves:
        if grundy_grid[move[0]][move[1]] ^ xor_result == 0:
            return (move[0], move[1], -1, -1)
    return None

def nim_strategy(game_state):
    # XOR operation on all piles
    xor_result = game_state[0] ^ game_state[1] ^ game_state[2] ^ game_state[3]

    # Check if the XOR result is non-zero
    if xor_result == 0:
        # The game is in a P-position
        return "P", None
    else:
        # The game is in an N-position

        # Find the first non-empty pile
        for i, pile in enumerate(game_state):
            reduced_pile_size = pile ^ xor_result
            if reduced_pile_size < pile:
                # Suggest a winning move by reducing the chosen pile to the appropriate size
                suggestion = (i, pile - reduced_pile_size)
                return "N", suggestion



def update_root_nodesAI(drawn_lines, nodes, root_nodes):
    for line in drawn_lines:
        ground = pygame.Rect(WIDTH // 2, -70 + HEIGHT // 2, WIDTH // 2, HEIGHT // 10)
        if ground.collidepoint(line[0]) and line[0] not in root_nodes:
            root_nodes.append(line[0])
        if ground.collidepoint(line[1]) and line[1] not in root_nodes:
            root_nodes.append(line[1])
    for root in root_nodes:
        found = False
        for line in drawn_lines:
            if root == line[0] or root == line[1]:
                found = True
        if found == False:
            root_nodes.remove(root)

def update_nodesAI(drawn_lines, nodes, root_nodes):
    for line in drawn_lines:
        if line[0] not in nodes:
            nodes.append(line[0])
        if line[1] not in nodes:
            nodes.append(line[1])
    for node in nodes:
        found = False
        for line in drawn_lines:
            if node == line[0] or node == line[1]:
                found = True
        if found == False:
            nodes.remove(node)

def dfs1(graph, node, visited):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs1(graph, neighbor, visited)

def remove_unconnected_nodes(nodes, lines, roots):
    # Create an adjacency list representation of the graph
    graph = {node: [] for node in nodes}
    for line in lines:
        graph[line[0]].append(line[1])
        graph[line[1]].append(line[0])

    # Perform DFS starting from each root node
    visited = set()
    for root in roots:
        if root not in visited:
            dfs1(graph, root, visited)

    # Filter nodes and lines based on visited nodes
    connected_nodes = [node for node in nodes if node in visited]
    connected_lines = [line for line in lines if line[0] in visited and line[1] in visited]

    return connected_nodes, connected_lines



def is_terminal(position):
    """Check if the position is terminal."""
    return len(position) == 0


def apply_move(position, nodes, root_nodes, move):
    """Apply the move to the position and return the new position."""
    new_position = position.copy()
    if move in new_position:
        new_position.remove(move)
    update_root_nodesAI(position, nodes, root_nodes)
    update_nodesAI(position, nodes, root_nodes)
    nodes, position = remove_unconnected_nodes(nodes, position, root_nodes)
    return new_position

def get_moves(position, turn):
    moves = []
    for line in position:
        if turn == 0:
            if line[2] != RED:
                moves.append(line)
        elif turn == 1:
            if line[2] != BLUE:
                moves.append(line)
    return moves



def find_split_nodes(drawn_lines, nodes, root_nodes):
    split_nodes = []
    if len(nodes) != 0:
        for node in nodes:
            con_lines = 0
            for line in drawn_lines:
                if line[0] == node or line[1] == node:
                    con_lines += 1
            if con_lines >= 3:
                split_nodes.append(node)
    return split_nodes

def find_leaf_nodes(drawn_lines, nodes, root_nodes):
    leaf_nodes = []
    for node in nodes:
        lines = 0
        for line in drawn_lines:
            if line[0] == node or line[1] == node:
                lines += 1
        if lines < 2:
            leaf_nodes.append(node)
    return leaf_nodes



def create_graph(drawn_lines):
    graph = nx.Graph()
    for line in drawn_lines:
        node1 = line[0]
        node2 = line[1]
        graph.add_edge(node1, node2)
    return graph

def add_lines(node, amount, drawn_lines, nodes):
    # Determine the coordinates of the new node
    x, y = node
    new_node = (x + 10, y)  # Assuming the new node is created at a distance of 10 units horizontally

    # Add the line from the current node to the new node to the drawn lines
    drawn_lines.append((node, new_node, GREEN))

    # Add the new node to the list of nodes
    nodes.append(new_node)

    # Keep adding lines until the desired amount is reached
    for _ in range(amount - 1):  # Subtract 1 because the initial line is already added
        # Update the current node to the new node
        node = new_node

        # Create the next node at a distance of 10 units horizontally
        new_node = (node[0] + 10, node[1])

        # Add the line from the current node to the new node to the drawn lines
        drawn_lines.append((node, new_node, GREEN))

        # Add the new node to the list of nodes
        nodes.append(new_node)

    return drawn_lines, nodes

def get_nodes_from_lines(lines):
    nodes = set()  # Using a set to automatically collect unique nodes

    # Iterate through each line and collect unique nodes
    for line in lines:
        node1 = line[0]
        node2 = line[1]
        nodes.add(node1)
        nodes.add(node2)

    return list(nodes)

def trace_distance_to_split(graph, split_nodes, leaf_nodes, drawn_lines, nodes):
    leaf_distances = {}
    traversed_lines = []
    visited_nodes = []
    def dfs(node, parent, distance):
        if node in split_nodes:
            return distance, node  # Found a split node

        for neighbor in graph.neighbors(node):
            if neighbor != parent:  # Avoid revisiting the parent node
                traversed_lines.append((neighbor, node, GREEN))
                visited_nodes.append(neighbor)
                result = dfs(neighbor, node, distance + 1)
                if result is not None:  # Only update if a split node is found in the subtree
                    return result

        return None

    for leaf_node in leaf_nodes:
        result = dfs(leaf_node, None, 0)
        if result is not None:
            distance, split_node = result
            leaf_distances[leaf_node] = (distance, split_node)
    for split_node in split_nodes:
        split_tot = 0
        for key, value in leaf_distances.items():
            if value[1] == split_node:
                split_tot ^= value[0]
        if split_tot > 0:
            drawn_lines, nodes = add_lines(split_node, split_tot, drawn_lines, nodes)

    return drawn_lines, nodes, traversed_lines, visited_nodes

def seperate_into_componants(drawn_lines, nodes, root_nodes):
    graph = create_graph(drawn_lines)
    # Find connected components
    components = list(nx.connected_components(graph))

    # List to store components with drawn lines, nodes, and root nodes
    component_list = []

    for component in components:
        component_drawn_lines = [line for line in drawn_lines if line[0] in component and line[1] in component]
        component_nodes = [node for node in nodes if node in component]
        component_root_nodes = [root_node for root_node in root_nodes if root_node in component]
        component_list.append([component_drawn_lines, component_nodes, component_root_nodes])

    return component_list

def perform_colon_principle(drawn_lines, nodes, root_nodes):
    split_nodes = find_split_nodes(drawn_lines, nodes, root_nodes)
    while len(split_nodes) > 0:
        leaf_nodes = find_leaf_nodes(drawn_lines, nodes, root_nodes)
        for n in leaf_nodes:
            if n in root_nodes:
                leaf_nodes.remove(n)
        graph = create_graph(drawn_lines)
        drawn_lines, nodes, lines_to_remove, visited_nodes = trace_distance_to_split(graph, split_nodes, leaf_nodes, drawn_lines, nodes)
        drawn_lines = list(set(drawn_lines))
        for line in lines_to_remove:
            if line in drawn_lines[:]:
                drawn_lines.remove(line)
        for line in drawn_lines:
            if (line[1], line[0], line[2]) in drawn_lines:
                drawn_lines.remove((line[1], line[0], line[2]))
        nodes = get_nodes_from_lines(drawn_lines)
        split_nodes = find_split_nodes(drawn_lines, nodes, root_nodes)
    grundy = len(drawn_lines)
    return grundy

def find_cycles(graph):
    def dfs(node, visited, parent, cycle_nodes):
        visited[node] = True
        cycle_nodes.append(node)
        for neighbor in graph[node]:
            if not visited[neighbor]:
                if dfs(neighbor, visited, node, cycle_nodes):
                    return True
            elif parent != neighbor:
                if neighbor in cycle_nodes:
                    idx = cycle_nodes.index(neighbor)
                    cycles.append(cycle_nodes[idx:])
                    return True
        cycle_nodes.pop()
        return False

    visited = {node: False for node in graph}
    cycles = []
    for node in graph:
        if not visited[node]:
            cycle_nodes = []
            dfs(node, visited, None, cycle_nodes)
    return cycles


from collections import deque
def closest_node(graph, root, nodes):
    # Perform BFS starting from the root node
    queue = deque([(root, 0)])  # (node, distance)
    visited = set()

    while queue:
        node, distance = queue.popleft()
        visited.add(node)

        # Check if the current node is in the list of nodes
        if node in nodes:
            return node, distance

        # Explore neighbors of the current node
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append((neighbor, distance + 1))

    # If no node from the list is reachable from the root
    return None, float('inf')


def perform_fusion_principle2(drawn_lines, nodes, root_nodes, recursive = True):
    graph = create_graph(drawn_lines)
    cycles = find_cycles(graph)
    if len(cycles) == 0:
        return drawn_lines, nodes, root_nodes
    cycle = min_length_list(cycles)
    key_node = closest_node(graph, root_nodes[0], cycle)[0]
    updated_drawn_lines = []
    for line in drawn_lines:
        if line[0] in cycle and line[1] in cycle:
            pass
        elif line[0] in cycle and line in drawn_lines and line[0] != key_node:
            if (key_node, line[1], GREEN) in drawn_lines or (line[1], key_node, GREEN) in drawn_lines:
                updated_drawn_lines.append((key_node, (random.randint(1,200), random.randint(1,200)), GREEN))
            else:
                updated_drawn_lines.append((key_node, line[1], GREEN))
        elif line[1] in cycle and line in drawn_lines and line[1] != key_node:
            if (line[0], key_node, GREEN) in drawn_lines or (key_node, line[0], GREEN) in drawn_lines:
                updated_drawn_lines.append(((random.randint(1,200), random.randint(1,200)), key_node, GREEN))
            else:
                updated_drawn_lines.append((line[0], key_node, GREEN))
        else:
            if line in updated_drawn_lines:
                updated_drawn_lines.append(((random.randint(1,200), random.randint(1,200)), key_node, GREEN))
            else:
                updated_drawn_lines.append(line)
    if len(cycles[0]) % 2 == 1:
        updated_drawn_lines.append((key_node, (random.randint(1, 200), random.randint(1, 200)), GREEN))
    if not recursive:
        update_nodesAI(updated_drawn_lines, nodes, root_nodes)
        nodes, updated_drawn_lines = remove_unconnected_nodes(nodes, updated_drawn_lines, root_nodes)
        return updated_drawn_lines, nodes, root_nodes
    else:
        graph = create_graph(updated_drawn_lines)
        cycles = find_cycles(graph)
        if len(cycles) == 0:
            update_nodesAI(updated_drawn_lines, nodes, root_nodes)
            nodes, updated_drawn_lines = remove_unconnected_nodes(nodes, updated_drawn_lines, root_nodes)
            return updated_drawn_lines, nodes, root_nodes
        else:
            update_nodesAI(updated_drawn_lines, nodes, root_nodes)
            nodes, updated_drawn_lines = remove_unconnected_nodes(nodes, updated_drawn_lines, root_nodes)
            return perform_fusion_principle2(updated_drawn_lines, nodes, root_nodes, recursive=True)


def suggest_impartial_hack_move(xor_val, nim_grid, drawn_lines, nodes, root_nodes):
    for line in copy(drawn_lines):  # Iterate over a copy of drawn_lines
        updated_lines = copy(drawn_lines)
        updated_lines.remove(line)

        # Update the game state
        update_root_nodesAI(updated_lines, nodes, root_nodes)
        update_nodesAI(updated_lines, nodes, root_nodes)
        nodes, lines = remove_unconnected_nodes(nodes, updated_lines, root_nodes)
        # Calculate Grundy values
        grunds = compute_grundies(lines, nodes, root_nodes)
        print("Grundy values:", grunds)
        xor = 0
        for grund in grunds:
            xor ^= grund
        print("XOR:", xor)
        print(xor_val)
        # Check if a move exists that balances the nim-sum
        if xor ^ xor_val == 0:
            print("remove line ", line)
            return line
    return None

def pick_random_move(frog_grid, nim_grid, drawn_lines):
    print("playing random move")
    a = random.choice([0, 1])
    if a == 0:
        # Pick a random heap number from nim_grid
        heap_number = random.choice(range(len(nim_grid)))

        # Ensure the selected heap has stones
        if nim_grid[heap_number] > 0:
            # Pick a random amount to remove, within the range of stones in the heap
            amount_to_remove = random.randint(1, nim_grid[heap_number])
            return (heap_number, amount_to_remove)
    if len(drawn_lines) != 0:
        random_line = random.choice(drawn_lines)
        return random_line
    else:
        for i in range(len(nim_grid)):
            if nim_grid[i] != 0:
                return (i, 1)
        for i in range(5):
            for j in range(5):
                if frog_grid[i][j] == 1:
                    moves = find_all_moves_for_piece(frog_grid, i, j)
        random_move = random.choice(moves)
        return (random_move[0], random_move[1], -1, -1)

def compute_grundies(drawn_lines, nodes, root_nodes):
    hack_grunds = []
    componants = seperate_into_componants(drawn_lines, nodes, root_nodes)
    for comp in componants:
        fused_lines, fused_nodes, root_nodes = perform_fusion_principle2(comp[0], comp[1], comp[2])
        hack_grund = perform_colon_principle(fused_lines, fused_nodes, root_nodes)
        hack_grunds.append(hack_grund)
    return hack_grunds

def calc_impartial_pos(frog_grid, nim_grid, drawn_lines, nodes, root_nodes):
    hack_grunds = compute_grundies(drawn_lines, nodes, root_nodes)
    print("position grunds: " + str(hack_grunds))
    xor_result = 0
    for val in nim_grid:
        xor_result ^= val
    wyt_val = get_current_wyt_grund(frog_grid)
    xor_not_hack = wyt_val ^ xor_result
    for grund in hack_grunds:
        xor_result ^= grund
    full_xor_result = wyt_val ^ xor_result
    # Find the first non-empty pile
    for i, pile in enumerate(nim_grid):
        reduced_pile_size = pile ^ full_xor_result
        if reduced_pile_size < pile:
            # Suggest a winning move by reducing the chosen pile to the appropriate size
            suggestion = (i, pile - reduced_pile_size)
            return suggestion
    if find_wyt_move(xor_result, frog_grid) != None:
        return find_wyt_move(xor_result, frog_grid)
    if suggest_impartial_hack_move(xor_not_hack, nim_grid, drawn_lines, nodes, root_nodes) != None:
        return suggest_impartial_hack_move(xor_not_hack, nim_grid, drawn_lines, nodes, root_nodes)
    return pick_random_move(frog_grid, nim_grid, drawn_lines)


def play_AI_move(frog_grid, nim_grid, drawn_lines, nodes, root_nodes):
    move = calc_impartial_pos(frog_grid, nim_grid, drawn_lines, nodes, root_nodes)
    if len(move) == 2:
        i, j = move
        nim_grid[i] -= j
    elif len(move) == 3:
        drawn_lines.remove(move)
        update_root_nodesAI(drawn_lines, nodes, root_nodes)
        update_nodesAI(drawn_lines, nodes, root_nodes)
        nodes, drawn_lines = remove_unconnected_nodes(nodes, drawn_lines, root_nodes)
    elif len(move) == 4:
        for i in range(5):
            for j in range(5):
                if frog_grid[i][j] == 1:
                    frog_grid[i][j] = 0
        frog_grid[move[0]][move[1]] = 1
    return frog_grid, nim_grid, drawn_lines, nodes, root_nodes


#print(perform_fusion_principle(greenL7, greenN7, greenRN7)[0])











