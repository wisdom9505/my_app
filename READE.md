# Django Band Website

This project is a simple Django-based website for a fictional band. It features multiple pages and incorporates a database-driven component. The website allows users to view band information, upcoming events, and access a member login system.

## Project Features
- **Home Page:** An overview of the band, including a brief history and mission statement.
- **Events Page:** A database-driven list of upcoming events with details such as date, time, and venue.
- **Members Page:** Information about band members, including their roles and biographies.
- **User Authentication:** Users can log in to access exclusive content and features.

## Technologies Used
- **Django:** The web framework used to build the site.
- **SQLite:** The default database for storing user and event data.
- **HTML/CSS:** For frontend design and layout.
- **Bootstrap:** For responsive design.

## Installation

To run this project locally, follow these steps:

### Prerequisites

Make sure you have the following installed:
- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Step 1: Clone the Repository

Open your terminal and run the following commands:

```bash
git clone https://github.com/wisdom9505/Wiz_App.git
cd django-band-website

Step 2: Build and Run the Docker Container
Once you are in the project directory, use the following command to build and run the Docker container:
docker-compose up --build

Step 3: Access the Application
After the Docker container has started, you can access the application by navigating to http://localhost:8000 in your web browse

Step 4: Install Requirements (if needed)
If you need to install additional requirements, you can do so by running:

bash
Copy code
docker-compose exec web pip install -r requirements.txt
