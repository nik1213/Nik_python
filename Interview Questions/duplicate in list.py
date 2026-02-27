X = ["He","we","ikf","he","we","kfgk","we","hel"]

seen = set()
duplicate = set()

for word in X:
    if word in seen:
        duplicate.add(word)
    else:
        seen.add(word)

print(duplicate)