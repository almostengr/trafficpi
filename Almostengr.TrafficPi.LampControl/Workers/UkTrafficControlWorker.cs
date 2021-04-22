using System;
using System.Device.Gpio;
using System.Threading;
using System.Threading.Tasks;
using Microsoft.Extensions.Logging;

namespace Almostengr.TrafficPi.LampControl.Workers
{
    public class UkTrafficControlWorker : BaseControlWorker
    {
        private readonly ILogger<UkTrafficControlWorker> _logger;

        public UkTrafficControlWorker(ILogger<UkTrafficControlWorker> logger, GpioController gpioController, AppSettings appSettings) : 
            base(logger, gpioController, appSettings)
        {
            _logger = logger;
        }

        protected override async Task ExecuteAsync(CancellationToken stoppingToken)
        {
            int wait;

            while (!stoppingToken.IsCancellationRequested)
            {
                ChangeSignal(LampOff, LampOff, LampOn);
                wait = RedGreenDelay();
                await Task.Delay(TimeSpan.FromSeconds(wait));

                ChangeSignal(LampOff, LampOn, LampOff);
                wait = YellowDelay();
                await Task.Delay(TimeSpan.FromSeconds(wait));

                ChangeSignal(LampOn, LampOff, LampOff);
                wait = RedGreenDelay();
                await Task.Delay(TimeSpan.FromSeconds(wait));

                ChangeSignal(LampOn, LampOn, LampOff);
                wait = YellowDelay();
                await Task.Delay(TimeSpan.FromSeconds(wait));
            }
        }
    }
}