'''
Time & Space:
create(): O(path.length()), get(): O(1).

space:
file():
In worst case, e.g., path = "/a/b/c/d/e/f/g/...", all the path family cost 2 + 4 + 6 + ... + 2n = n * (n + 1).
So the space cost O(path.length() ^ 2).

'''

from collections import defaultdict


class File(object):
    def __init__(self, name):
        self.map = defaultdict(File)
        self.name = name
        self.value = -1


class FileSystem(object):

    def __init__(self):
        self.root = File("")

    def create(self, path, value):
        """
        :type path: str
        :type value: int
        :rtype: bool
        """
        array = path.split("/")
        cur = self.root
        for i in range(1, len(array)):
            name = array[i]
            if name not in cur.map:
                if i == len(array) - 1:
                    cur.map[name] = File(name)
                else:
                    return False
            cur = cur.map[name]

        if cur.value != -1:
            return False
        cur.value = value

        return True

    def get(self, path):
        """
        :type path: str
        :rtype: int
        """
        cur = self.root
        array = path.split("/")
        for i in range(1, len(array)):
            name = array[i]
            if name not in cur.map:
                return -1
            cur = cur.map[name]
        return cur.value

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.create(path,value)
# param_2 = obj.get(path)


class FileSystem_easy:

    def __init__(self):
        self.paths = defaultdict()

    def createPath(self, path: str, value: int) -> bool:

        # Step-1: basic path validations
        if path == "/" or len(path) == 0 or path in self.paths:
            return False

        # Step-2: if the parent doesn't exist. Note that "/" is a valid parent.
        parent = path[:path.rfind('/')]
        if len(parent) > 1 and parent not in self.paths:
            return False

        # Step-3: add this new path and return true.
        self.paths[path] = value
        return True

    def get(self, path: str) -> int:
        return self.paths.get(path, -1)