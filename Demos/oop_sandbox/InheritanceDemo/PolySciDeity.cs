namespace InheritanceDemo;

// A base class is not always abstract. We make it abstract when we don't want to allow this class to be 
// instantiated. If it's abstract, only derived classes can be instantiated. The abstract class is just there
// to provide common functionality.

// All of the "core" things that a deity can do are in here.
public class PoliSciDeity : Deity
{
    public PoliSciDeity( string name, Deity.DeityGender gender ) : base( name, Deity.DeityDisposition.Evil, gender ) { }

    override public void Sing()
    {
        // Note that we're calling a protected method from the base class - we have access to any protected members from the base.
        Console.WriteLine( TranslateToCommonVoice( "I am the growth and decay of a people; I am the its lord and its thief." ) );
    }
}