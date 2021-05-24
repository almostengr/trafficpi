using System;
using System.Device.Gpio;
using System.Threading;
using System.Threading.Tasks;
using Microsoft.Extensions.Logging;

namespace Almostengr.TrafficPi.LampControl.Workers
{
    public class UsTrafficWorker : BaseWorker
    {
        private readonly ILogger<UsTrafficWorker> _logger;

        public UsTrafficWorker(ILogger<UsTrafficWorker> logger, GpioController gpioController, AppSettings appSettings) :
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
                wait = random.Next(5, 60);
                await Task.Delay(TimeSpan.FromSeconds(wait), stoppingToken);

                ChangeSignal(LampOff, LampOn, LampOff);
                wait = random.Next(1,5);
                await Task.Delay(TimeSpan.FromSeconds(wait), stoppingToken);

                ChangeSignal(LampOn, LampOff, LampOff);
                wait = random.Next(5,60);
                await Task.Delay(TimeSpan.FromSeconds(wait), stoppingToken);
            }
        }
    }
}