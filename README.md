# Essay Craft ✍️

## About ℹ️

Essay Craft is an AI-powered application designed to assist users in crafting insightful essay roadmaps effortlessly. Whether you need to analyze an essay or create a structured roadmap for essay writing, Essay Craft provides powerful tools to streamline your writing process.

Check out this YouTube video to see EssayCraft in action: [EssayCraft Demo](https://youtu.be/v5EXeqmfHRY)

## Tech Stack 🛠️

Essay Craft is built using the following technologies:

- Python 🐍
- Flask 🌐
- HTML 📄
- CSS (including Tailwind CSS for styling) 🎨
- JavaScript (minimal for frontend interactions) 🖥️
- JSON (for data storage) 🗃️
- Mindsdb (for connecting to llm provided by mdb.ai) 🧠


## How to Use 🚀

1. **Install Docker and MindsDB**:
   - Follow the MindsDB Docker installation guide: [Setup MindsDB with Docker](https://docs.mindsdb.com/setup/self-hosted/docker).
   - Ensure Docker is installed on your system.

2. **Get API Key from mdb.ai**:
   - Obtain an API key from [mdb.ai](https://mdb.ai).
   - Create a `.env` file in the project root and add your MindsDB API key.


3. **Set Up Python Virtual Environment**:
   - Create and activate a virtual environment (recommended):

     ```sh
     python -m venv venv
     source venv/bin/activate  # On Windows use `venv\Scripts\activate`
     ```

4. **Install Dependencies**:
   - Install required Python packages from `requirements.txt`:

     ```sh
     pip install -r requirements.txt
     ```

5. **Run Setup Script**:
   - Run `setup.py` script to set up the database and any initial configurations:

     ```sh
     python mindsdb_setup.py
     ```

6. **Run the Application**:
   - Start the Flask application:

     ```sh
     python app.py
     ```

7. **Access the Application**:
   - Open a web browser and go to [http://127.0.0.1:5000](http://127.0.0.1:5000) to access the quiz app.
   - Explore and try out different quizzes!

## Star if You Like ⭐

If you find Essay Craft useful, consider giving it a star on GitHub! Your support means a lot.

## Connect with Me 🌐

- GitHub: [Your GitHub Profile](https://github.com/IrfanshaikH-7)
- LinkedIn: [Your LinkedIn Profile](https://www.linkedin.com/in/irfanshaikh-n7)
# EssayCraft
