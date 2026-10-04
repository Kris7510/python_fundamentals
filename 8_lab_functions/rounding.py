def rounded (num: int):
    return round(num)

num_ = list(map(float, input().split(" ")))


for i in range(len(num_)):
    num_[i] = rounded(num_[i])
print(num_)
