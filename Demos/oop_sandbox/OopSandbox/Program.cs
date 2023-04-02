using EncapsulationDemo;
using InheritanceDemo;

namespace OopSandbox;

internal class Program
{
	// The program starts in this function. You can umcomment methods as you like.
	static void Main( string[] args )
	{
		//DoEcapsulationDemo();
		//DoInheritanceDemo();
	}

	// TODO: InterfaceDemo

	static void DoEcapsulationDemo()
	{
		// Create an instance of the Exploder class.
		Exploder exploder = new Exploder();

		// We can access TimesExploded because it is publically exposed.
		Console.WriteLine( $"Exploder object has exploded {exploder.TimesExploded} times" );

		// Note that "Explode" is the only method available to use (publically exposed) - it's all we need to know about as a user of this class.
		exploder.Explode();

		// We can access TimesExploded because it is publically exposed.
		Console.WriteLine( $"Exploder object has exploded {exploder.TimesExploded} times" );
	}

	static void DoInheritanceDemo()
	{
		AccountingDeity dennis_from_accounting = new AccountingDeity( "Dennis", Deity.DeityGender.Masculine );
		DoPolymorphismStuff( dennis_from_accounting );

		CompSciDeity turing_of_britannia = new CompSciDeity( "Alan", Deity.DeityGender.Masculine );
		DoPolymorphismStuff( turing_of_britannia );

		// Only the CompSciDeity can write programs, so it's the only deity with this method.
		turing_of_britannia.WriteProgram();

		PoliSciDeity emily_your_ex = new PoliSciDeity( "Emily", Deity.DeityGender.Feminine );
		DoPolymorphismStuff( emily_your_ex );
	}

	static void DoPolymorphismStuff( Deity deity )
	{
		// With polymorphism, we can sub in any deity, because we know all deities implement the methods below.
		// In this case we are calling methods from the base class.
		Console.WriteLine( "Citizens are praying..." );
		deity.ReceivePrayer();
		Console.WriteLine();

		Console.WriteLine( "Citizens are unhappy..." );
		deity.ReceiveInsult();
		Console.WriteLine();

		Console.WriteLine( "Deity is singing..." );
		deity.Sing();
		Console.WriteLine();
	}
}

