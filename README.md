# Graph

This repository is our submission for **Lab 2** of **Toán cho Trí Tuệ Nhân Tạo** course. Our group involves:
* `Nguyễn Khắc Duy - 22C15026`
* `Lê Thị Cẩm Thi - 22C15044`

## Notes

`BFS` and `DFS` are implemented by using the adjacency list. Specifically, `queue` is replaced by `deque` to significantly improve the performance of `BFS` (the outputs of the benchmark function show that `deque` is **20** times faster at `BFS` than conventional `queue`).

## Guidelines

### Install

```
$ git clone https://github.com/KhacDuyNguyen0/Graph.git
$ cd Graph
```

### Build the graph

To build the graph for BFS and DFS visiting, add the desired vertices and edges in `bfsGraph()` and `dfsGraph()` respectively.
### BFS and DFS visit

```
$ python -u main.py
```