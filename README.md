# Papa's Pancakeria Bot

A Python bot that plays [Papa's Pancakeria](https://www.coolmathgames.com/0-papas-pancakeria) automatically. It reads the game state by computing pixel sums of screen regions and drives the game via simulated mouse and keyboard input.

[![Bot playing Papa's Pancakeria](https://img.youtube.com/vi/tgEf2_qM-M4/0.jpg)](https://www.youtube.com/watch?v=tgEf2_qM-M4)

## Background

This project started after following a tutorial that built a similar bot for Sushi Go Round, another Flash cooking game. Papa's Pancakeria was a natural next target.

Over the years it became a recurring project — something to return to whenever there were new things to apply. Each pass left the code noticeably better than the last:

- Early versions used raw lists to represent orders and had all station logic mixed together
- Station logic was separated into dedicated classes (`OrderStation`, `GrillStation`, `BuildStation`, `DrinkStation`)
- Raw order lists were replaced with proper dataclasses (`Order`, `Drink`, `Topping`)
- A priority-based game loop was added so the bot always attends to the grill first, preventing burnt pancakes and failed orders

The end result is less a finished product and more a snapshot of accumulated learning.

## How It Works

### Screen detection

Rather than using image template matching or computer vision, the bot identifies game states by summing the pixel values within fixed screen regions and comparing against pre-computed reference values stored in `src/constants/item_sums.txt`.

For example, to detect whether a customer is waiting at the counter, the bot computes the pixel sum of the order floor area and checks whether it differs from the known "empty" sum. To read an order ticket, it computes the pixel sum of each ticket slot and looks up the result in the ingredient table.

This works because the game renders consistently at a fixed resolution — the same ingredient in the same ticket slot always produces the same pixel sum.

Unknown topping counts prompt for user input and are written back to `item_sums.txt` automatically, so the bot learns as it encounters new combinations.

### Game loop

The main loop in `game_loop.py` runs on a fixed task priority:

```
1. Check the grill — flip or remove finished pancakes
2. Check for new customers
3. Start cooking any orders waiting on the grill
4. Make drinks
5. Build the pancake (apply toppings and sauces)
6. Serve the finished order
```

The bot always handles the highest-priority pending task first, then loops. Grill management takes priority because a burnt pancake fails the order entirely.

### Stations

The game has four stations, each handled by a dedicated class:

| Station | File | Responsibility |
|---------|------|----------------|
| Order | `order_station.py` | Reads customer order tickets via pixel sum lookup. Interprets ingredients, topping counts, and drinks. |
| Grill | `grill_station.py` | Manages the grill. Tracks cook time, triggers flips, and removes finished pancakes. |
| Build | `build_station.py` | Assembles the order — applies base, sauces, and toppings in the correct sequence via click and drag. |
| Drink | `drink_station.py` | Selects cup size, flavour, and any extras for drink orders. |

`station_changer.py` handles navigating between them by clicking the station tabs in the game UI.

## Project Structure

```
run.py                      # CLI entry point
src/
  pancake_bot.py            # Top-level bot (start, continue, first-day handling)
  game_loop.py              # Priority-based main loop
  game_gui.py               # Start game / advance to next day
  station_changer.py        # Switches between game stations
  win_control.py            # pyautogui wrapper (mouse, keyboard, cursor paths)
  ticket_line.py            # Tracks active orders
  order.py                  # Order datatype
  drink.py                  # Drink datatype
  topping.py                # Topping datatype
  sum_area.py               # Pixel sum utility
  tutorial_sequence.py      # Handles the first-day tutorial
  stations/
    order_station.py
    grill_station.py
    build_station.py
    drink_station.py
  constants/
    constants.py            # Screen coordinates and reference pixel sums
    item_sums.txt           # Ingredient fingerprint table (pixel sum → ingredient name)
    toppings.json           # Topping configuration
```

## Requirements

- Python 3
- [pyautogui](https://pyautogui.readthedocs.io/)
- Papa's Pancakeria running in a browser window at a fixed position and resolution

The bot uses hardcoded screen coordinates with an `X_PAD` / `Y_PAD` offset to account for window position. If your browser window is in a different position, update `Coor.X_PAD` and `Coor.Y_PAD` in `src/constants/constants.py`.

## Running

```bash
# Start from the main menu
python run.py

# Resume from a game already in progress
python run.py continue

# Resume, treating the current day as the first day
python run.py continue_first
```

### Debug / development commands

```bash
# Print the pixel sum of a screen region (used to add new ingredients to item_sums.txt)
python run.py sum_area

# Test an individual station action
python run.py build_sauce <topping_name>
python run.py build_topping <topping_name> <count>
python run.py build_base
python run.py make_drink
```

## License

MIT
