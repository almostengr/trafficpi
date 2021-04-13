namespace Almostengr.TrafficPi
{
    class Program
    {
        static void Main(string[] args)
        {
            ITrafficControl control = new ManualControl();
            // control.RunControl(args);
            control.RunControl();
        }
    }
}
