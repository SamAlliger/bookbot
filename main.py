def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(f"--- Begin report of {f} ---")
        print(f"{word_count(file_contents)} words found in the document")
        sorted_count = character_count(file_contents)
        for character in sorted_count:
            # Characters you want to exclude from the result go here
            ignored_characters = [" ", "\n"]
            if character["character"] not in ignored_characters:
                print(f"The '{character["character"]}' character was found {character["counter"]} times")
        print("--- End report ---")
        
# Count of words in the provided file
def word_count(file):
    # Get a list of words from text, then the length of that list
    return len(file.split())

# List with chracter/counter pairs of all characters in the provided file
def character_count(file):
    # Convert to lowercase to avoid duplication
    lowercase_file = file.lower()
    # Fill dictionary with characters if they don't exist, otherwise increment the appropriate count
    counts = {}
    for character in lowercase_file:
        if character in counts:
            counts[character] += 1
        else:
            counts[character] = 1
    # Move character/count pairs to a list for sorting
    sortable_counts = []
    for count in counts:
        sortable_counts.append({"character": count, "counter": counts[count]})
    # Doing the actual sorting, see sort_on function for the key
    sortable_counts.sort(reverse=True, key=sort_on)
    return sortable_counts

# Sorting function for character_count
def sort_on(sortable_counts):
    return sortable_counts["counter"]

main()