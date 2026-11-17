from collections import deque

queue = deque()


def addCall(customerID, callTime):
    call = (customerID, callTime)
    queue.append(call)
    print("Call added to queue")


def answerCall():
    if len(queue) == 0:
        print("Queue is empty")
    else:
        call = queue.popleft()
        print("Answered call:", call[0])
        print("Call time:", call[1])


def viewQueue():
    if len(queue) == 0:
        print("Queue is empty")
    else:
        print("Pending calls:")
        for call in queue:
            print("Customer ID:", call[0], "Call Time:", call[1])


def isQueueEmpty():
    return len(queue) == 0


while True:
    print("\n1. Add Call")
    print("2. Answer Call")
    print("3. View Queue")
    print("4. Check Queue Empty")
    print("5. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        cid = int(input("Enter Customer ID: "))
        call_time = int(input("Enter Call Time: "))
        addCall(cid, call_time)
    elif ch == 2:
        answerCall()
    elif ch == 3:
        viewQueue()
    elif ch == 4:
        print("Queue Empty:", isQueueEmpty())
    elif ch == 5:
        break
    else:
        print("Invalid choice")
