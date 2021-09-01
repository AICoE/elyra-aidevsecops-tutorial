# Store your changes on your GitHub repo

If you don't have a GitHub token, you can create one following GitHub docs: [create GitHub token](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token).

## Push your changes using JupyterLab Git extension

If you are running this tutorial on Operate First your work-in-progress notebooks can be saved in your JupyterHub PVC by hitting the save button on the top panel. 
Nevertheless, it is a good practice to push your changes to the GitHub repo when you finish working on your project, so that all your work can be saved. 

In order to do that from within JupyterHub using the [Jupyterlab Git extension](https://github.com/jupyterlab/jupyterlab-git):

1. Go to Git Box panel on the left to check what files have been changed.

    <div style="text-align:center">
    <img alt="Go to Git Box Panel" src="https://raw.githubusercontent.com/thoth-station/elyra-aidevsecops-tutorial/master/docs/images/GotoGitBoxPanel.png">
    </div>

2. Stage the files you want to push to your GitHub repo.

    <div style="text-align:center">
    <img alt="Stage the files" src="https://raw.githubusercontent.com/thoth-station/elyra-aidevsecops-tutorial/master/docs/images/StageFiles.png">
    </div>

3. Add Summary of your changes (a.k.a commit message) and select Commit.

    <div style="text-align:center">
    <img alt="Commit Changes" src="https://raw.githubusercontent.com/thoth-station/elyra-aidevsecops-tutorial/master/docs/images/CommitChanges.png">
    </div>

    NOTE: _If you are doing this for the first time, git requires user email and user name to be set.(The extension will open a Dialog Form to insert them)_

    <div style="text-align:center">
    <img alt="Insert User Name and Email" src="https://raw.githubusercontent.com/thoth-station/elyra-aidevsecops-tutorial/master/docs/images/InsertUserNameEmail.png">
    </div>


4. Select Push Changes.

    <div style="text-align:center">
    <img alt="Use Button to Push Changes" src="https://raw.githubusercontent.com/thoth-station/elyra-aidevsecops-tutorial/master/docs/images/UseButtonToPushChanges.png">
    </div>

5. Insert your Github account name and your GitHub token to push to the GitHub repo you cloned.

    <div style="text-align:center">
    <img alt="Push Changes with GitHub token" src="https://raw.githubusercontent.com/thoth-station/elyra-aidevsecops-tutorial/master/docs/images/PushGitHubToken.png">
    </div>

## Push your changes using the terminal in JupyterLab

[Jupyterlab Git extension](https://github.com/jupyterlab/jupyterlab-git) is limited to one repository at the moment. Therefore if you want to clone another repo and push changes you need to use the git commands from the Terminal.

1. Open terminal from the icon in the Launcher.

    <div style="text-align:center">
    <img alt="Open Terminal" src="https://raw.githubusercontent.com/thoth-station/elyra-aidevsecops-tutorial/master/docs/images/OpenTerminal.png">
    </div>

2. Start using the git commands:

    <div style="text-align:center">
    <img alt="Use Git Commands" src="https://raw.githubusercontent.com/thoth-station/elyra-aidevsecops-tutorial/master/docs/images/UseTerminal.png">
    </div>

- `git clone <repo>` to clone a new repo.

- `git add <file>` after you modify files to put them in stage.

- `git commit -m "<commit message>"` to commit the changes in stage. _NOTE: If you are doing this for the first time, git requires user email and user name to be set._

    <div style="text-align:center">
    <img alt="First commit" src="https://raw.githubusercontent.com/thoth-station/elyra-aidevsecops-tutorial/master/docs/images/FirsCommit.png">
    </div>

- `git push origin <branch>` to push your changes.


### Open Pull Request against the repo you want to contribute

Once you are satisfied with your changes you can open a Pull Request directly from your fork.

## Next Step

[Set bots and pipelines to create releases, build images and enable dependency management](./thoth-aicoe-services.md)
