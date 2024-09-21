from stack import Stack

if __name__ == "__main__":
    my_stack = Stack()

    # Push various strings
    my_stack.push("phewww")
    my_stack.push("ka-booom")
    my_stack.push("di-shoom")
    my_stack.push("pow")
    my_stack.push("bang")
    my_stack.push("ka-ching")

    # Display stack
    print("\nCurrent Stack with Strings:")
    my_stack.display()

    # Peek at the top item
    print("\nPeeking at the top item:")
    my_stack.peek()

    # Pop the top item
    print("\nPopping the top item:")
    my_stack.pop()

    # Display stack after pop
    print("\nStack after popping:")
    my_stack.display()