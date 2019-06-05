# emotion_tracker.py

emotion_dict = {}
while True:
  user_feeling = input("Type how you are feeling or 'done': ").lower()
  if user_feeling == "done":
    break
  if user_feeling in emotion_dict:
    emotion_dict[user_feeling] += 1
  else:
    emotion_dict[user_feeling] = 1

highest_num = 0
highest_emo = ''
for emo in emotion_dict:
    if emotion_dict[emo] > highest_num:
        highest_num = emotion_dict[emo]
        highest_emo = emo
print(f"You mostly felt {highest_emo}")
