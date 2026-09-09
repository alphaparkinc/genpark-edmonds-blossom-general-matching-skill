import sys
import json
from client import EdmondsBlossomMatcher

def handle_request(req):
    method = req.get("method")
    params = req.get("params", {})
    if method == "match":
        m = EdmondsBlossomMatcher()
        return m.compute_matching(params.get("num_nodes", 4), [tuple(e) for e in params.get("edges", [])])
    return {"error": "Unknown method"}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        req = json.loads(line)
        res = handle_request(req)
        print(json.dumps(res))
        sys.stdout.flush()

if __name__ == "__main__":
    main()
