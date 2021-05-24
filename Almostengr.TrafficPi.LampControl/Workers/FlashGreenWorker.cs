using System;
using System.Device.Gpio;
using System.Threading;
using System.Threading.Tasks;
using Microsoft.Extensions.Logging;

namespace Almostengr.TrafficPi.LampControl.Workers
{
    public class FlashGreenWorker : BaseWorker
    {
        private readonly AppSettings _appSettings;

        public FlashGreenWorker(ILogger<FlashGreenWorker> logger, GpioController gpioController, AppSettings appSettings) : 
            base(logger, gpioController, appSettings)
        {
            _appSettings = appSettings;
        }

        protected override async Task ExecuteAsync(CancellationToken stoppingToken)
        {
            bool signalIlluminated = true;

            while (!stoppingToken.IsCancellationRequested)
            {
                signalIlluminated = FlashSignal(_appSettings.GreenLightPin, signalIlluminated);
                await Task.Delay(TimeSpan.FromMilliseconds(FlasherDelay), stoppingToken);
            }
        }
        
    }
}