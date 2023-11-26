# """ -------------------- ParkingFourSpaces.py     --------------------------
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
# #   |   4   |   3   |
# #   +-------+-------+
# #   |   1   |   2   |
# #   +-------+-------+
# #       ^
# #    entrance

# spaces = {
#     1: [2, 4],
#     2: [1, 3],
#     3: [2, 4],
#     4: [1, 3],
# }

# # **** The Parking Initial State Diagram
# # **** Διάγραμμα Αρχικής Κατάστασης του Πάρκινγκ
# #
# #   +--------+--------+
# #   |  P3 NO |  P2 NO |
# #   +--------+--------+
# #   |   E    |  P1 NO |
# #   +--------+--------+
# #       ^
# #   3 vehicles waiting


# # **** The problem's initial state
# # **** Αρχική Κατάσταση Προβλήματος
# #
# # 1st element: number of vehicles outside parking
# # 2nd element: space 1 (which is also the entrance space)
# # 3rd element: space 2
# # 4th element: space 3
# # 5th element: space 4


# # state= [3, ['E', 'NO'], ['P1', 'NO'], ['P2', 'NO'], ['P3', 'NO']]


# # ******** Operators
# # ******** Τελεστές

# '''
#  **** Τελεστής IN:
#  **** Είσοδος αυτοκινήτου και τοποθέτηση σε άδεια πλατφόρμα στο χώρο εισόδου (1)
#  # Car entrance and placement in an empty platform in the entrance space (1)
# '''


# def enter(state):
#     if state[0] != 0 and state[1][0][0] == 'P' and state[1][
#         1] == 'NO':  # υπάρχει πλατφόρμα στο χώρο εισόδου χωρίς αυτοκίνητο (NO)
#         new_state = [state[0] - 1] + [[state[1][0], 'YES']] + state[2:]  # είσοδος αυτοκινήτου στο parking
#         return new_state


# '''
#  **** Βοηθητικη συναρτηση swap: 
#  **** Αντιμεταθέτει μέσα σε μια λιστα state τα δυο στoιχεία της που βρίσκονται στις θέσεις i & j
#  #### Swaps two elements in a list state at positions i and j
# '''


# def swap(state_l, i, j):
#     state_l[i], state_l[j] = state_l[j], state_l[i]
#     return state_l


# '''
#  **** Τελεστής neighbour1:
#  **** Μετακίνηση 1ης πλατφόρμας που συνορεύει με κενό χώρο προς το γειτονικό της κενό χώρο 
#  **** αντιμετάθεση e με πλατφόρμα, π.χ. [3, ['P1', 'NO'], ['P2', 'NO'], ['E', 'NO'], ['P3', 'NO']] ---> [3, ['P1', 'NO'], ['E', 'NO'], ['P2', 'NO'], ['P3', 'NO']]
 
#  #### Moves the 1st platform adjacent to an empty space to the neighboring empty space
#  #### Swaps 'E' with a platform, e.g., [3, ['P1', 'NO'], ['P2', 'NO'], ['E', 'NO'], ['P3', 'NO']] ---> [3, ['P1', 'NO'], ['E', 'NO'], ['P2', 'NO'], ['P3', 'NO']]
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
 
#  #### Moves the 2nd platform adjacent to an empty space to the neighboring empty space
#  #### Swaps 'E' with a platform, e.g., [3, ['P1', 'NO'], ['P2', 'NO'], ['E', 'NO'], ['P3', 'NO']] ---> [3, ['P1', 'NO'], ['P2', 'NO'], ['P3', 'NO'], ['E', 'NO']]

# '''


# def neighbour2(state):
#     elem = ['E', 'NO']
#     i = state.index(elem) if elem in state else -1
#     if i >= 0:
#         swap(state, i, spaces[i][1])
#         return state


# '''
#  **** Συνάρτηση εύρεσης απογόνων της τρέχουσας κατάστασης
#  #### Function to find children of the current state

# '''


# def find_children(state):
#     children = []

#     enter_state = copy.deepcopy(state)
#     enter_child = enter(enter_state)

#     tr1_state = copy.deepcopy(state)
#     tr1_child = neighbour1(tr1_state)

#     tr2_state = copy.deepcopy(state)
#     tr2_child = neighbour2(tr2_state)

#     if tr1_child is not None:
#         children.append(tr1_child)

#     if tr2_child is not None:
#         children.append(tr2_child)

#     if enter_child is not None:
#         children.append(enter_child)

#     return children


# """ ----------------------------------------------------------------------------
# **** FRONT
# **** Διαχείριση Μετώπου

# # Managing the Front
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
# # Managing the Queue

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


# def sort_front(front):
#     if front:
#         temp_front = front
#         distances = []

#         for i in range(len(front)):
#             platform_pos = -1
#             empty_pos = 0
#             for j in range(1, len(front[i])):
#                 if front[i][j][0][0] == 'P' and front[i][j][1] == 'NO' and platform_pos == -1:
#                     platform_pos = j % 2 + j // 2
#                     # break
#                 if front[i][j][0] == 'E':
#                     empty_pos = j // 2 + j % 2

#             if platform_pos != -1:
#                 distance = abs(platform_pos - empty_pos)
#             else:
#                 distance = -1

#             distances.append(distance)

#         for i in range(len(front)):
#             for j in range(0, len(front) - i - 1):
#                 if distances[j] > distances[j + 1]:
#                     temp_front[j], temp_front[j + 1] = temp_front[j + 1], temp_front[j]
#                     distances[j], distances[j + 1] = distances[j + 1], distances[j]

#         return temp_front
#     else:
#         return front


# def sort_queue(queue):
#     if queue:
#         # temp_front = front
#         distances = []

#         for i in range(len(queue)):

#             temp_queue = queue

#             base = queue[i][-1]

#             platform_pos = -1
#             empty_pos = 0

#             for j in range(1, len(base)):
#                 if base[j][0] == 'P' and base[j][1] == 'NO' and platform_pos == -1:
#                     platform_pos = j % 2 + j // 2

#                 if base[j][0] == 'E':
#                     empty_pos = j // 2 + j % 2

#             if platform_pos != -1:
#                 distance = abs(platform_pos - empty_pos)
#             else:
#                 distance = -1

#             distances.append(distance)

#         for i in range(len(queue)):
#             for j in range(0, len(queue) - i - 1):
#                 if distances[j] > distances[j + 1]:
#                     temp_queue[j], temp_queue[j + 1] = temp_queue[j + 1], temp_queue[j]
#                     distances[j], distances[j + 1] = distances[j + 1], distances[j]

#         return temp_queue
#     else:
#         return queue


# """" ----------------------------------------------------------------------------
# ** Executing the code
# ** κλήση εκτέλεσης κώδικα
# """


# def main():
#     initial_state = [3, ['E', 'NO'], ['P1', 'NO'], ['P2', 'NO'], ['P3', 'NO']]
#     # goal = [0, ['P1', 'YES'], ['P2', 'YES'], ['P3', 'YES'], ['E', 'NO']]
#     method = 'BestFS'

#     """ ----------------------------------------------------------------------------
#     **** starting search
#     **** έναρξη αναζήτησης
#     """

#     # dfs_search_recursive_front(initial_state, [], [['',''],['',''],['',''],['p','']], 'DFS')
#     print('____BEGIN__SEARCHING____')
#     # find_solution(make_front(initial_state), [], goal, method)

#     find_solution(make_front(initial_state), make_queue(initial_state), [], method)

#     print("--- %s seconds ---" % (time.time() - start_time))

#     # find_solution(make_front(initial_state), [],  method)


# if __name__ == "__main__":
#     main()

# Importing necessary libraries
import copy
import sys
import time

# Setting recursion limit and starting time
sys.setrecursionlimit(10 ** 6)
start_time = time.time()

# Definition of parking spaces and initial state
spaces = {
    1: [2, 4],
    2: [1, 3],
    3: [2, 4],
    4: [1, 3],
}

initial_state = [3, ['E', 'NO'], ['P1', 'NO'], ['P2', 'NO'], ['P3', 'NO']]

# Definition of operators (e.g., entering a car, moving platforms)
# These are functions that modify the state
def enter(state):
    # Entering a car into an empty platform at the entrance
    if state[0] != 0 and state[1][0][0] == 'P' and state[1][1] == 'NO':
        new_state = [state[0] - 1] + [[state[1][0], 'YES']] + state[2:]
        return new_state

def swap(state_l, i, j):
    # Helper function to swap elements in a list
    state_l[i], state_l[j] = state_l[j], state_l[i]
    return state_l

def neighbour1(state):
    # Moving the 1st platform adjacent to an empty space
    elem = ['E', 'NO']
    i = state.index(elem) if elem in state else -1
    if i >= 0:
        swap(state, i, spaces[i][0])
        return state

def neighbour2(state):
    # Moving the 2nd platform adjacent to an empty space
    elem = ['E', 'NO']
    i = state.index(elem) if elem in state else -1
    if i >= 0:
        swap(state, i, spaces[i][1])
        return state

def find_children(state):
    # Generating child states by applying operators
    children = []
    enter_state = copy.deepcopy(state)
    enter_child = enter(enter_state)
    tr1_state = copy.deepcopy(state)
    tr1_child = neighbour1(tr1_state)
    tr2_state = copy.deepcopy(state)
    tr2_child = neighbour2(tr2_state)

    if tr1_child is not None:
        children.append(tr1_child)
    if tr2_child is not None:
        children.append(tr2_child)
    if enter_child is not None:
        children.append(enter_child)

    return children

# Initialization of the front (used in the search process)
def make_front(state):
    return [state]

# Expanding the front (DFS, BFS, BestFS)
def expand_front(front, method):
    # Implementation of different search methods
    if method == 'DFS':
        if front:
            node = front.pop(0)
            for child in find_children(node):
                front.insert(0, child)
    elif method == 'BFS':
        if front:
            node = front.pop(0)
            for child in find_children(node):
                front.append(child)
    elif method == 'BestFS':
        if front:
            node = front.pop(0)
            for child in find_children(node):
                front.insert(0, child)
            front = sort_front(front)  # Sorting the front
    return front

# Initialization of the queue (used in the search process)
def make_queue(state):
    return [[state]]

# Expanding the queue (DFS, BFS, BestFS)
def extend_queue(queue, method):
    # Implementation of different search methods
    if method == 'DFS':
        node = queue.pop(0)
        queue_copy = copy.deepcopy(queue)
        children = find_children(node[-1])
        for child in children:
            path = copy.deepcopy(node)
            path.append(child)
            queue_copy.insert(0, path)
    elif method == 'BFS':
        node = queue.pop(0)
        queue_copy = copy.deepcopy(queue)
        children = find_children(node[-1])
        for child in children:
            path = copy.deepcopy(node)
            path.append(child)
            queue_copy.append(path)
    elif method == 'BestFS':
        node = queue.pop(0)
        queue_copy = copy.deepcopy(queue)
        children = find_children(node[-1])
        for child in children:
            path = copy.deepcopy(node)
            path.append(child)
            queue_copy.insert(0, path)
        queue_copy = sort_queue(queue_copy)  # Sorting the queue
    return queue_copy

# Recursive function for finding the solution
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
        front_children = expand_front(front_copy, method)
        queue_copy = copy.deepcopy(queue)
        queue_children = extend_queue(queue_copy, method)
        closed_copy = copy.deepcopy(closed)
        find_solution(front_children, queue_children, closed_copy, method)

# Sorting the front based on distances
def sort_front(front):
    if front:
        temp_front = front
        distances = []

        for i in range(len(front)):
            platform_pos = -1
            empty_pos = 0
            for j in range(1, len(front[i])):
                if front[i][j][0][0] == 'P' and front[i][j][1] == 'NO' and platform_pos == -1:
                    platform_pos = j % 2 + j // 2
                if front[i][j][0] == 'E':
                    empty_pos = j // 2 + j % 2
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

# Sorting the queue based on distances
def sort_queue(queue):
    if queue:
        distances = []

        for i in range(len(queue)):
            base = queue[i][-1]
            platform_pos = -1
            empty_pos = 0
            for j in range(1, len(base)):
                if base[j][0
