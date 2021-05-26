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
        internal Random random = new Random();
        internal PinValue LampOff = PinValue.High;
        internal PinValue LampOn = PinValue.Low;
        internal const int FlasherDelay = 700;
        private const int RedLightPin = 11;
        private const int YellowLightPin = 9;
        private const int GreenLightPin = 10;

        public BaseWorker(ILogger<BaseWorker> logger)
        {
            _logger = logger;
        }

        protected override async Task ExecuteAsync(CancellationToken stoppingToken)
        {
            throw new NotImplementedException();
        }

        internal void ChangeSignal(PinValue redLight, PinValue yellowLight, PinValue greenLight, GpioController gpio)
        {
            gpio.Write(RedLightPin, redLight);
            gpio.Write(YellowLightPin, yellowLight);
            gpio.Write(GreenLightPin, greenLight);
        }

        internal GpioController ShutdownGpio(GpioController gpio)
        {
            _logger.LogInformation("Shutting down traffic controller");

            gpio.Write(RedLightPin, LampOff);
            gpio.Write(YellowLightPin, LampOff);
            gpio.Write(GreenLightPin, LampOff);

            gpio.ClosePin(RedLightPin);
            gpio.ClosePin(YellowLightPin);
            gpio.ClosePin(GreenLightPin);
            
            return gpio;
        }

        internal void InitializeGpio(GpioController gpio)
        {
            _logger.LogInformation("Initializing traffic controller");

            gpio.OpenPin(RedLightPin, PinMode.Output);
            gpio.OpenPin(YellowLightPin, PinMode.Output);
            gpio.OpenPin(GreenLightPin, PinMode.Output);
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