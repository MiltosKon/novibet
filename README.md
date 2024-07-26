
## Description
This project first scrapes soccer match information, including team names and start times, from the live schedule page. It then checks the live betting page to ensure that these matches appear on time.

## Installation

```bash
git clone https://github.com/MiltosKon/novibet.git
cd novibet
python -m venv .venv #optional 
pip install -r requirements.txt
```

## Usage
Running main.py will start a continuous process that will keep running indefinitely until you manually stop it. During this time, a JSON report (for internal project use) and an XML report will be continuously generated and stored in the data directory. Additionally, a screenshot will be taken and saved in the event of a failure.
```bash
python main.py
```
