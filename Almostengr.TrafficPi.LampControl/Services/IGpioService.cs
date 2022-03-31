using System.Device.Gpio;

namespace Almostengr.TrafficPi.LampControl.Services
{
    public interface IGpioService
    {
        void OpenInputPin(int pinNumber);
        void OpenOutputPin(int pinNumber);
        void OpenOutputPins(int[] pinNumbers);
        void CloseInputPun(int pinNumber);
        void CloseOutputPin(int pinNumber);
        void CloseOutputPins(int[] pinNumbers);
        void TurnOnGpio(int pinNumber);
        void TurnOnGpio(int[] pinNumbers);
        void TurnOffGpio(int pinNumber);
        void TurnOffGpio(int[] pinNumbers);
        bool IsButtonPressed(int pinNumber);
    }
}