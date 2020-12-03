# CroSiteSpellCheck
Python script to spell check croatian websites.
The script iterates through all internal links of a website and checks for spelling and grammar errors using [Hašek](https://ispravi.me/).

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install selenium, BeautifulSoup, requests, html2text.
Download and install latest gecko webdriver for your platform - https://github.com/mozilla/geckodriver/releases.
```bash
pip install -r requirements.txt
```

## Usage
Add gecko driver dir to your path.

```bash
python3 spc.py "https://link_to_a_croatian_website.hr/"
```

## Contributing


## License

