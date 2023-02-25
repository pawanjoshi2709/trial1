import multiprocessing
def square1(index, value):
    value[index] = value[index]**2
if __name__ == '__main__':
    arr = multiprocessing.Array('i', [2,3,6,7,8,8,9,3,3,3])
    process = []
    for i in range(10):
        m = multiprocessing.Process(target = square1, args = (i, arr))
        process.append(m)
        m.start()
    for m in process:
        m.join()
    print(list(arr))