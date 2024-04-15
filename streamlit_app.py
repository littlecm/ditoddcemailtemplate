import streamlit as st

def generate_email(to, name, location, main_url, date, staging_url, manager):
    email_template = f"""
Hey {to} Support,

I'm reaching out regarding {name} in {location} ({main_url}). We are transitioning our website from Dealer Inspire to Dealer.com, with the changeover scheduled for {date}.

To ensure a smooth transition, can you confirm if we require updated integration scripts compatible with Dealer.com for our services with you? Our staging site, {staging_url}, will switch over to our main website, {main_url}.

Could you assist with implementing these updates on our staging site (if time permits) for review before we go live? Your prompt support would greatly aid in maintaining uninterrupted service for our customers. Included in this email is {manager}, who is our Project Manager at Dealer.com.

Let me know if you need any additional information from {manager} or I!

Thanks in advance!
"""
    return email_template

st.title("Email Template Generator for Dealership Website Transition")

third_party = st.text_input("Third Party Name")
dealership_name = st.text_input("Dealership Name")
dealership_location = st.text_input("Dealership Location")
dealership_url = st.text_input("Dealership URL")
switch_over_date = st.text_input("Dealership Switchover Date")
staging_site_url = st.text_input("Dealership Staging Site URL")
project_manager = st.text_input("Project Manager Name")

if st.button("Generate Email"):
    email = generate_email(third_party, dealership_name, dealership_location, dealership_url, switch_over_date, staging_site_url, project_manager)
    st.text_area("Copy the email template below:", email, height=300)
