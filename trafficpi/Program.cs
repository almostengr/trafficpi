namespace Almostengr.TrafficPi
{
    class Program
    {
        static void Main(string[] args)
        {
            ITrafficControl control = new ManualControl();
            // ITrafficControl control = new TrafficControl();
            // control.RunControl(args);
            control.RunControl();
        }
    }
}
