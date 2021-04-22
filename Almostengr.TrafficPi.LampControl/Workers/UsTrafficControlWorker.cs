using System;
using System.Device.Gpio;
using System.Threading;
using System.Threading.Tasks;
using Microsoft.Extensions.Logging;

namespace Almostengr.TrafficPi.LampControl.Workers
{
    public class UsTrafficControlWorker : BaseControlWorker
    {
        private readonly ILogger<UsTrafficControlWorker> _logger;

        public UsTrafficControlWorker(ILogger<UsTrafficControlWorker> logger, GpioController gpioController, AppSettings appSettings) :
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
                await Task.Delay(TimeSpan.FromSeconds(wait));

                ChangeSignal(LampOff, LampOn, LampOff);
                wait = random.Next(1,5);
                await Task.Delay(TimeSpan.FromSeconds(wait));

                ChangeSignal(LampOn, LampOff, LampOff);
                wait = random.Next(5,60);
                await Task.Delay(TimeSpan.FromSeconds(wait));
            }
        }
    }
}