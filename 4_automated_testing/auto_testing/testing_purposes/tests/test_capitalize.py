from capitalize import capitalize

if capitalize('hello') != 'Hello':
    raise Exception('Function is not working correctly!')

if capitalize('') != '':
    raise Exception('Function is not working correctly!')

print('All tests are passed')

