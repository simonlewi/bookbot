# BookBot
BookBot is my first [Boot.dev](https://www.boot.dev) project!

## Features

- Counts total number of words in a text file
- Performs character frequency analysis
- Displays results in a formatted console output

## Usage

```bash
python3 main.py <path_to_book>
```

Example output:
```
============ BOOKBOT ============
Analyzing book found at book.txt
----------- Word Count ----------
Found 1234 total words
--------- Character Count -------
a: 400
t: 300
s: 250
============= END ===============
```

## Requirements

- Python 3.x

## Project Structure

- [`main.py`](main.py) - Main program entry point
- [`stats.py`](stats.py) - Contains word and character counting logic

## Getting Started

1. Clone this repository
2. Prepare a text file you want to analyze
3. Run the program with your text file as argument:
   ```bash
   python3 main.py path/to/your/book.txt
   ```

## Error Handling

The program will display usage instructions if no file path is provided.
