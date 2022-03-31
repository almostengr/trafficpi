namespace Almostengr.TrafficPi.LampControl.Services
{
    public interface ISensorService
    {
        bool IsButtonPressed(int pinNumber);
    }
}