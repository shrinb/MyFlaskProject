# MyFlaskProject

Description of the Project:
  ✅This is a Flask web application that provides functionality to retrieve the count of distinct queries based on a given date prefix. 
  ✅The application loads data from a TSV file containing timestamped queries 
  ✅Then allows users to input a date prefix to retrieve the count of distinct queries for that specific date range.

Guidance to Run the Project:
  ✅Clone the repository to your local machine and Make sure you have the following files:
        ⏺ MyApp.py: The main Python file containing the Flask application logic.
        ⏺ Welcome.html: HTML template for the welcome page, where users can input the date prefix.
        ⏺ hn_logs.tsv: Sample TSV file containing timestamped queries
  ✅Make sure you have Python and Flask installed.
  ✅Run MyApp.py using Python.
  ✅Open a web browser and navigate to http://localhost:5000/ to access the welcome page.
  ✅Enter a date prefix in the input field and click "Submit" to retrieve the count of distinct queries for that date range.  

The Idea-To have an input field in welcome page:
  ✅My flask application provides a welcoming interface for users to input their query range and dynamically generates the count of unique queries
                "showcasing an efficient and user-friendly approach to analyzing query data"

Cons of not having an Input field in welcome page:
  ✅An aspect of the previous implementation that presented a challenge was that 
         users were required to manually adjust the route in order to specify their desired query range and output.

Discussing the alternative idea which I have:
  ✅Date Range Picker:
      ⏺ Description: Implement a date range picker component where users can select both start and end dates for their query range.
      ⏺ Pros: Allows users to specify precise date ranges with ease. Enhances user experience by providing a comprehensive selection mechanism.
      ⏺ Cons: Requires more advanced front-end development skills to implement. 
