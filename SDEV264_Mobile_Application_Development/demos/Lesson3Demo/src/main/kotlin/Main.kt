import lesson3demo.classes.*

// We're allowed to pass in a base class as a function argument.
// We can call any public function on that base class, but not protected or private ones.

fun moveVehicle(auto: Automobile, seconds: Int = 1, direction: String? = null, turnUnits: Int? = null ) {
    // Update direction if arguments were provided.
    if (direction == "left") auto.turnLeft (turnUnits ?: 0)
    else if (direction == "right") auto.turnRight (turnUnits ?: 0)

    // Move for the specified number of seconds
    auto.move (seconds)

    // Print new coordinates
    auto.printCoordinates()
}
fun testVehicle( auto: Automobile ) {
    println(auto)

    auto.move(1)
    auto.printCoordinates()

    auto.turnRight()
    auto.move(2)
    auto.printCoordinates()

    auto.turnLeft()
    auto.move(3)
    auto.printCoordinates()
}

fun main(args: Array<String>) {
    val x = 0.0
    val y = 0.0
    val heading = 0

    // Create an instance (object) of the subclass for an Automobile - NormalCar.
    var car = NormalCar( "piece of junk", heading, x, y)
    println(car)
    moveVehicle (car, 1)
    moveVehicle (car, 1, "left",1)
    moveVehicle (car, 2, "right",1)
    println()

    // Create another instance (object) of the subclass for an Automobile - GridCar.
    var gridCar = GridCar("right angle only", heading, x, y)
    println(gridCar)
    moveVehicle (gridCar, 1)
    moveVehicle (gridCar, 1, "left",1)
    moveVehicle (gridCar, 2, "right",1)
    println()

    // Create another instance (object) of the subclass for an Automobile - RocketCar.
    var rocketCar = RocketCar("really really fast", heading, x, y)
    println(rocketCar)
    moveVehicle (rocketCar, 1)
    moveVehicle (rocketCar, 1, "left",45)
    moveVehicle (rocketCar, 2, "right",10)
    println()
}