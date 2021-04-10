using System.Device.Gpio;

namespace Almostengr.TrafficPi.Signal.Enumerables
{
    public static class LampState
    {
        public static PinValue On {
            get {
                return PinValue.High;
            }
        }
        public static PinValue Off {
            get {
                return PinValue.Low;
            }
        }
        
    }
}