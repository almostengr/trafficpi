using Almostengr.TrafficPi.LampControl.Common;

namespace Almostengr.TrafficPi.LampControl.Services
{
    public class CarWaitingSensorService : ISensorService
    {
        private readonly IGpioService _gpioService;

        public CarWaitingSensorService(IGpioService gpioService)
        {
            _gpioService = gpioService;
            _gpioService.OpenInputPin(InputPin.CarSensor);
        }

        public bool IsButtonPressed(int pinNumber)
        {
            return _gpioService.IsButtonPressed(pinNumber);
        }
    }
}