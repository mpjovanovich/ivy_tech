import kotlin.math.*

// You do not need to modify this class.
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

/* 
 * TODO: Create a class for Square here.
 * The class should inherit from the RegularPolygon class.
 * The class should implement any abstract methods from the base class.
 * The class should define a public method named printDetails. 
 * 		This method should call the printDetails method from the RegularPolygon 
 * 		class, passing in the name of the shape as an argument.
 */
 
/* 
 * TODO: Create a class for Triangle here.
 * The class should inherit from the RegularPolygon class.
 * The class should implement any abstract methods from the base class.
 * The class should define a public method named printDetails. 
 * 		This method should call the printDetails method from the RegularPolygon 
 * 		class, passing in the name of the shape as an argument.
 * Note: the area formula for a triangle is: (a^2 * √3)/4, where "a" is the length of one side
 */

// You do not need to modify this function. You may wish to comment / uncomment the lines within
// as you are working through a solution.
fun main() {
    val s1 = Square(1.0)
    s1.printDetails()
    
    val s2 = Square(2.0)
    s2.printDetails()
    
    val t1 = Triangle(1.0)
    t1.printDetails()
    
    val t2 = Triangle(2.0)
    t2.printDetails()
}


// After you're done, you should get the following printout:
/* 
    Square [numSides: 4, sideLength: 1.0, area: 1.0]
    Square [numSides: 4, sideLength: 2.0, area: 4.0]
    Triangle [numSides: 3, sideLength: 1.0, area: 0.4330127018922193]
    Triangle [numSides: 3, sideLength: 2.0, area: 1.7320508075688772]
 */