import json
from match import Match

def main():

    # Aquire json file from command line
    try:
        data = input()
    except EOFError:
        print('Input not valid. Please try again.')
        return

    # Regularize JSON data
    data = data.replace("'", '"')

    # Convert JSON to python dictionary
    try:
        data = json.loads(data)
    except json.JSONDecodeError:
        print('Please provide a valid JSON file.')
        return


    # Instantiate match object
    match = Match(data)

    # Perform match operations
    match.processInput()    
    match.createGraph()

    # Output result
    match.printMatches()

if __name__ == '__main__':
    main()