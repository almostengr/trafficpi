using System;
using System.Device.Gpio;
using System.Threading;
using System.Threading.Tasks;
using Almostengr.TrafficPi.LampControl.Common;
using Almostengr.TrafficPi.LampControl.Services;
using Microsoft.Extensions.Logging;

namespace Almostengr.TrafficPi.LampControl.Workers
{
    public class RedLightWorker : BaseWorker
    {
        // private readonly GpioController _gpio;
        

        // public RedLightWorker(ILogger<BaseWorker> logger, GpioController gpio) : base(logger)
        // {
        //     _gpio = gpio;
        // }

        public RedLightWorker(ILogger<BaseWorker> logger, ISignalIndicationService signalIndication) : base(logger, signalIndication)
        {
            // _signalIndication = signalIndication;
        }

        // public override Task StartAsync(CancellationToken cancellationToken)
        // {
        //     // InitializeGpio(_gpio);

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
                // ChangeSignal(LampOn, LampOff, LampOff, _gpio);
                _signalIndication.RedLight();
                await Task.Delay(TimeSpan.FromMinutes(DelaySeconds.Maximum), stoppingToken);
            }
        }
    }
}