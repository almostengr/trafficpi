using System;
using System.Device.Gpio;
using System.Threading;
using System.Threading.Tasks;
using Almostengr.TrafficPi.LampControl.Services;
using Microsoft.Extensions.Logging;

namespace Almostengr.TrafficPi.LampControl.Workers
{
    public class FlashYellowWorker : BaseWorker
    {
        public FlashYellowWorker(ILogger<BaseWorker> logger, ISignalIndicationService signalIndication) : base(logger, signalIndication)
        {
        }

        // private readonly GpioController _gpio;

        // public FlashYellowWorker(ILogger<FlashGreenWorker> logger, GpioController gpio) : 
        //     base(logger)
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
                await Task.Delay(TimeSpan.FromMilliseconds(FlasherDelay), stoppingToken);

                // ChangeSignal(LampOff, LampOff, LampOff, _gpio);
                _signalIndication.NoLights();
                await Task.Delay(TimeSpan.FromMilliseconds(FlasherDelay), stoppingToken);
            }
        }

    }
}