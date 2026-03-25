# Профилирование

Исходная программа работает в 275163 раза дольше, чем оптимизированная (1761.68s VS 0.0064023s).<br>
Пиковое потребление памяти снижено с 37.9 MiB до 35.1 MiB. Количество аллокаций снижено с 7865 до 3216.

# По времени:
## После оптимизации
Wrote profile results to 'main.py.lprof'<br>
Timer unit: 1e-06 s

Total time: 0.0064023 s<br>
File: main.py<br>
Function: batch_generator at line 5

Line # |     Hits     |    Time | Per Hit  | % Time |  Line Contents
==============================================================
     5                                           @profile
     6                                           def batch_generator(file_obj, size):
     7         1          1.6      1.6      0.0      batch = set()
     8      7867       1210.8      0.2     18.9      for line in file_obj:
     9      7866       1447.2      0.2     22.6          word = line.strip()
    10      7866        731.9      0.1     11.4          if word:
    11      7866       1631.7      0.2     25.5              batch.add(word)
    12      7866       1378.8      0.2     21.5          if len(batch) >= size:
    13                                                       yield batch
    14                                                       batch = set()
    15         1          0.1      0.1      0.0      if batch:
    16         1          0.2      0.2      0.0          yield batch

Total time: 0.0006741 s<br>
File: main.py<br>
Function: count_batch_frequencies at line 19

Line # |     Hits     |    Time | Per Hit  | % Time |  Line Contents
==============================================================
    19                                           @profile
    20                                           def count_batch_frequencies(words_from_text, words_to_find):
    21         1         14.0     14.0      2.1      frequencies = {word: 0 for word in words_to_find}
    22      3216        225.9      0.1     33.5      for word in words_from_text:
    23      3215        342.4      0.1     50.8          if word in frequencies:
    24       632         91.7      0.1     13.6              frequencies[word] += 1
    25
    26         1          0.1      0.1      0.0      return frequencies

Total time: 0.228065 s<br>
File: main.py<br>
Function: get_text at line 29

Line # |     Hits     |    Time | Per Hit  | % Time |  Line Contents
==============================================================
    29                                           @profile
    30                                           def get_text(url):
    31         1          0.1      0.1      0.0      try:
    32         1     228025.2 228025.2    100.0          response = requests.get(url)
    33         1         39.5     39.5      0.0          return response.text
    34                                               except Exception as e:
    35                                                   print(f"Error loading text: {e}")
    36                                                   raise
    60                                               except PermissionError:
    61                                                   print(f"Error: permission for reading '{words_file}' denied.")
    62                                               except UnicodeDecodeError as e:
    63                                                   print(f"Error decoding '{words_file}': {e}")
    64                                               except Exception as e:
    65                                                   print(f"Unexpected error: {e}")


## До оптимизации
Total time: 1761.68 s<br>
File: main_old.py<br>
Function: get_text at line 5

Line # |     Hits     |    Time | Per Hit  | % Time |  Line Contents
==============================================================
     5                                           @profile
     6                                           def get_text(url):
     7      7866 1761539709.5 223943.5    100.0      response = requests.get(url)
     8      7866     141147.9     17.9      0.0      return response.text

Total time: 1773.28 s<br>
File: main_old.py<br>
Function: count_word_frequencies at line 11

Line # |     Hits     |    Time | Per Hit  | % Time |  Line Contents
==============================================================
    11                                           @profile
    12                                           def count_word_frequencies(url, word):
    13      7866 1767729355.1 224730.4     99.7      text = get_text(url)
    14      7866    1150141.4    146.2      0.1      words = text.split()
    15      7866       1697.4      0.2      0.0      count = 0
    16  25297056    1888803.6      0.1      0.1      for w in words:
    17  25289190    2506512.9      0.1      0.1          if w == word:
    18     51042       6137.0      0.1      0.0              count += 1
    19      7866        762.9      0.1      0.0      return count

Total time: 1775.66 s<br>
File: main_old.py<br>
Function: main at line 22

Line # |     Hits     |    Time | Per Hit  | % Time |  Line Contents
==============================================================
    22                                           @profile
    23                                           def main():
    24         1          1.0      1.0      0.0      words_file = "words.txt"
    25         1          0.1      0.1      0.0      url = "https://eng.mipt.ru/why-mipt/"
    26
    27         1          0.1      0.1      0.0      words_to_count = []
    28         2         56.7     28.4      0.0      with open(words_file, 'r') as file:
    29      7867       1020.4      0.1      0.0          for line in file:
    30      7866       1098.7      0.1      0.0              word = line.strip()
    31      7866        635.0      0.1      0.0              if word:
    32      7866       1136.7      0.1      0.0                  words_to_count.append(word)
    33
    34         1          0.2      0.2      0.0      frequencies = {}
    35      7867       2983.7      0.4      0.0      for word in words_to_count:
    36      7866 1775653577.6 225737.8    100.0          frequencies[word] = count_word_frequencies(url, word)
    37
    38         1        342.5    342.5      0.0      print(frequencies)


# По памяти:
## После оптимизации

Filename: main.py

Line #  |  Mem usage  |  Increment | Occurrences |  Line Contents
=============================================================
    30     31.6 MiB     31.6 MiB           1   @profile
    31                                         def get_text(url):
    32     31.6 MiB      0.0 MiB           1       try:
    33     35.1 MiB      3.5 MiB           1           response = requests.get(url)
    34     35.1 MiB      0.1 MiB           1           return response.text
    35                                             except Exception as e:
    36                                                 print(f"Error loading text: {e}")
    37                                                 raise


Filename: main.py

Line #  |  Mem usage  |  Increment | Occurrences |  Line Contents
=============================================================
    20     34.6 MiB     34.6 MiB           1   @profile
    21                                         def count_batch_frequencies(words_from_text, words_to_find):
    22     34.6 MiB      0.0 MiB          96       frequencies = {word: 0 for word in words_to_find}
    23     34.6 MiB      0.0 MiB        3216       for word in words_from_text:
    24     34.6 MiB      0.0 MiB        3215           if word in frequencies:
    25     34.6 MiB      0.0 MiB         632               frequencies[word] += 1
    26
    27     34.6 MiB      0.0 MiB           1       return frequencies

Filename: main.py

Line #  |  Mem usage  |  Increment | Occurrences |  Line Contents
=============================================================
    40     31.5 MiB     31.5 MiB           1   @profile
    41                                         def main():
    42     31.5 MiB      0.0 MiB           1       words_file = "words.txt"
    43     31.5 MiB      0.0 MiB           1       url = "https://eng.mipt.ru/why-mipt/"
    44     31.5 MiB      0.0 MiB           1       batch_size = 100
    45
    46     31.5 MiB      0.0 MiB           1       try:
    47     34.8 MiB      3.3 MiB           1           text = get_text(url).lower()
    48     35.1 MiB  -1449.0 MiB        3218           words_from_text = [word.strip() for word in text.split()]
    49     34.6 MiB     -0.5 MiB           1           all_frequencies = {}
    50
    51     34.6 MiB      0.0 MiB           2           with open(words_file, 'r', encoding='utf-8') as file:
    52     34.6 MiB      0.0 MiB           2               for i, batch in enumerate(batch_generator(file, batch_size), 1):
    53     34.6 MiB      0.0 MiB           1                   batch_results = count_batch_frequencies(words_from_text, batch)
    54     34.6 MiB      0.0 MiB           1                   all_frequencies.update(batch_results)
    55
    56     34.6 MiB      0.0 MiB         187           all_frequencies = dict(sorted(all_frequencies.items(), key=lambda item: item[1], reverse=True))
    57     34.6 MiB      0.0 MiB           1           print(all_frequencies)
    58
    59                                             except FileNotFoundError:
    60                                                 print(f"Error: file '{words_file}' not found.")
    61                                             except PermissionError:
    62                                                 print(f"Error: permission for reading '{words_file}' denied.")
    63                                             except UnicodeDecodeError as e:
    64                                                 print(f"Error decoding '{words_file}': {e}")
    65                                             except Exception as e:
    66                                                 print(f"Unexpected error: {e}")

## До оптимизации:


Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     6     37.6 MiB     37.6 MiB           1   @profile
     7                                         def get_text(url):
     8     37.6 MiB      0.0 MiB           1       response = requests.get(url)
     9     37.6 MiB      0.0 MiB           1       return response.text


Filename: main_old.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    12     37.6 MiB     37.6 MiB           1   @profile
    13                                         def count_word_frequencies(url, word):
    14     37.6 MiB      0.0 MiB           1       text = get_text(url)
    15     37.6 MiB      0.0 MiB           1       words = text.split()
    16     37.6 MiB      0.0 MiB           1       count = 0
    17     37.6 MiB      0.0 MiB        3216       for w in words:
    18     37.6 MiB      0.0 MiB        3215           if w == word:
    19                                                     count += 1
    20     37.6 MiB      0.0 MiB           1       return count


Filename: main_old.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    23     31.3 MiB     31.3 MiB           1   @profile
    24                                         def main():
    25     31.3 MiB      0.0 MiB           1       words_file = "words.txt"
    26     31.3 MiB      0.0 MiB           1       url = "https://eng.mipt.ru/why-mipt/"
    27
    30     31.8 MiB      0.0 MiB        7867           for line in file:
    31     31.8 MiB      0.5 MiB        7866               word = line.strip()
    32     31.8 MiB      0.0 MiB        7866               if word:
    33     31.8 MiB      0.1 MiB        7866                   words_to_count.append(word)
    34
    35     31.8 MiB      0.0 MiB           1       frequencies = {}
    36     37.9 MiB  -3153.6 MiB        7867       for word in words_to_count:
    37     37.9 MiB  -3147.5 MiB        7866           frequencies[word] = count_word_frequencies(url, word)
    38
    39     37.6 MiB     -0.3 MiB           1       print(frequencies)
