bird_h = float(input())
bird_sh= float(input())
tree_sh = float(input())

ratio = bird_h / bird_sh

print(round((tree_sh - bird_sh)*ratio, 2))
