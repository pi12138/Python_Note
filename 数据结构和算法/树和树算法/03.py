# coding:utf-8
"""
二叉树的实现
深度优先遍历
    - 先序遍历
    - 中序遍历
    - 后序遍历
    02.py递归实现
    03.py栈实现
"""


class Node(object):
    """树的节点"""
    def __init__(self, item):
        self.item = item
        # 左右子节点
        self.lchild = None
        self.rchild = None


class BinaryTree(object):
    """二叉树"""
    def __init__ (self):
        """二叉树初始化"""
        self.root = None

    def add(self, item):
        node = Node(item)
        if self.root is None:
            self.root = node
            return
        else:
            # 借助队列遍历
            queue = []
            queue.append(self.root)
            # 对已有节点遍历
            while queue:
                current = queue.pop(0)
                if current.lchild is None:
                    # 如果左边子节点为空则添加到左边
                    current.lchild = node
                    return
                elif current.rchild is None:
                    current.rchild = node
                    return
                else:
                    # 如果左右子节点均存在，则将左右子节点添加到队列然后继续遍历
                    queue.append(current.lchild)
                    queue.append(current.rchild)

    def preorder_travel(self, root):
        """先序遍历"""
        if root is None:
            return
        else:
            stack = []
            current = root

            # 当stack和current均为空时退出
            while stack or current:
                # 当当前节点为空时退出
                while current:
                    print(current.item, end=" ")
                    # 当前节点入栈
                    stack.append(current)
                    # 先遍历左子节点
                    current = current.lchild
                # 当current = None 退出循环
                # 当前节点出栈，
                current = stack.pop()
                current = current.rchild

    def inorder_travel(self, root):
        """中序遍历"""
        if root is None:
            return
        else:
            stack = []
            current = root

            while stack or current:
                # 一直查找左节点一直入栈
                while current:
                    stack.append(current)
                    current = current.lchild
                # 当current = None时
                # 该节点不存在左节点，该节点出栈，查找右节点
                current = stack.pop()
                print(current.item, end=" ")
                current = current.rchild

    def postorder_travel(self, root):
        """后序遍历"""
        if root is None:
            return
        else:
            # 两个栈分别存储节点
            stack1 = []
            stack2 = []
            # current = root
            stack1.append(root)

            while stack1:
                # 该节点出栈1，然后左右节点进栈1（对于左右子节点，也是右节点先出栈1）
                current = stack1.pop()
                if current.lchild is not None:
                    stack1.append(current.lchild)
                if current.rchild is not None:
                    stack1.append(current.rchild)
                # 该节点入栈2
                stack2.append(current)
            while stack2:
                print(stack2.pop().item, end=" ")


if __name__ == "__main__":
    bt1 = BinaryTree()

    bt1.add("0")
    bt1.add("1")
    bt1.add("2")
    bt1.add("3")
    bt1.add("4")
    bt1.add("5")
    bt1.add("6")
    bt1.add("7")
    bt1.add("8")
    bt1.add("9")

    print("先序遍历：")
    bt1.preorder_travel(bt1.root)
    print(" ")
    print("中序遍历")
    bt1.inorder_travel(bt1.root)
    print(" ")
    print("后序遍历")
    bt1.postorder_travel(bt1.root)