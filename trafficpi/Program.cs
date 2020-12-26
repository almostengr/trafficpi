namespace Almostengr.TrafficPi
{
    class Program
    {
        static void Main(string[] args)
        {
            TrafficControl control = new TrafficControl();
            control.RunControl(args);
        }
    }
}
