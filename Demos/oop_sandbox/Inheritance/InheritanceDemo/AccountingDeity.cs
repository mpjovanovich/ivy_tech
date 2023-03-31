
namespace InheritanceDemo;

// In this class we inerit from our Deity base class. It allows us to use the members defined in Deity.
// All of the "core" things that a deity can do are in here.
public class AccountingDeity( string name, Gender gender ) : Deity( name, Disposition.Evil, gender )
{
    public void Sing()
    {
        // Note that we're calling a protected method from the base class - we have access to any protected members from the base.
        Console.WriteLine( TranslateToCommonVoice( "...*mumbles*...fiscal responsibility...*unintelligibe sounds*...took my stapler." ) );
    }
}