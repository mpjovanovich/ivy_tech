fun replaceElements(items:MutableList<String>, target:String, replacement:String): MutableList<String> {
	// Data types that can accept a type argument in angle brackets, <>, are called
	// generics.
    var replacedItems = mutableListOf<String>()
    
    for (item in items) {
        if (item == target) replacedItems.add(replacement) else replacedItems.add(item)
    }
    
    return replacedItems
}


/** 
 * This "replace list item" program acceps two arguments:
 * The first is the item in the shopping list to be replaced.
 * The second is the item that will replace the first.
*/
fun main(args: Array<String>) {
    // Sometimes it's best to rename obscure variable names so that
    // it's easier to tell what we're referencing.
    val itemToReplace = args[0]
    val replacementItem = args[1]
    
	// If the compiler can infer the type of the collection then we don't have to provide
	// a type argument to the generic.
    var shoppingList = mutableListOf( "apple", "banana", "orange" )
    var newShoppingList = replaceElements(shoppingList, itemToReplace, replacementItem)
    
    println ("Old list: $shoppingList")
    println ("New list: $newShoppingList")
}