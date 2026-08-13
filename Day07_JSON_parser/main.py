index = 0
with open("./test.json") as f:
    lines = f.readlines()
    content = ""
    for line in lines:
        content += line.strip().strip('\n')

special_char_lookup = {
    "n": "\n",
    '"': '"',
    "/": "/",
    "b": "\b",
    "f": "\f",
    "r": "\r",
    "t": "\t",
    "\\": "\\"
}

def parse_list():
    global index, content
    index += 1
    result = []
    while index < len(content):
        next_character = content[index]

        if next_character == ']':
            index += 1
            break
        elif next_character == ',':
            index += 1
            continue

        list_value = parse_sequence()
        result.append(list_value)
    return result

def parse_object():
    global index, content
    index += 1
    result = {}
    while index < len(content):
        next_character = content[index]

        if next_character == '}':
            index += 1
            break
        elif next_character == ',':
            index += 1
            continue

        key = parse_sequence()
        index += 1
        value = parse_sequence()
        result[key] = value
    return result

def parse_string():
    global index, content
    result = ''
    index += 1

    while index < len(content):
        next_character = content[index]

        if next_character == '"':
            index += 1
            break
        elif next_character == '\\':
            special = special_char_lookup.get(content[index+1])
            if special is not None:
                result += special
                index += 2
            else:
                result += str("\\")
                index += 1
        else:
            result += next_character
            index += 1

    return result

def parse_number():
    global index, content
    result = ""
    while index < len(content):
        next_character = content[index]

        if not next_character.isnumeric() and next_character != '.':
            break

        result += next_character
        index += 1

    result = float(result)
    
    return int(result) if result.is_integer() else result

def parse_true():
    global index, content

    index += 4
    return True

def parse_false():
    global index, content

    index += 5
    return False

def parse_null():
    global index, content

    index += 4
    return False

def parse_sequence():
    global index, content
    character = content[index]

    if character == '[':
        return parse_list()
    elif character == '{':
        return parse_object()
    elif character == '"':
        return parse_string()
    elif character == 'f':
        return parse_false()
    elif character == 't':
        return parse_true()
    elif character == 'n':
        return parse_null()
    elif character == ' ':
        index += 1
        return parse_sequence()
    else:
        return parse_number()

def main():
    sequence = parse_sequence()
    print(sequence)

if __name__ == "__main__":
    main()