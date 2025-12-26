-Prerequisites
Ensure the following are installed on the target system:

Python 3.9 or higher
pip (Python package manager)
Git
Verify installation:

python --version
pip --version

-Setup and Execution (Any Machine)
Clone the Repository
git clone https://github.com/sidkumar28/armoriq-mcp-server.git
cd armoriq-mcp-server
cd armoriq-mcp-server

-Create and Activate Virtual Environment
python3 -m venv venv
source venv/bin/activate

Windows
python -m venv venv
source venv/Scripts/activate

Install Dependencies
pip install -r requirements.txt

Run the Server Locally
uvicorn app.main:app --reload

Access API documentation:
http://127.0.0.1:8000/docs

Deployment on Remote / Cloud Machine (EC2)
Start Server with Public Access
uvicorn app.main:app --host 0.0.0.0 --port 8000

Access from browser:
http://65.1.130.135:8000/docs
