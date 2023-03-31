namespace EncapsulationDemo;

public class Exploder 
{
    private const double START_FUSE_LENGTH = 10.0; // cm
    private const double FUSE_CONSUMPTION_RATE = 1.0; // cm per second

    // PUBLIC PROPERTIES 
    public int TimesExploded { get; set; }

    // PRIVATE PROPERTIES / FIELDS
    private double CurrentFuseLength { get; set; }

    // PUBLIC METHODS
    public void Explode()
    {
        int elapsed_seconds = 0;
        PrimeFuse();
        while( CurrentFuseLength > 0 )
        {
            Console.WriteLine( "Counter: " + elapsed_seconds + " seconds..." );
            Console.WriteLine( "Fuse left: " + CurrentFuseLength + "cm" );
            ConsumeFuse( 1 );
            elapsed_seconds++;
        }
            
        Console.WriteLine( "Counter: RUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUN!!!" );
        Console.WriteLine( "..(*lackluster explosion*)..(*weak puff of smoke*)..." );
        Console.WriteLine();
    }

    // PRIVATE METHODS
    private void PrimeFuse()
    {
        CurrentFuseLength = START_FUSE_LENGTH;
    }
    private void ConsumeFuse( int seconds )
    {
        CurrentFuseLength -= seconds * FUSE_CONSUMPTION_RATE;
    }
}
