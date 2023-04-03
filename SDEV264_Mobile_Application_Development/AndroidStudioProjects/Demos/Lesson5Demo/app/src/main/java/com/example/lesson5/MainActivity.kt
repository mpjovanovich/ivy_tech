package com.example.lesson5

import android.graphics.Color
import android.opengl.Visibility
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import com.example.lesson5.databinding.ActivityMainBinding

// TO SHOWCASE THIS LAB:
// Layouts -
//  The attributes > layout section
//  Margins
//  Chains
//  Alignment constraints
// Groups - visibility
class MainActivity : AppCompatActivity() {

    // Note that this variable is scoped to the whole class, so that we can access it from any
    // method that we create.
    private lateinit var binding: ActivityMainBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        /*
        * If we uncomment the line below, we will get a runtime error:
        *
        * AndroidRuntime: FATAL EXCEPTION: main
        * Caused by: kotlin.UninitializedPropertyAccessException: lateinit property binding has not
        * been initialized.
        *
        * This is because the actual process of making the views (controls) available to us as
        * properties on the "binding" variable doesn't take place until the "inflate" method is
        * called on that varniable.
        */

        // binding.calculateButton.text = "bla"

        binding = ActivityMainBinding.inflate(layoutInflater)

        setContentView(binding.root)

        binding.testButton.setOnClickListener{ doClickStuff() }
    }

    private fun doClickStuff() {
        // Note - we can set this as often as we want, but it won't change after we set it once.
        binding.mockView1.setBackgroundColor(Color.parseColor("#999999"))

        // This is how we'd get the text to alternate.
        if (binding.textView.text.toString() == "I am a new message...") {
            binding.textView.text = "I am an old message..."
        } else {
            binding.textView.text = null
            binding.textView.text = "I am a new message..."
        }

        // This is how we toggle visibility of a group.
        if (binding.mockGroup.visibility == View.VISIBLE) {
            binding.mockGroup.visibility = View.INVISIBLE
        } else {
            binding.mockGroup.visibility = View.VISIBLE
        }
    }
}