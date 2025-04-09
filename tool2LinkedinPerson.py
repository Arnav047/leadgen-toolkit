#!/usr/bin/env python
# coding: utf-8

# In[8]:


import streamlit as st
import requests
import pandas as pd


# In[9]:


def get_lever_jobs(company):
    try:
        url = f"https://api.lever.co/v0/postings/{company}?mode=json"
        response = requests.get(url)
        if response.status_code == 200:
            jobs = response.json()
            return [{
                "Title": job.get("text", ""),
                "Location": job.get("categories", {}).get("location", ""),
                "Department": job.get("categories", {}).get("team", ""),
                "Commitment": job.get("categories", {}).get("commitment", ""),
                "URL": job.get("hostedUrl", "")
            } for job in jobs]
    except:
        return []
    return []

def get_greenhouse_jobs(company):
    try:
        url = f"https://boards-api.greenhouse.io/v1/boards/{company}/jobs"
        response = requests.get(url)
        if response.status_code == 200:
            jobs = response.json().get("jobs", [])
            return [{
                "Title": job.get("title", ""),
                "Location": job.get("location", {}).get("name", ""),
                "Department": job.get("departments", [{}])[0].get("name", "") if job.get("departments") else "",
                "Commitment": "",
                "URL": job.get("absolute_url", "")
            } for job in jobs]
    except:
        return []
    return []

def is_relevant(title):
    keywords = ["data", "ai", "ml", "machine learning", "artificial intelligence", "sales", "analytics"]
    return any(k in title.lower() for k in keywords)



# In[10]:


st.set_page_config(page_title="Job Role Analyzer", layout="wide")
st.title("Job Role Analyzer")
st.markdown("Search job openings across Lever & Greenhouse for AI/Data/Sales roles.")

company_input = st.text_input("Enter Company Slug (e.g., openai, notion, databricks):")

if company_input:
    st.info(f"Searching for job postings at **{company_input}**...")

    lever = get_lever_jobs(company_input)
    greenhouse = get_greenhouse_jobs(company_input)

    all_jobs = lever + greenhouse
    df = pd.DataFrame(all_jobs)

    if not df.empty:
        df["Relevant"] = df["Title"].apply(is_relevant)
        filter_roles = st.checkbox("Show only AI/Data/Sales roles", value=True)

        if filter_roles:
            df = df[df["Relevant"]]

        st.success(f"Found {len(df)} job(s).")
        st.dataframe(df.drop(columns=["Relevant"]), use_container_width=True)
    else:
        st.error("No jobs found on Lever or Greenhouse.")


# In[ ]:




