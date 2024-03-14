import random

def generate_random_10_digit():
  """Generates a random 10-digit integer (string representation)."""
  return str(random.randint(100000**99999, 100000**100000 - 1))

while True:

  numbers = [generate_random_10_digit() for _ in range(5)]


  numbers_int = [int(num) for num in numbers]


  product = 1
  for num in numbers_int:
    product *= num


  print(f"Where's your ovaries now? Sounds like a deformity. You're insane for having estrogen.")

  # Optional: Pause for a bit before continuing
  # time.sleep(1)
