a = list(map(int, input().split()))


def build(v, tl, tr):
    if tl == tr: 
        tree[v] = a[tl]
    else:
        tm = int((tl + tr)/2)
        build(2 * v, tl, tm) #left tree
        build(2 * v + 1, tm + 1, tr) #right tree
        tree[v] = tree[2 * v] + tree[2 * v + 1] 
    return tree
def update(v, tl, tr, pos, new_val):
    if tl == tr: # Nếu đoạn hiện tại chỉ có 1 phần tử (lá)
        tree[v] = new_val # Cập nhật giá trị tại nút lá
    else:
        tm = int((tl + tr) / 2) # Tìm điểm giữa của đoạn
        if pos <= tm: # Nếu vị trí cần cập nhật nằm bên trái
            update(2 * v, tl, tm, pos, new_val) # Đệ quy cập nhật cây con trái
        else: # Nếu vị trí cần cập nhật nằm bên phải
            update(2 * v + 1, tm + 1, tr, pos, new_val) # Đệ quy cập nhật cây con phải
        tree[v] = tree[2 * v] + tree[2 * v + 1] # Cập nhật lại giá trị nút cha từ hai con

N = len(a)
tree = [0] * (4 * N)
build(1, 0, N - 1)
print(tree)


