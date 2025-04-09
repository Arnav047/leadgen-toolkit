#!/usr/bin/env python
# coding: utf-8

# In[29]:


from googlesearch import search
import time
import csv


# In[30]:


def get_linkedin_url(company_name):
    query = f"{company_name} site:linkedin.com/company"
    try:
        for result in search(query, num_results=10):
            if "linkedin.com/company" in result:
                return result.split("?")[0]
    except Exception as e:
        return f"Error: {str(e)}"
    return "Not found"

def save_to_csv(companies, filename="linkedin_urls.csv"):
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Company", "LinkedIn URL"])
        for company in companies:
            url = get_linkedin_url(company)
            print(f"{company} → {url}")
            writer.writerow([company, url])
            time.sleep(1)



# In[31]:


if __name__ == "__main__":
    companies = ["Oracle", "Deloitte", "NVIDIA", "Google"]
    save_to_csv(companies)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[32]:


import streamlit as st
import pandas as pd
import requests
from googlesearch import search
from urllib.parse import urlparse
import time


# In[33]:


def get_linkedin_url(company_name):
    query = f"{company_name} site:linkedin.com/company"
    try:
        for result in search(query, num_results=10):
            if "linkedin.com/company" in result:
                url = result.split("?")[0]
                if validate_linkedin_url(url):
                    return url
    except Exception as e:
        return f"Error: {str(e)}"
    return "Not found"

def validate_linkedin_url(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0"
        }
        response = requests.get(url, headers=headers, timeout=5)
        return response.status_code == 200
    except:
        return False



# In[34]:


st.title("🔍 LinkedIn Company Finder Tool")
st.write("Upload a CSV file with a column named `Company`, and we'll fetch their LinkedIn URLs.")

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    if "Company" not in df.columns:
        st.error("CSV must contain a 'Company' column.")
    else:
        st.success(f"Found {len(df)} companies.")
        if st.button("🔎 Find LinkedIn URLs"):
            results = []
            with st.spinner("Searching for LinkedIn URLs..."):
                for i, row in df.iterrows():
                    company = row["Company"]
                    url = get_linkedin_url(company)
                    results.append(url)
                    time.sleep(1)
            
            df["LinkedIn URL"] = results
            st.success("Done! 🎉")
            st.write(df)

            csv_download = df.to_csv(index=False).encode("utf-8")
            st.download_button(
                label="📥 Download Results CSV",
                data=csv_download,
                file_name="linkedin_results.csv",
                mime="text/csv"
            )


# In[ ]:





# In[ ]:




