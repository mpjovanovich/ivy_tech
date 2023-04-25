package com.example.life

import androidx.compose.runtime.MutableState

class LifeGrid(val gridSize: Int) {

    var grid: Array<BooleanArray>

    init {
        grid = createGrid()
    }

    fun updateGrid() {
        var newGrid = createGrid()
        for(r in 0 until gridSize){
            for(c in 0 until gridSize){
                newGrid[r][c] = evaluateLife(r,c)
            }
        }
        grid = newGrid
    }

    private fun createGrid(): Array<BooleanArray> {
        var cellState = Array(
            gridSize,
            { BooleanArray(gridSize) { false } }
        )
        return cellState
    }

    private fun evaluateLife(row: Int, col: Int): Boolean {
        var isAlive = grid[row][col]
        var livingNeighborCount = 0

        // Convenience variables - it's annoying to read without these.
        val above = row-1
        val below = row+1
        val left = col-1
        val right = col+1

        val hasAbove = above >= 0
        val hasBelow = below < gridSize
        val hasLeft = left >= 0
        val hasRight = right < gridSize

        // Above, above left, above right
        if( hasAbove && grid[above][col] ) livingNeighborCount++
        if( hasAbove && hasLeft && grid[above][left] ) livingNeighborCount++
        if( hasAbove && hasRight && grid[above][right] ) livingNeighborCount++

        // Below, below left, below right
        if( hasBelow && grid[below][col] ) livingNeighborCount++
        if( hasBelow && hasLeft && grid[below][left] ) livingNeighborCount++
        if( hasBelow && hasRight && grid[below][right] ) livingNeighborCount++

        // Left, right...
        if( hasLeft && grid[row][left] ) livingNeighborCount++
        if( hasRight && grid[row][right] ) livingNeighborCount++


        if(isAlive) {
            if(livingNeighborCount < 2 || livingNeighborCount > 3)  isAlive = false
        } else if(livingNeighborCount == 3) {
            isAlive = true
        }

        return isAlive
    }
}