# Serbian Letters Frequency Tree 🌳

A Python application that analyzes the frequency of Serbian letters (both Cyrillic and Latin alphabets) in text and generates an ASCII tree visualization showing letters sorted by their occurrence frequency.

## Features

- ✅ Support for both Serbian Cyrillic and Latin alphabets
- ✅ Proper handling of multi-character letters (Lj, Nj, Dž in Latin; Љ, Њ, Џ in Cyrillic)
- ✅ Case-insensitive analysis
- ✅ Beautiful ASCII tree visualization
- ✅ Displays both count and percentage for each letter
- ✅ Flexible input methods (file, stdin, or direct string)
- ✅ Command-line interface with customizable output file

## Serbian Alphabets

### Cyrillic Alphabet (30 letters)
```
А, Б, В, Г, Д, Ђ, Е, Ж, З, И, Ј, К, Л, Љ, М, Н, Њ, О, П, Р, С, Т, Ћ, У, Ф, Х, Ц, Ч, Џ, Ш
```

### Latin Alphabet (30 letters)
```
A, B, C, Č, Ć, D, Dž, Đ, E, F, G, H, I, J, K, L, Lj, M, N, Nj, O, P, R, S, Š, T, U, V, Z, Ž
```

## Installation

This project uses only Python standard library, so no additional dependencies are required.

**Requirements:**
- Python 3.6 or higher

**Clone the repository:**
```bash
git clone https://github.com/sasa5linkar/serbian-letters-frequency-tree.git
cd serbian-letters-frequency-tree
```

## Usage

### Basic Usage

**Analyze a text file:**
```bash
python serbian_frequency.py input.txt
```
This will create `frequency_tree.txt` with the results.

**Specify custom output file:**
```bash
python serbian_frequency.py input.txt output.txt
```

**Read from stdin:**
```bash
cat input.txt | python serbian_frequency.py
# or
echo "Текст на српском" | python serbian_frequency.py
# or
python serbian_frequency.py < input.txt
```

**Interactive input (type or paste text, then press Ctrl+D):**
```bash
python serbian_frequency.py
```

### Command-Line Options

```bash
python serbian_frequency.py --help
```

Output:
```
usage: serbian_frequency.py [-h] [input_file] [output_file]

Analyze Serbian letter frequencies and generate an ASCII tree visualization.

positional arguments:
  input_file   Input text file (optional, defaults to stdin)
  output_file  Output file for the ASCII tree (default: frequency_tree.txt)

options:
  -h, --help   show this help message and exit
```

## Example

### Input Text (`example_input.txt`)

```
Пример текста на српском језику са ћириличним писмом.
Овај текст садржи различите српске слове као што су Ђ, Ж, Љ, Њ, Ћ, Џ и Ш.
Фреквенција слова у тексту може бити корисна за различите анализе.

Primer teksta na srpskom jeziku sa latiničnim pismom.
Ovaj tekst sadrži različite srpske slove kao što su Đ, Č, Ć, Š, Ž, Lj, Nj i Dž.
Frekvencija slova u tekstu može biti korisna za različite analize.

Мешовити текст / Mixed text with both alphabets.
```

### Output Tree (`frequency_tree.txt`)

```
Serbian Letter Frequency Tree
==================================================

Total Serbian letters: 341
  Cyrillic: 165
  Latin: 176

Cyrillic Letter Frequency Tree
============================================================
Total: 165 letters

                            *
                           /|\
                          / | \
                         /  |  \

                         / И (20, 12.1%) \
                           Е (15, 9.1%)
                          ~ С (15, 9.1%) ~
                         / А (14, 8.5%) \
                           Т (13, 7.9%)
                          ~ К (10, 6.1%) ~
                         / О (10, 6.1%) \
                        Р (10, 6.1%)
                       ~ М (7, 4.2%) ~
                      / Л (6, 3.6%) \
                        В (5, 3.0%)
                       ~ З (5, 3.0%) ~
                      / Н (5, 3.0%) \
                        П (4, 2.4%)
                    ~ У (4, 2.4%) ~
                   / Ј (3, 1.8%) \
                     Ж (3, 1.8%)
                    ~ Ч (3, 1.8%) ~
                   / Ш (3, 1.8%) \
                     Ћ (2, 1.2%)
                    ~ Ђ (1, 0.6%) ~
                      / Љ (1, 0.6%) \
                        Њ (1, 0.6%)
                       ~ Џ (1, 0.6%) ~
                      / Б (1, 0.6%) \
                        Д (1, 0.6%)
                       ~ Ф (1, 0.6%) ~
                      / Ц (1, 0.6%) \

                           |||
                           |||
                           |||
                         =======

Latin Letter Frequency Tree
============================================================
Total: 176 letters

                            *
                           /|\
                          / | \
                         /  |  \

                         / I (19, 10.8%) \
                           A (17, 9.7%)
                          ~ E (16, 9.1%) ~
                         / T (16, 9.1%) \
                           S (15, 8.5%)
                          ~ O (10, 5.7%) ~
                         / K (9, 5.1%) \
                        R (9, 5.1%)
                       ~ L (7, 4.0%) ~
                      / M (7, 4.0%) \
                        N (6, 3.4%)
                       ~ P (5, 2.8%) ~
                      / Z (5, 2.8%) \
                        U (4, 2.3%)
                    ~ V (4, 2.3%) ~
                   / Č (4, 2.3%) \
                     B (3, 1.7%)
                    ~ H (3, 1.7%) ~
                   / J (3, 1.7%) \
                     Ž (3, 1.7%)
                    ~ D (2, 1.1%) ~
                      / Š (2, 1.1%) \
                        C (1, 0.6%)
                       ~ Dž (1, 0.6%) ~
                      / F (1, 0.6%) \
                        Lj (1, 0.6%)
                       ~ Nj (1, 0.6%) ~
                      / Ć (1, 0.6%) \
                        Đ (1, 0.6%)

                           |||
                           |||
                           |||
                         =======
```

**Note:** The output displays decorative ASCII trees - one for Cyrillic letters and one for Latin letters. Letters are arranged by frequency from top (most frequent) to bottom (least frequent), creating a visual tree shape. Each letter shows its count and percentage within its alphabet.

## How It Works

1. **Letter Extraction**: The program scans the input text and extracts all Serbian letters, properly handling multi-character letters like Lj, Nj, Dž (Latin) and Љ, Њ, Џ (Cyrillic). Letters are separated into Cyrillic and Latin groups.

2. **Frequency Calculation**: Counts occurrences of each letter within its alphabet (case-insensitive) and calculates percentages relative to the total letters in that alphabet.

3. **Tree Generation**: Creates a decorative ASCII tree visualization with two separate sections - one for Cyrillic letters and one for Latin letters. Each tree displays letters arranged by frequency from top (most frequent) to bottom (least frequent), creating a visual tree shape with decorative branches.

4. **Output**: Saves the tree to a file and displays it in the console.

## Edge Cases Handled

- **Empty input**: Displays a message indicating no text was provided
- **No Serbian letters found**: Shows appropriate message when input contains no Serbian letters
- **Mixed alphabets**: Correctly handles text containing both Cyrillic and Latin Serbian letters
- **File not found**: Provides clear error message if input file doesn't exist
- **I/O errors**: Handles file reading/writing errors gracefully

## Code Structure

The application is organized into modular functions:

- `extract_serbian_letters()`: Extracts Serbian letters from text with proper multi-character handling
- `calculate_frequencies()`: Calculates letter frequencies and percentages
- `generate_ascii_tree()`: Creates the ASCII tree visualization
- `read_input()`: Handles input from files or stdin
- `write_output()`: Writes output to file
- `main()`: Command-line interface and orchestration

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.

## Author

Created by [sasa5linkar](https://github.com/sasa5linkar)

## Acknowledgments

- Inspired by the need to analyze Serbian text efficiently
- Uses Unicode for proper display of Cyrillic and special Latin characters