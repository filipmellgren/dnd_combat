# Dungeons, Dragons & Dilemmas

You find yourself in the depths of a dungeon as you discover an ancient tomb full of valuable relics. Among the items you find is a two-handed greataxe. Due to its weight, you can't pick it up unless you let go of both your handaxe and your shield. You now face a dilemma: should you pick up the greataxe, or continue down the dungeon with your less lethal handaxe and safety provided by your shield?

Fortunately, you carry a book provided to you by a fellow dungeoneer containing a guide to adventuring. You begin to read as you ponder your decision.

## Survivability
First, you learn about the concept of survivability. The ability of a character to sustain damage. This is provided to you as: $\text{Survival Time} = \frac{\text{Hit Points}}{\text{Expected Damage per Round}}$. The greater the value, the longer you are able to stand in a fight. Clearly, your shield contributes positively to this number.

You are then told that Surival Time is related to your probability of surviving a single round of combat, and that this is given by $P(\text{Survive}) = 1 - \frac{1}{\text{Survival Time}}$. This relation depends on the assumption that you get knocked down with a constant probability any given round, irrespective of your hit points. A rough assumption given that your survival rests on it, but one your fellow dungeoneer made anyway out of recklessness. You decide to continue reading despite this apparent indifference to your life's worth.

## Total Expected Damage
The next chapter explains that the total amount of damage you will ever deal, depends on how much damage you do per unit of time, multiplied by the time until you get knocked down: $\text{Total Expected Damage} = \text{Damage per round} \cdot \text{Survival Time}$. Fair enough you think, hoping that the time you are knocked-out is far away and that you will continue to explore many dungeons in the future. You do however realize that the greataxe staring at you will deal damage faster than the handaxe, and that your day of dooms draws closer without a shield.

### Variance of Total Expected Damage
The chapter contains a quirky appendix that contains scribbles you need to roll at least a 15 on a D20 in order to understand. It says that the "variance of total expected damage is given by the [law of total variance](https://en.wikipedia.org/wiki/Law_of_total_variance)". Being of somewhat chaotic energy, you are not sure this is a law you wish to abide by, but your wisdom tells you that it might be useful to read, so you continue reading. It says $\text{Var TED} = \text{Survival Time} \cdot \left(\text{Var(DPR)} \cdot P(\text{Survive}) + DPR^2 \cdot P(\text{Survive})  \cdot (1-P(\text{Survive}) ) \right)$.

Where DPR is a concept you have heard of, meaning the amount of damage your character is expected to deal in any given round, and variance is a measure of the variability of that damage. With your handaxe attacks, the DPR evaluates to $P(\text{hit} \cdot (E(D6) + \text{Str Mod}) = 4.225$ given your 3 in Strength modification and 65% probability to hit on any given attack while its variance of your attack, given that you hit is given by 2.92, and the complication that you don't always hit means you need to compute the expected variance plus the variance of the expectaiton given by $0.65 \cdot 3.5^2 \cdot 0.35) = 2.79$, which evaluates to $0.65 \cdot 2.92 + 2.79 = 4.7$.

## Risk free damage
Being a bit confused by the whole notion of variance, you learn that the variance is zero for risk free attacks. Essentially, damage that can be done by you without rolling a dice. While this is not much, it feels convenient to know your party can always blend in some risk free damage from that consistently nice cantrip with the more risky dice throws that tend to always be low when you need them the most.

## Combat Efficiency Ratio
After reading a bunch of unintelligible nonsense, you flip pages to the concluding chapter where you find: $\text{Character efficiency} = \frac{\text{Total Expected Damage} - \text{Risk Free Damage}}{\sqrt{Var(\text{Total Expected Damage})}}$ and learn that this is somehow tells you how you should think about whether to pick up that greataxe or not.

You begin to calculate the option value of the choices you are facing as you see the dungeon's dragon approaching you...



