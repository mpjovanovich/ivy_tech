package lesson3demo.classes

private const val TURN_DEGREES = 1
private const val VELOCITY = 1.0

// The base constructor is called with arguments passed in for the first two parameters. The code that
// instantiates this object will never be able to modify these values.
class NormalCar(private val carDescription: String, heading: Int = 0, x: Double = 0.0, y: Double = 0.0):
    Automobile(TURN_DEGREES, VELOCITY, heading = heading, x = x, y = y) {
    /**
     * Overrides the default value that will print when we call a print function.
     */
    public override fun toString(): String {
        return super.toString() + "\r\nI am a $carDescription car."
    }
}