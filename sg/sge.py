queue = [] * 50
HeadPointer = -1
TailPointer = 0


def Enqueue(id_string):
    global TailPointer, HeadPointer, queue

    # Check if the queue is full
    if TailPointer >= 50:
        print("Queue is full. Cannot enqueue new ID.")
        return

    # If the queue is empty, update HeadPointer to point to the first element
    if HeadPointer == -1:
        HeadPointer = 0

    # Insert the ID into the queue at the position of TailPointer
    queue[TailPointer] = id_string
    print(f"Enqueued ID: {id_string} at position {TailPointer}")

    # Move the TailPointer to the next position
    TailPointer += 1

