import json

def extract_keys(filename, *args):
    result = []
    try:
        with open(filename) as f:
            data = json.load(f)
            for arg in args:
                try:
                    result.append(data[arg])
                except KeyError:
                    result.append(None)
                except TypeError:
                    return [None] * len(args)
    except FileNotFoundError:
        print(f'No file {filename}!')
    return result

print(extract_keys('input.json', 'name', 'email', 'post index'))
print(extract_keys('input2.json', 'name', 'email', 'post index'))
