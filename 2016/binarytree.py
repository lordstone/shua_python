class BinaryTreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    @classmethod
    def read_number(cls, s):
        n, i = 0, 0
        if s[0] == '#':
            return None, s[2:]
        while s[i] != ',':
            n *= 10
            n += int(s[i])
            i += 1
        return n, s[i+1:]

    @classmethod
    def serialize(cls, root):
        if root is None:
            return "#,"
        s = cls.serialize(root.left)
        s += cls.serialize(root.right)
        return str(root.val) + "," + s

    @classmethod
    def deserialize(cls, s):
        myroot = None
        if len(s) > 0:
            val, s = cls.read_number(s)
            if val is not None:
                myroot = BinaryTreeNode(val)
                if len(s) > 0:
                    myroot.left, s = cls.deserialize(s)
                if len(s) > 0:
                    myroot.right, s = cls.deserialize(s)
        return myroot, s


mystr = "1,2,4,#,#,#,3,5,#,#,6,#,#,"
proot, mystr = BinaryTreeNode.deserialize(mystr)
mystr = BinaryTreeNode.serialize(proot)
print(mystr)
