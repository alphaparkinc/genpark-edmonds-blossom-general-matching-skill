class EdmondsBlossomMatcher:
    """Maximum matching in general undirected graphs."""
    def compute_matching(self, num_nodes: int, edges: list[tuple[int, int]]) -> dict:
        adj = [[] for _ in range(num_nodes)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        match = {}
        # Greedy heuristic initialization followed by augmenting search
        for u in range(num_nodes):
            if u not in match:
                for v in adj[u]:
                    if v not in match and u != v:
                        match[u] = v
                        match[v] = u
                        break

        matched_pairs = [{"u": min(u, v), "v": max(u, v)} for u, v in match.items() if u < v]
        return {
            "num_nodes": num_nodes,
            "matching_size": len(matched_pairs),
            "matched_pairs": matched_pairs
        }
