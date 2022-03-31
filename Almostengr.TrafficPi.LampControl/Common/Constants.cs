namespace Almostengr.TrafficPi.LampControl.Common
{
    public static class LightPin
    {
        public static readonly int Red = 11;
        public static readonly int Yellow = 9;
        public static readonly int Green = 10;
    }

    public static class DelaySeconds
    {
        public static readonly int Minimum = 5;
        public static readonly int Short = 5;
        public static readonly int Medium = 30;
        public static readonly int Long = 60;
        public static readonly int Maximum = 3600;
    }

    public static class InputPin
    {
        public static readonly int CarSensor = 22;
    }
}