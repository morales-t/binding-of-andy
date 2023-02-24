# Welcome to your coding journey Andy

## Getting Started
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
In theory - all you need to run your code is to have a language downloaded - and have some system to save text (Hello mr. Microsoft Word). But in reality no one really just does that (for the most part). People will use IDE (integrated development environments) so that they have an easy way to execute their code, have a helpful text editor that will highlight things to make coding in a specific language easier, have easy access to the terminal, have bells and whisles that makes coding easier, and most importantly make it so everything is in darkmode.

Which IDE you use is a heavily personal choice - so there is no "right" answer - but out of all the ones I've used, I've found the most helpful on to be VScode (Visual Studio Code).

Just for now - I'm going to have you download the program - which you can do [here](https://code.visualstudio.com/).

## Downloading Python
Okay, I'm going to be real with you, I know you already have it downloaded. But some of the settings + boxes when you first downloaded were super important to click, and they are a huge pain in the ass to setup if you don't click them. So we're going to have you uninstall and then reinstall python, and I'm going to tell you the boxes to click.

Normally - I suggest using the latest version of Python because it's faster and more up to date. But PyGame doesn't seem to support 3.11 well currently, so we're going oldschool (hello mr 3.10).

Download 3.10 [here](https://www.python.org/downloads/release/python-31010/). You want Windows Install (64-bit).

Open that sucker up, and click uninstall, and wait for 3 years while it does it's thing.

Now open that sucker up agian. **_BEFORE CLICKING INSTALL_ now - please for the love of the lord, click the button at the bottom that says "Add python.exe to PATH"**. Then you click install now.

Then by good god you should have python install the way the lord intended. Let's test it though. Go to the Command Propt - and type in "python".

If it says Python 3.10.10 and a bunch of shit after then praise the sun. If not, DM me please. Then type in: exit()


## Downloading Packages to Python

### Overview
The thing to always keep in mind, is that programming is an incredibly collaborative community. And as a collaborative community, what people find is that multiple people will run into the same problem multiple times. Because of this - people will often make "Packages" (this pre-written code), so that you can use someone else's code to help accomplish this task. This code is usually super super optimized and smart - because packages that alot of people use are "Open Source", which basically means aton of really passionate people work together on the code to make it better and better.

### In Practice
Now, the thing to keep in mind, is that no one is all knowing and all seeing. Because of this reality, the package creators won't know what other packages you'll be using when coding. Because of this - conflicts can arise (i.e. you can't install two packages of something at the same time).

Because of that - people will often create "environments" of python. That is python with some packages installed - that are seperate from all your other "enivoronments" of python with other packages installed. This ensures you don't need to worry about those conflicts as much.

Luckily - IDEs make this incredible simple to use - because this is incredibly standard.

### Environment Setup
Open up that sucker of VScode. Then Open the folder with this repo in it (Hello, now you can see me, the file making this text) by clicking on File then Open Folder.

Now lets open up that sucker of a terminal. Click on Terminal at the top (should be another option like "File") - and click on New Terminal.

This should open up this console at the bottom of the screen. By default - I think windows uses powershell, which I hate with the passion of 1000 suns. So what you'll want to do is click on the drop down arrow right next to the plus sign at the top right of the terminal. Then click on "Select Default Profile".

Then from the options - click on "Git Bash", which is our new savior from stupid dumb powershell.

Then Click on that sweet plus sign and say goodbye to powershell to never return.

You may have gotten to this point and said "Why haven't I made an environment yet", and I'd agree with you, so let's do it. In the terminal type in

```
python -m venv env
```

You've just made your environment, congratulations!.

Now - lets open that sweet venv. Type in the following and press enter.

```
source env/scripts/activate
```

Congratulations! Now you have an env (this should be used by default by VScode which is sweet).

### Downloading PyGame

PyGame is one of those sweet ass packages I was talking about. Let's install it with "pip" which is the tool used to download them packages from the internet.

Type in the following in the terminal and press enter

```
pip install pygame
```

Lets make sure it worked.

In the terminal - type in python. Then type in the following and press enter
```
import pygame
```

If you did that, and didn't get a load of errors, then you've done it! We're finally ready!!!!

type in the following in the terminal, and press enter
```
exit()
```

# 🎉 CONGRATULATIONS, WE'RE READY TO CODE 🎉