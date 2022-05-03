class Node:
    def __init__(self, item=None, link=None):
        self.item, self.link = item, link


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        node = self.head
        print('h->', end="")
        while node is not None:
            print("{}->".format(node.item), end="")
            node = node.link
        print(None)

    def insert_node(self, p, new_node):
        if self.head is None:
            self.head = new_node
        elif p is None:
            new_node.link = self.head
            self.head = new_node
        else:
            new_node.link = p.link
            p.link = new_node

    def delete_node(self, p, removed):
        if removed == self.head:
            self.head = removed.link
        else:
            p.link = removed.link
        del removed

    def insert_first(self, item):  # insert before head
        new_node = Node(item)
        self.insert_node(p=None, new_node=new_node)

    def insert_last(self, item):  # insert after tail
        new_node = Node(item)
        p = self.head
        while p is not None and p.link is not None:  # p link가 none이먄 p가 tail
            p = p.link
        self.insert_node(p=p, new_node=new_node)

    def search(self, item):  # returns the node holding item
        node = self.head
        while node is not None:
            if node.item == item:
                return node
            node = node.link
        return None

    def search_prev(self, item):  # returns the node holding item and the previous node
        p = None
        node = self.head
        while node is not None:
            if node.item == item:
                return node, p
            p = node
            node = node.link
        return None, p  # 찾는 item이 tail일 경우 ? item 전 prev가 tail?

    def delete(self, item):
        # search_prev로 node를 찾기
        # 찾은거가지고 delete_node로 삭제
        removed, p = self.search_prev(item)
        if removed == None:
            print("Item Not Found")
            return
        self.delete_node(p, removed)

    def reverse(self):
        p = None
        node = self.head
        while node != None:
            temp = node.link
            node.link = p
            p = node
            node = temp
        self.head = p


L = LinkedList()
while True:
    cmd = input()
    if cmd == "exit":
        break
    elif cmd == "print":
        L.print_list()
    elif cmd == "reverse":
        L.reverse()
    else:
        cmd, param = cmd.split()
        if cmd == "ins_first":
            L.insert_first(int(param))
        elif cmd == "ins_last":
            L.insert_last(int(param))
        elif cmd == "find":
            node = L.search(int(param))
            if node is None:
                print('Item Not Found')
            else:
                print("{} Found".format(node.item))
        elif cmd == "del":
            L.delete(int(param))
