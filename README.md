# THE HANGMAN

![Project Image](docs/project.png)

A version of the classic game The hangman using the command line and Python programming language deployed with Heroku.

Visit the live site: [Hangman]()

# Table of contents

- [User Experience (UX)](#User-Experience-UX)

  - [User Stories](#User-Stories)

- [Design](#Design)

  - [Flowchart](#Flowchart)
  - [Features](#Features)

- [Technologies Used](#Technologies-Used)

  - [Languages Used](#languages-used)
  - [Frameworks, Libraries & Programs Used](#frameworks-libraries--programs-used)

- [Deployment & Local Development](#Deployment--Local-Development)

  - [Deployment](#Deployment)
  - [Local Development](#Local-Development)
    - [How to Fork](#How-to-Fork)
    - [How to Clone](#How-to-Clone)

- [Testing](#Testing)

- [Credits](#Credits)
  - [Code Used](#code-used)
  - [Content](#content)
  - [Media](#media)
  - [Acknowledgments](#Acknowledgments)

---

## User Experience (UX)

#### Key information for the site

This section provides insight into the UX process, focusing on who this game is for, the main aims of the project and how it can help users meet their needs.

Project goals:

- To encourage people to play the hangman game.

- To provide an easy and user-friendly command line game.

### User Stories

#### First-Time Visitor Goals

- As a first-time visitor, I want to start a new game using the comand line.
- As a first-time visitor, I want to see how many attempts I have left when playing.
- As a first-time visitor, I want to see the words I guessed so far displayed.
- As a first-time visitor, I want the app to ask me if I want to play again or not when finishing.

#### Returning Visitor Goals

- As a returning visitor, I want to see my results.

#### Frequent Visitor Goals

- As a frequent visitor, I want to be able to play the game using different categories.

---

## Design

### Flowchart

Here flowchart.

### Features

#### Existing Features

Features here

**Feature A**

![Feature A image]()

- This does abc.

**Category selection**

![Category selection image]()

- When the user selects to start the game, the terminal displays options to select between different word categories grouped by themes.

**Score counter**

![Score counter image]()

- This counts the score obtained by the player, adds 25 per letter guessed and 200 if the player guesses the word in full, it displays this data to the terminal for user feedback.
---

### Features Left to Implement

In the future, I would like to:

- Refine the score counter so it would add more points the earlier the full word is guessed.

- Add colours to the terminal.

- Add a feature in which the user can select words sorted by length.

- Add a multiplayer feature.

---

## Technologies Used

### Languages Used

The language used is Python

### Frameworks, Libraries & Programs Used

[Lucid chart](https://www.lucidchart.com/pages/) - Used to create flowcharts.

[Git](https://git-scm.com/) - For version control.

[GitHub](https://github.com/) - To save and store the files for the website.

[Code from anywhere](https://app.codeanywhere.com/) - To write, edit and save code.

[Google Fonts](https://fonts.google.com/) - To import fonts for the website.

[Shields](https://shields.io/) - To add badges to the readme file.

[Amiresponsive](https://ui.dev/amiresponsive) - To generate a mockup in different screen sizes.

[Colorama](https://pypi.org/project/colorama/) - To change colours in the terminal

[Heroku](https://id.heroku.com/) - To deploy the App.

[ASCII Art Generator](https://patorjk.com/)

## Deployment & Local Development

### Deployment

- This site was deployed by completing the following steps:

1. Log in to [Heroku](https://id.heroku.com) or create an account
2. On the main page click the button labeled New in the top right corner and from the drop-down menu select Create New App
3. You must enter a unique app name
4. Next select your region
5. Click on the Create App button
6. The next page is the project’s Deploy Tab. Click on the Settings Tab and scroll down to Config Vars
7. Click Reveal Config Vars and enter port into the Key box and 8000 into the Value box and click the Add button
8. Click Reveal Config Vars again and enter CREDS into the Key box and the Google credentials into the Value box
9. Next, scroll down to the Buildpack section click Add Buildpack select Python and click Save Changes
10. Repeat step 8 to add node.js. o Note: The Buildpacks must be in the correct order. If not click and drag them to move into the correct order
11. Scroll to the top of the page and choose the Deploy tab
12. Select Github as the deployment method
13. Confirm you want to connect to GitHub
14. Search for the repository name and click the connect button
15. Scroll to the bottom of the deploy page and select the preferred deployment type
16. Click either Enable Automatic Deploys for automatic deployment when you push updates to Github

### Local Development

#### How to Fork

To fork the Zest-studi-o/P03-Hangman repository:

1. Log in (or sign up) to Github.
2. Go to the repository for this project, Zest-studi-o/P03-Hangman.
3. Click the Fork button in the top right corner.

#### How to Clone

To clone the Zest-studi-o/P03-Hangman repository:

1. Log in (or sign up) to GitHub.
2. Go to the repository for this project, Zest-studi-o/Zest-studi-o/P03-Hangman.
3. Click on the code button, select whether you would like to clone with HTTPS, SSH or GitHub CLI and copy the link shown.
4. Open the terminal in your code editor and change the current working directory to the location you want to use for the cloned directory.
5. Type 'git clone' into the terminal and then paste the link you copied in step 3. Press enter.

---

## Testing

Please refer to [TESTING.md](TESTING.md) file for all testing carried out.

## Credits

### Code Used

- [How to build HANGMAN with Python in 10 MINUTES](https://www.youtube.com/watch?v=m4nEnsavl6w) - I used this tutorial to help me with understanding how to create a basic hangman game to build upon it using Python.

- I used other student examples as a reference to understand how to build my own game and what is expected for the app and readme.md, [Hangaman 1](https://github.com/PedroCristo/portfolio_project_3), [Hangaman 2](https://github.com/one1189/hangman) those projects were also helpful to find resources that helped me build the game, such as the use of ASCII Art, Lucid Chart, Colorama or reference material.

### Content

All the words in the different categories are taken from:

- [Countries](https://github.com/one1189/hangman)
- [Food](https://github.com/one1189/hangman)
- [General](https://www.youtube.com/watch?v=m4nEnsavl6w)

### Media

- [ASCII Art Generator - Logo](https://patorjk.com/software/taag/#p=display&v=0&f=Ogre&t=The%20Hangman)

### Acknowledgments

- [Derek MCAuley](https://github.com/derekmcauley7), my Code Institute Mentor.
- Tutor support at Code Institute.
