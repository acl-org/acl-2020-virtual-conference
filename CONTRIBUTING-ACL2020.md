# How to Contribute to ACL-2020

Notes: see [CONTRIBUTING.md](./CONTRIBUTING.md) for general instructions.

## Setup Environment

Before you start, please make sure you have a GitHub account and have your ssh key added to your GitHub account. Also, Python should be installed into your device to setup the environment.

### Get a GitHub Repository

```shell
cd /path/to/the/local/folder
git clone git@github.com:acl-org/acl-2020-virtual-conference.git
```

By then, you will be able to download all content from ```acl-2020-virtual-conference``` repository to your local folder. If you are familiar with ```git```, you can also download the content by clicking the green button and the "Download ZIP" button and extract to your local folder.



### Install Required Package

First, move to the repo folder:

```shell
cd acl-2020-virtual-conference
```

Then install required packages:

``` shell
pip install -r requirements.txt
```

Additionally, you can create a virtual Python environment before the installation. There are many ways to create virtual environments in Python, which the following commands will guide you to create one using ```virtualenvwrapper``` with Python 3.x.

```shell
#----------------------------------------------------
# on Ubuntu
sudo apt-get install python3-pip
sudo pip3 install virtualenvwrapper
#----------------------------------------------------
# on MacOS
# install python3 if needed
brew install python3
#----------------------------------------------------
which python3 # find the path to python3.x
which virtualenvwrapper.sh # find the path to the virtualenverapper installation script
# change the bash script file to activate wrapper
nano ~/.bashrc
# in the ~/.bashrc file
# modify the following lines accordingly and add them at the end of the file
export VIRTUALENVWRAPPER_PYTHON='the output of which python3'
source 'the output of which virtualenvwrapper.sh'
# close ~./bashrc by pressing ctrl+x and save the changes by pressing "y"
# refresh the bash profile
source ~/.bashrc
# create virtual environment for acl
mkvirtualenv --python='the output of which python3' your_env_name
# by now you will have a python3.x virtual environment specificaly for acl-2020
# if you accidiently quit the current session,
# you can reactivate the environemnt by the following code
workon your_env_name
# install required packages
pip install -r requirements.txt
```



Now the environment is activated.



## How to Create Pull Request

As mentioned in the [GitHub help documentation](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request), creating a pull request can propose and collaborate on changes to a repository. Those changes will be proposed to a *branch*, which ensures that the ```master``` branch only contains finished and approved works. 



```shell
# pull the newest update from the master branch
git pull
# create local branch
git checkout -b your_branch_name
```

By now you have created a new local branch. Then you can make contributions to the content. Once you've finished, use the following command in the terminal to commit to the local branch.

```shell
git add . # add all files
git add file_changed # only add file the named file_changed
git commit -am 'your update logs'
git push --set-upstream origin your_branch_name # setup the upstream
```

Now you can open a pull request on the repository's website. Additionally, on the repository's page, you should click ```New pull request``` button near the ```Branch: master```. Then it will redirect to a new page. On this page, you need to be very carefully for the choices of base repository and head repository. Following the example shown in this document, the head repository should be ```acl-org/acl-2020-virtual-conference```, and ```compare: your_branch_name``` next to the head repository menu. The base repository should be ```acl-org/acl-2020-virtual-conference```.  Then you can click the green button ```Create pull request```. By clicking this button, you have created a new pull request and a collaborator will be notified and review your changes. The collaborator will discuss any further changes for your contributions. Once approved, your branch will be merged into ```master``` branch. Before you make any further contributions, don't forget to ```git pull``` to update your local files.

For more details about opening a pull request on the website, please check the  [GitHub help documentation](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).



## Additional Instructions



Here are additional instructions for working on the ACL2020 fork.
1. Run the command below check out the private [sitedata_acl2020](https://github.com/acl-org/acl-2020-virtual-conference-sitedata).
    ```bash
    git submodule update --init --recursive
    ```
   * You need to clone with SSH instead of HTTPS to get the git submodule working.
   * All ACL2020 sitedate are stored in this folder.
2. All images should be saved under [static/images/acl2020](./static/images/acl2020) folder.


## Deploy at AWS with login authentication
TBD
