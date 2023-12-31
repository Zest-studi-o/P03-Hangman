# THE HANGMAN

![The Hangman mockup](docs/mockup.png)

A version of the popular and classic game The Hangman created and played using the command line and the Python programming language which has been deployed with Heroku.

Visit the live site: [The Hangman](https://p03-hangman-ebeea9faff7c.herokuapp.com/)

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

This section provides insight into the UX process, with a focus on the people who this game has been created for, the main aims of the project and how it can help users to meet their needs.

Project goals:

- To encourage people to play the hangman game.

- To provide an easy and user-friendly command line game.

### User Stories

#### First-Time Visitor Goals

- As a first-time visitor, I want to start a new game using the command line.
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

![Flowchart](docs/hangman-flowchart.jpeg)

### Features

#### Existing Features

**Logo**

- The game Hangman visual identity.

![Logo](docs/features/logo.png)

**Welcome screen**

- The user is welcomed to the game, the logo displays and they can input their name and ensure they are happy with their selected option.

![Welcome screen](docs/features/welcome-screen.png)

**Category selection**

- The user can choose a word category to play the game. When the user selects to start the game, the terminal displays options to select between different word categories which are grouped by theme.

![Select category](docs/features/category.png)

**Play**

- After selecting a category and confirming that they are happy to play the user is prompted to a screen with the hangman stage 1, different stages are displayed as the player progresses through the game.

![Play](docs/features/play.png)

**Score counter**

- This counts the score obtained by the player, it adds 25 per letter guessed and 200 if the player guesses the word in full, it displays this data to the terminal for user feedback.

![Score counter](docs/features/score.png)

**Game over**

- When losing a game, the name of the player, score and game over ASCII Art are displayed.

![Game over art](docs/features/game-over-art.png)
![Game over message](docs/features/game-over-message.png)

**End Game screen**

- When finishing a game the user is prompted with a screen in which they can decide whether to start a new game, have a look at the leader board, or exit the game.

![End game](docs/features/end.png)

**Leader board**

- When finishing the game the user can see the leader board showing the top 10 scores achieved by previous players.

![Leader board](docs/features/leaderboard.png)

- The scores get stored in google sheets, the game returns the top 10 player name and scores from this database.
  This sheet is connected to the code through the Google Drive and Google Sheet API by the Google Cloud Platform.

![Leader board](docs/features/google-sheets.png)

- This code connects google sheets and the game.

![Connect code](docs/features/connect-code.png)

![Import Gspread](docs/features/import-gspread.png)

---

### Features Left to Implement

In the future, I would like to:

- Refine the score counter so it would add more points the earlier the full word is guessed.

- Refine the word display so no words would be repeated when a player selects the same category in consecutive games.

- Refine the leader board, so the same name cannot be repeated with the same scores, to avoid duplicate entries.

- Add colours to the terminal.

- Add more ASCII art and formatting to the terminal.

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

[Shields](https://shields.io/) - To add badges to the readme file.

[Amiresponsive](https://ui.dev/amiresponsive) - To generate a mockup in different screen sizes.

[Bandicam](https://www.bandicam.com/es/) - To screen record bugs and features.

[Windows photo feature](https://www.microsoft.com/en-us/windows/photo-movie-editor) - To trim screen recording.

[Veed](https://www.veed.io/convert/mp4-to-gif?gad=1&gclid=CjwKCAjwgqejBhBAEiwAuWHioCzHSc5XTTdsnixrxavlvLKEi4i_YeN__Xol0nANQCBhw60caeyF3RoC31wQAvD_BwE) - To convert mp4 to gif

[Heroku](https://id.heroku.com/) - To deploy the App.

[Code Institute template](https://github.com/Code-Institute-Org/p3-template) - To run the game in the terminal using Heroku.

[ASCII Art Generator](https://patorjk.com/) - To generate ASCII Art

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
9. Next, scroll down to the Build pack section click Add Build pack select Python and click Save Changes
10. Repeat step 8 to add node.js. o Note: The Build packs must be in the correct order. If not click and drag them to move into the correct order
11. Scroll to the top of the page and choose the Deploy tab
12. Select Github as the deployment method
13. Confirm you want to connect to GitHub
14. Search for the repository name and click the connect button
15. Scroll to the bottom of the deploy page and select the preferred deployment type
16. Click either Enable Automatic Deploys for automatic deployment when you push updates to GitHub

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

- I used other student examples as a reference to understand how to build my own game and what is expected for the app and readme, [Hangman 1](https://github.com/PedroCristo/portfolio_project_3), [Hangman 2](https://github.com/one1189/hangman) those projects were also helpful to find resources that helped me build the game, such as the use of ASCII Art, Lucid Chart, or other reference material.

### Content

All the words in the different categories are taken from:

- [Countries](https://github.com/one1189/hangman)
- [Food](https://github.com/one1189/hangman)
- [General](https://www.youtube.com/watch?v=m4nEnsavl6w)

### Media

- [ASCII Art Generator - Logo](https://patorjk.com/software/taag/#p=display&v=0&f=Ogre&t=The%20Hangman)

- [ASCII Art Generator - Leader board](https://patorjk.com/software/taag/#p=display&h=2&v=3&f=Digital&t=LEADERBOARD)

- [ASCII Art - Game over](https://textart4u.blogspot.com/2013/05/game-over-text-art.html)

- [ASCII Art - You win!](https://patorjk.com/software/taag/#p=display&f=ANSI%20Regular&t=You%20Win!)

### Acknowledgments

- [Derek MCAuley](https://github.com/derekmcauley7), my Code Institute Mentor.
