
namespace InheritanceDemo;

// In this class we inerit from our Deity base class. It allows us to use the members defined in Deity.
// All of the "core" things that a deity can do are in here.
public class CompSciDeity : Deity
{
    public CompSciDeity( string name, Deity.DeityGender gender ) : base( name, Deity.DeityDisposition.Evil, gender ) { }

	override public void Sing()
    {
        // Note that we're calling a protected method from the base class - we have access to any protected members from the base.
        Console.WriteLine( TranslateToCommonVoice( "I am the architect; mine is the spirit of creation. I am the architect; the world is bound by my imagination alone." ) );
    }

    // We can also add functionality that is specific to the derived class.
    public void WriteProgram()
    {
        Console.WriteLine( TranslateToCommonVoice( "I have written a program. 'Tis good, I shall rest now." ) );
    }
}