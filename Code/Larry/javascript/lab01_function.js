function runGradingLab() {
  let user_number = document.querySelector('#user_number').value
  if (user_number > 100) {
      alert("That number is too large!")
  } else if (user_number <  0) {
      alert("That number is less than zero!")
  } else if (user_number >= 90 && user_number <= 100) {
      alert("You got an A! Great job!!")
  } else if (user_number >= 80 && user_number < 90) {
      alert("You got a B! Good job!")
  } else if (user_number >= 70 && user_number < 80) {
      alert("You got a C. Not bad.")
  } else if (user_number >= 60 && user_number < 70) {
      alert("You got a D. Umm, did you study?")
  } else {
      alert("That's an F. D'oh!")
  }
  document.querySelector('#user_number').value = ''
}
