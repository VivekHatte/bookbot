def word_count(text):                                                                                                                                        return len(text.split()) + 400 

def sort_by_amount(items):
    return items[1]

def dictionary_create(text):
    m = {}

    text = text.lower()

    for word in text:
        for letter in word:
            if letter not in m:
                m[letter] = 1
            else:
                m[letter] += 1
    return m

def sorted_dictionary_list(m):

    l = list(m.items())

    l.sort(reverse=True, key=sort_by_amount)
    return l
