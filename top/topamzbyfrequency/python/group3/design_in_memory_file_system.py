"""
Implement the FileSystem class:

- FileSystem() Initializes the object of the system.
- List<String> ls(String path)
-- If path is a file path, returns a list that only contains this file's name.
-- If path is a directory path, returns the list of file and directory names in this directory.

The answer should in lexicographic order.
- void mkdir(String path) Makes a new directory according to the given path. The given directory path does not exist.
 If the middle directories in the path do not exist, you should create them as well.
- void addContentToFile(String filePath, String content)
-- If filePath does not exist, creates that file containing given content.
-- If filePath already exists, appends the given content to original content.
- String readContentFromFile(String filePath) Returns the content in the file at filePath.

Example:
Input
["FileSystem", "ls", "mkdir", "addContentToFile", "ls", "readContentFromFile"]
[[], ["/"], ["/a/b/c"], ["/a/b/c/d", "hello"], ["/"], ["/a/b/c/d"]]
Output
[null, [], null, null, ["a"], "hello"]

Explanation
FileSystem fileSystem = new FileSystem();
fileSystem.ls("/");                         // return []
fileSystem.mkdir("/a/b/c");
fileSystem.addContentToFile("/a/b/c/d", "hello");
fileSystem.ls("/");                         // return ["a"]
fileSystem.readContentFromFile("/a/b/c/d"); // return "hello"

Tag: 588/2927 , R257/2935 , R13/50 (amz)
"""
import collections


class TrieNode:
    def __init__(self):
        self.child = collections.defaultdict(TrieNode)
        self.is_file = False
        self.content = ""
        self.name = ""


class FileSystem:
    def __init__(self):
        self.root = TrieNode()

    def ls(self, path: str) -> list[str]:
        res = []
        path = path.split('/')[1:]
        cur = self.root
        if path[0] != '':
            for p in path:
                cur = cur.child[p]
        if cur.is_file:
            return [cur.name]
        for ch in cur.child:
            res.append(ch)
        return sorted(res)

    def mkdir(self, path: str) -> None:
        cur = self.root
        paths = path.split('/')[1:]
        for p in paths:
            cur = cur.child[p]
            cur.name = p

    def add_content_to_file(self, file_path: str, content: str) -> None:
        cur = self.root
        file_path = file_path.split('/')[1:]
        for p in file_path:
            cur = cur.child[p]
            cur.name = p
        cur.is_file = True
        cur.content += content

    def read_content_from_file(self, file_path: str) -> str:
        cur = self.root
        file_path = file_path.split('/')[1:]
        for p in file_path:
            cur = cur.child[p]
        if cur.is_file:
            return cur.content


def main():
    file_system = FileSystem()
    print(file_system.ls("/"))                                    # return []
    file_system.mkdir("/a/b/c")
    file_system.add_content_to_file("/a/b/c/d", "hello")
    print(file_system.ls("/"))                                    # return ["a"]
    print(file_system.read_content_from_file("/a/b/c/d"))         # return "hello"


if __name__ == "__main__":
    main()
