Moodle API Integration with Python

Overview

This project provides a Python script to connect to the Moodle API and perform operations such as retrieving site information and user data. It uses the REST protocol for communication with the Moodle instance.

Requirements

Before using the script, ensure that the following are enabled and configured in your Moodle instance:

Enable Web Services: Web services must be enabled in the Advanced Features settings of Moodle.

Enable Protocols: At least one protocol (e.g., REST) must be enabled.

Create a Specific User: Create a dedicated user for web service operations.

Check User Capability: Assign the necessary capabilities (webservice/rest:use, etc.) to the user.

Select a Service: Define a service with the required functions and authorize the user to access it.

Add Functions: Add the required functions to the service (e.g., core_webservice_get_site_info, core_user_get_users).

Select a Specific User: Authorize the specific user to access the service.

Create a Token: Generate a token for the web service user to authenticate API requests.

Enable Developer Documentation: Enable developer documentation for web services in Moodle.

Test the Service: Test the API endpoints to ensure proper functionality.

Steps to Enable Moodle Web Services

Refer to the Moodle documentation for detailed steps: Moodle Web Services Overview.

Installation

Clone this repository:

git clone https://github.com/yourusername/moodle-api-python.git
cd moodle-api-python

Create and activate a virtual environment:

python -m venv venv

# On Linux/Mac
source venv/bin/activate

# On Windows
venv\Scripts\activate

Install the required Python libraries:

pip install -r requirements.txt

Configuration

Set the following environment variables in your system:

MOODLE_BASE_URL: The base URL of your Moodle instance (e.g., http://your-moodle-site.com).

MOODLE_API_TOKEN: The token generated for the web service user.

Alternatively, you can directly set these values in the script (not recommended for production environments).

Usage

Get Site Information

Retrieve basic information about your Moodle site:

from moodle_api_user_list import test_site_info

info = test_site_info()
print(info)

Get a List of Users

Retrieve a list of users with optional search criteria:

from moodle_api_user_list import get_users

# Fetch all users
all_users = get_users()
print(all_users)

# Fetch users with specific criteria
specific_users = get_users(criteria=[{'key': 'email', 'value': 'user@example.com'}])
print(specific_users)

Running the Streamlit App

If the project includes a Streamlit app, you can run it as follows:

Ensure the virtual environment is activated:

# On Linux/Mac
source venv/bin/activate

# On Windows
venv\Scripts\activate

Run the Streamlit app:

streamlit run app_name.py

Replace app_name.py with the actual filename of your Streamlit app.

Contributing

Feel free to fork this repository and submit pull requests for new features or bug fixes.

License

This project is licensed under the MIT License - see the LICENSE file for details.
