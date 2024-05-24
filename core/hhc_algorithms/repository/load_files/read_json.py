import json

def read_jsons(path_file: str):
    array_objects = []
    try:
        with open(path_file) as file:
            # Parse the JSON array items one by one
            array_objects = json.load(file)
            file.close()
    except FileNotFoundError as fnf:
        print(f'The file {path_file} was not found.')
    except Exception as e:
        print(f'Error occurred: {e}')
    return array_objects





