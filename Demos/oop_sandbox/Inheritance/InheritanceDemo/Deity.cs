namespace InheritanceDemo;

// A base class is not always abstract. We make it abstract when we don't want to allow this class to be 
// instantiated. If it's abstract, only derived classes can be instantiated. The abstract class is just there
// to provide common functionality.

// All of the "core" things that a deity can do are in here.
abstract class Deity
{
    public enum Disposition
    {
        Good,
        Evil,
        Ambivalent
    }
    public enum Gender
    {
        Masculine,
        Feminine,
        Neuter,
        Bigender
    }

    // Constructor
    public Deity( string name, Disposition disposition, Gender gender )
    {
        this.Disposition = disposition;
    }

    protected string Name { get; set; }
    protected Disposition Disposition { get; set; } // Good, Evil, or Ambivalent
    protected Gender Gender { get; set; }

    abstract public void Sing();

    public void ReceiveInsult()
    {
        if( this.Disposition == Disposition.Good )
            TranslateToCommonVoice( "You have offended your God, but have been forgiven." );
        else if( this.Disposition == Disposition.Ambivalent )
            TranslateToCommonVoice( "Your God remembers your deeds. Justice will follow its course at the time of my choosing." );
        else if( this.Disposition == Disposition.Evil )
            TranslateToCommonVoice( "Woe to you, who live to see such a time. Your destruction is at hand." );
    }

    public void ReceivePrayer()
    {
        if( this.Disposition == Disposition.Good )
            TranslateToCommonVoice( "Yea - 'tis right that you worship so." );
        else if( this.Disposition == Disposition.Ambivalent )
            TranslateToCommonVoice( "...(*snores*)..." );
        else if( this.Disposition == Disposition.Evil )
            TranslateToCommonVoice( "Ah yeah, that's the good stuff... lay it on me." );
    }

    protected string TranslateToCommonVoice( string message )
    {
        string pronoun = "his";
        switch( this.Gender )
        {
            case Gender.Feminine:
                pronoun = "her";
                break;
            case Gender.Neuter:
            case Gender.Bigender:
                // TODO: randomize
                break;
            case Gender.Masculine:
            default:
                break;
        }

        return String.Format( "The voice of the Almighty {0}, to {1} followers: {2}", this.Name, pronoun, message );
    }
}
