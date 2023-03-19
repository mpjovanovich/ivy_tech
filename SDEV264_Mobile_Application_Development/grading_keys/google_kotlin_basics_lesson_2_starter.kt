// This template goes with Lesson2, Functions from the URL:
// https://developer.android.com/courses/pathways/android-development-with-kotlin-2

// Section: 2.1.3.Step1.3
//import java.util.* // This library is needed for randoms

/*
Section: 2.1.3
*/

// Section: 2.1.3.Step1.1
fun feedTheFish() {
    // TODO: Replace function body with your solution
    return Unit
}

// Section: 2.1.3.Step1.2
fun randomDay() : String {
    // TODO: Replace function body with your solution
    return ""
}

// Section: 2.1.3.Step2.1
fun fishFood1(day : String) : String {
    // TODO: Replace function body with your solution
    return ""
}

fun feedTheFish1() {
    val day = randomDay()
    val food = fishFood1(day)
    println ("Today is $day and the fish eat $food")
}

// Section: 2.1.3.Step2.2
fun fishFood2(day : String) : String {
    // TODO: Replace function body with your solution
    return ""
}

fun feedTheFish2() {
    val day = randomDay()
    val food = fishFood2(day)
    println ("Today is $day and the fish eat $food")
}

// Section: 2.1.3.Step2.3
fun fishFood3(day : String) : String {
    // TODO: Replace function body with your solution
    return ""
}

fun feedTheFish3() {
    val day = randomDay()
    val food = fishFood3(day)
    println ("Today is $day and the fish eat $food")
}

/*
Section: 2.1.4
*/

// Section: 2.1.4.Step1.1
fun swim(speed: String = "fast") {
    // TODO: Replace function body with your solution
    return Unit
}

// Section: 2.1.4.Step2.1
fun shouldChangeWater(day: String, temperature: Int = 22, dirty: Int = 20): Boolean {
    // TODO: Replace function body with your solution
    return false
}

// Section: 2.1.4.Step2.2
fun feedTheFish4() {
    val day = randomDay()
    val food = fishFood1(day)
    println("Today is $day and the fish eat $food")
    println("Change water: ${shouldChangeWater(day)}")
}

// Section: 2.1.4.Step3.1
fun isTooHot(temperature: Int) = false // TODO: Replace function body with your solution

fun isDirty(dirty: Int) = false // TODO: Replace function body with your solution

fun isSunday(day: String) = false // TODO: Replace function body with your solution

// Section: 2.1.4.Step3.2
fun shouldChangeWater2(day: String, temperature: Int = 22, dirty: Int = 20): Boolean {
    // TODO: Replace function body with your solution
    return false
}

fun feedTheFish5() {
    val day = randomDay()
    val food = fishFood1(day)
    println("Today is $day and the fish eat $food")
    println("Change water: ${shouldChangeWater2(day)}")
}

/*
Section: 2.1.6
*/

// Section: 2.1.6.Step2.1
fun updateDirty(dirty: Int, operation: (Int) -> Int): Int {
    // TODO: Replace function body with your solution
    return 0
}

// Section: 2.1.6.Step2.3
fun increaseDirty(start: Int) = 0 // TODO: Replace function body with your solution

// Main function - the program execution will start here by convention.
fun main(args: Array<String>): Unit {
    /*
    Section: 2.1.1
    */
    println("Section: 2.1.1")

    // Section: 2.1.1.Step2.1
    println("Hello, world!")

    // Section: 2.1.1.Step4.1
    // TODO: update to match tutorial
    println()

    /*
    Section: 2.1.2
    */
    println()
    println("Section: 2.1.2")

    // Section: 2.1.2.1
    // TODO: update to match tutorial
    val isUnit = Unit
    println(isUnit)

    // Section: 2.1.2.4
    // TODO: update to match tutorial
    val temperature = 10
    val isHot = false
    println(isHot)

    // Section: 2.1.2.5
    // TODO: replace with appropriate contents
    val message = ""
    println(message)

    /*
    Section: 2.1.3
    */
    println()
    println("Section: 2.1.3")

    // Section: 2.1.3.Step1.1
    feedTheFish()

    // Section: 2.1.3.Step2.1
    feedTheFish1()

    // Section: 2.1.3.Step2.2
    feedTheFish2()

    // Section: 2.1.3.Step2.3
    feedTheFish3()

    /*
    Section: 2.1.4
    */
    println()
    println("Section: 2.1.4")

    // Section: 2.1.4.Step1.2
    // TODO: update to match tutorial
    swim() // uses default speed
    swim() // positional argument
    swim() // named parameter

    // Section: 2.1.4.Step2.3
    feedTheFish4()

    // Section: 2.1.4.Step3.3
    feedTheFish5()

    /*
    Section: 2.1.5
    */
    println()
    println("Section: 2.1.5")

    // Section: 2.1.5.Step1.1
    val decorations = listOf ("rock", "pagoda", "plastic plant", "alligator", "flowerpot")

    // Section: 2.1.5.Step1.2
    // TODO: update to match tutorial
    println()

    // Section: 2.1.5.Step2.1
    // TODO: update to match tutorial
    println("eager: ")

    // Section: 2.1.5.Step2.2
    // TODO: update to match tutorial
    println("filtered: ")

    // Section: 2.1.5.Step2.3
    // TODO: update to match tutorial
    println("new list: ")

    // Section: 2.1.5.Step2.5
    val lazyMap = decorations.asSequence().map {
        // TODO: update to match tutorial
    }

    // Section: 2.1.5.Step2.6
    println("lazy: ")
    println("-----")
    println("first: ")
    println("-----")
    println("all: ")

    // Section: 2.1.5.Step2.8
    // TODO: update to match tutorial
    val lazyMap2 = decorations.asSequence().filter {it[0] == 'p'}.map {
        // TODO: update to match tutorial
    }
    println("-----")
    println("filtered: ")

    // Section: 2.1.5.Step2.11
    // TODO: update to match tutorial
    println("-----")
    println("Flat: ")

    /*
    Section: 2.1.6
    */
    println()
    println("Section: 2.1.6")

    // Section: 2.1.6.Step1.1
    // TODO: update to match tutorial
    var dirtyLevel = 20
    //val waterFilter: ...
    //println(waterFilter(dirtyLevel))

    // Section: 2.1.6.Step1.2
    // TODO: update to match tutorial
    //val waterFilter2 = ...
    //println(waterFilter2(dirtyLevel))

    // Section: 2.1.6.Step2.2
    // TODO: update to match tutorial
    //val waterFilter3: ...
    //println(updateDirty(30, waterFilter3))

    // Section: 2.1.6.Step2.3
    // TODO: update to match tutorial
    //println()
}
