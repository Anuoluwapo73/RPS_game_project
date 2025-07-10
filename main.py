from RPS import player
from RPS_game import play, quincy, abbey, kris

print("Playing against quincy...")
result = play(player, quincy, 1000)
print(f"You won {result * 100:.1f}% of the games.")

print("Playing against abbey...")
result = play(player, abbey, 1000)
print(f"You won {result * 100:.1f}% of the games.")

print("Playing against kris...")
result = play(player, kris, 1000)
print(f"You won {result * 100:.1f}% of the games.")



