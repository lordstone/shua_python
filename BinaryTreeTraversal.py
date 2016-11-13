import collections


class TreeNode(object):

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Tree(object):

    def __init__(self, root_val=-1):
        self.root = TreeNode(root_val)

    def get_root(self):
        return self.root

    def list_to_tree(self, node_list):
        for i in node_list:
            self.add_node(i)

    def add_node(self, val):
        cur = self.get_root()
        if cur.val == -1:
            cur.val = val
        else:
            q = collections.deque()
            q.append(cur)
            while q:
                tn = q.popleft()
                if tn.left is None:
                    tn.left = TreeNode(val)
                    return
                elif tn.right is None:
                    tn.right = TreeNode(val)
                    return
                else:
                    q.append(tn.left)
                    q.append(tn.right)

    def preorder_traversal_recursion(self):
        res = []

        def do_preorder(root):
            if root is None:
                return
            res.append(root.val)
            do_preorder(root.left)
            do_preorder(root.right)

        do_preorder(self.root)
        return res

    def inorder_traversal_recursion(self):
        res = []

        def do_inorder(root):
            if root is None:
                return
            do_inorder(root.left)
            res.append(root.val)
            do_inorder(root.right)

        do_inorder(self.root)
        return res

    def postorder_traversal_recursion(self):
        res = []

        def do_postorder(root):
            if root is None:
                return
            do_postorder(root.left)
            do_postorder(root.right)
            res.append(root.val)

        do_postorder(self.root)
        return res

    def preorder_traversal_iteration(self):
        if self.get_root() is None:
            return []
        q, res = [], []
        q.append(self.get_root())
        while q:
            cur = q.pop()
            res.append(cur.val)
            if cur.right:
                q.append(cur.right)
            if cur.left:
                q.append(cur.left)
        return res

    def inorder_traversal_iteration(self):
        if self.get_root() is None:
            return []
        q, res, cur = [], [], self.get_root()
        while q or cur:
            while cur:
                q.append(cur)
                cur = cur.left
            cur = q.pop()
            res.append(cur.val)
            cur = cur.right
        return res

    def postorder_traversal_iteration(self):
        if self.get_root() is None:
            return []
        stack1, stack2, res = [], [], []
        cur = self.get_root()
        stack1.append(cur)
        while stack1:
            cur = stack1.pop()
            stack2.append(cur)
            if cur.left:
                stack1.append(cur.left)
            if cur.right:
                stack1.append(cur.right)
        while stack2:
            res.append(stack2.pop().val)
        return res

    def level_traversal(self):
        if self.get_root() is None:
            return []
        q, res = collections.deque([self.get_root()]), []
        while q:
            cur = q.popleft()
            res.append(cur.val)
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
        return res

t = Tree()
ls = list(range(30))
t.list_to_tree(ls)
print(t.preorder_traversal_recursion())
print(t.inorder_traversal_recursion())
print(t.postorder_traversal_recursion())
print(t.preorder_traversal_iteration())
print(t.inorder_traversal_iteration())
print(t.postorder_traversal_iteration())
print(t.level_traversal())
