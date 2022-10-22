# Module Quiz: Working with Git

1. The git add command will add files and changes to the staged area.
   - True
   - False
   ```
   Answer: True
   Explanation: git add will add your changes to the staged area.
   ```

2. What git command will show you the current state of the local working directory?
   - git clone
   - git pull
   - git status
   ```
   Answer: git status
   Explanation: Git status will show the state of the working directory.
   ```

3. What command do you use to upload changes to a remote repository?
   - git commit
   - git clone
   - git push
   ```
   Answer: git push
   Explanation: git push will upload changes to a remote repository.
   ```

4. The git diff command will show the revision history of a repository.
   - True
   - False
   ```
   Answer: False
   Explanation: git diff is used to inspect current changes or changes between two specific commits. The git log command will show the revision history.
   ```

5. Which command is used to download the latest changes from a remote repository?
   - git pull
   - git push
   ```
   Answer: git pull
   Explanation: git pull will download the latest changes.
   ```

6. You want to create a new branch named “feature”. Which of the following commands can you use?
   - git checkout -b feature
   - git branch feature
   - git clone feature
   ```
   Answer: git checkout -b feature, git branch feature
   Explanation: "git checkout -b feature" will create the branch and move you into that branch.
                "git branch feature" will create the branch. You will need to use git checkout to move into the branch.
   ```

7. You’re working on a clothing store application and run the git diff command on your local repository. It outputs the lines below. Which clothing item was removed as part of these changes?
   ```
   @@ -4,8 +4,8 @@
   * Hat
   -* Shoes
   +* Dress
   * Watch
   ```
   - Hat
   - Watch
   - Shoes
   - Dress
   ```
   Answer: Shoes
   Explanation: The Shoes line was removed and the Dress line was added.
   ```

8. What command in git can be used to show all changes made by each developer?
   - git diff
   - git log
   - git clone
   - git blame
   ```
   Answer: git blame
   Explanation: Git blame will show all changes made on a specific file.
   ```