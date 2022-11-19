def game():
    return 100


score = game()

with open('Chapter 9\highest_score.txt') as f:
    highest_score_Str = f.read()

if highest_score_Str == '':
    with open('Chapter 9\highest_score.txt', 'w') as f:
        f.write(str(score))

elif int(highest_score_Str) < score:
    with open('Chapter 9\highest_score.txt', 'w') as f:
        f.write(str(score))
