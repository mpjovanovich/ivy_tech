// All of the libraries/packages that we need will be imported via these "using" statements.
using EncapsulationDemo;
using InheritanceDemo;

// This is our main function.
//DoEcapsulationDemo();
//DoInheritanceDemo();

// TODO: InterfaceDemo

static void DoEcapsulationDemo()
{
    // Create an instance of the Exploder class.
    Exploder exploder = new Exploder();

    // Note that "Explode" is the only method available to use - it's all we need to know about as a user of this class.
    exploder.Explode();
}

static void DoPolymorphismStuff( Deity deity )
{
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

static void DoInheritanceDemo()
{
    AccountingDeity dennis_from_accounting = new AccountingDeity( "Dennis", Deity.DeityGender.Masculine );
    DoPolymorphismStuff( dennis_from_accounting );

    CompSciDeity turing_of_britannia = new CompSciDeity( "Alan", Deity.DeityGender.Masculine );
    DoPolymorphismStuff( turing_of_britannia );

    // Only the CompSciDeity can write programs.
    turing_of_britannia.WriteProgram();

    PoliSciDeity emily_your_ex = new PoliSciDeity( "Emily", Deity.DeityGender.Feminine );
    DoPolymorphismStuff( emily_your_ex );
}
