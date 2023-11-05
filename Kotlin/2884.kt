// https://www.acmicpc.net/problem/2884  알람 시계

fun main() {
    val ( inputHour, inputMinute ) = readln().split(' ').map { it.toInt() }
    val minuteTime = inputHour*60 + inputMinute + 1440 // 1440은 0시 0분 이하일 때를 대비한 보정값

    val resultTime = ( minuteTime - 45 ) % 1440
    val resultHour = resultTime / 60
    val resultMinute = resultTime % 60
    println( "$resultHour $resultMinute" )

}
