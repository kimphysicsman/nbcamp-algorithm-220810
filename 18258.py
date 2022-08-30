# 문제
# 정수를 저장하는 큐를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.
#
# 명령은 총 여섯 가지이다.
#
# push X: 정수 X를 큐에 넣는 연산이다.
# pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 큐에 들어있는 정수의 개수를 출력한다.
# empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
# front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# 입력
# 첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 2,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다. 주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 문제에 나와있지 않은 명령이 주어지는 경우는 없다.
#
# 출력
# 출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.


import sys

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def push(self, value):
        self.size += 1
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            new_tail = Node(value)
            self.tail.next = new_tail
            self.tail = new_tail

    def pop(self):
        self.size -= 1
        if self.head is None:
            return -1

        old_head_value = self.head.value
        self.head = self.head.next

        return old_head_value

    def size_(self):

        return self.size

    def empty(self):
        if self.head is None:
            return True
        return False

    def front(self):
        if self.head is None:
            return -1
        return self.head.value

    def back(self):
        if self.head is None:
            return -1
        return self.tail.value


def main():
    queue = Queue()

    # n = int(input("input N : "))
    n = int(sys.stdin.readline())

    for _ in range(n):
        # command = input("input Command : ").split()
        command = sys.stdin.readline().split()
        if command[0] == "push":
            queue.push(command[1])
        elif command[0] == "pop":
            print(queue.pop())
        elif command[0] == "size":
            print(queue.size_())
        elif command[0] == "empty":
            if queue.empty():
                print("1")
            else:
                print("0")
        elif command[0] == "front":
            print(queue.front())
        elif command[0] == "back":
            print(queue.back())


main()

