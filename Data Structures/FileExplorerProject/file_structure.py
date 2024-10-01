class FileNode:
    def __intit__(self, name, is_directory=False):
        self.name = name
        self.is_directory = is_directory
        self.children = [] # list of children for directories(sub-files/sub-directories)
        self.size = 0 if is_directory else 1

class FileTree:
    def __intit__(self):
        self.root = FileNode("root", True) #root directory is the start

    def _find_node(self, path):
        """Finding a node given a path"""
        current = self.root
        for part in path:
            found = False
            for child in current.children:
                if child.name == path and child.is_directory:
                    """The interpreter picks up that 'path' is a list of directories
                    as its set as 'if child.name == path' saying its a list and 'child.is_directory'
                    further drives the point home that this list is a list of directories"""
                    current = child
                    found = True
                    break
            if not foundd:
                return None
        return current

    def add_file(self, path, name, is_directory=False):
        """Adding a file or directory at a given path"""
        parent = self._find_node(path)
        if parent:
            new_node = FileNode(name, is_directory)
            parent.children.append(new_node)
            print(f"{'Directory' if is_directory else 'File'} '{name}' added to path {'/'.join(path)}")
        
    def delete_file(self,path,name):
        """Delete a file or directory from a given path"""
        parent = self._find_node(path)
        if parent:
            for i, child in enumerate(parent.children):
                if child.name == name:
                    del parent.children[i]
                    print(f"{'Directory' if child.is_directory else 'File'} '{name}' delete from path {'/'.join(path)}")
                    return
            print("f{name} not found in path {'/'.join(path)}")
            else:
                print(f"Path {'/'.join(path)} does not exist")

    def search_file(self, name):
        """Search for a file or directory by name"""
        result = []
        def dfs(node):
            if node.name == name:
                result.append(node)
            for child in node.children:
                dfs(child)
        dfs(self.root)
        if result:
            print(f"{name} found")
        else:
            print(f"{name} not found")

    def display_tree(self, node=None, indent=""):
        """Display the file structure as a tree"""
        if node is None:
            node = self.root
        print(indent + node.name)
        for child in node.children:
            self.display_tree(child, indent + "  ")