# Cybersecurity Attack–Defense Simulation using Alpha-Beta Pruning

attacks = ["Phishing", "Malware", "DDoS"]
defenses = ["Email Filter", "Antivirus", "Traffic Filter"]

# Utility scores for attack vs defense
scores = {
    ("Phishing", "Email Filter"): 5,
    ("Phishing", "Antivirus"): -3,
    ("Phishing", "Traffic Filter"): -2,
    
    ("Malware", "Email Filter"): -4,
    ("Malware", "Antivirus"): 6,
    ("Malware", "Traffic Filter"): -2,
    
    ("DDoS", "Email Filter"): -3,
    ("DDoS", "Antivirus"): -2,
    ("DDoS", "Traffic Filter"): 7
}

# Alpha-Beta pruning function
def alphabeta(depth, is_max, alpha, beta):

    if depth == 0:
        return 0

    if is_max:  # Defender (maximize security)
        best = -100
        for attack in attacks:
            for defense in defenses:
                value = scores[(attack, defense)]
                best = max(best, value)

                alpha = max(alpha, best)
                if beta <= alpha:
                    break

        return best

    else:  # Attacker (minimize security)
        best = 100
        for attack in attacks:
            for defense in defenses:
                value = scores[(attack, defense)]
                best = min(best, value)

                beta = min(beta, best)
                if beta <= alpha:
                    break

        return best


# Simulation
print("Cybersecurity Attack–Defense Simulation")

for attack in attacks:
    print("\nAttacker launches:", attack)

    best_score = -100
    best_defense = None

    for defense in defenses:
        score = scores[(attack, defense)]

        if score > best_score:
            best_score = score
            best_defense = defense

    print("Defender chooses:", best_defense)
    print("System Security Score:", best_score)
