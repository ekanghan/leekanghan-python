import pickle
import os

def input_scores():
    scores = []
    count = 1
    print("[점수 입력]")
    while True:
        score_str = input(f"#{count}? ")
        if score_str == '-1':
            break
        else:
            scores.append(int(score_str))
            count += 1
    return scores

def get_average(score_list):
    if not score_list:
        return 0
    total = 0
    for score in score_list:
        total += score
    return total / len(score_list)

def show_scores(score_list):
    score_strs = []
    for score in score_list:
        score_strs.append(str(score))
    print("\n[점수 출력]")
    print("개인 점수:", end=" ")
    for i in range(len(score_list)):
        print(f"{score_list[i]}", end = " ")
    print(f"\n평균: {get_average(score_list):.1f}")

def save_scores(score_list, filename="score.bin"):
    with open(filename, 'wb') as f:
        pickle.dump(score_list, f)

def load_scores(filename="score.bin"):
    if os.path.exists(filename):
        with open(filename, 'rb') as f:
            loaded_scores = pickle.load(f)
            print("[파일 읽기]")
        return loaded_scores
    else:
        return []

filename = "score.bin"
student_scores = load_scores(filename)

if student_scores == []:
    student_scores = input_scores()

show_scores(student_scores)
save_scores(student_scores, filename)