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

        public FlashYellowWorker(ILogger<FlashYellowWorker> logger, GpioController gpioController, AppSettings appSettings) :
            base(logger, gpioController, appSettings)
        {
            _appSettings = appSettings;
        }

        protected override async Task ExecuteAsync(CancellationToken stoppingToken)
        {
            bool signalIlluminated = true;

            while (!stoppingToken.IsCancellationRequested)
            {
                signalIlluminated = FlashSignal(_appSettings.YellowLightPin, signalIlluminated);
                await Task.Delay(TimeSpan.FromMilliseconds(FlasherDelay), stoppingToken);
            }
        }

    }
}