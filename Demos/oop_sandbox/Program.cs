// All of the libraries/packages that we need will be imported via these "using" statements.
using EncapsulationDemo;
using InheritanceDemo;

// This is our main function.
static public void Main(string[] args) 
{
    DoEcapsulationDemo();
}

static private void DoEcapsulationDemo()
{
    // Create an instance of the Exploder class.
    Exploder exploder = new Exploder();

    // Note that "Explode" is the only method available to use - it's all we need to know about as a user of this class.
    Exploder.Explode();
}