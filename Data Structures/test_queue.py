from Queue import Queue

if __name__ == "__main__":
    my_queue = Queue()

    # Enqueue items to the queue
    my_queue.enqueue('task1')
    my_queue.enqueue('task2')
    my_queue.enqueue('task3')
    my_queue.enqueue('task4')

    # Display the queue
    print("\nCurrent Queue:")
    my_queue.display()

    # Peek at the front item
    print("\nPeeking at the front item:")
    my_queue.peek()

    # Dequeue the front item
    print("\nDequeuing the front item:")
    my_queue.dequeue()

    # Display the queue after dequeue
    print("\nQueue after dequeuing:")
    my_queue.display()

    # Check the size of the queue
    print(f"\nCurrent queue size: {my_queue.size()}")
