using System;
using System.Device.Gpio;
using System.Threading;
using System.Threading.Tasks;
using Almostengr.TrafficPi.LampControl.Services;
using Microsoft.Extensions.Logging;

namespace Almostengr.TrafficPi.LampControl.Workers
{
    public class FlashGreenWorker : BaseWorker
    {
        // private readonly GpioController _gpio;

        // public FlashGreenWorker(ILogger<FlashGreenWorker> logger, GpioController gpio) : 
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

        public FlashGreenWorker(ILogger<BaseWorker> logger, ISignalIndicationService signalIndication) : 
            base(logger, signalIndication)
        {
        }
        
        protected override async Task ExecuteAsync(CancellationToken stoppingToken)
        {
            while (!stoppingToken.IsCancellationRequested)
            {
                // ChangeSignal(LampOff, LampOff, LampOn);
                _signalIndication.GreenLight();
                await Task.Delay(TimeSpan.FromMilliseconds(FlasherDelay), stoppingToken);

                // ChangeSignal(LampOff, LampOff, LampOff);
                _signalIndication.NoLights();
                await Task.Delay(TimeSpan.FromMilliseconds(FlasherDelay), stoppingToken);
            }
        }

    }
}