# Lab: Create a Repository with Forking

## Instructions

__Step 1:__ Open the Terminal and authenticate using `gh (Github CLI)`:
```
gh auth login
```

__Step 2:__ Create an authentication token in your Github account with specified scopes given in the terminal. Copy it from Github and paste it. Verify autherization was successful.

__Step 3:__ Visit the [class repo](https://github.com/Meta-Front-End-Developer-PC/m3l2_forking_lab) and click the `fork` button.

__Step 4:__ Clone the repository using the `GitHub CLI` command.
```
gh repo clone <YOUR USERNAME>/<REPOSITORY-NAME>
```

__Step 5:__ Move to the repo directory by using 
```
cd <REPOSITORY-NAME>
```

__Step 6:__ Create and checkout a new branch.
```
git checkout -b my-branch
```

__Step 7:__ Open and edit the `class.MD` file

Add your first name

Add your location

Add the name of the certification you are working on

__Step 8:__ Add your changes
```
git add class.MD
```

__Step 9:__ Commit your changes with a message
```
git commit
```

__Step 10:__ Push your changes to your fork
```
git push origin my-branch
```

__Step 11:__ Visit the [class repo](https://github.com/Meta-Front-End-Developer-PC/m3l2_forking_lab) and click `Pull Requests`.

__Step 12:__ Click on `New Pull Request`.

__Step 13:__ On the compare page click `compare across forks`

__Step 14:__ Select the main branch as `base`

__Step 15:__ Select your fork and the committed branch (my-branch) as `fork`

__Step 16:__ Give your pull request a title and description.

__Step 17:__ Click `Create Pull Request` button to initiate your pull request.

__Step 18:__ Once your pull request is complete copy the pull request ID.

## Self-review

1. In git, the default branch of a repo is called the ____________.
   - Secondary Branch
   - Main Branch
   - Super Branch
   - Primary Branch
   ```
   Answer: Main Branch
   Explanation: The default branch is known as the main branch, or, master branch on older repositories.
   ```

2. What is the request to merge forked changes called?
   - Code Request
   - Pull Request
   - Push Request
   ```
   Answer: Pull Request
   Explanation: You open a pull request to request merging of your forked changes.
   ```

3. When you clone a forked repository, what does origin refer to?
   - The original repository
   - Another developer’s repository
   - The forked repository
   ```
   Answer: The forked repository
   Explanation: The origin will always default to the clone URL. In this case, the forked repository is the origin.
   ```