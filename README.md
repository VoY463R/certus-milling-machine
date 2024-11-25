# Fuel cells mapping and milling process

## Description

The tool responsible for automating the milling and mapping process using the Certus milling machine.

## Installation

1. Clone the repository to your local machine:
```bash
git clone https://github.com/VoY463R/certus-milling-machine.git
```
2. Navigate to the project folder:
```bash
cd your-project
```
3. Install the dependencies:
```bash
pip install -r requirements.txt
```
4. Run the project:
```bash
python app.py
```

## Usage

After launching, first determine the position of the mouse cursor where it should go when the “Map” or “Milling” button is pressed first.<br>
Then name the first fuel cell.<br>
**Example**:
```markdown
a8-1
```
Next, choose whether you want to deal with the “Top” or “Bot” side. **You can only choose one of these options at a time!**<br>At the very end, generate a list of links using the “Generate DFC List” button.

## Testing
To run unit tests use the following command:
```bash
pytest
```