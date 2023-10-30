fun main(){
    var odd = true  // 홀수 줄:true, 짝수 줄:false
    var i = -1      // 줄별 탐색 시작 위치
    var count = 0   // F의 개수

    repeat(8) {
        val line = readln()

        i = when (odd) {
            true -> 0
            else -> 1
        }

        for(j in i..7 step(2))
            if ( line[j] == 'F' )
                count++

        odd = !odd
    }

    print(count)    
}
