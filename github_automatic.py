from github import Github
g = Github("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")

# Then play with your Github objects:
for repo in g.get_user().get_repos():
    print(repo.name)