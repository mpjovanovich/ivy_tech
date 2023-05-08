
// Main
List<int> _winners = new List<int>();

// Run the functinos 100 times and see which ones finished first.
for ( int i = 0; i < 100; i++ )
	DoSyncStuff( _winners );
	//DoAsyncStuff( _winners );

var ones = _winners.Where( x => x == 1 ).Count();
var twos = _winners.Where( x => x == 2 ).Count();
Console.WriteLine( $"Number of ones: { ones }" );
Console.WriteLine( $"Number of twos: { twos }" );

static void DoSyncStuff( List<int> _winners )
{
	// Create an array/list that will store the results of each function in whichever
	// order they complete.
	var function_complete_list = new List<int>();

	// Run each function synchronously.
	// A synchronous task will block! This means each line will execute in order.
	var func1_result = Func1();
	var func2_result = Func2();

	// Each function will add its result to the complete list.
	function_complete_list.Add( func1_result );
	function_complete_list.Add( func2_result );

	// Add the first function that completed to the winners list.
	_winners.Add( function_complete_list[0] );
}

static void DoAsyncStuff( List<int> _winners )
{
	// Create an array/list that will store the results of each function in whichever
	// order they complete.
	var function_complete_list = new List<int>();
	List<Task> tasks = new List<Task>();

	// Add each function to its own thread of execution (async).
	// Each function will add its result to the complete list.
	// An asynchronous task will not block! This means that the threads can process concurrently
	// (in parallel).
	tasks.Add( Task.Factory.StartNew( () => function_complete_list.Add(Func1()) ) );
	tasks.Add( Task.Factory.StartNew( () => function_complete_list.Add(Func2()) ) );

	// Wait for both threads to finish
	Task.WaitAll( tasks.ToArray() );

	// Add the first function that completed to the winners list.
	_winners.Add( function_complete_list[0] );
}

static int Func1()
{
	System.Threading.Thread.Sleep( 10 );
	return 1;
}

static int Func2()
{
	System.Threading.Thread.Sleep( 10 );
	return 2;
}
