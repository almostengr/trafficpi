namespace Almostengr.TrafficPi
{
    class Program
    {
        static void Main(string[] args)
        {
            ITrafficControl control = new MockControl();
            // control.RunControl(args);
            control.RunControl();
        }
    }
}
