# BRACU-Lost-and-Found

To upload your "BRACU Lost and Found" website to GitHub and run it on your university lab PC, follow these steps:

### 1. **Create a GitHub Repository**
   - **Sign in to GitHub**: Go to [github.com](https://github.com) and sign in or create a new account.
   - **Create a new repository**:
     - On your GitHub homepage, click the `+` icon in the top right corner and select **New repository**.
     - Name your repository (e.g., `BRACU-Lost-and-Found`).
     - Choose whether to make it public or private.
     - Click **Create repository**.

### 2. **Set Up Git on Your Local Machine (University Lab PC)**
   - **Install Git**: If Git is not installed, download and install it from [git-scm.com](https://git-scm.com).
   - **Configure Git**: Open the terminal (or Git Bash) and configure your Git settings.
     ```bash
     git config --global user.name "Your Name"
     git config --global user.email "your.email@example.com"
     ```

### 3. **Initialize Git in Your Project Directory**
   - Navigate to your project folder (the directory containing `backend` and `frontend`) using the terminal.
     ```bash
     cd /path/to/your/project
     ```
   - Initialize a Git repository in your project:
     ```bash
     git init
     ```

### 4. **Add Your Project Files to Git**
   - Stage all files for the commit:
     ```bash
     git add .
     ```
   - Commit your changes:
     ```bash
     git commit -m "Initial commit of BRACU Lost and Found project"
     ```

### 5. **Link Your Local Repository to GitHub**
   - Add the GitHub repository URL as a remote:
     ```bash
     git remote add origin https://github.com/your-username/BRACU-Lost-and-Found.git
     ```

### 6. **Push Your Code to GitHub**
   - Push your local code to the GitHub repository:
     ```bash
     git push -u origin master
     ```

### 7. **Run the Project on the University Lab PC**

To run your project on the university lab PC, follow these steps:

#### 7.1 **Clone the Repository on the Lab PC**
   - On the university PC, install Git if it's not installed.
   - Clone your repository from GitHub:
     ```bash
     git clone https://github.com/your-username/BRACU-Lost-and-Found.git
     ```

#### 7.2 **Set Up the Backend (Flask)**
   - Navigate to the `backend` directory:
     ```bash
     cd BRACU-Lost-and-Found/backend
     ```
   - **Set up a virtual environment**:
     ```bash
     python -m venv venv
     ```
   - **Activate the virtual environment**:
     - On Windows:
       ```bash
       venv\Scripts\activate
       ```
     - On macOS/Linux:
       ```bash
       source venv/bin/activate
       ```
   - **Install the required dependencies**:
     ```bash
     pip install -r requirements.txt
     ```
   - **Run the Flask app** (if `app.py` is your entry point):
     ```bash
     python app.py
     ```


### 7. **Access the Application**
   - **Backend**: If you're running the Flask app, it will be accessible at `http://localhost:5000` or another port if configured differently.
   - **Frontend**: The React app will be accessible at `http://localhost:3000`.

With these steps, you can upload your project to GitHub and run it on the university PC. Let me know if you need further assistance!
