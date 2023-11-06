// https://www.acmicpc.net/problem/4344 평균은 넘겠지

fun main() {
    val testCase = readln().toInt()
    val result = mutableListOf<String>()

    repeat(testCase) {
        val line = readln().split(' ').map { it.toInt() }.toMutableList()

        line.removeAt(0)    // line.drop(1) : 앞에서부터 한개의 원소 제거하기

        val aboveAverage = line.count { it > line.average() }
        val proportion: Double = aboveAverage / line.size.toDouble() * 100

        val tmpResult = String.format("%.3f", proportion) + "%"
        result.add(tmpResult)

    }

    result.forEach { item ->
        println(item)
    }

}

// https://kotlinworld.com/12#%ED%--%--%EC%-E%A-%ED%--%A-%EC%--%--%--%EB%AA%A-%EB%A-%-D  filter, take, drop 사용법에 관한 글
