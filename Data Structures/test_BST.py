from bst import BinarySearchTree
import random



if __name__ == "__main__":
    # Creating a instance of bst
    bst = BinarySearchTree()

    # Inserting values into the bst with random
    bst.insert(50)
    bst.insert(30)
    bst.insert(70)
    bst.insert(20)
    bst.insert(40)
    bst.insert(60)
    bst.insert(80)
    bst.insert(10)
    bst.insert(90)


    # Traverse the tree in-order (print values in asc -> dsc)
    print("\nIn-order Traversal of BST:")
    bst.inorder_traverse()

    #Searching for a value in BST
    print("\n\nSearching for 99 in the BST")
    found = bst.search(99)
    print(f"Found: {found}")

    print("\nSearching for 999(not included) in BST:")
    found = bst.search(999)
    print(f"Found: {found}")

    # Finding the max value in the BST
    print(f"/nMaximum value in the BST: {bst.max_value()}")

    # Finding the min value in the BST
    print(f"\nMinimum value in the BST: {bst.min_value()}")