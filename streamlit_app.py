import streamlit as st
from streamlit.components.v1 import html

def generate_email_html(to, name, location, main_url, date, staging_url, manager):
    email_template = f"""
<html>
<body>
<p>Hey <strong>{to} Support</strong>,</p>

<p>I'm reaching out regarding <strong>{name}</strong> in <strong>{location}</strong> (<a href="{main_url}">{main_url}</a>). We are transitioning our website from Dealer Inspire to Dealer.com, with the changeover scheduled for <strong>{date}</strong>.</p>

<p>To ensure a smooth transition, can you confirm if we require updated integration scripts compatible with Dealer.com for our services with you? Our staging site, <a href="{staging_url}">{staging_url}</a>, will switch over to our main website, <a href="{main_url}">{main_url}</a>.</p>

<p>Could you assist with implementing these updates on our staging site (if time permits) for review before we go live? Your prompt support would greatly aid in maintaining uninterrupted service for our customers. Included in this email is <strong>{manager}</strong>, who is our Project Manager at Dealer.com.</p>

<p>Let me know if you need any additional information from {manager} or I!</p>

<p>Thanks in advance!</p>
</body>
</html>
"""
    return email_template

st.title("HTML Email Template Generator for Dealership Website Transition")

third_party = st.text_input("Third Party Name")
dealership_name = st.text_input("Dealership Name")
dealership_location = st.text_input("Dealership Location")
dealership_url = st.text_input("Dealership URL")
switch_over_date = st.text_input("Dealership Switchover Date")
staging_site_url = st.text_input("Dealership Staging Site URL")
project_manager = st.text_input("Project Manager Name")

if st.button("Generate Email"):
    email_html = generate_email_html(third_party, dealership_name, dealership_location, dealership_url, switch_over_date, staging_site_url, project_manager)
    st.text_area("Copy and paste the HTML below into your email client:", email_html, height=300)
    html(email_html)  # Display the formatted HTML for preview
