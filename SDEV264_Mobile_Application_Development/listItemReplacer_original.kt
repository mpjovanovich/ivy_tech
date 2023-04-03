/** 
 * This "replace list item" program acceps two arguments:
 * The first is the item in the shopping list to be replaced.
 * The second is the item that will replace the first.
*/
fun main(args: Array<String>) {
    var shoppingList = mutableListOf( "apple", "banana", "orange" )
    var newShoppingList = mutableListOf<String>()    
    
    // We can use the arguments that were passed into the main function for our
    // replacement below.
    for (item in shoppingList) {
        if (item == args[0]) newShoppingList.add(args[1]) else newShoppingList.add(item)
    }  
    
    println ("Old list: $shoppingList")
    println ("New list: $newShoppingList")
}