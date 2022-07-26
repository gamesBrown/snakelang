
gh repo create

$repo_name= Read-Host -Prompt "Enter Project Name"
$comment = Read-Host -Prompt "Enter First Commit Comment"

git init
git add .
git commit -m $comment
git branch -M main
git remote add origin https://gamesBrown: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@github.com/gamesBrown/$repo_name.git

git push -u origin main