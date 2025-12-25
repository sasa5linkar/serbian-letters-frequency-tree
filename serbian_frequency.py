#!/usr/bin/env python3
"""
Serbian Letters Frequency Tree
Analyzes Serbian text (Cyrillic and Latin) and generates an ASCII tree visualization
showing letter frequencies sorted by occurrence.
"""

import sys
import argparse
from collections import Counter
from typing import Dict, List, Tuple


# Serbian alphabets (single-character letters only)
# Note: Multi-character letters (Dž, Lj, Nj) are handled separately below
SERBIAN_CYRILLIC = [
    'А', 'Б', 'В', 'Г', 'Д', 'Ђ', 'Е', 'Ж', 'З', 'И', 'Ј', 'К', 'Л', 'Љ',
    'М', 'Н', 'Њ', 'О', 'П', 'Р', 'С', 'Т', 'Ћ', 'У', 'Ф', 'Х', 'Ц', 'Ч',
    'Џ', 'Ш'
]

SERBIAN_LATIN = [
    'A', 'B', 'C', 'Č', 'Ć', 'D', 'Đ', 'E', 'F', 'G', 'H', 'I', 'J',
    'K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'Š', 'T', 'U', 'V',
    'Z', 'Ž'
]

# Multi-character letters for proper matching (must be checked first)
# Note: After uppercase, Latin digraphs become DŽ, LJ, NJ (both chars uppercase)
# We normalize them back to Dž, Lj, Nj for consistent display
MULTI_CHAR_LATIN_UPPER = ['DŽ', 'LJ', 'NJ']
MULTI_CHAR_LATIN_ORIGINAL = ['Dž', 'Lj', 'Nj']
MULTI_CHAR_CYRILLIC = ['Љ', 'Њ', 'Џ']


def normalize_text(text: str) -> str:
    """Convert text to uppercase for case-insensitive comparison."""
    return text.upper()


def extract_serbian_letters(text: str) -> Tuple[List[str], List[str]]:
    """
    Extract Serbian letters from text, properly handling multi-character letters.
    Separates Cyrillic and Latin letters.
    
    Args:
        text: Input text to analyze
        
    Returns:
        Tuple of (cyrillic_letters, latin_letters)
    """
    text = normalize_text(text)
    cyrillic_letters = []
    latin_letters = []
    i = 0
    
    while i < len(text):
        matched = False
        
        # Check for multi-character letters first (2 characters)
        if i + 1 < len(text):
            two_char = text[i:i+2]
            if two_char in MULTI_CHAR_CYRILLIC:
                cyrillic_letters.append(two_char)
                i += 2
                matched = True
                continue
            elif two_char in MULTI_CHAR_LATIN_UPPER:
                # Normalize DŽ, LJ, NJ to Dž, Lj, Nj for display
                if two_char == 'DŽ':
                    latin_letters.append('Dž')
                elif two_char == 'LJ':
                    latin_letters.append('Lj')
                elif two_char == 'NJ':
                    latin_letters.append('Nj')
                else:
                    # Should never reach here, but keep for safety
                    latin_letters.append(two_char)
                i += 2
                matched = True
                continue
        
        # Check for single-character letters
        if not matched:
            char = text[i]
            if char in SERBIAN_CYRILLIC:
                cyrillic_letters.append(char)
            elif char in SERBIAN_LATIN:
                latin_letters.append(char)
            i += 1
    
    return cyrillic_letters, latin_letters


def calculate_frequencies(letters: List[str]) -> List[Tuple[str, int, float]]:
    """
    Calculate frequency of each letter.
    
    Args:
        letters: List of letters to analyze
        
    Returns:
        List of tuples (letter, count, percentage) sorted by frequency (descending)
    """
    if not letters:
        return []
    
    counter = Counter(letters)
    total = len(letters)
    
    # Create list of (letter, count, percentage) and sort by count descending
    frequencies = [
        (letter, count, (count / total) * 100)
        for letter, count in counter.items()
    ]
    
    # Sort by count (descending), then by letter (ascending) for ties
    frequencies.sort(key=lambda x: (-x[1], x[0]))
    
    return frequencies


def generate_ascii_tree(frequencies: List[Tuple[str, int, float]], alphabet_name: str = "") -> str:
    """
    Generate ASCII tree visualization of letter frequencies.
    
    Args:
        frequencies: List of tuples (letter, count, percentage)
        alphabet_name: Name of the alphabet (e.g., "Cyrillic", "Latin")
        
    Returns:
        String containing ASCII tree representation
    """
    if not frequencies:
        return ""
    
    lines = []
    
    if alphabet_name:
        lines.append(f"{alphabet_name} Letters")
        lines.append("-" * 50)
    
    total_letters = sum(count for _, count, _ in frequencies)
    lines.append(f"Total: {total_letters}")
    lines.append("")
    
    # Generate tree structure
    for idx, (letter, count, percentage) in enumerate(frequencies):
        is_last = (idx == len(frequencies) - 1)
        
        if idx == 0:
            # Root of the tree
            prefix = "┌── "
            continuation = ""
        elif is_last:
            # Last item
            prefix = "└── "
            continuation = "    "
        else:
            # Middle items
            prefix = "├── "
            continuation = "│   "
        
        # Format the letter entry
        line = f"{prefix}{letter}: {count} ({percentage:.2f}%)"
        lines.append(line)
    
    return "\n".join(lines) + "\n"


def generate_combined_tree(cyrillic_freq: List[Tuple[str, int, float]], 
                          latin_freq: List[Tuple[str, int, float]]) -> str:
    """
    Generate combined ASCII tree with separate sections for Cyrillic and Latin.
    
    Args:
        cyrillic_freq: List of tuples (letter, count, percentage) for Cyrillic
        latin_freq: List of tuples (letter, count, percentage) for Latin
        
    Returns:
        String containing combined ASCII tree representation
    """
    lines = []
    lines.append("Serbian Letter Frequency Tree")
    lines.append("=" * 50)
    lines.append("")
    
    total_cyrillic = sum(count for _, count, _ in cyrillic_freq) if cyrillic_freq else 0
    total_latin = sum(count for _, count, _ in latin_freq) if latin_freq else 0
    total_all = total_cyrillic + total_latin
    
    if total_all == 0:
        return "No Serbian letters found in the input text.\n"
    
    lines.append(f"Total Serbian letters: {total_all}")
    lines.append(f"  Cyrillic: {total_cyrillic}")
    lines.append(f"  Latin: {total_latin}")
    lines.append("")
    
    # Generate Cyrillic tree
    if cyrillic_freq:
        cyrillic_tree = generate_ascii_tree(cyrillic_freq, "Cyrillic")
        lines.append(cyrillic_tree)
    
    # Generate Latin tree
    if latin_freq:
        latin_tree = generate_ascii_tree(latin_freq, "Latin")
        lines.append(latin_tree)
    
    return "\n".join(lines)


def read_input(input_source: str = None) -> str:
    """
    Read input text from file, string, or stdin.
    
    Args:
        input_source: File path or None for stdin
        
    Returns:
        Input text as string
    """
    if input_source:
        try:
            with open(input_source, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            print(f"Error: File '{input_source}' not found.", file=sys.stderr)
            sys.exit(1)
        except IOError as e:
            print(f"Error reading file '{input_source}': {e}", file=sys.stderr)
            sys.exit(1)
    else:
        # Read from stdin
        return sys.stdin.read()


def write_output(content: str, output_file: str):
    """
    Write content to output file.
    
    Args:
        content: Text to write
        output_file: Output file path
    """
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Output written to: {output_file}")
    except IOError as e:
        print(f"Error writing to file '{output_file}': {e}", file=sys.stderr)
        sys.exit(1)


def main():
    """Main function to run the Serbian letter frequency analyzer."""
    parser = argparse.ArgumentParser(
        description='Analyze Serbian letter frequencies and generate an ASCII tree visualization.',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s input.txt                    # Read from input.txt, write to frequency_tree.txt
  %(prog)s input.txt output.txt         # Read from input.txt, write to output.txt
  cat input.txt | %(prog)s              # Read from stdin, write to frequency_tree.txt
  %(prog)s                              # Read from stdin, write to frequency_tree.txt
        """
    )
    
    parser.add_argument(
        'input_file',
        nargs='?',
        help='Input text file (optional, defaults to stdin)'
    )
    
    parser.add_argument(
        'output_file',
        nargs='?',
        default='frequency_tree.txt',
        help='Output file for the ASCII tree (default: frequency_tree.txt)'
    )
    
    args = parser.parse_args()
    
    # Read input
    try:
        text = read_input(args.input_file)
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.", file=sys.stderr)
        sys.exit(1)
    
    # Handle empty input
    if not text.strip():
        print("Warning: Input text is empty.", file=sys.stderr)
        tree = "No text provided.\n"
    else:
        # Extract Serbian letters (separated by alphabet)
        cyrillic_letters, latin_letters = extract_serbian_letters(text)
        
        # Calculate frequencies for each alphabet
        cyrillic_freq = calculate_frequencies(cyrillic_letters)
        latin_freq = calculate_frequencies(latin_letters)
        
        # Generate combined ASCII tree
        tree = generate_combined_tree(cyrillic_freq, latin_freq)
    
    # Write output
    write_output(tree, args.output_file)
    
    # Also print to console
    print("\n" + tree)


if __name__ == "__main__":
    main()
