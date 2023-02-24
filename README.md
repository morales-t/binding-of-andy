# binding-of-andy

## Getting Started.
Hola Andy, welcome to your programming journey. In these instructions - we're going to go over the pre-work to get you setup. This is the boring stuff needed at the start, so you can really hit the ground running, with some good programming hygiene.

Keep in mind - alot of this is python specific - as each language is quite different when it comes to compiling code. I'll call out what is python specific.

The first steps are:
- Setting up Git.
- Setting up VScode
- Downloading Python
- Downloading Packages to Python

## Setting up Git (Not Python Specific)

### Overview
Git is a version control software that is applicable to just about all coding. It's critical so you can track + save changes to your code, rollback changes as needed, and collaborate with others (this makes it so we can both be working on the same files at the same time, without overwriting each other).

### Downloads
To get started - go ahead and download Git (and git bash) from the link [here](https://git-scm.com/). After this - you should have GitBash installed on your computer.

Next step is setting up a GitHub account. This is so your code is hosted in the cloud + you can collaborate on code together. Make an account at the site [here](https://github.com/).

### Git Nomencalture
- Repo : Think of this as the main folder for a project you're working on.
- Main/Master : This is the "official" version of the code, that people view as the primary version
- Branch : If multiple people are working on the same code at the same time - a branch will let you edit the code in a parallel universe where only you are the one editting the code. Then you "merge" this branch with the main - to bring your edits. I wouldn't worry about this for now - because I'm not going to have you use branches to start.
- Commit: It's basically a point and time that you "save" the files.

### Getting Started.
To get started, you need to add your private key to your github account. This is basically so when you're making changes - Github knows it's you (and allows you to see things only you can see). To do-so, follow the instructions [here](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account).

Next you need to download the repo we'll be working on (which is this 😊).

To do so - you "clone" the repo (i.e. copy it to your computer). To do so:
 - Open Git Bash
 - Go to the top right of the repo - there should be a green button called "Code.
 - Click on the "SSH" button
 - Copy the link it allows you to copy.
 - Go in GitBash and type in: git clone git@github.com:morales-t/binding-of-andy.git

Yay! Now you've downloaded the code.

If you want to run commands on this code - you have to be in the folder that represents the git repository (don't worry - things like VScode made this easy).

### Helpful Commands
- git pull - Download the latest changes of code
- git add . - Adds all changes to be commited (i.e. it's staging them to be saved)
- git commit -m "helpful message here" - Saves all staged changes with your helpful message
- git push - Pushes the code to the cloud (GitHub) so now it's really a part of main.
- git checkout -b branch_name - Makes a seperate branch to stage your changes in
- git push origin branch_name - Pushes your branch to main (in the cloud)

## Setting up VScode (Not Python Specific)
