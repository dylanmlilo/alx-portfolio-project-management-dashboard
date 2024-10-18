Nando Construction - Project Management Dashboard
Project Overview

This is a project management dashboard developed for a mock company, Nando Construction. The application allows users to log in with roles assigned to them (such as admin or regular user), providing access to a dashboard that displays important project metrics and data. Administrators have additional functionality to manage data via CRUD operations.

![image](https://github.com/user-attachments/assets/cb761af5-3176-48cd-86dc-fb9d45b2ce32)

![image](https://github.com/user-attachments/assets/552cc2da-24d0-42d5-823b-0753e9619951)

![image](https://github.com/user-attachments/assets/eaf2922f-2795-4fdd-a732-254db1439a99)

![image](https://github.com/user-attachments/assets/02d908bb-16a2-4e78-bd95-1c35fbdcff72)

![image](https://github.com/user-attachments/assets/5e1235ec-77f8-4038-9785-0b8968500b4e)

![image](https://github.com/user-attachments/assets/19c43433-4935-41e4-aa88-168bbbf0d72e)

![image](https://github.com/user-attachments/assets/72c4b994-c2ee-4d2c-b470-10750486b6a0)

![image](https://github.com/user-attachments/assets/a04b3254-4b9c-41b2-ae3c-c88830a970e1)

![image](https://github.com/user-attachments/assets/01fe0b42-de12-46dd-a9da-926d1071c108)

![image](https://github.com/user-attachments/assets/e08bf9f8-f448-4f73-b256-7b79c8b84cd8)

![image](https://github.com/user-attachments/assets/d98d086d-674d-45df-99ea-0d2cbcf083fc)

![image](https://github.com/user-attachments/assets/71b92ffe-90c9-48c2-b0c7-3854c0a984b7)

![image](https://github.com/user-attachments/assets/bed38c99-8a8a-4226-90d0-56fe32b66c40)

![image](https://github.com/user-attachments/assets/888d4f9d-c165-446c-94c7-6fcc56190b7f)

![image](https://github.com/user-attachments/assets/43cbb951-ba56-4f26-b0d3-e9861bc7fd4f)

![image](https://github.com/user-attachments/assets/abda3f4f-ec9d-4802-bb49-e774c60f8e29)

![image](https://github.com/user-attachments/assets/7069708c-0c1e-4c68-8442-10f1e4c4fe05)

![image](https://github.com/user-attachments/assets/e0416b06-5a36-40ec-96c4-6c73f4ce4640)

![image](https://github.com/user-attachments/assets/fb424f2c-5ef9-4db7-93b7-ad8aa898eb3f)

Key Features:

    Mobile Responsive: The dashboard is built with responsiveness in mind, ensuring smooth access and interaction from desktops, tablets, and smartphones.
    User Authentication: Role-based login for users and administrators.
    Admin Dashboard: Allows CRUD operations for project data.
    User Dashboard: Displays dynamic charts and tables for project management.
    Data Visualization: Graphs and tables to monitor project performance and progress.
    API Access: The dashboard can generate secure APIs to allow authorized data analysts to access and analyze the company's projects data for in-depth investigations.

Architecture & Technologies

This project is built using the following technologies:

    Front-end:
        HTML, CSS, JavaScript
        Bootstrap (for responsive UI design)
        Plotly (for interactive charts)
        Datatables (for interactive and dynamic tables)

    Back-end:
        Python Flask (for building the backend API and managing routes)
        MySQL Database (for storing project data)
        Authentication (role-based access control)

Development Report
Successes

    Implemented login functionality with user role authentication using Flask.
    Developed dynamic dashboards using Plotly for charts and Datatables for tables.
    Integrated CRUD operations into the admin dashboard for effective data manipulation.

Challenges

    Limited time to optimize code for performance.
    Difficulty selecting the right graphing tool, ultimately choosing Plotly.
    Managing integration between various technologies in the Flask framework.

Areas for Improvement

    Improve the speed of page loading, particularly on chart-heavy pages.
    Add more features to enhance user experience, such as advanced analytics.
    Improve the layout and user interface of the dashboard for better usability.

Lessons Learned

    Optimizing for performance while maintaining functionality is crucial for user experience.
    Flask is a flexible framework but requires careful planning for large-scale projects.
    Selecting the right tools at the start can save time later in development.

Next Steps

    Performance Optimization: Focus on optimizing page load times, especially with data-heavy pages.
    Feature Expansion: Add additional features such as project file management and task assignment.
    Layout Enhancements: Refine the user interface for a more intuitive and fluid experience.

Conclusion

Developing the Nando Construction Project Management Dashboard was an exciting and rewarding experience. I had the opportunity to integrate a variety of technologies and create a functional product that could be adapted for use by real companies. Looking forward, I am excited to continue refining the project, improving its performance, and adding new features.

Installation & Setup
Requirements

    Python 3.x
    Flask
    MySQL

Steps

    Clone the repository:

    bash

    git clone https://github.com/dylanmlilo/alx-project-management-dashboard.git

Install dependencies:

    bash

    pip install -r requirements.txt

Set up the MySQL database and update the Flask configuration for database credentials.

Run the project on your local server:

    bash

    flask run
