from bst import BinarySearchTree  # Import the BinarySearchTree class

if __name__ == "__main__":
    # Create an instance of BinarySearchTree
    bst = BinarySearchTree()

    # Insert values into the binary search tree
    bst.insert(50)
    bst.insert(30)
    bst.insert(70)
    bst.insert(20)
    bst.insert(40)
    bst.insert(60)
    bst.insert(80)

    # Traverse the tree in-order (should print values in sorted order)
    print("\nIn-order Traversal of the BST:")
    bst.inorder_traverse()  # Expected output: 20 30 40 50 60 70 80

    # Search for a value in the BST
    print("\n\nSearching for 40 in the BST:")
    found = bst.search(40)
    print(f"Found: {found}")  # Expected output: Found: True

    print("\nSearching for 100 in the BST:")
    found = bst.search(100)
    print(f"Found: {found}")  # Expected output: Found: False

    # Find the minimum value in the BST
    print(f"\nMinimum value in the BST: {bst.min_value()}")  # Expected output: 20

    # Find the maximum value in the BST
    print(f"Maximum value in the BST: {bst.max_value()}")  # Expected output: 80