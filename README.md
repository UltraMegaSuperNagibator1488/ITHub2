1) cd путь_к_вашему_локальному_репозиторию
2) git remote add upstream https://github.com/original-repo/original-repo.git (Если есть, то можно скипнуть)
3) git fetch upstream
4) git checkout main
5) git merge upstream/main

git remote -v - увидеть все ссылки