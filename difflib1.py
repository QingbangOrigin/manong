import difflib 

str_0 = 'git log --graph --pretty=oneline --abbrev-commit'
str_1 = 'git log --graph --pretty=online --abbrev-commit'

d = difflib.Differ()
diff = d.compare(str_0.splitlines(),str_1.splitlines())
print('\n'.join(list(diff)))
