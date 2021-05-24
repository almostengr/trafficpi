using System;
using System.Device.Gpio;
using System.Threading;
using System.Threading.Tasks;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;

namespace Almostengr.TrafficPi.LampControl.Workers
{
    public class BaseWorker : BackgroundService
    {
        private readonly ILogger<BaseWorker> _logger;
        private readonly GpioController _gpioController;
        private readonly AppSettings _appSettings;
        internal Random random = new Random();
        internal PinValue LampOff = PinValue.High;
        internal PinValue LampOn = PinValue.Low;
        internal const int FlasherDelay = 700;

        public BaseWorker(ILogger<BaseWorker> logger, GpioController gpioController, AppSettings appSettings)
        {
            _logger = logger;
            _gpioController = gpioController;
            _appSettings = appSettings;
        }

        public override Task StartAsync(CancellationToken cancellationToken)
        {
            _logger.LogInformation("Starting traffic controller");

            _gpioController.OpenPin(_appSettings.RedLightPin, PinMode.Output);
            _gpioController.OpenPin(_appSettings.YellowLightPin, PinMode.Output);
            _gpioController.OpenPin(_appSettings.GreenLightPin, PinMode.Output);
            
            return base.StartAsync(cancellationToken);
        }

        protected override async Task ExecuteAsync(CancellationToken stoppingToken)
        {
            throw new NotImplementedException();
        }

        public override Task StopAsync(CancellationToken cancellationToken)
        {
            _logger.LogInformation("Shutting down traffic controller");

            _gpioController.Write(_appSettings.RedLightPin, LampOff);
            _gpioController.Write(_appSettings.YellowLightPin, LampOff);
            _gpioController.Write(_appSettings.GreenLightPin, LampOff);

            _gpioController.ClosePin(_appSettings.RedLightPin);
            _gpioController.ClosePin(_appSettings.YellowLightPin);
            _gpioController.ClosePin(_appSettings.GreenLightPin);

            return base.StartAsync(cancellationToken);
        }

        internal void ChangeSignal(PinValue redLight, PinValue yellowLight, PinValue greenLight)
        {
            _gpioController.Write(_appSettings.RedLightPin, redLight);
            _gpioController.Write(_appSettings.YellowLightPin, yellowLight);
            _gpioController.Write(_appSettings.GreenLightPin, greenLight);
        }

        internal bool FlashSignal(int light, bool illuminated)
        {
            ChangeSignal(LampOff, LampOff, LampOff);

            if (illuminated)
            {
                _gpioController.Write(light, LampOff);
                return illuminated;
            }

            _gpioController.Write(light, LampOn);
            return illuminated;
        }

        internal virtual int YellowDelay()
        {
            return random.Next(1, 5);
        }

        internal virtual int RedGreenDelay()
        {
            return random.Next(5, 60);
        }
    }
}