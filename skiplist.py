from random import randint


class SkipNode:
    def __init__(self, height=0, elem=None):
        self.next = [None] * height
        self.elem = elem

    def __str__(self):
        return "| {} `|".format(self.elem)


class SkipList:
    def __init__(self):
        self.head = SkipNode()
        self.maxHeight = 0

    def find(self, elem, update=None):
        if update is None:
            update = self.update_list(elem)
        i = len(update) - 1
        for node in reversed(update):
            if node.next[i] is not None and node.next[i].elem == elem:
                return node.next[i]
            i -= 1
        return None

    def update_list(self, elem):
        update = [None] * self.maxHeight
        x = self.head
        for i in reversed(range(self.maxHeight)):
            while x.next[i] is not None and x.next[i].elem < elem:
                x = x.next[i]
            update[i] = x
        return update

    def contains(self, elems):
        return self.find(elems) != None

    def randomHeigt(self):
        height = 1
        while randint(1, 2) == 1:
            height += 1
        return height

    def insert(self, elem):
        node = SkipNode(self.randomHeigt(), elem)

        if len(node.next) > self.maxHeight:
            self.head.next.extend([None for _ in range(len(node.next) - self.maxHeight)])
            self.maxHeight = len(node.next)

        update = self.update_list(elem)
        if self.find(elem, update) is None:
            for i in range(len(node.next)):
                node.next[i] = update[i].next[i]
                update[i].next[i] = node

    def __str__(self):
        str_repr = ""
        sep = " -- "
        for i in reversed(range(self.maxHeight)):
            str_repr += "HEAD| {}".format(sep)
            current = self.head.next[i]
            while current is not None:
                str_repr += "{}{}".format(current, sep)
                current = current.next[i]
            str_repr += "\n"
        return str_repr


if __name__ == '__main__':
    skip_list = SkipList()
    skip_list.insert(1)
    skip_list.insert(4)
    skip_list.insert(5)
    skip_list.insert(3)
    skip_list.insert(2)
    skip_list.insert(11)
    skip_list.insert(11)

    print(skip_list.contains(11))
