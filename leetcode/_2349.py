from sortedcontainers import SortedList


class NumberContainers:

    def __init__(self):
        self.container_i_n = {}
        self.container_n_i = {}

    def change(self, index: int, number: int) -> None:
        if index in self.container_i_n and self.container_i_n[index] in self.container_n_i:
            self.container_n_i[self.container_i_n[index]].remove(index)
        self.container_i_n[index] = number
        if number in self.container_n_i:
            self.container_n_i[number].add(index)
        else:
            self.container_n_i[number] = SortedList([index])

    def find(self, number: int) -> int:
        if number in self.container_n_i and self.container_n_i[number]:
            return self.container_n_i[number][0]
        else:
            return -1


if __name__ == '__main__':
    n = NumberContainers()
    print(n.find(10))
    print(n.change(2, 10))
    print(n.change(1, 10))
    print(n.change(3, 10))
    print(n.change(5, 10))
    print(n.find(10))
    print(n.change(1, 20))
    print(n.find(10))