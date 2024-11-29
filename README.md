# LeetCode Problem Downloader

A clean LeetCode problem downloader that converts problems from LeetCode China to Markdown format.

## Features

- 🚀 Simple and intuitive GUI
- 📝 Automatically converts to Markdown format
- 🎨 Beautiful Dracula theme
- 👁️ Real-time preview
- 🔄 Supports code block conversion
- 🏷️ Retains problem tags
- 📊 Displays problem difficulty

## Requirements

- Python 3.6+
- PyQt5
- requests
- beautifulsoup4

## Installation

```bash
   pip install -r requirements.txt
```

## Usage

1. Run the program:

```bash
   python main.py
```

2. Enter the problem slug in the input box (e.g., `two-sum`).

3. Click the "Download" button.

4. The Markdown file will be saved automatically in the current directory.

## Example

Entering "two-sum" will download the "两数之和" problem and convert it to Markdown format.

## Project Structure

- main.py: Entry point of the program
- LeetCodeGUI.py: GUI implementation
- LeetCodeCrawler.py: Core crawling logic
- requirements.txt: Project dependencies
- README.md: Project documentation

## License

MIT License

## Notes

- This tool is for learning purposes only.
- Please do not send frequent requests to LeetCode servers.
- Using a VPN or proxy is recommended to improve access speed.
