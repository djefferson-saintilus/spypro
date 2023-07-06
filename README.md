# SpyPro - The Automate
#### Author: *Djefferson Saintilus*
![image](./config/bannerOfficial.svg)

SpyPro automates the pentesting process from reconnaissance to target exploitation. It is designed for CTF (Capture The Flag) challenges and has an educational purpose. Currently, it supports Linux boxes, and it is recommended to keep a manual notebook for all notes and the final report. The tool follows the PTES (Penetration Testing Execution Standard) methodology. It is in English and utilizes the Kali Linux database to load most of the tools.

## Prerequisites
- `python3`

## Supported by:
- `Kali-Linux`
- `Parrot OS`

## Target Audience
- Pentesters
- Hackers
- CTF Players
- Ethical Hackers

## Installation

1. Clone the SpyPro repository:
```
git clone https://github.com/your-username/SpyPro.git
```
2. Install the required dependencies:
```
pip install -r requirements.txt
```
3. Start SpyPro:
```
python main.py
```

## 1. SpyPro v1.0 Features
_______________________________________________________
- OS detection (Linux or Windows) using TTL OS identifier
- Perform a global Nmap scan with version and state on a range of 65335 ports, followed by a targeted Nmap scan based on the previous results.

-- NEW UPDATE -- v1.1
- Web directory enumeration

to be continued ...

## Contributing

Contributions to SpyPro are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.

```
Copyright 2019

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```
