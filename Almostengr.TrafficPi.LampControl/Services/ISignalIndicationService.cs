namespace Almostengr.TrafficPi.LampControl.Services
{
    public interface ISignalIndicationService
    {
        void RedLight();
        void YellowLight();
        void GreenLight();
        void RedYellowLights();
        void YellowGreenLights();
        void RedGreenLights();
        void AllLights();
        void NoLights();
        
        void InitializeLights();
        void ShutdownLights();
    }
}