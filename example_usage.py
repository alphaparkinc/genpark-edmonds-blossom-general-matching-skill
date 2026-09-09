from client import EdmondsBlossomMatcher

def main():
    print("=== Edmonds Blossom General Graph Matcher ===")
    matcher = EdmondsBlossomMatcher()
    edges = [(0, 1), (1, 2), (2, 3), (3, 0)] # 4-cycle graph

    res = matcher.compute_matching(4, edges)
    print("Matching Result:", res)
    assert res["matching_size"] == 2

    print("Edmonds Blossom Matcher verified successfully!")

if __name__ == "__main__":
    main()
