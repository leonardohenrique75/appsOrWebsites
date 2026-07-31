Game Catalog
A simple personal game catalog built with Python and Streamlit. It displays games, their platforms, genres, completion status, ratings, and cover images.
Features
•	Browse a personal game collection
•	Filter games by system, genre, and status
•	Search games by name
•	View game cover images
•	Run as a web interface with Streamlit
•	Includes an optional desktop interface built with Tkinter
Requirements
•	Python 3.10 or later
•	Dependencies listed in requirements.txt
Installation
Clone this repository and enter the project directory:
git clone https://github.com/YOUR-USERNAME/game-catalog.git
cd game-catalog
Install the dependencies:
pip install -r requirements.txt
Run the Web App
streamlit run app.py
Then open the local address shown in your terminal, usually:
http://localhost:8501
Run the Desktop App
python interface.py
Project Structure
app.py           # Streamlit web application
interface.py     # Tkinter desktop interface
main.py          # Command-line catalog utilities
games.json       # Game catalog data
games.xlsx       # Optional spreadsheet source
covers/          # Game cover images
Privacy and Security
This project is designed as a read-only catalog. The web interface does not provide file uploads, remote command execution, or access to files outside the project, but you can also edit the JSON file or even use your on Excel (.xlsx) file for having your own database on the file!
By default, Streamlit runs locally. Do not expose the application to the public internet unless you intentionally deploy it through a trusted hosting provider and understand that the displayed catalog data will be public.
Cover Images
Game cover images may be copyrighted and belong to their respective owners. They are included here for personal and educational purposes only. If you publish this repository publicly, make sure you have permission to distribute them, or replace them with original or properly licensed images.
License
Add a license file before accepting contributions or allowing others to reuse the code. The MIT License is a common choice for small open-source projects.

