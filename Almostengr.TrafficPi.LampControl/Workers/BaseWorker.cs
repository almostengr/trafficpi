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
        private readonly AppSettings _appSettings;
        internal Random random = new Random();
        internal PinValue LampOff = PinValue.High;
        internal PinValue LampOn = PinValue.Low;
        internal const int FlasherDelay = 700;

        public BaseWorker(ILogger<BaseWorker> logger, AppSettings appSettings)
        {
            _logger = logger;
            _appSettings = appSettings;
        }

        protected override async Task ExecuteAsync(CancellationToken stoppingToken)
        {
            throw new NotImplementedException();
        }

        internal void ChangeSignal(PinValue redLight, PinValue yellowLight, PinValue greenLight, GpioController gpio)
        {
            gpio.Write(_appSettings.RedLightPin, redLight);
            gpio.Write(_appSettings.YellowLightPin, yellowLight);
            gpio.Write(_appSettings.GreenLightPin, greenLight);
        }

        internal GpioController ShutdownGpio(GpioController gpio)
        {
            _logger.LogInformation("Shutting down traffic controller");

            gpio.Write(_appSettings.RedLightPin, LampOff);
            gpio.Write(_appSettings.YellowLightPin, LampOff);
            gpio.Write(_appSettings.GreenLightPin, LampOff);

            gpio.ClosePin(_appSettings.RedLightPin);
            gpio.ClosePin(_appSettings.YellowLightPin);
            gpio.ClosePin(_appSettings.GreenLightPin);
            
            return gpio;
        }

        internal void InitializeGpio(GpioController gpio)
        {
            _logger.LogInformation("Initializing traffic controller");

            gpio.OpenPin(_appSettings.RedLightPin, PinMode.Output);
            gpio.OpenPin(_appSettings.YellowLightPin, PinMode.Output);
            gpio.OpenPin(_appSettings.GreenLightPin, PinMode.Output);
        }

        internal int YellowDelay()
        {
            return random.Next(1, 5);
        }

        internal int RedGreenDelay()
        {
            return random.Next(5, 60);
        }
    }
}