def locate_card(cards, query):
    # Create a variable position with the value 0
    position = 0
    
    # Set up a loop for repetition
    while True:
        
        # Check if element at the current position matche the query
        if cards[position] == query:
            
            # Answer found! Return and exit..
            return position
        
        # Increment the position
        position += 1
        
        # Check if we have reached the end of the array
        if position == len(cards):
            
            # Number not found, return -1
            return -1
        



test = {
    'input': { 
        'cards': [13, 11, 10, 7, 4, 3, 1, 0], 
        'query': 7
    },
    'output': 3
}



tests = []

tests.append(test)

tests.append({
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 1
    },
    'output': 6
})

tests.append({
    'input': {
        'cards': [4, 2, 1, -1],
        'query': 4
    },
    'output': 0
})

tests.append({
    'input': {
        'cards': [3, -1, -9, -127],
        'query': -127
    },
    'output': 3
})

tests.append({
    'input': {
        'cards': [6],
        'query': 6
    },
    'output': 0 
})

tests.append({
    'input': {
        'cards': [9, 7, 5, 2, -9],
        'query': 4
    },
    'output': -1
})

tests.append({
    'input': {
        'cards': [],
        'query': 7
    },
    'output': -1
})

tests.append({
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 3
    },
    'output': 7
})

tests.append({
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 6
    },
    'output': 2
})


#for i in range (0,8) :
 #   locate_card(**tests[i]['input']) == tests[i]['output']

# gives error right ? bcz of empty thing 

def locate_card(cards, query):
    position = 0
    while position < len(cards):
        if cards[position] == query:
            return position
        position += 1
    return -1

#for i in range (0,8) :
#    print(locate_card(**tests[i]['input']) == tests[i]['output'])


cards = [12,10,6]
query = 6

print(locate_card(cards=cards,query=query))