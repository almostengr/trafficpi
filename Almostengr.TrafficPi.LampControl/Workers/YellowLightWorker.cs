using System;
using System.Device.Gpio;
using System.Threading;
using System.Threading.Tasks;
using Almostengr.TrafficPi.LampControl.Common;
using Almostengr.TrafficPi.LampControl.Services;
using Microsoft.Extensions.Logging;

namespace Almostengr.TrafficPi.LampControl.Workers
{
    public class YellowLightWorker : BaseWorker
    {
        // private readonly GpioController _gpio;

        public YellowLightWorker(ILogger<YellowLightWorker> logger, ISignalIndicationService signalIndication) : base(logger, signalIndication)
        {

        }

        // public YellowLightWorker(ILogger<BaseWorker> logger, GpioController gpio) : base(logger)
        // {
        //     _gpio = gpio;
        // }

        // public override Task StartAsync(CancellationToken cancellationToken)
        // {
        //     InitializeGpio(_gpio);
        //     return base.StartAsync(cancellationToken);
        // }

        // public override Task StopAsync(CancellationToken cancellationToken)
        // {
        //     ShutdownGpio(_gpio);
        //     return base.StopAsync(cancellationToken);
        // }

        protected override async Task ExecuteAsync(CancellationToken stoppingToken)
        {
            while (!stoppingToken.IsCancellationRequested)
            {
                // ChangeSignal(LampOff, LampOn, LampOff, _gpio);
                _signalIndication.YellowLight();
                await Task.Delay(TimeSpan.FromMinutes(DelaySeconds.Maximum), stoppingToken);
            }
        }
    }
}