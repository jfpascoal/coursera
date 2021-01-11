package recfun

object RecFun extends RecFunInterface {

  def main(args: Array[String]): Unit = {
    println("Pascal's Triangle")
    for (row <- 0 to 10) {
      for (col <- 0 to row)
        print(s"${pascal(col, row)} ")
      println()
    }
  }

  /**
   * Exercise 1
   */
  def pascal(c: Int, r: Int): Int = {
    if (c == 0 || c == r) 1 else pascal(c - 1, r - 1) + pascal(c, r - 1)
  }

  /**
   * Exercise 2
   */
  def balance(chars: List[Char]): Boolean = {

    def updateOpen(char: Char, open: Int): Int = {
      if (char == '(') open + 1 else if (char == ')') open - 1 else open
    }

    def countOpenParentheses(chars: List[Char], open: Int): Int = {
      val updated = updateOpen(chars.head, open)
      if (updated < 0 || chars.tail.isEmpty) {
        updated
      } else {
        countOpenParentheses(chars.tail, updated)
      }
    }

    if (chars.isEmpty) true else countOpenParentheses(chars, 0) == 0
  }

  /**
   * Exercise 3
   */
  /**
  def countChange(money: Int, coins: List[Int]): Int = {
    if (money == 0 || coins.isEmpty) 0 else
  }
  */
}
