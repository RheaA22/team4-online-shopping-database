## OUR TEAMS INFORMATION

Our names: Mihira Chandrakar, Rhea Aiyar, Mahiya Patil

Link to our video: https://drive.google.com/file/d/1D0bi2NrOlSz-kAyziI6typZM3MeHLueH/view?usp=sharing

Link to our git: https://github.com/RheaA22/team4-online-shopping-database.git

## Current Project Components

Currently, there are three major components that will each run in their own Docker Containers:

- Streamlit App in the `./app` directory
- Flask REST api in the `./api` directory
- MySQL Database that will be initialized with SQL script files from the `./database-files` directory

## Suggestion for Learning the Project Code Base

If you are not familiar with web app development, this code base might be confusing. But don't worry, it's not that bad.
Here are some suggestions for learning the code base:

1. Have two versions of the template repo - one for you to individually explore and lear and another for the team's
   project implementation.
1. Start by exploring the `./app` directory. This is where the Streamlit app is located. The Streamlit app is a
   Python-based web app that is used to interact with the user. It's a great way to build a simple web app without
   having to learn a lot of web development.
1. Next, explore the `./api` directory. This is where the Flask REST API is located. The REST API is used to interact
   with the database and perform other server-side tasks.
1. Finally, explore the `./database-files` directory. This is where the SQL scripts are located that will be used to
   initialize the MySQL database.

### Setting Up Your Personal Repo

1. In GitHub, click the **fork** button in the upper right corner of the repo screen.
1. When prompted, give the new repo a unique name, perhaps including your last name and the word 'personal'.
1. Once the fork has been created, clone YOUR forked version of the repo to your computer.
1. Set up the `.env` file in the `api` folder based on the `.env.template` file.
1. For running the testing containers (for your personal repo), you will tell `docker compose` to use a different
   configuration file named `docker-compose-testing.yaml`.
    1. `docker compose -f docker-compose-testing.yaml up -d` to start all the containers in the background
    1. `docker compose -f docker-compose-testing.yaml down` to shutdown and delete the containers
    1. `docker compose -f docker-compose-testing.yaml up db -d` only start the database container (replace db with api
       or app for the other two services as needed)
    1. `docker compose -f docker-compose-testing.yaml stop` to "turn off" the containers but not delete them.

### Setting Up Your Team's Repo

**Before you start**: As a team, one person needs to assume the role of _Team Project Repo Owner_.

1. The Team Project Repo Owner needs to fork this template repo into their own GitHub account **and give the repo a name
   consistent with your project's name**. If you're worried that the repo is public, don't. Every team is doing a
   different project.
1. In the newly forked team repo, the Team Project Repo Owner should go to the **Settings** tab, choose **Collaborators
   and Teams** on the left-side panel. Add each of your team members to the repository with Write access.

**Remaining Team Members**

1. Each of the other team members will receive an invitation to join. Obviously accept the invite.
1. Once that process is complete, each team member, including the repo owner, should clone the Team's Repo to their
   local machines (in a different location your Personal Project Repo).
1. Set up the `.env` file in the `api` folder based on the `.env.template` file.
1. For running the testing containers (for your team's repo):
    1. `docker compose up -d` to start all the containers in the background
    1. `docker compose down` to shutdown and delete the containers
    1. `docker compose up db -d` only start the database container (replace db with api or app for the other two
       services as needed)
    1. `docker compose stop` to "turn off" the containers but not delete them.

**Note:** You can also use the Docker Desktop GUI to start and stop the containers after the first initial run.


