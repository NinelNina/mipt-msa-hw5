import requests
#from line_profiler import profile
from memory_profiler import profile


@profile
def batch_generator(file_obj, size):
    batch = set()
    for line in file_obj:
        word = line.strip()
        if word:
            batch.add(word)
        if len(batch) >= size:
            yield batch
            batch = set()
    if batch:
        yield batch


@profile
def count_batch_frequencies(words_from_text, words_to_find):
    frequencies = {word: 0 for word in words_to_find}
    for word in words_from_text:
        if word in frequencies:
            frequencies[word] += 1

    return frequencies


@profile
def get_text(url):
    try:
        response = requests.get(url)
        return response.text
    except Exception as e:
        print(f"Error loading text: {e}")
        raise


@profile
def main():
    words_file = "words.txt"
    url = "https://eng.mipt.ru/why-mipt/"
    batch_size = 100

    try:
        text = get_text(url).lower()
        words_from_text = [word.strip() for word in text.split()]
        all_frequencies = {}

        with open(words_file, 'r', encoding='utf-8') as file:
            for i, batch in enumerate(batch_generator(file, batch_size), 1):
                batch_results = count_batch_frequencies(words_from_text, batch)
                all_frequencies.update(batch_results)

        all_frequencies = dict(sorted(all_frequencies.items(), key=lambda item: item[1], reverse=True))
        print(all_frequencies)

    except FileNotFoundError:
        print(f"Error: file '{words_file}' not found.")
    except PermissionError:
        print(f"Error: permission for reading '{words_file}' denied.")
    except UnicodeDecodeError as e:
        print(f"Error decoding '{words_file}': {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()