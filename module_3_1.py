calls = 0

def count_calls():
    global calls
    calls = calls +1
    #print(calls)

def string_info(string):
    a = (len(string), string.upper(), string.lower())
    count_calls()
    return a

def is_contains(string, list_to_search):
    count_calls()
    for i in list_to_search:
        if i.lower() == string.lower():
            return True
    return False





print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)