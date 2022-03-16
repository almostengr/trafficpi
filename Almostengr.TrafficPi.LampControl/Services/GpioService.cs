using System.Device.Gpio;

namespace Almostengr.TrafficPi.LampControl.Services
{
    public class GpioService : IGpioService
    {
        private readonly GpioController _gpioController;

        public GpioService(GpioController gpioController)
        {
            _gpioController = gpioController;
        }

        public void OpenOutputPin(int pinNumber)
        {
            _gpioController.OpenPin(pinNumber, PinMode.Output);
        }

        public void OpenOutputPins(int[] pinNumbers)
        {
            foreach (var pinNumber in pinNumbers)
            {
                OpenOutputPin(pinNumber);
            }
        }

        public void CloseOutputPins(int[] pinNumbers)
        {
            foreach (var pinNumber in pinNumbers)
            {
                CloseOutputPin(pinNumber);
            }
        }

        public void CloseOutputPin(int pinNumber)
        {
            _gpioController.ClosePin(pinNumber);
        }

        public void TurnOnGpio(int pinNumber)
        {
            _gpioController.Write(pinNumber, PinValue.High);
        }

        public void TurnOffGpio(int pinNumber)
        {
            _gpioController.Write(pinNumber, PinValue.Low);
        }

        public void TurnOnGpio(int[] pinNumbers)
        {
            foreach(var pinNumber in pinNumbers)
            {
                TurnOnGpio(pinNumber);
            }
        }

        public void TurnOffGpio(int[] pinNumbers)
        {
            foreach(var pinNumber in pinNumbers)
            {
                TurnOffGpio(pinNumber);
            }
        }
    }
}