namespace InheritanceDemo;

// A base class is not always abstract. We make it abstract when we don't want to allow this class to be 
// instantiated. If it's abstract, only derived classes can be instantiated. The abstract class is just there
// to provide common functionality.

// All of the "core" things that a deity can do are in here.
public abstract class Deity
{
    public enum DeityDisposition
    {
        Good,
        Evil,
        Ambivalent
    }
    public enum DeityGender
    {
        Masculine,
        Feminine,
        Neuter,
        Bigender
    }

    // Constructor
    public Deity( string name, DeityDisposition disposition, DeityGender gender )
    {
        this.Name = name;
        this.Disposition = disposition;
        this.Gender = gender;
    }

    protected string Name { get; set; }
    protected DeityDisposition Disposition { get; set; }
    protected DeityGender Gender { get; set; }

    abstract public void Sing();

    public void ReceiveInsult()
    {
        if( this.Disposition == DeityDisposition.Good )
            Console.WriteLine( TranslateToCommonVoice( "You have offended your God, but have been forgiven." ) );
        else if( this.Disposition == DeityDisposition.Ambivalent )
            Console.WriteLine( TranslateToCommonVoice( "Your God remembers your deeds. Justice will follow its course at the time of my choosing." ) );
        else if( this.Disposition == DeityDisposition.Evil )
            Console.WriteLine( TranslateToCommonVoice( "Woe to you, who live to see such a time. Your destruction is at hand." ) );
    }

    public void ReceivePrayer()
    {
        if( this.Disposition == DeityDisposition.Good )
            Console.WriteLine( TranslateToCommonVoice( "Yea - 'tis indeed right that you worship so." ) );
        else if( this.Disposition == DeityDisposition.Ambivalent )
            Console.WriteLine( TranslateToCommonVoice( "...(*snores*)..." ) );
        else if( this.Disposition == DeityDisposition.Evil )
            Console.WriteLine( TranslateToCommonVoice( "Ah yeah, that's the good stuff... lay it on me." ) );
    }

    protected string TranslateToCommonVoice( string message )
    {
        string pronoun = "his";
        switch( this.Gender )
        {
            case DeityGender.Feminine:
                pronoun = "her";
                break;
            case DeityGender.Neuter:
            case DeityGender.Bigender:
                // TODO: randomize
                break;
            case DeityGender.Masculine:
            default:
                break;
        }

        return String.Format( "The voice of the Almighty {0}, to {1} followers: {2}", this.Name, pronoun, message );
    }
}
