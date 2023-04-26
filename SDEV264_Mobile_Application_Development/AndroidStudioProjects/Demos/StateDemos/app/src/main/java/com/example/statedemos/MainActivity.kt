package com.example.statedemos

import android.os.Bundle
import android.widget.CheckBox
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.material.*
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.materialIcon
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.RectangleShape
import androidx.compose.ui.graphics.Shape
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import com.example.statedemos.ui.ExampleViewModel
import com.example.statedemos.ui.theme.StateDemosTheme
import androidx.lifecycle.viewmodel.compose.viewModel
import com.example.statedemos.ui.DistanceUnit

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            StateDemosTheme {
                // A surface container using the 'background' color from the theme
                Surface(
                    modifier = Modifier.fillMaxSize(),
                    color = MaterialTheme.colors.background
                ) {
//                    UiScopeExample()
//                    HoistedStateExample()
//                    ViewModelExample()
                }
            }
        }
    }
}

/* ***********************************************************
* Scenario 1 - state scoped to composable.
* Best for simple scenarios.
*********************************************************** */
@Composable
fun UiScopeExample() {
    // It makes sense to store "UI state" in the UI itself - the composable function.
    // There's no business logic, and it doesn't represent any kind of persistent data.
    var textVal by remember { mutableStateOf("") }

    Column(
        modifier = Modifier.fillMaxSize(),
        verticalArrangement = Arrangement.Center,
        horizontalAlignment = Alignment.CenterHorizontally
    ) {
        TextField(
            value = textVal,
            onValueChange = { textVal = it }
        )
    }
}

/* ***********************************************************
* Scenario 2 - hoisted state.
* For when you have state that more than one composable will use.
*********************************************************** */
@Composable
fun HoistedStateExample() {
    // This variable is the "hoisted" state.
    // We store it here in the HoistedStateExample composable, then it can be used in any
    // child composables that we pass it to.
    var itemChecked by remember { mutableStateOf(false) }

    Column(
        modifier = Modifier
            .fillMaxSize()
            .padding(20.dp),
        verticalArrangement = Arrangement.Bottom
    ) {
        ItemShower(itemChecked)

        Divider(modifier = Modifier.padding(bottom = 20.dp, top = 20.dp))

        LabeledCheckBox(
            label = "Show item?:",
            checked = itemChecked,
            // This callback function allows the LabeledCheckBox to change the state of itemChecked
            onCheckedChange = { itemChecked = !itemChecked }
        )
    }
}

@Composable
fun LabeledCheckBox(
    label: String,
    checked: Boolean,
    onCheckedChange: (Boolean) -> Unit
) {
    Row(
        modifier = Modifier.fillMaxWidth(),
        verticalAlignment = Alignment.CenterVertically
    ) {
        Text(label)
        Checkbox(checked = checked, onCheckedChange = onCheckedChange )
    }
}

@Composable
fun ItemShower(itemChecked: Boolean) {
    if (itemChecked) {
        Box(
            modifier = Modifier
                .clip(shape = RectangleShape)
                .size(50.dp)
                .background(Color.Red)
                .padding(horizontal = 10.dp)
        )
    }
}

/* ***********************************************************
* Scenario 3 - state from another layer.
* For full fledged applications with business logic.
*********************************************************** */
@Composable
fun ViewModelExample(
    exampleViewModel: ExampleViewModel = viewModel()
) {
    // We can adjust the text on the front end according to the current ViewModel state
    var unitDescription = ""
    if (exampleViewModel.unit == DistanceUnit.Miles) {
        unitDescription = "miles"
    } else if (exampleViewModel.unit == DistanceUnit.Kilometers) {
        unitDescription = "kilometers"
    }

    Column(
        modifier = Modifier.fillMaxSize(),
        verticalArrangement = Arrangement.Center,
        horizontalAlignment = Alignment.CenterHorizontally
    ) {
        TextField(
            value = exampleViewModel.distance,
            onValueChange = { exampleViewModel.updateDistance(it) }
        )
        Button( onClick = { exampleViewModel.convertUnit() } ) {
            Text("Convert to $unitDescription")
        }
    }
}

/* ***********************************************************
* Preview
*********************************************************** */
@Preview(showBackground = true)
@Composable
fun DefaultPreview() {
    StateDemosTheme {
//        UiScopeExample()
//        HoistedStateExample()
        ViewModelExample()
    }
}