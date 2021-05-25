using System;
using System.Device.Gpio;
using System.Threading;
using System.Threading.Tasks;
using Microsoft.Extensions.Logging;

namespace Almostengr.TrafficPi.LampControl.Workers
{
    public class FlashYellowWorker : BaseWorker
    {
        private readonly AppSettings _appSettings;
        private readonly GpioController _gpio;

        public FlashYellowWorker(ILogger<FlashYellowWorker> logger, GpioController gpio, AppSettings appSettings) :
            base(logger, appSettings)
        {
            _appSettings = appSettings;
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
                ChangeSignal(LampOff, LampOff, LampOff, _gpio);
                await Task.Delay(TimeSpan.FromMilliseconds(FlasherDelay), stoppingToken);

                ChangeSignal(LampOff, LampOn, LampOff, _gpio);
                await Task.Delay(TimeSpan.FromMilliseconds(FlasherDelay), stoppingToken);
            }
        }

    }
}