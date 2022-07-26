
$repo_name= Read-Host -Prompt "Enter Project Name"

mkdir $repo_name

Copy-Item -recurse templateHERE\* $repo_name


code $repo_name
cd $repo_name



