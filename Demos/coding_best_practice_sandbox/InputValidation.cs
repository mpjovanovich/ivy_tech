using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace coding_best_practice_sandbox
{
	internal static class AddNumbers
	{
		/************************************************************************
		* Concepts demonstrated:
		* Input validation
		* Refactoring
		* Exception handling
		* Encapsulation
		* Static classes/methods
		************************************************************************/

		/************************************************************************
		* In this simple program, we refactor a method going from worst to best.
		************************************************************************/

		public static void AddTwoNumbers1()
		{
			// Take whatever strings the user put in, convert to long, and add.
			Console.Write( "Enter the first number: " );
			string? input1 = Console.ReadLine();
			long num1 = Convert.ToInt64( input1 );

			Console.Write( "Enter the second number: " );
			string? input2 = Console.ReadLine();
			long num2 = Convert.ToInt64( Console.ReadLine() );

			Console.WriteLine( $"The result is: {num1 + num2}." );
		}

		// Better: increase code readability by nesting Console.Readline - eliminates temp variable
		// that offers no benefit. Temp variables are useful only if they increase code readability.
		// There are many cases where we would want them, e.g. accessing an element from a nested data
		// structure: long current_val = dictionary1[dictionary2[key]];
		public static void AddTwoNumbers2()
		{
			Console.Write( "Enter the first number: " );
			long num1 = Convert.ToInt64( Console.ReadLine() );

			Console.Write( "Enter the second number: " );
			long num2 = Convert.ToInt64( Console.ReadLine() );

			Console.WriteLine( $"The result is: {num1 + num2}." );
		}

		// Better: try/catch block will fail gracefully.
		public static void AddTwoNumbers3()
		{
			try
			{
				Console.Write( "Enter the first number: " );
				long num1 = Convert.ToInt64( Console.ReadLine() );

				Console.Write( "Enter the second number: " );
				long num2 = Convert.ToInt64( Console.ReadLine() );

				Console.WriteLine( $"The result is: {num1 + num2}." );
			}
			catch 
			{ 
				Console.WriteLine( "Something went wrong." );
			}
		}

		// Better: we told the user something useful about the exception, not just a generic garbage message.
		public static void AddTwoNumbers4()
		{
			try
			{
				Console.Write( "Enter the first number: " );
				long num1 = Convert.ToInt64( Console.ReadLine() );

				Console.Write( "Enter the second number: " );
				long num2 = Convert.ToInt64( Console.ReadLine() );

				Console.WriteLine( $"The result is: {num1 + num2}." );
			}
			catch( Exception ex )
			{ 
				Console.WriteLine( ex.Message );
			}
		}

		// Better: We allowed the user to retry if something went wrong with the number conversion.
		public static void AddTwoNumbers5()
		{
			long num1 = 0;
			long num2 = 0;
			bool success = false;

			while( !success )
			{
				try
				{
					Console.Write( "Enter the first number: " );
					num1 = Convert.ToInt64( Console.ReadLine() );
					success = true;
				}
				catch( Exception ex )
				{
					Console.WriteLine( ex.Message );
				}
			}

			success = false;
			while( !success )
			{
				try
				{
					Console.Write( "Enter the second number: " );
					num2 = Convert.ToInt64( Console.ReadLine() );
					success = true;
				}
				catch( Exception ex )
				{
					Console.WriteLine( ex.Message );
				}
			}

			Console.WriteLine( $"The result is: {num1 + num2}." );
		}

		// Better: we used a more specific exception type so that we're not trying to recover from
		// exceptions that have nothing to do with our input validation.
		public static void AddTwoNumbers6()
		{
			long num1 = 0;
			long num2 = 0;
			bool success = false;

			while( !success )
			{
				try
				{
					Console.Write( "Enter the first number: " );
					num1 = Convert.ToInt64( Console.ReadLine() );
					success = true;
				}
				catch( FormatException ex )
				{
					Console.WriteLine( ex.Message );
				}
			}

			success = false;
			while( !success )
			{
				try
				{
					Console.Write( "Enter the second number: " );
					num2 = Convert.ToInt64( Console.ReadLine() );
					success = true;
				}
				catch( FormatException ex )
				{
					Console.WriteLine( ex.Message );
				}
			}

			Console.WriteLine( $"The result is: {num1 + num2}." );
		}

		// Better: Use built in "TryParse" methods from the standard libraries to check for conversion errors
		// instead of throwing exceptions.The code is cleaner and more efficient, as they're built for this exact purpose.
		public static void AddTwoNumbers7()
		{
			long num1 = 0;
			long num2 = 0;

			Console.Write( "Enter the first number: " );
			while( !long.TryParse( Console.ReadLine(), out num1 ) )
			{
				Console.WriteLine( "Input could not be converted to a number. Please try again." );
				Console.Write( "Enter the first number: " );
			}

			Console.Write( "Enter the second number: " );
			while( !long.TryParse( Console.ReadLine(), out num2 ) )
			{
				Console.WriteLine( "Input could not be converted to a number. Please try again." );
				Console.Write( "Enter the second number: " );
			}

			Console.WriteLine( $"The result is: {num1 + num2}." );
		}

		// Better: Extracted common functionality into its own method, GetLongFromConsole.
		// We can succinctly express what we're doing, and limit the responsibility of each function.
		public static void AddTwoNumbers99()
		{
			long num1 = GetLongFromConsole( "Enter the first number: " );
			long num2 = GetLongFromConsole( "Enter the second number: " );
			Console.WriteLine( $"The result is: {num1 + num2}." );
		}

		private static long GetLongFromConsole( string prompt )
		{
			long num;
			Console.Write( prompt );

			while( !long.TryParse( Console.ReadLine(), out num ) )
			{
				Console.WriteLine( "Input could not be converted to a number. Please try again." );
				Console.Write( prompt );
			}

			return num;
		}
	}
}
