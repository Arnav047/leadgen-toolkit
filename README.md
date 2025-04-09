# leadgen-toolkit

This repository contains two lightweight tools designed to support lead generation and outreach research, inspired by the core ideas behind GetCohesiveAI’s scraping platform. The tools are built for speed and simplicity, allowing users to access publicly available intelligence on company hiring trends and professional LinkedIn profiles using streamlined interfaces and minimal dependencies.

The first tool, titled LinkedIn Account Finder, enables users to input a company name (via a CSV file) and receive a list of likely LinkedIn URLs for those companie. It uses a pre-existing dataset named companies.csv which contains sample company entries. The tool helps users—especially those involved in outreach or research—quickly identify and access company LinkedIn profiles. As an added feature, the tool also provides the option to download a CSV file that contains the LinkedIn URLs for all input companies, making it easier to document, share, or further analyze the collected data. This functionality can assist users in identifying professionals for networking, sales outreach, or candidate research.

The second tool, called Job Role Analyzer, takes a company name as input and scrapes real-time job openings from publicly accessible platforms like Lever and Greenhouse. It focuses on identifying opportunities in AI, data, and sales-related departments and presents job titles, departments, and locations in a clean tabular format. This offers users valuable hiring insights to assess whether a company is in a growth phase or open to product/service pitches in specific areas.

Each tool is implemented as a separate Streamlit application and can be run independently from the terminal. The design emphasizes practical, time-sensitive development with clear outputs relevant for recruiters, students, or sales professionals.

Setup Instructions
Clone this repository to your local machine:
git clone https://github.com/Arnav047/leadgen-toolkit.git

Navigate to the project folder:
cd leadgen-toolkit

pip install -r requirements.txt

Run the tools using the command line:

To launch the LinkedIn Account Finder tool:
streamlit run app.py

To launch the Job Role Analyzer tool:
streamlit run tool2LinkedinPerson.py

Ensure that the companies.csv file is placed in the same directory as app.py for proper execution.

Dataset Usage
The companies.csv file is used solely for the LinkedIn Account Finder tool to simulate company-specific employee profile lookups. This dataset includes example company names to demonstrate functionality and guide the search mechanism. It does not store any personal data or scraped information.

