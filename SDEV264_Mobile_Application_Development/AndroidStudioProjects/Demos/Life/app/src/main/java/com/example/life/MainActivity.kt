package com.example.life

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.background
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.*
import androidx.compose.material.Button
import androidx.compose.material.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.RectangleShape
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import com.example.life.ui.theme.LifeTheme
import androidx.compose.runtime.getValue
import androidx.compose.runtime.setValue

val GRID_SIZE = 10

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        var lifeGrid = LifeGrid(GRID_SIZE)
        setContent {
            LifeTheme {
                App()
            }
        }
    }
}

fun Modifier.createAliveModifier(): Modifier {
    return this
        .clip(RectangleShape)
        .background(Color.LightGray)
}

fun Modifier.createDeadModifier(): Modifier {
    return this
        .clip(RectangleShape)
        .background(Color.DarkGray)
}

@Composable
fun App(modifier: Modifier = Modifier) {
    var lifeGrid = LifeGrid(GRID_SIZE)
    var grid by remember { mutableStateOf(lifeGrid.grid) }

    Column(
        modifier = Modifier
            .background(Color.Gray)
            .fillMaxSize(),
        horizontalAlignment = Alignment.CenterHorizontally,
        verticalArrangement = Arrangement.Center
    ) {
        GameBoard(grid, lifeGrid.gridSize)
        Button(onClick = { lifeGrid.updateGrid() }) {
            Text("Next Time Step")
        }
    }
}

@Composable
fun GameBoard(grid: Array<BooleanArray>, gridSize: Int, modifier: Modifier = Modifier) {
    Column {
        for (rowIndex in 0 until gridSize) {
            Row {
                for (colIndex in 0 until gridSize) {
                    Cell(grid, rowIndex, colIndex)
                }
            }
        }
    }
}

@Composable
fun Cell(
    grid: Array<BooleanArray>,
    rowIndex: Int,
    colIndex: Int,
    modifier: Modifier = Modifier
) {
    var isAlive by remember { mutableStateOf(grid[rowIndex][colIndex]) }

    var mod = Modifier
        .size(30.dp)
        .padding(2.dp)
        .clickable {
            isAlive = !isAlive
            grid[rowIndex][colIndex] = isAlive
        }

    mod = if (isAlive) mod.createAliveModifier() else mod.createDeadModifier()

    Box(modifier = mod)
}

//@Preview(showBackground = true)
//@Composable
//fun DefaultPreview() {
//    LifeTheme {
//        App()
//    }
//}
