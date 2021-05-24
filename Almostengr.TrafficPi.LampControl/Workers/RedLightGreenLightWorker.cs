using System;
using System.Device.Gpio;
using System.Threading;
using System.Threading.Tasks;
using Microsoft.Extensions.Logging;

namespace Almostengr.TrafficPi.LampControl.Workers
{
    public class RedLightGreenLightWorker : BaseWorker
    {
        private readonly ILogger<RedLightGreenLightWorker> _logger;

        public RedLightGreenLightWorker(ILogger<RedLightGreenLightWorker> logger, GpioController gpioController, AppSettings appSettings) : 
            base(logger, gpioController, appSettings)
        {
            _logger = logger;
        }

        protected override async Task ExecuteAsync(CancellationToken stoppingToken)
        {
            int wait;

            while (!stoppingToken.IsCancellationRequested)
            {
                ChangeSignal(LampOn, LampOff, LampOff);
                wait = random.Next(1, 5);
                await Task.Delay(TimeSpan.FromSeconds(wait), stoppingToken);

                ChangeSignal(LampOff, LampOff, LampOn);
                wait = random.Next(1, 4);
                await Task.Delay(TimeSpan.FromSeconds(wait), stoppingToken);
            }
        }
    }
}