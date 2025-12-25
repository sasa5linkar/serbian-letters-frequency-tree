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

┌── И: 20 (5.87%)
├── I: 19 (5.57%)
├── A: 17 (4.99%)
├── E: 16 (4.69%)
├── T: 16 (4.69%)
├── S: 15 (4.40%)
├── Е: 15 (4.40%)
├── С: 15 (4.40%)
├── А: 14 (4.11%)
├── Т: 13 (3.81%)
├── O: 10 (2.93%)
├── К: 10 (2.93%)
├── О: 10 (2.93%)
├── Р: 10 (2.93%)
├── K: 9 (2.64%)
├── R: 9 (2.64%)
├── L: 7 (2.05%)
├── M: 7 (2.05%)
├── М: 7 (2.05%)
├── N: 6 (1.76%)
├── Л: 6 (1.76%)
├── P: 5 (1.47%)
├── Z: 5 (1.47%)
├── В: 5 (1.47%)
├── З: 5 (1.47%)
├── Н: 5 (1.47%)
├── U: 4 (1.17%)
├── V: 4 (1.17%)
├── Č: 4 (1.17%)
├── П: 4 (1.17%)
├── У: 4 (1.17%)
├── B: 3 (0.88%)
├── H: 3 (0.88%)
├── J: 3 (0.88%)
├── Ž: 3 (0.88%)
├── Ј: 3 (0.88%)
├── Ж: 3 (0.88%)
├── Ч: 3 (0.88%)
├── Ш: 3 (0.88%)
├── D: 2 (0.59%)
├── Š: 2 (0.59%)
├── Ћ: 2 (0.59%)
├── C: 1 (0.29%)
├── Dž: 1 (0.29%)
├── F: 1 (0.29%)
├── Lj: 1 (0.29%)
├── Nj: 1 (0.29%)
├── Ć: 1 (0.29%)
├── Đ: 1 (0.29%)
├── Ђ: 1 (0.29%)
├── Љ: 1 (0.29%)
├── Њ: 1 (0.29%)
├── Џ: 1 (0.29%)
├── Б: 1 (0.29%)
├── Д: 1 (0.29%)
├── Ф: 1 (0.29%)
└── Ц: 1 (0.29%)
```

## How It Works

1. **Letter Extraction**: The program scans the input text and extracts all Serbian letters, properly handling multi-character letters like Lj, Nj, Dž (Latin) and Љ, Њ, Џ (Cyrillic).

2. **Frequency Calculation**: Counts occurrences of each letter (case-insensitive) and calculates percentages.

3. **Tree Generation**: Creates an ASCII tree visualization with letters sorted by frequency in descending order (most frequent at the top).

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