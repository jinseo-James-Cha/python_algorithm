# each genre 2 song -> best album
# 1. first most genre
# 2. in genre most played
# 3. if played the same, lower id num

def solution(genres, plays):
    genre_nums = {}
    genre_id_and_played = {}
    
    for i, g in enumerate(genres):
        genre_nums[g] = genre_nums.get(g, 0) + plays[i]
        genre_id_and_played[g] = genre_id_and_played.get(g, []) + [[i, plays[i]]]
    
    answer = []
    # 장르별 1,2등을 어떻게 뽑지?
    sorted_genres = sorted(genre_nums.items(), key=lambda x: x[1], reverse=True)
    for g, n in sorted_genres:
        sorted_id_and_played = sorted(genre_id_and_played[g], key=lambda x: x[1], reverse=True)
        index = 0
        while index < 2 and index < len(sorted_id_and_played):
            answer.append(sorted_id_and_played[index][0])
            index += 1
        
    return answer