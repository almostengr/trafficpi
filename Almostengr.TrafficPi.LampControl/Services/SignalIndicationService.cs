using Almostengr.TrafficPi.LampControl.Common;

namespace Almostengr.TrafficPi.LampControl.Services
{
    public class SignalIndicationService : ISignalIndicationService
    {
        private readonly IGpioService _gpioService;

        public SignalIndicationService()
        {
            _gpioService = new GpioService();
            _gpioService.OpenOutputPins(new[] {LightPin.Red, LightPin.Yellow, LightPin.Green});
        }

        public SignalIndicationService(IGpioService gpioService)
        {
            _gpioService = gpioService;
            _gpioService.OpenOutputPins(new[] {LightPin.Red, LightPin.Yellow, LightPin.Green});
        }
        
        public void AllLights()
        {
            _gpioService.TurnOnGpio(new[] { LightPin.Red, LightPin.Yellow, LightPin.Green });
        }

        public void GreenLight()
        {
            _gpioService.TurnOffGpio(new[] { LightPin.Red, LightPin.Yellow });
            _gpioService.TurnOnGpio(LightPin.Green);
        }

        public void InitializeLights()
        {
            _gpioService.OpenOutputPins(new[] { LightPin.Red, LightPin.Yellow, LightPin.Green });
            _gpioService.TurnOffGpio(new[] { LightPin.Red, LightPin.Yellow, LightPin.Green });
        }

        public void NoLights()
        {
            _gpioService.TurnOffGpio(new[] { LightPin.Red, LightPin.Yellow, LightPin.Green });
        }

        public void RedGreenLights()
        {
            _gpioService.TurnOffGpio(LightPin.Yellow);
            _gpioService.TurnOnGpio(new[] { LightPin.Red, LightPin.Green });
        }

        public void RedLight()
        {
            _gpioService.TurnOffGpio(new[] { LightPin.Yellow, LightPin.Green });
            _gpioService.TurnOnGpio(LightPin.Red);
        }

        public void RedYellowLights()
        {
            _gpioService.TurnOffGpio(LightPin.Green);
            _gpioService.TurnOnGpio(new[] { LightPin.Red, LightPin.Yellow });
        }

        public void ShutdownLights()
        {
            _gpioService.TurnOffGpio(new[] { LightPin.Red, LightPin.Yellow, LightPin.Green });
            _gpioService.CloseOutputPins(new[] { LightPin.Red, LightPin.Yellow, LightPin.Green });
        }

        public void YellowGreenLights()
        {
            _gpioService.TurnOffGpio(LightPin.Red);
            _gpioService.TurnOnGpio(new[] { LightPin.Yellow, LightPin.Green });
        }

        public void YellowLight()
        {
            _gpioService.TurnOffGpio(new[] { LightPin.Red, LightPin.Green });
            _gpioService.TurnOnGpio(LightPin.Yellow);
        }
    }
}
