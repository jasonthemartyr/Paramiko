# Switch Checker

A simple Paramiko script that runs a user specified command against a list of switch IP's and then dumps the output into a text file. This script was designed to be used against CISCO NX-OS switches.
## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Python 3.X+ and Paramiko are required. To install Paramiko use the following:

```
pip install paramiko
```

### Installing

To install the script simply pull it from github using the following:

```
git clone  https://github.com/jasonthemartyr/NXOS-swchecker.git
```

## Deployment

Once the repo has been cloned initiate the script with:

```
python switchchecker.py
```
Then following the terminal prompts.

## Known Issues

The script uses getpass to retrieve a username/password so the username must match the local or TACACS/RADIUS account used to access network devices. Script and directory must have read, write, and execute privileges. 

## To Do's

General clean-up and consolidation of functions is still needing to be done.

## Built With

* [Pycharm](https://www.jetbrains.com/pycharm/) - The Python IDE used
* [Paramiko](http://www.paramiko.org/) - Python SSH module

## Authors

* **Jason Marter** - *Initial work* - [jasonthemartyr](https://github.com/jasonthemartyr/)

## Acknowledgments

Fedora tip to the following for putting up with me :P

* [brainmonkey](https://github.com/BrainMonkey)
* [jpurcell7](https://github.com/jpurcell7)