text = '''
Victor Hugo's ({}) tale of injustice, heroism and love follows the fortunes of Jean Valjean, an escaped convict determined to put his criminal past behind him. But his attempts to become a respected member of the community are constantly put under threat: by his own conscience, when, owing to a case of mistaken identity, another man is arrested in his place; and by the relentless investigations of the dogged Inspector Javert. It is not simply for himself that Valjean must stay free, however, for he has sworn to protect the baby daughter of Fantine, driven to prostitution by poverty. 

Norman Denny's ({}) lively English translation is accompanied by an introduction discussing Hugo's political and artistic aims in writing Les Miserables. 

Victor Hugo (1802-85) wrote volumes of criticism, dramas, satirical verse and political journalism but is best remembered for his novels, especially Notre-Dame de Paris (also known as The Hunchback of Notre-Dame) and Les Miserables, which was adapted into one of the most successful musicals of all time. 

'All human life is here'
Cameron Mackintosh, producer of the musical Les Miserables

'One of the half-dozen greatest novels of the world'
Upton Sinclair

'A great writer - inventive, witty, sly, innovatory' 
A. S. Byatt, author of Possession
'''

name = 'Victor'
word1 = 'writer'
word2 = 'witty'
numbers = "0123456789"
small_letters = 'abcdefghijklmnopqrstuvwxyz'
big_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

name_index = text.find(name)
name_plus3 = text[name_index: name_index+len(name)+3]
word1_index = text.find(word1, 0, 100)
word2_index = text.find(word2, int(len(text)/2), len(text))
count_characters = text.count('of')
is_text_starts_with_name = text.startswith(name)
is_text_ends_with_name = text.endswith(name)
text = text.format('1822-95', '1807-63')
words = text.split(' ')
text1 = ''.join(words)
text2 = ','.join(words)
text3 = '_'.join(words)
text4 = ' '.join(words)
text5 = text.replace('of', '@🐔')
text6 = text.capitalize()
text7 = text.replace('a', '')
text8 = text.strip()

upper_name = name.upper()
lower_name = name.lower()
is_name_upper = name.isupper()
is_name_lower = name.islower()
is_big_letters_upper = big_letters.isupper()
is_small_letters_lower = small_letters.islower()
stringed_integer = '90'.isnumeric()
stringed_float = '90.5'.isnumeric()
converted_int = int('90')
converted_float = float('90.5')
converted_string = str(183)
is_digit = converted_string[1].isdigit()
edges = small_letters[0] + big_letters[-1]
body = numbers[1:-1]
evens = numbers[::2]
odds = numbers[1::2]

print('name', name)
print('word1', word1)
print('word2', word2)
print('numbers', numbers)
print('small_letters', small_letters)
print('big_letters', big_letters)
print('name_index', name_index)
print('name_plus3', name_plus3)
print('word1_index', word1_index)
print('word2_index', word2_index)
print('count_characters -> \'of\' in the text', count_characters)
print('is_text_starts_with_name', is_text_starts_with_name)
print('is_text_ends_with_name', is_text_ends_with_name)
print('\n\n\n\n\n', 'text', text, '\n\n\n\n\n')
print('\n\n\n\n\n', 'words', words, '\n\n\n\n\n')
print('\n\n\n\n\n', 'text1', text1, '\n\n\n\n\n')
print('\n\n\n\n\n', 'text2', text2, '\n\n\n\n\n')
print('\n\n\n\n\n', 'text3', text3, '\n\n\n\n\n')
print('\n\n\n\n\n', 'text4', text4, '\n\n\n\n\n')
print('\n\n\n\n\n', 'text5', text5, '\n\n\n\n\n')
print('\n\n\n\n\n', 'text6', text6, '\n\n\n\n\n')
print('\n\n\n\n\n', 'text7', text7, '\n\n\n\n\n')
print('\n\n\n\n\n', 'text8', text8, '\n\n\n\n\n')
print('upper_name', upper_name)
print('lower_name', lower_name)
print('is_name_upper', is_name_upper)
print('is_name_lower', is_name_lower)
print('is_big_letters_upper', is_big_letters_upper)
print('is_small_letters_lower', is_small_letters_lower)
print('stringed_integer', stringed_integer)
print('stringed_float', stringed_float)
print('converted_int', converted_int)
print('converted_float', converted_float)
print('converted_string', converted_string)
print('is_digit', is_digit)
print('edges', edges)
print('body', body)
print('evens', evens)
print('odds', odds)
