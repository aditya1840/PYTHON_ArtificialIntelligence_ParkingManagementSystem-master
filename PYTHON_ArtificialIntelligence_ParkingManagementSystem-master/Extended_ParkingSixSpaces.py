# """ -------------------- Extended_ParkingSixSpaces.py    --------------------------
# ******** Search Code for DFS  and other search methods
# ******** (expanding front only)
# ******** Authors:
# ********            Velasco Paola
# ********            Micha Evagelia
# ******** University of West Attica 2020
# ******** Informatics Computer Engineering
# ********
# """

# import copy

# import sys

# import time

# start_time = time.time()

# sys.setrecursionlimit(10 ** 6)

# # **** The Parking Spaces Diagram
# # **** Διάγραμμα των Χώρων του Πάρκινγκ
# #
# #   +-------+-------+
# #   |   5   |   4   |
# #   +-------+-------+
# #   |   6   |   3   |
# #   +-------+-------+
# #   |   1   |   2   |
# #   +-------+-------+
# #       ^
# #    entrance

# spaces = {
#     1: [2, 6],
#     2: [1, 3],
#     3: [2, 4, 6],
#     4: [3, 5],
#     5: [4, 6],
#     6: [1, 3, 5]
# }

# # **** The Parking Initial State Diagram
# # **** The Parking Initial State Diagram
# # **** Διάγραμμα Αρχικής Κατάστασης του Πάρκινγκ
# #   +--------+--------+
# #   |  P4 NO |  P3 NO |
# #   +--------+--------+
# #   |  P5 NO |  P2 NO |
# #   +--------+--------+
# #   |   E    |  P1 NO |
# #   +--------+--------+
# #       ^
# #   5 vehicles waiting

# # **** The problem's initial state
# # **** Αρχική Κατάσταση Προβλήματος
# #
# # 1ο στοιχείο : πλήθος αυτοκινήτων εκτος parking
# # 2ο στοιχείο : χώρος 1 (που ειναι και ο χώρος εισόδου)
# # 3ο στοιχείο : χώρος 2
# # 4ο στοιχείο : χώρος 3
# # 5ο στοιχείο : χώρος 4
# # 6ο στοιχείο : χώρος 5
# # 7ο στοιχείο : χώρος 6

# # state = [1, ['E', 'NO'], ['P1', 'NO'], ['P2', 'NO'], ['P3', 'NO'], ['P4','NO'],['P5','NO']]


# # ******** Operators
# # ******** Τελεστές

# '''
#  **** Τελεστής IN:
#  **** Είσοδος αυτοκινήτου και τοποθέτηση σε άδεια πλατφόρμα στο χώρο εισόδου (1)
# '''


# def enter(state):
#     if state[0] != 0 and state[1][0][0] == 'P' and state[1][
#         1] == 'NO':  # υπάρχει πλατφόρμα στο χώρο εισόδου χωρίς αυτοκίνητο (NO)
#         new_state = [state[0] - 1] + [[state[1][0], 'YES']] + state[2:]  # είσοδος αυτοκινήτου στο parking
#         return new_state


# '''
#  **** Βοηθητικη συναρτηση swap: 
#  **** Αντιμεταθέτει μέσα σε μια λιστα state τα δυο στoιχεία της που βρίσκονται στις θέσεις i & j
# '''


# def swap(state_l, i, j):
#     state_l[i], state_l[j] = state_l[j], state_l[i]
#     return state_l


# '''
#  **** Τελεστής neighbour1:
#  **** Μετακίνηση 1ης πλατφόρμας που συνορεύει με κενό χώρο προς το γειτονικό της κενό χώρο 
#  **** αντιμετάθεση e με πλατφόρμα, π.χ. [3, ['P1', 'NO'], ['P2', 'NO'], ['E', 'NO'], ['P3', 'NO']] ---> [3, ['P1', 'NO'], ['E', 'NO'], ['P2', 'NO'], ['P3', 'NO']]
# '''


# def neighbour1(state):
#     elem = ['E', 'NO']
#     i = state.index(elem) if elem in state else -1
#     if i >= 0:
#         swap(state, i, spaces[i][0])
#         return state


# '''
#  **** Τελεστής neighbour2:
#  **** Μετακίνηση 2ης πλατφόρμας που συνορεύει με κενό χώρο προς τον γειτονικό της κενό χώρο
#  **** αντιμετάθεση e με πλατφόρμα, π.χ. [3, ['P1', 'NO'], ['P2', 'NO'], ['E', 'NO'], ['P3', 'NO']] ---> [3, ['P1', 'NO'], ['P2', 'NO'], ['P3', 'NO'], ['E', 'NO']]
# '''


# def neighbour2(state):
#     elem = ['E', 'NO']
#     i = state.index(elem) if elem in state else -1
#     if i >= 0:
#         swap(state, i, spaces[i][1])
#         return state


# '''
#  **** Τελεστής neighbour3:
#  **** Μετακίνηση 3ης πλατφόρμας που συνορεύει με κενό χώρο προς τον γειτονικό της κενό χώρο
#  **** αντιμετάθεση e με πλατφόρμα, π.χ. [3, ['P1', 'NO'], ['P2', 'NO'], ['E', 'NO'], ['P3', 'NO']] ---> [3, ['P1', 'NO'], ['P2', 'NO'], ['P3', 'NO'], ['E', 'NO']]
# '''


# def neighbour3(state):
#     elem = ['E', 'NO']
#     i = state.index(elem) if elem in state else -1
#     if i >= 0 and len(spaces[i]) == 3:
#         swap(state, i, spaces[i][2])
#         return state


# '''
# Συνάρτηση εύρεσης απογόνων της τρέχουσας κατάστασης
# '''


# def find_children(state):
#     children = []

#     enter_state = copy.deepcopy(state)
#     enter_child = enter(enter_state)

#     tr1_state = copy.deepcopy(state)
#     tr1_child = neighbour1(tr1_state)

#     tr2_state = copy.deepcopy(state)
#     tr2_child = neighbour2(tr2_state)

#     tr3_state = copy.deepcopy(state)
#     tr3_child = neighbour3(tr3_state)

#     if tr1_child is not None:
#         children.append(tr1_child)

#     if tr2_child is not None:
#         children.append(tr2_child)

#     if tr3_child is not None:
#         children.append(tr3_child)

#     if enter_child is not None:
#         children.append(enter_child)

#     return children


# """ ----------------------------------------------------------------------------
# **** FRONT
# **** Διαχείριση Μετώπου
# """

# """ ----------------------------------------------------------------------------
# ** initialization of front
# ** Αρχικοποίηση Μετώπου
# """


# def make_front(state):
#     return [state]


# """ ----------------------------------------------------------------------------
# **** expanding front
# **** επέκταση μετώπου    
# """


# def expand_front(front,
#                  method):  # παίρνει ως όρισμα όλο το τρέχον μέτωπο και τη μέθοδο που έχουμε διαλέξει από τη main()
#     if method == 'DFS':
#         if front:
#             print("Front:")
#             print(front)  # τρέχουσα κατάσταση
#             node = front.pop(0)  # αφαίρεσε το πρώτο στοιχείο του μετώπου
#             for child in find_children(node):
#                 front.insert(0, child)  # Βάλε κάθε παιδί που περιέχει η λίστα children[] στο μέτωπο στην πρώτη θέση

#     elif method == 'BFS':
#         if front:
#             print("Front:")
#             print(front)
#             node = front.pop(0)  # αφαίρεσε το πρώτο στοιχείο του μετώπου
#             for child in find_children(node):
#                 front.append(child)  # Βάλε κάθε παιδί που περιέχει η λίστα children[] στο τέλος του μετώπου

#     elif method == 'BestFS':
#         if front:
#             print("Front:")
#             print(front)
#             node = front.pop(0)  # αφαίρεσε το πρώτο στοιχείο της λίστας-front
#             for child in find_children(node):
#                 front.insert(0, child)  # πρόσθεσε τα παιδιά του στην αρχή της λίστας
#             front = sort_front(
#                 front)  # κλήση συνάρτησης sort_front για ταξινόμηση. Η front στο τέλος θα έχει ταξινομημένα τις καταστάσεις
#     # else: "other methods to be added"

#     return front  # επέστρεψε το καινούριο μέτωπο που περιέχει τα παιδιά και όχι τον γονέα τους.


# """ ----------------------------------------------------------------------------
# **** QUEUE
# **** Διαχείριση ουράς
# """

# """ ----------------------------------------------------------------------------
# ** initialization of queue
# ** Αρχικοποίηση ουράς
# """


# def make_queue(state):
#     return [[state]]


# """ ----------------------------------------------------------------------------
# **** expanding queue
# **** επέκταση ουράς
# """


# def extend_queue(queue,
#                  method):  # η συνάρτηση λαμβάνει ως όρισμα την τρέχουσα ουρά και την επιλγμένη μέθοδο από τη main()

#     if method == 'DFS':
#         print("Queue:")
#         print(queue)
#         node = queue.pop(0)  # αφαίρεσε το πρώτο μονοπάτι και αποθήκευσέ τη στην node
#         queue_copy = copy.deepcopy(queue)  # αντιγραφή της τρέχουσας ουράς χωρίς
#         children = find_children(
#             node[-1])  # Βρες τα παιδιά της κατάστασης που βρίσκεται στο τέλος του μονοπατιού που βρίσκεται στο node
#         for child in children:  # Για κάθε παιδί
#             path = copy.deepcopy(node)  # κάνε αντιγραφή το node στο path
#             path.append(child)  # και πρόσθεσε στο path το παιδί
#             queue_copy.insert(0, path)  # Τέλος πρόσθεσε το path στην αρχή της ουράς

#     elif method == 'BFS':  # ίδια διαδικασία με τη DFS με τη μόνη διαφορά στη σειρά εισαγωγής του παιδιού
#         print("Queue:")
#         print(queue)
#         node = queue.pop(0)
#         queue_copy = copy.deepcopy(queue)
#         children = find_children(node[-1])
#         for child in children:
#             path = copy.deepcopy(node)
#             path.append(child)
#             queue_copy.append(path)  # Πρόσθεσε το path στο τέλος της ουράς

#     elif method == 'BestFS':
#         print("Queue:")
#         print(queue)
#         node = queue.pop(0)
#         queue_copy = copy.deepcopy(queue)
#         children = find_children(node[-1])
#         for child in children:
#             path = copy.deepcopy(node)
#             path.append(child)
#             queue_copy.insert(0, path)
#         queue_copy = sort_queue(queue_copy)  # ταξινόμησε την ουρά
#     # else: "other methods to be added"

#     return queue_copy


# """ ----------------------------------------------------------------------------
# **** Basic recursive function to create search tree (recursive tree expansion)
# **** Βασική αναδρομική συνάρτηση για δημιουργία δέντρου αναζήτησης (αναδρομική επέκταση δέντρου)
# """


# def is_goal_state(front):
#     if front[0] == 0:
#         return 1
#     else:
#         return 0


# def find_solution(front, queue, closed, method):
#     if not front:  # αν η πρώτη κατάσταση στο τρέχον μέτωπο υπάρχει στη λίστα closed[]
#         print('_NO_SOLUTION_FOUND_')

#     elif front[0] in closed:  # αν η πρώτη κατάσταση στο τρέχον μέτωπο υπάρχει στη λίστα closed[]
#         new_front = copy.deepcopy(front)  # αντιγραφή front στο new_front
#         new_front.pop(0)  # αφαίρεση του πρώτου στοιχείου από το new_front
#         new_queue = copy.deepcopy(queue)
#         new_queue.pop(0)  # αφαίρεση του πρώτου στοιχείου από το new_queue
#         find_solution(new_front, new_queue, closed, method)  # αναδρομική κλήση

#     elif is_goal_state(front[0]):  # Αν το η πρώτη κατάσταση στο τρέχον μέτωπο είναι η τελική κατάσταση
#         # elif front[0]==goal:
#         print('_GOAL_FOUND_')
#         print("Front: \n", front[0])  # Εκτύπωσε την πρώτη κατάσταση η οποία ταυτίζεται με την τελική κατάσταση
#         print("Queue: \n", queue[0])  # Εκτύπωσε την ουρά η οποία ταυτίζεται με την τελική κατάσταση

#     else:  # Αν δεν ισχύει τίποτα από τα παραπάνω
#         closed.append(
#             front[0])  # Πρόσθεσε στο τέλος της λίστας-closed, την πρώτη κατάσταση (πρώτο στοιχείο) στο τρέχον μέτωπο
#         front_copy = copy.deepcopy(front)  # Αντιγραφή του front στο front_copy
#         front_children = expand_front(front_copy,
#                                       method)  # Κλήση της συνάρτησης expand_front και επιστροφή τιμή της στην front children
#         queue_copy = copy.deepcopy(queue)  # Αντιγραφή του queue στο queue_copy
#         queue_children = extend_queue(queue_copy,
#                                       method)  # Κλήση της συνάρτησης expand_queue και επιστροφή τιμή της στην ουρά children
#         closed_copy = copy.deepcopy(closed)
#         find_solution(front_children, queue_children, closed_copy, method)


# """
# -----------------
# """


# # Συνάρτηση για ταξινόμηση του μετώπου
# # Η ταξινόμηση γίνεται με βάση την απόσταση κενής πλατφόρμας με κενό χώρο
# def sort_front(front):
#     if front:
#         temp_front = front
#         distances = []
#         # Για κάθε κατάσταση μέσα στο μέτωπο
#         for i in range(len(front)):
#             # Αρχικόποιηση τιμών
#             platform_pos = -1
#             empty_pos = 0
#             # Για κάθε λίστα κάθε κατάστασης
#             for j in range(1, len(front[i])):
#                 # Ελέγχουμε αν υπάρχει κενή πλατφόρμα και καταγράφουμε τη θέση της
#                 if front[i][j][0] == 'P' and front[i][j][1] == 'NO' and platform_pos == -1:
#                     # Με το πηλίκο βρίσκουμε τη θέση οριζόντια και με το υπόλοιπο κάθετα
#                     platform_pos = j // 3 + j % 2
#                 # break
#                 # Καταγράφουμε τη θέση του κενού χώρου
#                 if front[i][j][0] == 'E':
#                     # Με το πηλίκο βρίσκουμε τη θέση οριζόντια και με το υπόλοιπο κάθετα
#                     empty_pos = j // 3 + j % 2

#             if platform_pos != -1:
#                 # Υπολογίζουμε απόσταση
#                 distance = abs(platform_pos - empty_pos)
#             else:
#                 # Αν δεν υπάρχει βάζουμε αρνητική τιμή
#                 distance = -1

#             distances.append(distance)

#         # Bubble sort για τις καταστάσεις του μετώπου
#         for i in range(len(front)):
#             for j in range(0, len(front) - i - 1):
#                 if distances[j] > distances[j + 1]:
#                     temp_front[j], temp_front[j + 1] = temp_front[j + 1], temp_front[j]
#                     distances[j], distances[j + 1] = distances[j + 1], distances[j]

#         return temp_front  # επιστροφή ταξινομημένου μετώπου
#     else:
#         return front

#     # Συνάρτηση για ταξινόμηση της ουράς


# # Η ταξινόμηση γίνεται με βάση την απόσταση κενής πλατφόρμας με κενό χώρο όπως και στη sort_front
# def sort_queue(queue):
#     if queue:
#         distances = []

#         for i in range(len(queue)):

#             temp_queue = queue
#             # Παίρνουμε τη τελευταία κατάσταση για κάθε στοιχείο
#             base = queue[i][-1]
#             # Αρχικόποιηση τιμών
#             platform_pos = -1
#             empty_pos = 0
#             # Για κάθε λίστα κάθε κατάστασης
#             for j in range(1, len(base)):
#                 # Ελέγχουμε αν υπάρχει κενή πλατφόρμα και καταγράφουμε τη θέση της
#                 if base[j][0] == 'P' and base[j][1] == 'NO' and platform_pos == -1:
#                     # Με το πηλίκο βρίσκουμε τη θέση οριζόντια και με το υπόλοιπο κάθετα
#                     platform_pos = j // 3 + j % 2
#                 # Καταγράφουμε τη θέση του κενού χώρου
#                 if base[j][0] == 'E':
#                     empty_pos = j // 3 + j % 2

#             if platform_pos != -1:
#                 # Υπολογίζουμε απόσταση
#                 distance = abs(platform_pos - empty_pos)
#             else:
#                 distance = -1

#             distances.append(distance)

#         # Bubble sort για τις καταστάσεις του μετώπου
#         for i in range(len(queue)):
#             for j in range(0, len(queue) - i - 1):
#                 if distances[j] > distances[j + 1]:
#                     temp_queue[j], temp_queue[j + 1] = temp_queue[j + 1], temp_queue[j]
#                     distances[j], distances[j + 1] = distances[j + 1], distances[j]

#         return temp_queue  # επιστροφή ταξινομημένης ουράς
#     else:
#         return queue


# """" ----------------------------------------------------------------------------
# ** Executing the code
# ** κλήση εκτέλεσης κώδικα
# """


# def main():
#     initial_state = [5, ['E', 'NO'], ['P1', 'NO'], ['P2', 'NO'], ['P3', 'NO'], ['P4', 'NO'], ['P5', 'NO']]

#     method = 'BestFS'

#     """ ----------------------------------------------------------------------------
#     **** starting search
#     **** έναρξη αναζήτησης
#     """

#     print('____BEGIN__SEARCHING____')

#     find_solution(make_front(initial_state), make_queue(initial_state), [], method)

#     print("--- %s seconds ---" % (time.time() - start_time))


# if __name__ == "__main__":
#     main()

import copy
import sys
import time

# Set recursion limit
sys.setrecursionlimit(10 ** 6)

# Define parking spaces diagram
spaces = {
    1: [2, 6],
    2: [1, 3],
    3: [2, 4, 6],
    4: [3, 5],
    5: [4, 6],
    6: [1, 3, 5]
}

# Define initial state
initial_state = [5, ['E', 'NO'], ['P1', 'NO'], ['P2', 'NO'], ['P3', 'NO'], ['P4', 'NO'], ['P5', 'NO']]

# Define operators (enter, swap, and move operations)
def enter(state):
    if state[0] != 0 and state[1][0][0] == 'P' and state[1][1] == 'NO':
        new_state = [state[0] - 1] + [[state[1][0], 'YES']] + state[2:]
        return new_state

def swap(state_l, i, j):
    state_l[i], state_l[j] = state_l[j], state_l[i]
    return state_l

def move_platform(state, i):
    swap(state, i, spaces[i][0])
    return state

# Define function to find children of the current state
def find_children(state):
    children = []
    enter_state = copy.deepcopy(state)
    enter_child = enter(enter_state)
    tr1_state = copy.deepcopy(state)
    tr1_child = move_platform(tr1_state, spaces[1][0])
    tr2_state = copy.deepcopy(state)
    tr2_child = move_platform(tr2_state, spaces[2][0])
    tr3_state = copy.deepcopy(state)
    tr3_child = move_platform(tr3_state, spaces[3][0])

    if tr1_child is not None:
        children.append(tr1_child)

    if tr2_child is not None:
        children.append(tr2_child)

    if tr3_child is not None:
        children.append(tr3_child)

    if enter_child is not None:
        children.append(enter_child)

    return children

# Function to sort the front based on the distance between empty space and platform
def sort_front(front):
    if front:
        temp_front = front
        distances = []
        for i in range(len(front)):
            base = front[i][-1]
            platform_pos = -1
            empty_pos = 0
            for j in range(1, len(base)):
                if base[j][0] == 'P' and base[j][1] == 'NO' and platform_pos == -1:
                    platform_pos = j // 3 + j % 2
                if base[j][0] == 'E':
                    empty_pos = j // 3 + j % 2

            if platform_pos != -1:
                distance = abs(platform_pos - empty_pos)
            else:
                distance = -1

            distances.append(distance)

        for i in range(len(front)):
            for j in range(0, len(front) - i - 1):
                if distances[j] > distances[j + 1]:
                    temp_front[j], temp_front[j + 1] = temp_front[j + 1], temp_front[j]
                    distances[j], distances[j + 1] = distances[j + 1], distances[j]

        return temp_front
    else:
        return front

# Function to find solution using search methods (DFS, BFS, BestFS)
def find_solution(front, queue, closed, method):
    if not front:
        print('_NO_SOLUTION_FOUND_')

    elif front[0] in closed:
        new_front = copy.deepcopy(front)
        new_front.pop(0)
        new_queue = copy.deepcopy(queue)
        new_queue.pop(0)
        find_solution(new_front, new_queue, closed, method)

    elif is_goal_state(front[0]):
        print('_GOAL_FOUND_')
        print("Front: \n", front[0])
        print("Queue: \n", queue[0])

    else:
        closed.append(front[0])
        front_copy = copy.deepcopy(front)
        front_children = sort_front(find_children(front_copy))
        queue_copy = copy.deepcopy(queue)
        queue_children = extend_queue(queue_copy, method)
        closed_copy = copy.deepcopy(closed)
        find_solution(front_children, queue_children, closed_copy, method)

# Main function
def main():
    method = 'BestFS'
    print('____BEGIN__SEARCHING____')
    find_solution([initial_state], [[initial_state]], [], method)

if __name__ == "__main__":
    main()
