import kotlin.math.*

abstract class RegularPolygon(protected val numSides: Int, protected val sideLength: Double) {
    
    init { 
        calculateArea() 
    }
    
    protected fun printDetails( shapeName: String = "Polygon") {
        println ("$shapeName [numSides: $numSides, sideLength: $sideLength, area: $area]")
    }
    
    protected var area: Double? = null
    
    abstract fun calculateArea()
}

class Triangle(sideLength: Double) : RegularPolygon(numSides = 3, sideLength = sideLength) {
    override fun calculateArea() { 
        area = (sideLength * sideLength * sqrt(3.0)) / 4.0
    }
    
    fun printDetails() {
        printDetails( "Triangle" )
    }
}

class Square(sideLength: Double) : RegularPolygon(numSides = 4, sideLength = sideLength) {
    override fun calculateArea() { 
        area = sideLength * sideLength
    }
    
    fun printDetails() {
        printDetails( "Square" )
    }
}

fun main() {
    val s = Square(1.0)
    s.printDetails()
    val t = Triangle(1.0)
    t.printDetails()
}
