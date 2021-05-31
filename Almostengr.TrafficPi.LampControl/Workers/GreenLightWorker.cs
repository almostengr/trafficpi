using System;
using System.Device.Gpio;
using System.Threading;
using System.Threading.Tasks;
using Microsoft.Extensions.Logging;

namespace Almostengr.TrafficPi.LampControl.Workers
{
    public class GreenLightWorker : BaseWorker
    {
        private readonly GpioController _gpio;

        public GreenLightWorker(ILogger<BaseWorker> logger, GpioController gpio) : base(logger)
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
            while (!stoppingToken.IsCancellationRequested)
            {
                ChangeSignal(LampOff, LampOff, LampOn, _gpio);
                await Task.Delay(TimeSpan.FromMinutes(1), stoppingToken);
            }
        }
    }
}