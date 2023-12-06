# HackerRank Assemble

HackerRank Assemble is a recruitment facilitation tool hosted on Streamlit Cloud, designed to streamline the process of aggregating candidate information from Greenhouse and HackerRank.


## Features

- **Greenhouse Integration**: Fetch LinkedIn and resume URLs using Greenhouse Job IDs.
- **HackerRank Integration**: Retrieve candidate details using HackerRank Test IDs.
- **Custom Data Retrieval**: Specify the number of entries for tailored data analysis.

## Quick Start

1. Access the platform on Streamlit Cloud: [HackerRank Assemble URL](https://code-wizard-hogwarts-hr-intern-project1-app.streamlit.app/)
 
2. Enter Greenhouse Job ID, HackerRank Test ID, and the number of entries.

3. View and analyze candidate data seamlessly.

## Getting Started


These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software:

- Python 3
- pip

### Installation

1. **Clone the Repository**

    ```bash
    git clone https://github.com/jaypatel-31/HackerRank-Assemble.git
    cd HackerRank-Assemble
    ```

2. **Set Up a Virtual Environment** (Optional, but recommended)

    - For Windows:
        ```bash
        python -m venv venv
        venv\Scripts\activate
        ```

    - For macOS and Linux:
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```

3. **Install Required Packages**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set Up Environment Variables**

    - Create a new `.env` file in the root directory of your project:

        ```bash
        touch .env
        ```

    - Open the `.env` file in a text editor and add your API keys and tokens:

        ```plaintext
        GREENHOUSE_API_KEY=your_greenhouse_api_key_here
        TOKEN=your_token_here
        ```

        Replace `your_greenhouse_api_key_here` and `your_token_here` with your actual API key and token values.

    **Important**: Ensure `.env` is added to your `.gitignore` file to keep these secrets out of version control.

5. **Run the Application**

    ```bash
    streamlit run app.py
    ```

    This command will start the Streamlit server, and the app should be accessible via a web browser at the address provided in the terminal.

