function roll(dice_value) {
  var dices = [4, 6, 8, 10, 20, 100];

  if (dices.includes(dice_value)) {
    result = Math.floor(Math.random() * dice_value) + 1;
    value = "1d" + dice_value;
    return result;
  } else {
    console.log("Enter a valid number: (4, 6, 8, 10, 20, 100)");
  }
}

test = roll(20);
