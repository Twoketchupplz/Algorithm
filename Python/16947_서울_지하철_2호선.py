"""
https://www.acmicpc.net/problem/16947
아이디어
지선을 끝에서부터 잘라내어 사이클을 찾는다.

각노드의 에지 개수를 담은 리스트 edge_cnt 를 만든다. O(n^2)
while 사이클만 남을때 까지:
    edge_cnt[idx]의 val이 1인 idx가 지선의 끝이다. val을 0으로 만든다.
    node[idx]에 연결된 유일한 node v를 찾는다. 윗줄과 함께 O(n^2)
    edge_cnt[v] -= 1
edge_cnt[idx] 중 val이 0이 아닌 idx가 사이클에 해당하는 node이다.
이후 거리는 BFS로 구한다.
"""