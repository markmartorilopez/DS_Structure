# DS Structure

- production ( Real production workload )
    - hotfixes ( branches that are quick fixes on production )

- staging ( duplicate from production env. If it passes all tests, swap it with production. )
- master ( main branch where we are going to merge all our features)
    - features


    ### Steps
git init
git add README.md
git commit -m "First commit"
git branch -M main
git remote add origin https://github.com/markmartorilopez/DS_Structure.git
git push -u origin main

git checkout -b production
git push --set-upstream origin production

git checkout -b staging
git push --set-upstream origin staging

git checkout main
git checkout -b feature/1-readme-update
git add README.md
git commit -m "#1 - update readme"
git push --set-upstream origin feature/1-readme-update


#### Add new color - Blue
- Open a ticket.
- Create feature branch adding ticket ID to the branch name.
- Edit code.
- Add code.
- Commit code to feature branch.
- Pull request to main.
- Accept.

#### Update Staging
git checkout staging
git merge main
When all the tests running in staging have passed...
We tag the staging version - Only Tagged Branches can be commited to Production.
git checkout staging
git tag 'v1.0.0' # mainupdate.minorupdate.hotfix
git push --tags

#### Production
git checkout production
git merge staging
git push

#### Hotfix - Change Color
To Green.