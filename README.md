Revised Overview for Moodle 4.5 API Integration with Python 3.12 and Streamlit
This project provides a Python script to connect to the Moodle API and perform operations such as retrieving site information and user data.
It uses the REST protocol for communication with the Moodle instance.

Overview
1. Follow the Steps to Enable Moodle Web Services
For detailed setup instructions, refer to the official Moodle Web Services Overview documentation.
These steps ensure your Moodle instance is properly configured for API usage.

MOODLE_API_TOKEN: A token generated for the web service user to authenticate API requests.
2. Enable the Required Functions
Make sure the following API functions are enabled in the Moodle Web Services configuration:

core_webservice_get_site_info
gradereport_user_get_grade_items
mod_assign_get_assignments
core_course_create_courses
core_course_get_courses_by_field
core_user_get_users
core_user_get_users_by_field
core_course_get_courses
core_user_view_user_list
Additionally, you can customize and add new functions if needed.

Installation
Clone this repository:

bash
Copy
Edit
git clone https://github.com/pdiaz-commits/python-apimoodle
cd moodle-api-python
Create and activate a virtual environment:

bash
Copy
Edit
# On Linux/Mac
python -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate
Install the required Python libraries:

bash
Copy
Edit
pip install -r requirements.txt
Configuration
Set the following environment variables in your system (recommended for production environments):

MOODLE_BASE_URL: The base URL of your Moodle instance (e.g., https://your-moodle-site.com).
MOODLE_API_TOKEN: The token generated for the web service user.
Alternatively, for quick testing, you can set these values directly in the script (not recommended for production use).

Usage
1. Open in a Browser
After configuring and running the project, access the Streamlit app through your browser. Examples:

https://your_domain:8502

2. Running the Streamlit App
If the project includes a Streamlit app, you can start it as follows:

Ensure the virtual environment is activated.
Run the app using:
bash
Copy
Edit
streamlit run app_name.py
Replace app_name.py with the actual filename of your Streamlit app.
Contributing
Feel free to fork this repository, contribute new features, or submit pull requests to fix issues or enhance functionality.

License
This project is licensed under the MIT License. See the LICENSE file for more details.
