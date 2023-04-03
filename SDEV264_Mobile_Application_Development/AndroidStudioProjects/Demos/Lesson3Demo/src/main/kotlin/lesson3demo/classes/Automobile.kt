package lesson3demo.classes

import kotlin.math.*

abstract class Automobile(private val turnDegrees: Int, private val velocity:Double, private var heading: Int = 0,
                          private var x: Double = 0.0, private var y: Double = 0.0) {
    /*
     * PUBLIC FUNCTIONS
     */
    /**
     * We will assume the automobile has a position and velocity set at time zero.
     * We do not allow turning while the object is in the "moving" state. It just coasts
     * for however many seconds we put in.
     */
    public fun move(seconds: Int) {
        println ("Moving straight for $seconds seconds...")
        x += cos(Math.toRadians(heading.toDouble())) * velocity * seconds.toDouble()
        y += sin(Math.toRadians(heading.toDouble())) * velocity * seconds.toDouble()
    }

    /**
     * This function turns the vehicle left by the specified units by altering the
     * direction property on the object.
     */
    public fun turnLeft(units: Int = 1) {
        println ("Turning left $units units...")
        turn (turnDegrees * units)
    }

    /**
     * This function turns the vehicle right by the specified units by altering the
     * direction property on the object.
     */
    public fun turnRight(units: Int = 1) {
        println ("Turning right $units units...")
        turn (-1 * turnDegrees * units)
    }

    /**
     * Prints the current x and y coordinates of the automobile, rounded to two decimal places.
     */
    public fun printCoordinates() { println ("${String.format("%.2f", x)}, ${String.format("%.2f", y)}") }

    /**
     * Overrides the default value that will print when we call a print function.
     */
    public override fun toString(): String { return "I am an automobile." }

    /*
     * PROTECTED FUNCTIONS
     */

    /*
     * PRIVATE FUNCTIONS
     */
    private fun turn(degrees: Int) {
        // If we end up over + or - 359, take us back into the range (-359,359)
        heading = (heading+degrees) % 360
        // If we ended up in a negative direction, take us back into positive domain (0,359).
        if (heading < 0) heading = heading + 360
    }
}