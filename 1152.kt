fun main() {
    val input = readln()
    val myInput = input.trim().split(" ")
    // 빈 문자열 처리

    if (input.isBlank()) {
        println(0)
    } else {
        print(myInput.size)
    }
}