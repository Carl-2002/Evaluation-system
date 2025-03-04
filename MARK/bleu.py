import jieba
from nltk.translate.bleu_score import sentence_bleu

def bleu(target, inference):
    target_fenci = ' '.join(jieba.cut(target))
    inference_fenci = ' '.join(jieba.cut(inference))

    reference = []  
    candidate = [] 

    reference.append(target_fenci.split())
    candidate = (inference_fenci.split())

    score1 = sentence_bleu(reference, candidate, weights=(1, 0, 0, 0))
    score2 = sentence_bleu(reference, candidate, weights=(0, 1, 0, 0))
    score3 = sentence_bleu(reference, candidate, weights=(0, 0, 1, 0))
    score4 = sentence_bleu(reference, candidate, weights=(0, 0, 0, 1))
    reference.clear()
    
    bleu_score = [score1, score2, score3, score4]
    print(bleu_score)
    return bleu_score
