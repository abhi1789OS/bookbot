
def main(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    num_words = count_words(file_contents)
    character_count = count_characters(file_contents)
    character_list = []
    for key in character_count:
        character_list.append({"name": key, "count": character_count[key]})
    character_list.sort(reverse=True, key=sort_on)

    print('--- Begin report of {} ---'.format(path_to_file))
    print(f'{num_words} words found in the document\n')

    for char_dict in character_list:
        if char_dict['name'].isalpha():
            print(f"The '{char_dict['name']}' was found {char_dict['count']} times")
    print('--- End report ---')


def count_words(text):
    return len(text.split())


def count_characters(text):
    text = text.lower()
    characters = {}
    for ch in text:
        if ch not in characters:
            characters[ch] = 1
        else:
            characters[ch] += 1
    return characters

def sort_on(character_dict):
    return character_dict['count']

main("books/frankenstein.txt")