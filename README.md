Moodle 4.5 API Integration with Python 3.12 and Streamlit

Overview

This project provides a Python script to connect to the Moodle API and perform operations such as retrieving site information and user data. 
It uses the REST protocol for communication with the Moodle instance.

1.-Follow the Steps to Enable Moodle Web Services
              For detailed setup instructions, refer to the official Moodle Web Services Overview documentation. 
              These steps ensure your Moodle instance is properly configured for API usage.
             
              MOODLE_API_TOKEN: The token generated for the web service user.

              Enable the Funtions  : 
              
                    core_webservice_get_site_info	
                    gradereport_user_get_grade_items	
                    mod_assign_get_assignments	
                    core_course_create_courses	
                    core_course_get_courses_by_field	
                    core_user_get_users	
                    core_user_get_users_by_field	
                    core_course_get_courses	
                    core_user_view_user_list	

              (Add amd customized new ones)



Installation

Clone this repository:

git clone https://github.com/pdiaz-commits/python-apimoodle

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

Go to your browser and open Exmaple : http://localhost:8502/


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


