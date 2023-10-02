using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace coding_best_practice_sandbox
{
	internal static class FileIOUtility
	{
		/************************************************************************
		* Concepts demonstrated:
		* Constants
		* Overloading
		* Input validation
		* Refactoring
		* Static classes/methods
		************************************************************************/

		/************************************************************************
		* In this hypothetical scenario, we have a case where many times in the program we have to write a text file,
		* and the file always has a custom header and footer applied.
		************************************************************************/

		// These constants are "hardcoded", and will not change. We use all caps for constants by convention.
		static private string HEADER_TEXT =
@"THE COW SAYS MOO PRODUCTION COMPANY
___
";

		static private string FOOTER_TEXT =
@"
___
prod{0}.v{1}.d{2:yyyyMMddhhmmsszzz}";

		/////////////////////////////////////////////////////////////////////////////////
		// PUBLIC METHODS
		/////////////////////////////////////////////////////////////////////////////////

		// We can use either an existing file or an in-memory stream. With overloads, it's best to keep functionality in one "base"
		// version, which is then called by others.
		public static void WriteTemplatedTextFile( string destination_path, string source_file )
		{
			if( Path.GetExtension( source_file ).ToLower() != ".txt" )
				throw new ArgumentException( "Cannot create templated file - source file must be a text file." );

			using( FileStream fs = new FileStream( source_file, FileMode.Open ) )
				WriteTemplatedTextFile( destination_path, fs );
		}

		public static void WriteTemplatedTextFile( string destination_path, Stream input_stream )
		{
			// Check for common errors at the beginning of the method.
			if( !Directory.Exists( Path.GetDirectoryName( destination_path ) ) )
				throw new ArgumentException( "Cannot create templated file - the directory for the specified destination path does not exist." );
			if( File.Exists( destination_path ) )
				throw new ArgumentException( "Cannot create templated file - destination path already exists." );

			// "using" statements will make sure system resources are disposed of properly.
			using( FileStream fs = File.Create( destination_path ) )
			{
				fs.Write( Encoding.ASCII.GetBytes( HEADER_TEXT ) );
				input_stream.CopyTo( fs );
				fs.Write( Encoding.ASCII.GetBytes( GetFooterText() ) );
			}
		}

		/////////////////////////////////////////////////////////////////////////////////
		// PRIVATE METHODS
		/////////////////////////////////////////////////////////////////////////////////

		private static string GetFooterText()
		{
			// We'd normally pull things like product code and version number from a configuration file, but I'm fudging it for this demo.
			string product_code = "Asyn";
			string version_number = "2.0.6";

			return String.Format( FOOTER_TEXT, product_code, version_number, DateTime.Now );
		}
	}
}
