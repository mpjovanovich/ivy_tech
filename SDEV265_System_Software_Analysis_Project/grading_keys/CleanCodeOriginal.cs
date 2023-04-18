using System;
using System.Collections.Generic;

public class Program
{
	private static void Main()
	{
		// Program execution will begin here.
		// If you don't have a way to run a C# program, you can use this link:
		// https://www.programiz.com/csharp-programming/online-compiler/
		RunProgram();
	}

	private static void RunProgram()
	{
		// Commands for quit, add, print.
		var commands = new List<char>() { 'q', 'a', 'p' };

		// This is a list of x,y coordinates.
		var points = new List<(double x, double y)>();

		// Here we add an initial set of items to the list.
		points.Add( (1.0, 2.2) );
		points.Add( (1.3, 2.2) );
		points.Add( (4.0, 2.7) );
		points.Add( (1.0, 3.2) );

		while( true )
		{
			char command;
			Console.Write( "Press 'a' to add a point, 'p' to print points, or 'q' to quit: " );
			while( !Char.TryParse( Console.ReadLine(), out command ) || !commands.Contains( command ) ) 
			{
				Console.WriteLine( "Invalid command." );
				Console.Write( "Press 'a' to add a point, 'p' to print points, or 'q' to quit: " );
			}

			if( command == 'q' )
			{
				// Exit the loop.
				break;
			}
			else if( command == 'a' )
			{
				double x;
				double y;

				// Add a point to the list.
				Console.Write( "Enter a value for x: " );
				while( !Double.TryParse( Console.ReadLine(), out x) ) 
				{
					Console.WriteLine( "Invalid value." );
					Console.Write( "Enter a value for x: " );
				}

				Console.Write( "Enter a value for y: " );
				while( !Double.TryParse( Console.ReadLine(), out y ) )
				{
					Console.WriteLine( "Invalid value." );
					Console.Write( "Enter a value for y: " );
				}

				points.Add( (x, y) );
			}
			else if( command == 'p' )
			{
				// Print the x and y coordinate of each point in the list.
				Console.WriteLine( "Existing points:" );
				foreach( var point in points )
					Console.WriteLine( $"x = {point.x}, y = {point.y}" );
			}

			// Add a spacer line between commands to make input look neater.
			Console.WriteLine();
		}
	}
}