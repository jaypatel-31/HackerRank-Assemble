import streamlit as st
import requests
import base64
import pandas as pd
from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

# Constants
GREENHOUSE_API_KEY = os.getenv('GREENHOUSE_API_KEY')
token = os.getenv('TOKEN')

GREENHOUSE_API_URL = 'https://harvest.greenhouse.io/v1/candidates'  # Endpoint for candidates

# Encoding the API Key with a colon appended
encoded_api_key = base64.b64encode(f'{GREENHOUSE_API_KEY}:'.encode('utf-8')).decode('utf-8')

# Headers for authentication
headers = {
    'Authorization': f'Basic {encoded_api_key}',
    'Content-Type': 'application/json'
}

def get_candidates(email):
    params = {'email': email}
    response = requests.get(GREENHOUSE_API_URL, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f'Error fetching data from Greenhouse: {response.status_code}, Response: {response.text}')
        return None

def extract_candidate_info(candidate_json):
    candidate_info = {}

    # Extract LinkedIn URL from answers
    for answer in candidate_json.get('applications', [])[0].get('answers', []):
        if answer.get('question') == 'LinkedIn Profile':
            candidate_info['LinkedIn'] = answer.get('answer')

    # Extract Resume URL
    for attachment in candidate_json.get('attachments', []):
        if attachment.get('type') == 'resume':
            candidate_info['Resume'] = attachment.get('url')

    # Extract location from addresses
    addresses = candidate_json.get('addresses', [])
    candidate_info['Locations'] = {
        'Home': next((addr['value'] for addr in addresses if addr['type'] == 'home'), None),
        'Work': next((addr['value'] for addr in addresses if addr['type'] == 'work'), None)
    }

    return candidate_info
    
def get_candidates(job_id=None, email=None):
    params = {}
    if job_id:
        params['job_id'] = job_id
    if email:
        params['email'] = email

    response = requests.get(GREENHOUSE_API_URL, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f'Error fetching data: {response.status_code}, Response: {response.text}')



def get_all_user(test_id, limit):
    get_candidate_url = f"https://www.hackerrank.com/x/api/v3/tests/{test_id}/candidates?limit={limit}&offset=1&c=completed&sort=percentage_score"
    
    #token = "abc"
    headers = {
        'Authorization': token
    }
    response = requests.get(get_candidate_url, headers=headers)
    return response.json()

def generate_candidate_link(candidate_uuid, role_id):
    #return f"https://www.hackerrank.com/work/packet/timeline?candidate_id={candidate_uuid}&role_id={role_id}"
    return f"https://www.hackerrank.com/work/packet/profile?candidate_id={candidate_uuid}&role_id={role_id}"


def main():
    st.title("HackerRank Assemble | Internship Project - Jay")

    # Sidebar for input controls
    with st.sidebar:
        st.header("Configuration")
        # Input for HackerRank Test ID
        test_id = st.text_input("Enter HackerRank Test ID:", value="1665990")  # Default value for easier testing
        # Input for Greenhouse Job ID
        job_id = st.text_input("Enter Greenhouse Job ID:", value="2653468")  # Default value for easier testing
        limit = st.number_input("Enter Limit:", min_value=1, value=10)  # Default value for easier testing

    # Main content
    if st.button("Fetch Data"):
        api_response = get_all_user(test_id, limit)
        candidates = []
        #print(api_response)
        for candidate in api_response['data']:
            candidate_uuid = candidate['candidate_uuid']
            link = generate_candidate_link(candidate_uuid, 'efe6c4a0f9f1')  # Role ID hardcoded as per instructions
            candidate_email = candidate['email']

            # Fetching data from Greenhouse
            greenhouse_data = get_candidates(job_id=job_id, email=candidate_email)
            if greenhouse_data:
                greenhouse_info = extract_candidate_info(greenhouse_data[0])  # Assuming the first match is the correct one
            else:
                greenhouse_info = {'LinkedIn': None, 'Resume': None}

            candidates.append({
                'Full Name': candidate['full_name'],
                'Email': candidate_email,
                'Score': candidate['score'],
                'Link': f'<a href="{link}" target="_blank">Link</a>' if link else 'Not available',
                'LinkedIn': f'<a href="{greenhouse_info.get("LinkedIn")}" target="_blank">LinkedIn</a>' if greenhouse_info.get('LinkedIn') else 'Not available',
                'Resume': f'<a href="{greenhouse_info.get("Resume")}" target="_blank">Resume</a>' if greenhouse_info.get('Resume') else 'Not available',
            })
        # Convert to DataFrame
        df = pd.DataFrame(candidates)

        # Custom Styling
        st.markdown("""
        <style>
        .dataframe th {
            background-color: #0169f9;
            color: white;
            text-align: left;
        }
        .dataframe td {
            text-align: left;
        }
        </style>
        """, unsafe_allow_html=True)

        # Render as HTML
        st.markdown(df.to_html(escape=False, index=False), unsafe_allow_html=True)

if __name__ == "__main__":
    main()
