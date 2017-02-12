# GOGS Key scraper
This little utility scrapes user public keys from a GOGS git server.

Install it so:
```bash
git clone https://github.com/sasha42/key-scraper.git
cd key-scraper
pip install -r requirements.txt
```

Run it so:
```bash
python key-scraper.py
```

You can set the base URL of your git whilst running the utility, or in advance by exporting an environment variable:
```bash
export BASE_URL="https://git.example.com"
```

### Limitations
This is a tiny tool that I quickly built up to solve a problem. No guarantees are made, us at own risk.

The biggest issue you'll probably face is that your GOGS installation has a slightly different layout and breaks the multi-page stuff. You can fix it by tweaking the number on line 30.
