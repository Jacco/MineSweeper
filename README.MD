# MineSweeper

MineSweeper is a game where you are faced with the challenge to clear a mine field. A number of mines are hidden in the field.

Each turn the player can choose to mark a location - to indicate that he thinks there is a mine in that location - or he can boldly clear the location. Marking is always safe but if you clearing a location will result in a big explosion and a `GAME OVER`. Luckily its just a game so you can try again 😊

Our finished game will look like this:

| |1|2|3|4|5|6|7|8|9|A|
|-|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|1️⃣| |1️⃣|⏹️|⏹️|⏹️|⏹️|⏹️|⏹️|⏹️|
|2|1️⃣|1️⃣|1️⃣|⏹️|⏹️|⏹️|⏹️|⏹️|⏹️|⏹️|
|3|⏹️|⏹️|⏹️|⏹️|⏹️|⏹️|⏹️|⏹️|⏹️|⏹️|
|4|⏹️|⏹️|⏹️|⏹️|⏹️|⏹️|⏹️|⏹️|⏹️|⏹️|
|5|⏹️|⏹️|⏹️|⏹️|⏹️|⏹️|⏹️|⏹️|⏹️|⏹️|
|6|⏹️|⏹️|⏹️|⏹️|⏹️|⏹️|⏹️|⏹️|⏹️|⏹️|
|7|⏹️|⏹️|⏹️|⏹️|⏹️|⏹️|⏹️|⏹️|⏹️|⏹️|
|8|⏹️|⏹️|⏹️|⏹️|⏹️|⏹️|⏹️|⏹️|⏹️|⏹️|
|9|⏹️|⏹️|⏹️|⏹️|⏹️|⏹️|⏹️|⏹️|⏹️|⏹️|
|A|⏹️|⏹️|⏹️|⏹️|⏹️|⏹️|⏹️|⏹️|⏹️|⏹️|


    row col [mark]: 1 2 m

# Skeleton

The code skeleton given contains the game loop already and displays a `mock` mine field with all `*`s.

It will repeatedly ask the player for input, and display the minefield again.

|1|2|3|4|5|6|7|8|9|A|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|*|*|*|*|*|*|*|*|*|*|
|*|*|*|*|*|*|*|*|*|*|
|*|*|*|*|*|*|*|*|*|*|
|*|*|*|*|*|*|*|*|*|*|
|*|*|*|*|*|*|*|*|*|*|
|*|*|*|*|*|*|*|*|*|*|
|*|*|*|*|*|*|*|*|*|*|
|*|*|*|*|*|*|*|*|*|*|
|*|*|*|*|*|*|*|*|*|*|
|*|*|*|*|*|*|*|*|*|*|

    row col [mark]: 1 2 m

A lot of work still needs to be done! Let's get to it!

To run our game type following in the terminal:

`python mines.py`

# Steps

- step1 - interpret user input
- step2 - add a minefield
- step3 - clear fields
- step4 - add initial mines
- step5 - add game over
- step6 - show mine counts
- step7 - proper display
- step8 - remaining + keep clearing

# Step 1

In the first step we are going to implement interpreting the user input.

```py
return input("row col [mark]: ")
```

When this code is executed is displays `row col [mark]: ` wait for user input (finished with a `return`). This string is then returned from the function.

We expect the user to supply us with 2 or 3 components: the row, the column and some indication wether the user wants to dig or mark the spot.

For the row and column a `coords` constant is already supplied.

To do this we need to:
- `split` the input on whitespace
- convert the first 2 to an integer number (0 based index in the `coords` string)
- if the player enters a 3rd part, we will interpret this `mark` instead of `dig`. This part should be converted to `True` or `False`

# Hints
<details>
  <summary>Click here</summary>
You can either use `variablename.split(' ')` or import the `re` module to do a more fancy `re.split(r'\s+', variablename)`.

You can use `coords.find('A')` will return the 0 based index of the first occurence of `A` in the string, which is `10`.

You can use destructuring to separate the results from the `split` over different variables `row, col, *mark = splitresultarray`.

Using `stringpart.upper()` will make interpeting the player input a bit more tolerant for when the player forgets to use capitals for the alphanumeric coordinates.

You can use `bool(variable)` to convert anything to 
</details>






