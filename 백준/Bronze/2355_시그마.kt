// https://www.acmicpc.net/problem/2355  시그마
import kotlin.math.abs

fun main() {

    val (a, b) = readln().split(' ').map { it.toLong() }    // int로 받으면 안됨.

    println( ( ( (a + b.toDouble() ) / 2 ) * ( abs(a - b) + 1) ).toInt() )
   // toFloat()하면 안됨. toDouble()하거나 1.0 곱해야 함.(소수점이 있는 수는 컴파일러가 Double 타입으로 추론한다.)
}

/* 코틀린 정수 자료형 : byte, short, int, long
int : 4바이트 ( -2^31 ~ 2^31 -1 )
long : 8바이트 ( -2^63 ~ 2^63 -1 )
*/

/* 코틀린 실수 자료형
  bits / significant bits / exponent bits / decimal digits
Float	32	24	8	6-7
Double	64	53	11	15-16
*/
