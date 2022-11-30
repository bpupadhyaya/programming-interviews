object TwoSumApp {
  def main(args: Array[String]): Unit = {
    val myNUms = List(10, 20, 35, 40, 5, 15, 25)
    val myTarget = 30
    val myResult = twoSum(myNUms, myTarget)
    println(myResult)
  }

  def twoSum(nums: List[Int], target: Int): List[List[Int]] =
    nums.combinations(2).collect {
      case x if x.sum == target =>
        x.map(nums.indexOf)
    }.toList
}