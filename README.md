# Email Forensic Tool (Python)

A tool that quickly parses through `.eml` files and says if the given email is spoofed or not. It also gives the user necessary information like sender's IP address and Message IDs. It can be useful for forensic analysts who need to analyze large EML files quickly or can be used by a non-technical person who can't understand RAW EML data.

## Features

- Detects spoofed emails from `.eml` files  
- Extracts sender's IP address  
- Displays Message IDs  
- Fast parsing for large EML datasets  
- Simple for non-technical users  

## Installation

Clone the repository:

```bash
git clone https://github.com/REVEAL1001/Email-Forensic-Tool-Python.git
cd Email-Forensic-Tool-Python
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Place your `.eml` files in the working directory.

Run the tool:

```bash
python main.py
```

Follow the instructions in the terminal to analyze your EML files.

## Example Output

```
Sender's IP Address: 192.168.1.1  
Message ID: <12345@example.com>  
Spoofed: Yes
```

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License

MIT

## Author
Sambardhan Khanal
[REVEAL1001](https://github.com/REVEAL1001)


