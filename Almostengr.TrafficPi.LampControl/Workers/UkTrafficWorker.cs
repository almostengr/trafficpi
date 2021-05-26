using System;
using System.Device.Gpio;
using System.Threading;
using System.Threading.Tasks;
using Microsoft.Extensions.Logging;

namespace Almostengr.TrafficPi.LampControl.Workers
{
    public class UkTrafficWorker : BaseWorker
    {
        private readonly GpioController _gpio;

        public UkTrafficWorker(ILogger<FlashGreenWorker> logger, GpioController gpio) : 
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
                ChangeSignal(LampOff, LampOff, LampOn, _gpio);
                wait = RedGreenDelay();
                await Task.Delay(TimeSpan.FromSeconds(wait), stoppingToken);

                ChangeSignal(LampOff, LampOn, LampOff, _gpio);
                wait = YellowDelay();
                await Task.Delay(TimeSpan.FromSeconds(wait), stoppingToken);

                ChangeSignal(LampOn, LampOff, LampOff, _gpio);
                wait = RedGreenDelay();
                await Task.Delay(TimeSpan.FromSeconds(wait), stoppingToken);

                ChangeSignal(LampOn, LampOn, LampOff, _gpio);
                wait = YellowDelay();
                await Task.Delay(TimeSpan.FromSeconds(wait), stoppingToken);
            }
        }
    }
}