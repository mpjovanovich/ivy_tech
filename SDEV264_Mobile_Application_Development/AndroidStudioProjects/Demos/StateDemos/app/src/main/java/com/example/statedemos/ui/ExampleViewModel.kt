package com.example.statedemos.ui

import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.setValue
import androidx.lifecycle.ViewModel

// The rules to handle UI updates and any logic that's not trivial go in the ViewModel.
// It also ensures that state persists through configuration changes.
class ExampleViewModel : ViewModel() {
    private val KILOMETERS_PER_MILE = 1.609344

    // These variables can only be set within this ViewModel class because they have
    // private setters. We never want the UI to set these directly - they are changed within
    // the current class.

    // Since this is going to be changed by the text field, we wrap it in a mutable state object
    // with the mutableStateOf function.
    var distance by mutableStateOf("")
        private set
    // The UI can't change this field, but it can read it.
    var unit: DistanceUnit = DistanceUnit.Miles
        private set

    fun convertUnit() {
        if (unit == DistanceUnit.Miles ){
            distance = convertMilesToKilometers(distance.toDouble())
            unit = DistanceUnit.Kilometers
        } else if (unit == DistanceUnit.Kilometers) {
            distance = convertKilometersToMiles(distance.toDouble())
            unit = DistanceUnit.Miles
        }
    }

    fun updateDistance(newDistance: String){
        distance = newDistance
    }

    private fun convertKilometersToMiles(kilometers: Double): String {
        return (kilometers / KILOMETERS_PER_MILE).toString()
    }

    private fun convertMilesToKilometers(miles: Double): String {
        return (miles * KILOMETERS_PER_MILE).toString()
    }
}

// This defines acceptable values for distance unit of measure
enum class DistanceUnit {
    Miles,
    Kilometers
}
