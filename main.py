import math

def evaluate_character(dpr, var_dpr, edt, hp, risk_free_dpr):
    # Calculate Survival Time (number of rounds character can survive taking EDT damage).
    st = hp / edt

    # Assuming an exponential distribution of survival time,
    # the inverse of survival time gives the rate at which death occurs.
    # Not super realistic given how HP and healig works in games, but a simplification.
    lambda_ = 1 / st

    # Calculate probability of survival each round.
    p_survive = 1 - lambda_

    # Calculate Total Expected Damage.
    ted = dpr * st

    # Calculate Variance of Total Expected Damage (with zero-inflation due to deaths.)
    # using law of total variance.
    var_ted = st * (var_dpr * p_survive + dpr**2 * p_survive * (1 - p_survive))
    st * (var_dpr * p_survive + dpr**2 * p_survive * (1 - p_survive))

    # Calculate Combat Efficiency Ratio (Sharpe Ratio for DnD).
    risk_free_total = risk_free_dpr * st
    cer = (ted - risk_free_total) / math.sqrt(var_ted)

    return {
        "Survival Time": round(st, 1),
        "Survival Probability per Round": round(p_survive, 1),
        "Total Expected Damage": round(ted, 1),
        "Combat Efficiency Ratio": round(cer, 1)
    }

# Example usage
character1 = evaluate_character(
    dpr=15, # Damage Per Round
    var_dpr=10, # Variance of Damage Per Round
    edt=30, # Expected Damage Taken per round
    hp=50, # Hit Points
    risk_free_dpr=0 # Damage Per Round from risk-free sources
) 

print(character1)

# Compare with a tankier character
character2 = evaluate_character(
    dpr = 10,
    var_dpr=10,
    edt=20,
    hp=70,
    risk_free_dpr=0 
)

print(character2)