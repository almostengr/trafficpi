using System;
using System.Device.Gpio;
using System.Collections.Generic;
using System.Linq;
using System.Threading;
using System.Threading.Tasks;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using Almostengr.TrafficPi.Signal.Enumerables;

namespace Almostengr.TrafficPi.LampControl.Workers
{
    public class BaseWorker : BackgroundService
    {
        private readonly ILogger<BaseWorker> _logger;
        internal GpioController gpioController;
        internal Random random = new Random();

        public BaseWorker(ILogger<BaseWorker> logger)
        {
            _logger = logger;
            gpioController = new GpioController();
        }

        public override Task StartAsync(CancellationToken cancellationToken)
        {
            gpioController.OpenPin((int)PinColor.Red, PinMode.Output);
            gpioController.OpenPin((int)PinColor.Yellow, PinMode.Output);
            gpioController.OpenPin((int)PinColor.Green, PinMode.Output);
            return base.StartAsync(cancellationToken);
        }

        protected override async Task ExecuteAsync(CancellationToken stoppingToken)
        {

        }

        public override Task StopAsync(CancellationToken cancellationToken)
        {
            _logger.LogInformation("Shutting down");
            gpioController.Write((int)PinColor.Red, PinValue.High);
            gpioController.Write((int)PinColor.Yellow, PinValue.High);
            gpioController.Write((int)PinColor.Green, PinValue.High);
            return base.StartAsync(cancellationToken);
        }

        internal void ChangeSignal(PinValue redLight, PinValue yellowLight, PinValue greenLight)
        {
            gpioController.Write(PinColor.Red, redLight);
            gpioController.Write(PinColor.Yellow, yellowLight);
            gpioController.Write(PinColor.Green, greenLight);
        }
    }
}