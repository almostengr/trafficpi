using System;
using System.Device.Gpio;
using System.Threading;
using System.Threading.Tasks;
using Microsoft.Extensions.Logging;

namespace Almostengr.TrafficPi.LampControl.Workers
{
    public class RedLightGreenLightWorker : BaseWorker
    {
        private readonly GpioController _gpio;

        public RedLightGreenLightWorker(ILogger<FlashGreenWorker> logger, GpioController gpio) : 
            base(logger)
        {
            _gpio = gpio;
        }

        public override Task StartAsync(CancellationToken cancellationToken)
        {
            InitializeGpio(_gpio);
            return base.StartAsync(cancellationToken);
        }

        public override Task StopAsync(CancellationToken cancellationToken)
        {
            ShutdownGpio(_gpio);
            return base.StopAsync(cancellationToken);
        }

        protected override async Task ExecuteAsync(CancellationToken stoppingToken)
        {
            int wait;

            while (!stoppingToken.IsCancellationRequested)
            {
                ChangeSignal(LampOn, LampOff, LampOff, _gpio);
                wait = random.Next(2, 10);
                await Task.Delay(TimeSpan.FromSeconds(wait), stoppingToken);

                ChangeSignal(LampOff, LampOff, LampOn, _gpio);
                wait = random.Next(1, 4);
                await Task.Delay(TimeSpan.FromSeconds(wait), stoppingToken);
            }
        }
    }
}