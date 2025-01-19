# Author: Pablo Díaz 
# Author: Maintainer (contact: diazpjdr@gmail.com)
# Date: 2025-01-16
# Description: Python script to connect to the Moodle API and retrieve data.
# License: MIT License

import streamlit as st
import pandas as pd
import requests
from pathlib import Path
import matplotlib.pyplot as plt
import plotly.express as px


import os
# Configuration for connecting Moodle API to Python using Streamlit
# Define the environment variables before running the script:
# MOODLE_BASE_URL: The base URL of your Moodle instance (e.g., http://localhost:8200)
# MOODLE_API_TOKEN: Your Moodle API token for authentication

#BASE_URL = os.getenv("MOODLE_BASE_URL")
#TOKEN = os.getenv("MOODLE_API_TOKEN")
#ENDPOINT = f"{BASE_URL}/webservice/rest/server.php"

# Auxiliary function for Moodle API calls
def make_request(function_name, params=None):
    if params is None:
        params = {}
    params.update({
        'wstoken': TOKEN,
        'wsfunction': function_name,
        'moodlewsrestformat': 'json'
    })
    try:
        response = requests.get(ENDPOINT, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

# Function to get site information
def test_site_info():
    """Retrieves basic information about the Moodle site."""
    result = make_request('core_webservice_get_site_info')
    return result

# Función para obtener datos de usuarios

# Function to get a list of users
def get_users(criteria=None):
    """Retrieves a list of users from the Moodle site.

    Args:
        criteria (list, optional): A list of dictionaries containing search criteria.
            Each dictionary should include keys like 'key' and 'value'. For example:
            [{'key': 'email', 'value': 'user@example.com'}].

    Returns:
        dict: The response from the Moodle API.
    """
    params = {}
    if criteria:
        params['criteria'] = criteria
    
    result = make_request('core_view_user_list', params=params)
    return result




# Function to get courses
def get_courses():
    """Retrieves a list of courses from Moodle."""
    return make_request('core_course_get_courses')

# Enhanced interface
def main():
    st.title("Python Streamlit integration Moodle API")
    st.subheader("Extend Moodle 4.5 with an interactive and enhanced interface.")
  

  
    st.markdown("""
    ### Unlocking the Potential of Extending Moodle with Python and Streamlit

    The integration of Moodle's API with Python and Streamlit unlocks transformative workflows, enabling the efficient management and visualization of educational data. By leveraging Python's analytical power and Streamlit's interactive capabilities, developers can create dynamic dashboards, automate report generation, and enhance user experiences in Moodle. This workflow not only demonstrates technical expertise in managing APIs and building custom tools but also highlights the impact of data-driven decision-making in modern education systems. Showcasing this approach in a portfolio emphasizes the potential to innovate and optimize learning platforms, making it a valuable asset for organizations aiming to improve their LMS capabilities.
    """)

    st.text("Extend Moodle with an interactive and enhanced interface.")
   # st.text("Integrate AI into Moodle in a personalized way.")



    # Section: Site Information
    with st.expander("Site Information"):
        if st.button("Load Site Information", key="site_info"):
            result = test_site_info()
            if "error" in result:
                st.error(f"Error: {result['error']}")
            else:
                st.success("Site information retrieved")
                # Display site information in an appealing way
                col1, col2 = st.columns([1, 3])
                with col1:
                    st.image(result.get("userpictureurl", ""), width=100, caption=result.get("fullname", "User"))
                with col2:
                    st.markdown(f"**Site Name:** {result.get('sitename', 'Unknown')}")
                    st.markdown(f"**Administrator:** {result.get('firstname', 'N/A')} {result.get('lastname', 'N/A')} ({result.get('username', 'N/A')})")
                    st.markdown(f"**Language:** {result.get('lang', 'N/A')}")
                    st.markdown(f"**Site URL:** [Visit Site]({result.get('siteurl', '#')})")

                # Available functions
                st.subheader("Available Functions")
                functions = result.get("functions", [])
                if functions:
                    functions_df = pd.DataFrame(functions)
                    st.dataframe(functions_df)
                else:
                    st.warning("No available functions found.")

                # Advanced features
                st.subheader("Advanced Features")
                advanced_features = result.get("advancedfeatures", [])
                if advanced_features:
                    features_df = pd.DataFrame(advanced_features)
                    features_df["Status"] = features_df["value"].apply(lambda x: "Enabled" if x else "Disabled")
                    st.dataframe(features_df[["name", "Status"]])
                else:
                    st.warning("No advanced features found.")

    

    # Section: Courses
    with st.expander("Courses"):
        if st.button("Load Courses", key="courses"):
            result = get_courses()
            if "error" in result:
                st.error(f"Error: {result['error']}")
            else:
                if isinstance(result, list):
                    st.success("Courses successfully retrieved")
                    courses = pd.DataFrame(result)
                    st.dataframe(courses[["id", "fullname", "shortname"]])
                    st.bar_chart(courses.set_index("fullname")["id"])
                else:
                    st.warning("No courses found.")

    with st.expander("Data Analysis"):
        if st.button("Data Analysis", key="Data Analysis"):
          
            result = get_courses()

            if "error" in result:
                st.error(f"Error: {result['error']}")
            else:
                if isinstance(result, list):
                    st.success("Data Analysis successfully retrieved")
                    courses = pd.DataFrame(result)
                    st.dataframe(courses[["id", "fullname", "shortname"]])
                    st.bar_chart(courses.set_index("fullname")["id"])

                    # Gráfico de líneas
                    st.subheader("Line Chart")
                    st.line_chart(courses.set_index("fullname")["id"])

                    # Gráfico de área
                    st.subheader("Area Chart")
                    st.area_chart(courses.set_index("fullname")["id"])

                    # Gráfico circular con Matplotlib
                    st.subheader("Pie Chart")
                    fig, ax = plt.subplots()
                    ax.pie(courses["id"], labels=courses["fullname"], autopct='%1.1f%%', startangle=90)
                    ax.axis('equal')  # Para que el gráfico sea un círculo
                    st.pyplot(fig)

                    # Gráfico circular con Plotly
                    st.subheader("Pie Chart (Interactive)")
                    fig = px.pie(courses, values="id", names="fullname", title="Course Distribution")
                    st.plotly_chart(fig)

                    # Gráfico de barras apiladas con Plotly
                    st.subheader("Stacked Bar Chart (Interactive)")
                    fig = px.bar(courses, x="fullname", y="id", title="Courses Bar Chart", text="id")
                    st.plotly_chart(fig)

                    # Gráfico de dispersión (Scatter Plot) con Plotly
                    st.subheader("Scatter Plot (Interactive)")
                    fig = px.scatter(courses, x="fullname", y="id", title="Course ID Scatter Plot", size="id")
                    st.plotly_chart(fig)






                else:
                    st.warning("No Data Analysis found.")      


                    
    with st.expander("Custom reports"):
        if st.button("Custom reports", key="Custom reports"):
         
            result = get_courses()
          
            if "error" in result:
                st.error(f"Error: {result['error']}")
            else:
                if isinstance(result, list):
                    st.success("Custom reports successfully retrieved")
                    courses = pd.DataFrame(result)
                    st.dataframe(courses[["id", "fullname", "shortname"]])
                    st.bar_chart(courses.set_index("fullname")["id"])
                else:
                    st.warning("No Custom reports found.")    

      # Section: Users
    with st.expander("Users"):
        if st.button("Load Users", key="users"):
            result = get_users()
            if "error" in result:
                st.error(f"Error: {result['error']}")
            else:
                if "users" in result:
                    users = pd.DataFrame(result["users"])
                    st.dataframe(users[["id", "firstname", "lastname", "email"]])
                else:
                    st.warning("No users found.")              



    # Section: Monitoring
    with st.expander("System Monitoring"):
        if st.button("Monitor System Activity", key="monitor_activity"):
            result = monitor_system_activity()
            st.json(result)

        if st.button("Check Cron Status", key="cron_status"):
            result = check_cron_status()
            st.json(result)

        if st.button("View System Logs", key="system_logs"):
            result = view_logs()
            st.json(result)

if __name__ == "__main__":
    main()
