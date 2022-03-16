using System;
using System.Device.Gpio;
using System.Threading;
using System.Threading.Tasks;
using Almostengr.TrafficPi.LampControl.Services;
using Microsoft.Extensions.Logging;

namespace Almostengr.TrafficPi.LampControl.Workers
{
    public class UsTrafficWorker : BaseWorker
    {
        // private readonly GpioController _gpio;

        // public UsTrafficWorker(ILogger<FlashGreenWorker> logger, GpioController gpio) : 
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

        public UsTrafficWorker(ILogger<BaseWorker> logger, ISignalIndicationService signalIndication) : base(logger, signalIndication)
        {
        }

        protected override async Task ExecuteAsync(CancellationToken stoppingToken)
        {
            int wait;

            while (!stoppingToken.IsCancellationRequested)
            {
                // ChangeSignal(LampOff, LampOff, LampOn, _gpio);
                _signalIndication.GreenLight();
                wait = RedGreenDelay();
                await Task.Delay(TimeSpan.FromSeconds(wait), stoppingToken);

                // ChangeSignal(LampOff, LampOn, LampOff, _gpio);
                _signalIndication.YellowLight();
                wait = YellowDelay();
                await Task.Delay(TimeSpan.FromSeconds(wait), stoppingToken);

                // ChangeSignal(LampOn, LampOff, LampOff, _gpio);
                _signalIndication.RedLight();
                wait = RedGreenDelay();
                await Task.Delay(TimeSpan.FromSeconds(wait), stoppingToken);
            }
        }
    }
}