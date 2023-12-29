import random;
import time;
import sys;

# Pokemon class
class Pokemon:
  def __init__(self, name, type, level = 5):
    self.name = name;
    self.type = type;
    self.level = level;
    self.health = level * 10;
    self.damage = level * 3;
    self.is_knocked_out = False;
  
  def __repr__(self):
    return (
      "Pokemon Name: " + self.name + "\n" +
      "Pokemon Type: " + self.type + "\n" +
      "Pokemon Level: " + str(self.level) + "\n" +
      "Pokemon Heath: " + str(self.health) + "\n" + 
      "Pokemon Damage: " + str(self.damage) + "\n" +
      "Knocked Out? " + self.is_knocked_out
    );

  def attack(self, opponent):
    # effective attack damage

    if ((self.type == "Fire" and opponent.type == "Grass") or (self.type == "Water" and opponent.type == "Fire") or (self.type == "Grass" and opponent.type == "Water")):
      print("\n" + self.name + " attacked " + opponent.name + " for " + str(self.damage * 2) + " It's SUPER effective!");

      if (opponent.health <= 0):
        opponent.is_knocked_out = True;
        time.sleep(2);
        print("\nThe opponent's " + opponent.name + " was knocked out!");

      opponent.health -= self.damage * 2;

    # weak attack damage

    elif ((self.type == "Fire" and opponent.type == "Water") or (self.type == "Water" and opponent.type == "Grass") or (self.type == "Grass" and opponent.type == "Fire")):
      print("\n" + self.name + " attacked " + opponent.name + " for " + str(self.damage / 2) + " It's not very effective...");

      opponent.health -= self.damage / 2;

      if (opponent.health <= 0):
        opponent.is_knocked_out = True;
        time.sleep(2);
        print("\nThe opponent's " + opponent.name + " was knocked out!");

    # normal attack damage

    else:
      print("\n" + self.name + " attacked " + opponent.name + " for " + str(self.damage) + " damage!");

      opponent.health -= self.damage;

      if (opponent.health <= 0):
        opponent.is_knocked_out = True;
        time.sleep(2);
        print("\nThe opponent's " + opponent.name + " was knocked out!");

  def heal(self):
    print("You used a potion on your " + self.name + " it healed 20 HP (health points)!");

    self.health += 20;

charmander = Pokemon("Charmander", "Fire", random.randint(1, 10));
squirtle = Pokemon("Squirtle", "Water", random.randint(1, 10));
balbasaur = Pokemon("Balbasaur", "Grass", random.randint(1, 10));
cyndaquil = Pokemon("Cyndaquil", "Fire", random.randint(1, 10));
totodile = Pokemon("Totodile", "Water", random.randint(1, 10));
treeko = Pokemon("Treeko", "Grass", random.randint(1, 10));
popplio = Pokemon("Popplio", "Water", random.randint(1, 10));
chikorita = Pokemon("Chikorita", "Grass", random.randint(1, 10));

trainer_one_pokemon = [];
trainer_two_pokemon = [];

# Trainer class
class Trainer:
  def __init__(self, name, trainer_one_pokemon, trainer_two_pokemon, player_num):
    self.name = name;
    self.tra1_pokemon = trainer_one_pokemon;
    self.tra2_pokemon = trainer_two_pokemon;
    self.active_pokemon = None;
    self.player_num = player_num;
    self.num_potions = 5;
  
  def __repr__(self):
    if self.player_num == 1:
      return (
        "Trainer Name: " + self.name + "\n" +
        "Pokemon: " + self.tra1_pokemon + "\n" +
        "Opponent's Pokemon: " + self.tra2_pokemon + "\n" +
        "Active Pokemon: " + self.active_pokemon + "\n" +
        "Player Number: " + self.player_num + "\n" +
        "Number of Potions: " + self.num_potions
      );

    elif self.player_num == 2:
      return (
        "Trainer Name: " + self.name + "\n" +
        "Pokemon: " + self.tra2_pokemon + "\n" +
        "Opponent's Pokemon: " + self.tra1_pokemon + "\n" +
        "Active Pokemon: " + self.active_pokemon + "\n" +
        "Player Number: " + self.player_num + "\n" +
        "Number of Potions: " + self.num_potions
      );

  # Trainer Name
  def enter_name(self):
    if self.player_num == 1:
      self.name = input("\nWelcome! player 1, please enter your name.\n");

    if self.player_num == 2:
      self.name = input("\nWelcome! player 2, please enter your name.\n");

  # Choose active pokemon
  def use_pokemon(self):
    # Initialization
    pokemon_names1 = [];
    for pokemon1 in self.tra1_pokemon:
      if pokemon1.is_knocked_out:
        return;
      else:
        pokemon_names1.append(pokemon1.name.lower());

    pokemon_names2 = [];
    for pokemon2 in self.tra2_pokemon:
      if pokemon2.is_knocked_out:
        return;
      else:
        pokemon_names2.append(pokemon2.name.lower());

    # Trainer One

    if self.player_num == 1:
      trainer_one_pokemon_str_arr = [];
      tra1_pokemon_obj = {};

      for pokemon in self.tra1_pokemon:
        pokemon_names = [];
        pokemon_names.append(pokemon.name);
        trainer_one_pokemon_str_arr.append(pokemon.name);

        for name in pokemon_names:
          tra1_pokemon_obj.update({ name.lower(): pokemon });

      trainer_one_pokemon_str = ", ".join(trainer_one_pokemon_str_arr);

      use_choice1 = input("\n" + self.name + " you currently have these pokemon: " + trainer_one_pokemon_str + " which pokemon would you like to use?\n").lower();

      while True:
        try:
          if pokemon_names1.index(use_choice1) != None:
            self.active_pokemon = tra1_pokemon_obj.get(use_choice1);
        except:
          print("\nSorry, could you please type a pokemon that you have.");

          time.sleep(3);

          use_choice1 = input("\nEither type " + trainer_one_pokemon_str + " to use for battle!\n").lower();
          continue;
        break;

    # Trainer Two

    elif self.player_num == 2:
      trainer_two_pokemon_str_arr = [];
      tra2_pokemon_obj = {};

      for pokemon in self.tra2_pokemon:
        pokemon_names = [];
        pokemon_names.append(pokemon.name);
        trainer_two_pokemon_str_arr.append(pokemon.name);

        for name in pokemon_names:
          tra2_pokemon_obj.update({ name.lower(): pokemon });

      trainer_two_pokemon_str = ", ".join(trainer_two_pokemon_str_arr);

      use_choice2 = input("\n" + self.name + " you currently have these pokemon: " + trainer_two_pokemon_str + " which pokemon would you like to use?\n").lower();

      while True:
        try:
          if pokemon_names2.index(use_choice2) != None:
            self.active_pokemon = tra2_pokemon_obj.get(use_choice2);
        except:
          print("\nSorry, could you please type a pokemon that you have.");

          time.sleep(3);

          use_choice2 = input("\nEither type " + trainer_two_pokemon_str + " to use for battle!\n").lower();
          continue;
        break;

  def choose_option(self, opponent):
    # Trainer One

    if self.player_num == 1:
      if self.active_pokemon.is_knocked_out:
        if len(self.tra1_pokemon) == 0:
          print("\nCongrats! " + opponent.name + ", you won!");
          sys.exit(1);

        elif len(self.tra2_pokemon) != 0:
          print("\n" + self.name + ", your active pokemon " + self.active_pokemon.name + " was knocked out! Please switch your pokemon.");
          time.sleep(2.5);
          self.use_pokemon();

      else:
        option_choice = input("\n" + self.name + ", would you like to attack, heal or switch your active pokemon?\n").lower();

        while option_choice != "attack" and option_choice != "heal" and option_choice != "switch":
          option_choice = input("\nPlease make sure you typed either attack, heal, or switch\n");

        if option_choice == "attack":
          self.active_pokemon.attack(opponent.active_pokemon);

        elif option_choice == "heal":
          if self.num_potions <= 0:
            print("\nYou out of healing potions you cannot heal you pokemon select a different option.\n");
            time.sleep(2);
            self.choose_option(opponent);
          else:
            self.active_pokemon.heal();
            self.num_potions -= 1;

        elif option_choice == "switch":
          self.use_pokemon();

  # Trainer Two

    elif self.player_num == 2:
      if self.active_pokemon.is_knocked_out:
        if len(self.tra2_pokemon) == 0:
          print("\nCongrats! " + opponent.name + ", you won!");
          sys.exit(1);

        elif len(self.tra2_pokemon) != 0:
          print("\n" + self.name + ", your active pokemon " + self.active_pokemon.name + " was knocked out! Please switch your pokemon.");
          time.sleep(2.5);
          self.use_pokemon();


      else:
        option_choice = input("\n" + self.name + ", would you like to attack, heal or switch your active pokemon?\n").lower();

        while option_choice != "attack" and option_choice != "heal" and option_choice != "switch":
          option_choice = input("\nPlease make sure you typed either attack, heal, or switch\n");

        if option_choice == "attack":
          self.active_pokemon.attack(opponent.active_pokemon);

        elif option_choice == "heal":
          if self.num_potions <= 0:
            print("\nYou out of healing potions you cannot heal you pokemon select a different option.\n");
            time.sleep(2);
            self.choose_option(opponent);
          else:
            self.active_pokemon.heal();
            self.num_potions -= 1;

        elif option_choice == "switch":
          self.use_pokemon();

# INITIALIZATION
trainer_one = Trainer("", trainer_one_pokemon, trainer_two_pokemon, 1);


trainer_two = Trainer("", trainer_one_pokemon, trainer_two_pokemon, 2);


# SETUP
trainer_one.enter_name();
trainer_two.enter_name();

print("\nIt's time to select your pokemon!");

time.sleep(2);

# POKEMON SELECTING
# First pokemon selection
first_choice = input("\n" + trainer_one.name + ", Would you rather have a Charmander or a Squirtle?\n").lower();

while first_choice != "charmander" and first_choice != "squirtle":
  first_choice = input("\nPlease make sure you either typed in Charmander or Squirtle as your choice.\n").lower();

if first_choice == "charmander":
  trainer_one_pokemon.append(charmander);
  trainer_two_pokemon.append(squirtle);

elif first_choice == "squirtle":
  trainer_one_pokemon.append(squirtle);
  trainer_two_pokemon.append(charmander);

# Second pokemon selection
second_choice = input("\n" + trainer_two.name + ", Would you rather have a Balbasaur or Cyndaquil?\n").lower();

while second_choice != "balbasaur" and second_choice != "cyndaquil":
  second_choice = input("\nPlease make sure you either typed in Balbasaur or Cyndaquil as your choice.\n").lower();

if second_choice == "balbasaur":
  trainer_two_pokemon.append(balbasaur);
  trainer_one_pokemon.append(cyndaquil);

elif second_choice == "cyndaquil":
  trainer_two_pokemon.append(cyndaquil);
  trainer_one_pokemon.append(balbasaur);

# Third pokemon selection
third_choice = input("\n" + trainer_one.name + ", Would you rather have a Totodile or a Treeko\n").lower();

while third_choice != "totodile" and third_choice != "treeko":
  third_choice = input("\nPlease make sure you either typed in Totodile or Treeko as your choice.\n").lower();

if third_choice == "totodile":
  trainer_one_pokemon.append(totodile);
  trainer_two_pokemon.append(treeko);

elif third_choice == "treeko":
  trainer_one_pokemon.append(treeko);
  trainer_two_pokemon.append(totodile);

# Fourth pokemon selection
fourth_choice = input("\n" + trainer_two.name + ", Would you rather have a Popplio or a Chikorita?\n").lower();

while fourth_choice != "popplio" and fourth_choice != "chikorita":
  fourth_choice = input("\nPlease make sure you either typed in Popplio or Chikorita as your choice.\n").lower();

if fourth_choice == "popplio":
  trainer_two_pokemon.append(popplio);
  trainer_one_pokemon.append(chikorita);

elif fourth_choice == "chikorita":
  trainer_two_pokemon.append(chikorita);
  trainer_one_pokemon.append(popplio);

print("\nAll done!");

time.sleep(2);

# BATTLE TIME!
print("\nIt's time for battle!");

time.sleep(2);

trainer_one.use_pokemon();
trainer_two.use_pokemon();

trainer_one_turn = True;
trainer_two_turn = False;

while True:
  if trainer_one_turn:
    trainer_one.choose_option(trainer_two);
    trainer_one_turn = False;
    trainer_two_turn = True;
  elif trainer_two_turn:
    trainer_two.choose_option(trainer_one);
    trainer_two_turn = False;
    trainer_one_turn = True;

  for pokemon in trainer_one_pokemon:
    if (pokemon.is_knocked_out == True):
      trainer_one_pokemon.remove(pokemon);

  for pokemon in trainer_two_pokemon:
    if (pokemon.is_knocked_out == True):
      trainer_two_pokemon.remove(pokemon);
