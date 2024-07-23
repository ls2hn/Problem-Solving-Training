// https://www.acmicpc.net/problem/1547 공

fun main(){
    val num = readln().toInt()      // num : 컵의 위치를 바꾼 횟수 M
    var ball = 1    // 공 위치

    repeat(num) {     //  for (i in 1..num) {  이 코드도 됨
        val (x, y) = readln().split(' ').map { it.toInt() }

        if (ball == x) {
            ball = y
        } else if (ball == y) {
            ball = x
        }

//        ball = when {
//            x == ball -> y
//            y == ball -> x
//            else -> continue
//        }                         // 이 코드도 됨

    }

    print(ball)

}
