# write a program implement the queue
list = []

while True:
    p = int(input('''
                1. push Elements
                2. pop First element
                3. Front element in the list
                4. Last element in the list
                5. Display Queue
                6. exit from the list

    '''))

    if p == 1:
        m = input("Enter the element ")
        list.append(m)
        print(list)

    elif p == 2:
        if len(list) == 0:
            print("list is empty")
        else:
            del list[0]
            print(list)
    elif p == 3:
        if len(list) == 0:
            print("Queue is empty")
        else:
            print("First Queue values", list[0])

    elif p==4 :
        if len(list)==0 :
            print("Empty Queue")
        else:
            print("Last queue value ",list[-1])
    elif p == 5:
        print("Display queue", list)
    elif p==6:
        break
    else:
        print("this is the invalid option")

        