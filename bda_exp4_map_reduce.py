import re
from collections import defaultdict

# mapper: convert each word into a key-value pair (word, 1)
# text : str
def mapper(text):
    # use regex to find words, ignoring punctuation and case
    words = re.findall(r"\b[\w']+\b", text.lower())
    
    return [(word, 1) for word in words]


# shuffle and sort: group values by each word
# mapped_data : list[pair[str, int]]
def shuffle(mapped_data):
    # grouped_data : dict[str, list[int]]
    grouped_data = defaultdict(list)

    for word, count in mapped_data:
        grouped_data[word].append(count)
 
    return grouped_data


# reducer: add the counts for each word
# grouped_data : dict[str, list[int]]
def reducer(grouped_data):
    result = {}
    # dict[str, int]
    for word, counts in grouped_data.items():
        result[word] = sum(counts)
    
    return result


if __name__ == "__main__":
    
    text = """
    Hello World
    Hello Python
    World of Python
    """


    mapped_data = mapper(text)
    grouped_data = shuffle(mapped_data)
    word_counts = reducer(grouped_data)

    print("Word Counts:")
    for word, count in sorted(word_counts.items()):
        print(f"{word}: {count}")