/*
// Note - we can leave off the args array if we never use it.
// Note - Kotlin's version of the void type is "kotlin.Unit".

// Short version:
fun main() {
    println ("Hello, world!" )
}
*/

import java.util.* // Needed for randoms

/*
Section: 2.1.3 - Function Definitions
Section: 2.1.4 - Function Definitions
*/
fun randomDay() : String {
	val week = arrayOf("Monday", "Tuesday", "Wednesday", "Thursday",
				"Friday", "Saturday", "Sunday")
	return week[Random().nextInt(week.size)]
}

fun fishFood(day : String) : String {
	return when (day) {
		"Monday" -> "flakes"
		"Wednesday" -> "redworms"
		"Thursday" -> "granules"
		"Friday" -> "mosquitoes"
		"Sunday" -> "plankton"
		else -> "nothing"
	}
}

fun feedTheFish() {
	val day = randomDay()
	val food = fishFood(day)

	println("Today is $day and the fish eat $food")
	println("Change water: ${shouldChangeWater(day)}")
}

fun swim(speed: String = "fast") {
   println("swimming $speed")
}

fun isTooHot(temperature: Int) = temperature > 30

fun isDirty(dirty: Int) = dirty > 30

fun isSunday(day: String) = day == "Sunday"

fun shouldChangeWater(day: String, temperature: Int = 22, dirty: Int = 20): Boolean {
    return when {
        isTooHot(temperature) -> true
        isDirty(dirty) -> true
        isSunday(day) -> true
        else  -> false
    }
}

// Full version:
fun main(args: Array<String>): Unit {
    /*
    Section: 2.1.1 - Output
    */
    println("Section: 2.1.1")

    println("Hello ${args[0]}!")

    /*
    Section: 2.1.2 - Output
    */
    println()
    println("Section: 2.1.2")

    // Will assign kotlin.Unit
    val isUnit = println("This is an expression")
    println(isUnit)

    val temperature = 10
    val isHot = if (temperature > 50) true else false
    println(isHot)

    val message = "The water temperature is ${ if (temperature > 50) 
					"too warm" else "OK" }."
    println(message)

    /*
    Section: 2.1.3 - Output
    */
    println()
    println("Section: 2.1.3")

	feedTheFish()

    /*
    Section: 2.1.4 - Output
    */
    println()
    println("Section: 2.1.4")

	swim()   // uses default speed
	swim("slow")   // positional argument
	swim(speed="turtle-like")   // named parameter

	feedTheFish()

    /*
    Section: 2.1.5 - Output
    */
    println()
    println("Section: 2.1.5")

	val decorations = listOf ("rock", "pagoda", "plastic plant", "alligator", "flowerpot")

	// eager, creates a new list
    val eager = decorations.filter { it [0] == 'p' }
    println("eager: $eager")

	// lazy, will wait until asked to evaluate
    val filtered = decorations.asSequence().filter { it[0] == 'p' }
    println("filtered: $filtered")

	// force evaluation of the lazy list
    val newList = filtered.toList()
    println("new list: $newList")

	val lazyMap = decorations.asSequence().map {
        println("access: $it")
        it
    }
    println("lazy: $lazyMap")
    println("-----")
    println("first: ${lazyMap.first()}")
    println("-----")
    println("all: ${lazyMap.toList()}")

    val lazyMap2 = decorations.asSequence().filter {it[0] == 'p'}.map {
        println("access: $it")
        it
    }
    println("-----")
    println("filtered: ${lazyMap2.toList()}")

	val mysports = listOf("basketball", "fishing", "running")
	val myplayers = listOf("LeBron James", "Ernest Hemingway", "Usain Bolt")
	val mycities = listOf("Los Angeles", "Chicago", "Jamaica")
	val mylist = listOf(mysports, myplayers, mycities)     // list of lists
	println("-----")
	println("Flat: ${mylist.flatten()}")

    /*
    Section: 2.1.6 - Output
    */
    println()
    println("Section: 2.1.6")

    var dirtyLevel = 20
    val waterFilter = { dirty : Int -> dirty / 2 }
    println(waterFilter(dirtyLevel))
}
